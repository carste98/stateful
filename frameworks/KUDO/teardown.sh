#!/bin/bash


kubectl kudo uninstall --instance first-operator-instance
kubectl kudo init --upgrade --dry-run --output yaml | kubectl delete -f -

kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.7.1/cert-manager.yaml
