# This is the code for setting up - [Shell Operator](https://github.com/flant/shell-operator)

## Requirements:
1. A docker account
2. Setup docker so it can be run in bash or linux



## How to run:
1. Download files.
2. Add a '.env' file in the root folder with `DOCKER_USER=<USERNAME>`.
3. Run `./setup.sh` - must be logged in to docker in bash and docker daemon must be running.

## Verify that operating is running
1. Verify existing operator namespace by running `kubectl get ns`
```console
NAME                   STATUS   AGE
example-monitor-pods   Active   3s
```

3. Verify that the pod is running `kubectl get all -n example-monitor-pods`.
```console
NAME                 READY   STATUS    RESTARTS   AGE
pod/shell-operator   1/1     Running   0          88s
```
5. Check that there is no errors with the operator `kubectl logs pod/shell-operator -n example-monitor-pods | grep "error"` which should only return messages initializing error counters. 

```console
{"level":"info","msg":"Create metric counter shell_operator_hook_enable_kubernetes_bindings_errors_total","operator.component":"metricStorage","time":"2022-04-29T09:19:47Z"}
{"level":"info","msg":"Create metric counter shell_operator_hook_run_errors_total","operator.component":"metricStorage","time":"2022-04-29T09:19:47Z"}
{"level":"info","msg":"Create metric counter shell_operator_hook_run_allowed_errors_total","operator.component":"metricStorage","time":"2022-04-29T09:19:47Z"}
```

## Test the functionality
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
3. Run `kubectl get pods` to verify the existence of a set of pods where the amount is equal to the size field in the **CR** defined in the previous step.

```console
NAME         READY   STATUS    RESTARTS   AGE
psql-pod-0   1/1     Running   0          21s
psql-pod-1   1/1     Running   0          16s
psql-pod-2   1/1     Running   0          11s
psql-pod-3   1/1     Running   0          6s
```
4. Run `kubectl get pvc` to verify the existence of persistent volume claims for each of the pods.
```console
www-psql-pod-0           Bound    pvc-c3851023-c41b-4119-a33a-9b70f824f40a   1Gi        RWO            standard       5m1s
www-psql-pod-1           Bound    pvc-c3c5b1de-6a40-4917-9e6a-933df32cb2d2   1Gi        RWO            standard       4m56s
www-psql-pod-2           Bound    pvc-54b0d668-caad-4cae-ab53-06d8b1d3d91d   1Gi        RWO            standard       4m51s
www-psql-pod-3           Bound    pvc-f661e263-8662-470e-a41a-1059319dab4a   1Gi        RWO            standard       4m46s
```

## Comments about framework

1. Some things are kind of hardcoded in this solution which may be due to either (1) my lack of understanding how to properly leverage the framework to do this kind of task or (2) the framework is not suitable for this kind of use case. It still uses variables for sizing as specified by the operator template and it watches an externally added **CR**.
2. This framework could be useful if you are proficient in writing scripts.
3. This framework probably shines in scenarios when you want to have scheduled events which acts as cronjobs, inside the cluster.
