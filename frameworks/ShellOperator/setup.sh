#!/bin/bash

# Local .env
if [ -f .env ]; then
    # Load Environment Variables
    export $(cat .env | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
fi

#Build and push docker image
docker build -t $DOCKER_USER/shelloperator .
docker push $DOCKER_USER/shelloperator

#create RBAC for shell-operator
kubectl create namespace example-monitor-pods
kubectl create serviceaccount monitor-pods-acc --namespace example-monitor-pods
kubectl create clusterrole monitor-pods --verb=get,watch,list,create --resource=pods,StatefulSet
kubectl create clusterrolebinding monitor-pods --clusterrole=monitor-pods --serviceaccount=example-monitor-pods:monitor-pods-acc

# Deploy shell-operator as pod inside cluster
#kubectl -n example-monitor-pods apply -f shell-operator-pod.yaml

export DOCKER_USER=$DOCKER_USER
envsubst < shell-operator-pod.yaml | kubectl -n example-monitor-pods apply -f -