# This is the code for setting up - [Kopf](https://github.com/nolar/kopf)

Kopf is a framework which utilizes Python to create operators. It is possible to run the operators in two ways:
1. As operators usually are run, inside the cluster
2. Locally.

I have tested running Kopf both ways and the method is only slightly different. Both ways will be explained.


## Requirements:
1. check [Kopf Installation Docs]() for supported Python version - **(2022-04-29) : Python >= 3.7 (CPython and PyPy are officially tested and supported)**

## Locally:
### How to run:
1. Download files.
2. Add a '.env' file in the root folder with `DOCKER_USER=<USERNAME>`.
3. Run `./setuplocal.sh`

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

### Comments about framework

## Inside the cluster
