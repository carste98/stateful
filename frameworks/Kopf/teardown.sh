#!/bin/bash

kubectl delete crd psqls.test.com

kubectl delete -f https://github.com/nolar/kopf/raw/main/peering.yaml
kubectl delete -f rbac.yaml

kubectl delete -f deployOperator.yaml
