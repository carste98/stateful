# This is the code for setting up - [Kopf](https://github.com/nolar/kopf)

Kopf is a framework which utilizes Python to create operators. It is possible to run the operators in two ways:
1. As operators usually are run, inside the cluster
2. Locally.

I have tested running Kopf both ways and the method is only slightly different. Both ways will be explained.

!IMPORTANT: Everything here is done on windows in a linux environment (WSL2) and all other ways of running it is untested which means the instructions may or may not work depending on system.


## Requirements:
1. check [Kopf Installation Docs]() for supported Python version - **(2022-04-29) : Python >= 3.7 (CPython and PyPy are officially tested and supported)**
2. Install pip for bash

## Locally:
### How to run:
1. Download files
2. Run `./setuplocal.sh`

### Verify that operating is running
1. When running locally the operator is running in the terminal windows where the setup script was executed and stays functional until the process is terminated. Incoming events that affect the operator will thus appear in this window as they happen.
```console
[2022-05-02 10:32:18,794] kopf._core.engines.a [INFO    ] Initial authentication has been initiated.
[2022-05-02 10:32:20,023] kopf.activities.auth [INFO    ] Activity 'login_via_pykube' succeeded.
[2022-05-02 10:32:20,053] kopf.activities.auth [INFO    ] Activity 'login_via_client' succeeded.
[2022-05-02 10:32:20,054] kopf._core.engines.a [INFO    ] Initial authentication has finished.
|
```

### Test the functionality
1. Run `kubectl get pods` which should not contain any pods.
```console
No resources found in default namespace.
```
2. Run `kubectl apply -f psql-cr.yaml` to insert a CR in to the cluster.
```yaml
apiVersion: test.com/v1
kind: psql
metadata:
  name: psql-sample
spec:
  size: 4
```
which results in input similar to this from the operator 
```console
StatefulSet psql-pod created
[2022-05-02 10:36:16,758] kopf.objects         [INFO    ] [default/psql-sample] Handler 'create_fn' succeeded.
[2022-05-02 10:36:16,760] kopf.objects         [INFO    ] [default/psql-sample] Creation is processed: 1 succeeded; 0 failed.
```
3. Run `kubectl get pods` to see that the amount of pods created by the operator is equal to the size field in the **CR** spec.
```console
NAME            READY   STATUS    RESTARTS   AGE
psql-sample-0   1/1     Running   0          2m36s
psql-sample-1   1/1     Running   0          2m23s
psql-sample-2   1/1     Running   0          2m10s
psql-sample-3   1/1     Running   0          118s
```
4. Run `kubectl get pvc` to verify the existence of peristent volume claims for each of the pods.
```console
www-psql-pod-0   Bound    pvc-9604e41c-bea5-4c2a-aea8-cba3ad369cac   1Gi        RWO            standard       46m
www-psql-pod-1   Bound    pvc-10881d1c-8965-4dc8-8b91-a442ad8817f4   1Gi        RWO            standard       46m
www-psql-pod-2   Bound    pvc-5fd94206-14a8-4be3-ab01-1293b44975b7   1Gi        RWO            standard       46m
www-psql-pod-3   Bound    pvc-5f829bd0-90e3-4958-9c41-31e2f131db11   1Gi        RWO            standard       45m
```


## Inside the cluster

### How to run:
1. Download files
2. Add a '.env' file in the root folder with `DOCKER_USER=<USERNAME>`.
3. Run `./setupInCluster.sh` - must be logged in to docker in bash and docker daemon must be running.


### Verify that the operator is running
1. Run `kubectl get all` which should output information similar to this:

```console
NAME                                 READY   STATUS    RESTARTS   AGE
pod/kopf-operator-6d47d5875c-ghgz9   1/1     Running   0          9m59s

NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/kopf-operator   1/1     1            1           9m59s

NAME                                       DESIRED   CURRENT   READY   AGE
replicaset.apps/kopf-operator-6d47d5875c   1         1         1       9m59s
```

2. Run `kubectl logs` for the pod to get information about the operator.
```console
[2022-05-02 10:14:51,410] kopf._core.reactor.r [DEBUG   ] Starting Kopf 1.35.4.
[2022-05-02 10:14:51,411] kopf._core.engines.a [INFO    ] Initial authentication has been initiated.
[2022-05-02 10:14:51,412] kopf.activities.auth [DEBUG   ] Activity 'login_via_pykube' is invoked.
[2022-05-02 10:14:51,414] kopf.activities.auth [DEBUG   ] Pykube is configured in cluster with service account.
[2022-05-02 10:14:51,414] kopf.activities.auth [INFO    ] Activity 'login_via_pykube' succeeded.
[2022-05-02 10:14:51,415] kopf.activities.auth [DEBUG   ] Activity 'login_via_client' is invoked.
[2022-05-02 10:14:51,416] kopf.activities.auth [DEBUG   ] Client is configured in cluster with service account.
[2022-05-02 10:14:51,417] kopf.activities.auth [INFO    ] Activity 'login_via_client' succeeded.
[2022-05-02 10:14:51,418] kopf._core.engines.a [INFO    ] Initial authentication has finished.
[2022-05-02 10:14:51,456] kopf._cogs.clients.w [DEBUG   ] Starting the watch-stream for customresourcedefinitions.v1.apiextensions.k8s.io cluster-wide.
[2022-05-02 10:14:51,459] kopf._cogs.clients.w [DEBUG   ] Starting the watch-stream for clusterkopfpeerings.v1.kopf.dev cluster-wide.
[2022-05-02 10:14:51,461] kopf._cogs.clients.w [DEBUG   ] Starting the watch-stream for psqls.v1.test.com cluster-wide.
[2022-05-02 10:14:51,489] kopf._core.engines.p [DEBUG   ] Keep-alive in 'default' cluster-wide: ok.
[2022-05-02 10:15:45,535] kopf._core.engines.p [DEBUG   ] Keep-alive in 'default' cluster-wide: ok.
```

### Test the functionality
1. Run `kubectl get pods` which should only contain the operator pod. 
```console
NAME                             READY   STATUS    RESTARTS   AGE
kopf-operator-6d47d5875c-ghgz9   1/1     Running   0          3m3s
```
2. Run `kubectl apply -f psql-cr.yaml` to insert a CR in to the cluster.
```yaml
apiVersion: test.com/v1
kind: psql
metadata:
  name: psql-sample
spec:
  size: 4
```
3. Run `kubectl get pods` to verify the existence of a set of pods where the amount is equal to the size field in the **CR** defined in the previous step.

```console
NAME                             READY   STATUS    RESTARTS   AGE
psql-pod-0                       1/1     Running   0          60s
psql-pod-1                       1/1     Running   0          49s
psql-pod-2                       1/1     Running   0          23s
psql-pod-3                       1/1     Running   0          12s
```
4. Run `kubectl get pvc` to verify the existence of persistent volume claims for each of the pods.
```console
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
www-psql-pod-0   Bound    pvc-a5b6ae10-96e4-4fd6-b2db-77e0cd5e1db7   1Gi        RWO            standard       21m
www-psql-pod-1   Bound    pvc-f1a42ffd-1483-41ec-87ea-d95013a56af9   1Gi        RWO            standard       20m
www-psql-pod-2   Bound    pvc-ef96e1e3-b4d2-48b2-a419-43e5772e34bf   1Gi        RWO            standard       20m
www-psql-pod-3   Bound    pvc-31adf56c-46ee-4970-8fd6-09bebe5b8391   1Gi        RWO            standard       19m
```

## Comments about framework

1. I think this framework is good if you are used to writing using Python. It is intuitive to setup functions and access attributes on Kubernetes objects. 
2. Being able to easily switch between running locally and in cluster is one of the best features of the framework. It is very fast to boot up a new version of the operator and simply watch the live logs in the open terminal when you run locally. This means that it is possible to get better error-logging by using native python functions such as "print". With error logging you can find the errors in the operators faster and then when the operator runs without problems locally you can move it to the cluster and test it there aswell. If you instead were to run it in the cluster every time it would take a lot longer due to having to build a base image.
3. This framework strongly leverages the kubernetes library for python. The docs for that library are quite extensive and semi-hard to navigate.
4. The peering and RBAC configuration is structured and highly configurable which is good in a security minded aspect but still it would be great if it were automatically generated to ease the development.



## Stats gathered using [repostat](https://github.com/vifactor/repostat) for kopf

<body>
    <dt>Project name</dt>
        <dd>kopf</dd>
    <dt>Branch analysed</dt>
        <dd>main</dd>
    <dt>Lifespan</dt>
        <dd>from 2019-03-06 to 2022-04-02</dd>
    <dt>Project age</dt>
        <dd>1122 days, 361 active days
            (32.17%)</dd>
            <dt>Authors count</dt>
        <dd>48</dd>
    <dt>Commits count</dt>
        <dd> 1623 total
            (inc. 25.32% merge commits) </dd>
        <dd> 1.45 per day </dd>
        <dd> 4.50 per active day </dd>
        <dd> 33.81 per author </dd>
    <dt>Total files count</dt>
        <dd>391</dd>
    <dt>Total lines count</dt>
        <dd>51281 (104596 added, 53315 removed)</dd>
</dl>
<p style="text-align:right;"> Report generated on 2022-05-03 20:11 </p>
</body>
