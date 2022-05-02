#!/bin/bash


kubectl delete namespace ansible-system
kubectl delete -f config/samples/db_v1alpha1_psql.yaml
kubectl delete statefulset psql-sample-psql
