# This is the code for setting up - [KUDO](https://github.com/kudobuilder/kudo)

## Requirements:
1. Krew package manager
2. kubectl version 1.13.0 or newer [Kudo Install](https://kudo.dev/docs/cli/installation.html#cli-installation)


## How to run:
1. Download files.
3. Run `./setup.sh`.
4. If there is an error:
```console
Internal error occurred: failed calling webhook "instance-admission.kudo.dev"
```
wait for a minute or two and try running `kubectl kudo install ./`. 

## Verify that operating is running and test functionality
1. Verify existing operator namespace by running `kubectl get ns`
```console
NAME              STATUS   AGE
cert-manager      Active   18m
kudo-system       Active   5m45s
```

2. Verify that the operator is running `kubectl get operator`.
```console
NAME             AGE
first-operator   6m13s
```

3. Verify that there is a statefulset with the size specified in **params.yaml** `kubectl get pods`.
```console
NAME     READY   STATUS    RESTARTS   AGE
psql-0   1/1     Running   0          102s
psql-1   1/1     Running   0          87s
psql-2   1/1     Running   0          75s
psql-3   1/1     Running   0          61s
```

4. Run `kubectl get pvc` to verify the existence of persistent volume claims for each of the pods.
```console
NAME                    STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
www-psql-0              Bound    pvc-49547153-f04c-40cf-9d49-cd48c6cdadac   1Gi        RWO            standard       6m43s
www-psql-1              Bound    pvc-4e113542-4084-4158-bb79-1d1fc60b8f93   1Gi        RWO            standard       6m29s
www-psql-2              Bound    pvc-d3ae174b-db26-4a1f-996c-7e7d647f15a0   1Gi        RWO            standard       6m16s
www-psql-3              Bound    pvc-4f76ff09-0e85-4ccb-bc20-11382a517c8b   1Gi        RWO            standard       6m2s
```

## Comments about framework

1. This is the only framework that I couldn't really create the kind of operator I wanted (where an event is triggered when a CR is inserted into the cluster). Instead I settled for simply deploying a statefulset + pvcs.
2. This Framework is not really made for this type of test, instead it should be used to structure advanced deployment schemas where different **pipe-tasks** can be leveraged ([pipe tasks](https://kudo.dev/docs/developing-operators/tasks.html#pipe-task)).
3. It seems the documentation is semi-outdated. It is almost a year since the last push to the GitHub (as of 2022-05-02) which is probably a dealbreaker.
4. I think that using Operator Framework with Ansible is just objectively better since Ansible in itself is very close to the declarative approach used in KUDO. If you combine that with the support and available tutorials it is a no-brainer.

## Stats gathered using [repostat](https://github.com/vifactor/repostat) for KUDO
<body>
    <dl>
    <dt>Project name</dt>
        <dd>kudo</dd>
    <dt>Branch analysed</dt>
        <dd>main</dd>
    <dt>Lifespan</dt>
        <dd>from 2016-06-25 to 2021-07-02</dd>
    <dt>Project age</dt>
        <dd>1833 days, 405 active days
            (22.09%)</dd>
            <dt>Authors count</dt>
        <dd>64</dd>
    <dt>Commits count</dt>
        <dd> 1030 total
            (inc. 2.04% merge commits) </dd>
        <dd> 0.56 per day </dd>
        <dd> 2.54 per active day </dd>
        <dd> 16.09 per author </dd>
    <dt>Total files count</dt>
        <dd>765</dd>
    <dt>Total lines count</dt>
        <dd>103818 (3454048 added, 3350230 removed)</dd>
</dl>
<p style="text-align:right;"> Report generated on 2022-05-03 20:08 </p>
</body>
