#!/bin/bash

kubectl apply -f psql-crd.yaml
pip install -r requirements.txt
kopf run operator.py