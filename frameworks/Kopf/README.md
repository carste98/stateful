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
3. Run `kubectl get pods` to see that the amount of pods created by the operator is equal to the size field in the **CR** spec.
```console
NAME            READY   STATUS    RESTARTS   AGE
psql-sample-0   1/1     Running   0          2m36s
psql-sample-1   1/1     Running   0          2m23s
psql-sample-2   1/1     Running   0          2m10s
psql-sample-3   1/1     Running   0          118s
```
### Comments about framework

## Inside the cluster
