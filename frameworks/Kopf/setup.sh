#!/bin/bash

#kubectl apply -f https://github.com/nolar/kopf/raw/main/peering.yaml
kubectl apply -f crd.yml
pip install -r requirements.txt

kopf run operator.py
