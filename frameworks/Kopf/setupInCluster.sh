#!/bin/bash

# RBAC
kubectl apply -f https://github.com/nolar/kopf/raw/main/peering.yaml

sleep 1

# RBAC
kubectl apply -f https://github.com/nolar/kopf/raw/main/peering.yaml

# CRD
kubectl apply -f psql-crd.yaml


# .env
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
fi

# Push operator image to image repository
docker build -t $DOCKER_USER/kopf-operator .
docker push $DOCKER_USER/kopf-operator

# rbac privileges
kubectl apply -f rbac.yaml

export DOCKER_USER=$DOCKER_USER
envsubst < deployOperator.yaml | kubectl apply -f -