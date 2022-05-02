import os
import kopf 
import kubernetes
import yaml
@kopf.on.create('test.com', 'v1', 'psql') 
def create_fn(body, spec, **kwargs): 

    # Get info from CR psql object 
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    size = spec['size']
    img = 'postgres:latest'

    # Read yaml and insert variables.
    path = os.path.join(os.path.dirname(__file__), 'psql-ss.yaml')
    tmpl = open(path, 'rt').read()
    text = tmpl.format(size=size, img=img)
    data = yaml.safe_load(text)
    
    # statefulset template 
    # statefulSet = {
    #     'apiVersion': 'apps/v1',
    #     'metadata': {
    #         'name' : name,
    #         'namespace': 'default'
    #     },
    #     'spec': {
    #         'replicas': size,
    #         'minReadySeconds': 10,
    #         'selector': {
    #             'matchLabels': {
    #                 'app' : 'psql'
    #             }
    #         },
    #         'template': {
    #             'metadata': {
    #                 'labels': {
    #                     'app': 'psql'
    #                 }
    #             },
    #             'spec': {
    #                 'containers': [{
    #                     'image': image,
    #                     'name': name,
    #                     'ports': [{'containerPort': 5432}],
    #                     'env': [
    #                         {
    #                             'name': 'POSTGRES_PASSWORD',
    #                             'value': 'admin'
    #                         },
    #                         {
    #                             'name': 'POSTGRES_USER',
    #                             'value': 'user'
    #                         },
    #                         {
    #                             'name': 'POSTGRES_DB',
    #                             'value': 'db'
    #                         },
    #                         {
    #                             'name': 'PGDATA',
    #                             'value': '/mnt/data'
    #                         }
    #                     ],
    #                     'volumeMounts': [
    #                         {
    #                         'name': 'kopf-pv',
    #                         'mountPath': '/mnt'
    #                         }
    #                     ]
    #                 }]
    #             },
                # 'volumeClaimTemplates': [{
                #     'metadata': {
                #         'name': 'kopf-pv'
                #     },
                #     'spec': {
                #         'accessModes': "ReadWriteOnce",
                #         'storageClassName': 'psql-storage',
                #         'resources': {
                #             'requests': {
                #                 'storage': '1Gi'
                #             }
                #         }
                #     }
                # }],
    #         }
    #     }
    # }
    # pvc = {
    #     'kind': 'PersistentVolumeClaim',
    #     'apiVersion': 'v1',
    #     'metadata': {
    #         'name' : 'kopf-pv',
    #     },
    #     'spec': {
    #         'accessModes': ["ReadWriteOnce"],
    #         'resources': {
    #             'requests': {
    #                 'storage': '1Gi'
    #             }
    #         }
    #     }
    # } 
 
    # Make the statefulset the child of the CR psql object 
    kopf.adopt(data, owner=body) 
  
    apiAppsV1 = kubernetes.client.AppsV1Api() 
    # apiV1 = kubernetes.client.CoreV1Api() 
    
    # Create statefulset
    # pvcObj = apiV1.create_namespaced_persistent_volume_claim(namespace=namespace,body=pvc)
    statefulsetObj = apiAppsV1.create_namespaced_stateful_set(namespace=namespace, body=data)
    print(f"StatefulSet {statefulsetObj.metadata.name} created") 
    # print(f"PV {pvcObj.metadata.name} created") 

    # Update status 
    msg = f"Statefulset and PV created : {name}" 
    return {'message': msg}