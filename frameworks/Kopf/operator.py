import kopf 
import kubernetes

@kopf.on.create('test.com', 'v1', 'psql') 
def create_fn(body, spec, **kwargs): 

    # Get info from CR psql object 
    name = body['metadata']['name'] 
    namespace = body['metadata']['namespace'] 
    size = spec['size']
    
    image = 'postgres:latest'

    # statefulset template 
    statefulSet = {
        'apiVersion': 'apps/v1',
        'metadata': {
            'name' : name,
            'namespace': 'default'
        },
        'spec': {
            'replicas': size,
            'minReadySeconds': 10,
            'selector': {
                'matchLabels': {
                    'app' : 'psql'
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': 'psql'
                    }
                },
                'spec': {
                    'containers': [{
                        'image': image,
                        'name': name,
                        'ports': [{'containerPort': 5432}],
                        'env': [
                            {
                                'name': 'POSTGRES_PASSWORD',
                                'value': 'admin'
                            },
                            {
                                'name': 'POSTGRES_USER',
                                'value': 'user'
                            },
                            {
                                'name': 'POSTGRES_DB',
                                'value': 'db'
                            }
                        ]
                    }]
                },
                'volumeClaimTemplates': [{
                    'metadata': {
                        'name': 'www'
                    },
                    'spec': {
                        'accessModes': "ReadWriteOnce",
                        'storageClassName': 'psql-storage',
                        'resources': {
                            'requests': {
                                'storage': '1Gi'
                            }
                        }
                    }
                }]
            }
        }
    } 
 
    # Make the statefulset the child of the CR psql object 
    kopf.adopt(statefulSet, owner=body) 
  
    api = kubernetes.client.AppsV1Api() 
    
    # Create statefulset
    obj = api.create_namespaced_stateful_set(namespace, statefulSet) 
    print(f"StatefulSet {obj.metadata.name} created") 

    # Update status 
    msg = f"Statefulset and PV created : {name}" 
    return {'message': msg}