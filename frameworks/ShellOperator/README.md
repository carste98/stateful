# This is the code for setting up - [Shell Operator](https://github.com/flant/shell-operator)

## Requirements:
1. A docker account
2. setup docker so it can be run in bash or linux



## How to run:
1. download files.
2. add a '.env' file in the root folder with `DOCKER_USER=<USERNAME>`.
3. run `./setup.sh` - must be logged in to docker in bash and docker daemon must be running.

## Verify that operating is running
1. Verify existing operator namespace by running `k get ns`
2. Verify that the pod is running `k get all -n example-monitor-pods`.
3. Check that there is no errors with the operator `k logs pod/shell-operator -n example-monitor-pods`

## Test the functionality
1. Run `k get pods` which should not contain any pods.
2. Run `k apply -f psql-cr.yaml` to insert a CR in to the cluster.
3. Run `k get pods` to verify the existence of a set of pods.
4. 
