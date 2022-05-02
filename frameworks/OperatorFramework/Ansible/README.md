# This is the code for setting up - [Operator Framework : Ansible](https://operatorframework.io/)


## Requirements:

1. Install everything listed on the following page: [Operator Framework Installation](https://sdk.operatorframework.io/docs/building-operators/ansible/installation/).
2. A docker account
3. Setup docker so it can be run in bash or linux

## How to run:
1. Download files.
2. Add a '.env' file in the root folder with `DOCKER_USER=<USERNAME>`.
3. To be able to run you need to be logged in to Docker.
4. If you do not have Operator-sdk installed, Run `./setup.sh download init` to download and install operator sdk and then init a project.
5. If Operator-sdk is already installed, Run `./setup.sh init` to initialize a project.
6. If you want to just run the operator again after shutting it down, Run `./setup.sh`.

## Verify that operating is running
1. Verify existing operator namespace by running `kubectl get ns`
```console
kNAME              STATUS   AGE
ansible-system    Active   7m23s
```

3. Verify that everything is running `kubectl get all -n ansible-system`.
```console
NAME                 READY   STATUS    RESTARTS   AGE
NAME                                              READY   STATUS    RESTARTS   AGE
pod/ansible-controller-manager-54794bd75c-rd52j   2/2     Running   0          7m50s

NAME                                                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/ansible-controller-manager-metrics-service   ClusterIP   10.172.8.249   <none>        8443/TCP   7m50s

NAME                                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ansible-controller-manager   1/1     1            1           7m50s

NAME                                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/ansible-controller-manager-54794bd75c   1         1         1       7m50s
```
5. Run `kubectl logs pod/ansible-controller-manager-54794bd75c-rd52j -n ansible-system` to see the output of the operator.

## Test the functionality
1. Run `kubectl get pods` which should not contain any pods.
```console
No resources found in default namespace.
```
2. Run `kubectl apply -f config/samples/db_v1alpha1_psql.yaml` to insert a CR in to the cluster.
```yaml
apiVersion: db.hub.docker.com/v1alpha1
kind: Psql
metadata:
  name: psql-sample
spec:
  size: 4
```
3. Run `kubectl get pods` to verify the existence of a set of pods where the amount is equal to the size field in the **CR** defined in the previous step.

```console
NAME                 READY   STATUS    RESTARTS   AGE
psql-sample-psql-0   1/1     Running   0          118s
psql-sample-psql-1   1/1     Running   0          107s
psql-sample-psql-2   1/1     Running   0          89s
psql-sample-psql-3   1/1     Running   0          78s
```
4. Run `kubectl get pvc` to verify the existence of persistent volume claims for each of the pods.
```console
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
www-psql-sample-psql-0   Bound    pvc-d048e333-7c2b-4908-af44-70ca7de2573b   1Gi        RWO            standard       18m
www-psql-sample-psql-1   Bound    pvc-5b5b0794-2ea9-40d8-a880-25e446404f38   1Gi        RWO            standard       18m
www-psql-sample-psql-2   Bound    pvc-06afab40-90a3-474b-a8aa-b35be3acda30   1Gi        RWO            standard       18m
www-psql-sample-psql-3   Bound    pvc-7c441de7-9e9b-4151-8d65-4b0d6c019534   1Gi        RWO            standard       18m
```

## Comments about framework

1. The framework creates a very large folder structure, which is why i chose to simply push the files I actually changed to make it easier to organise.
2. It feels high level and robust but as mentioned it is very comprenhensive and might take some time to truly understand.
3. It is possible to run operators locally with this framework which can be used for developing a bit faster but not much more than that.
4. Out of all framework, this seems to have the most tutorials and community support.
