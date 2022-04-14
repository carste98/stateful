#!/bin/bash


kubectl kudo uninstall --instance first-operator-instance
kubectl kudo init --upgrade --dry-run --output yaml | kubectl delete -f -


