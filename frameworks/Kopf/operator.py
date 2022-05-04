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

    # Make the statefulset the child of the CR psql object 
    kopf.adopt(data, owner=body) 
  
    apiAppsV1 = kubernetes.client.AppsV1Api() 
    # apiV1 = kubernetes.client.CoreV1Api() 
    
    # Create statefulset
    statefulsetObj = apiAppsV1.create_namespaced_stateful_set(namespace=namespace, body=data)
    print(f"StatefulSet {statefulsetObj.metadata.name} created") 
    # print(f"PV {pvcObj.metadata.name} created") 

    # Update status 
    msg = f"Statefulset and PV created : {name}" 
    return {'message': msg}