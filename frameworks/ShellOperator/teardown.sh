#!/bin/bash

kubectl delete ns example-monitor-pods
kubectl delete clusterrole monitor-pods
kubectl delete clusterrolebinding monitor-pods
kubectl delete -f psql-cr.yaml
kubectl delete statefulset psql-pod
