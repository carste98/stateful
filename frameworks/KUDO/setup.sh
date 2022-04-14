#!/bin/bash


# Install cert manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.7.1/cert-manager.yaml

# Install KUDO
kubectl kudo init

# Mount this operator
kubectl kudo install ./
