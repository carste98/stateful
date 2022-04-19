#!/bin/bash

kubectl delete crd psqls.test.com
kubectl delete -f psql-cr.yaml
kubectl delete psql psql-sample
