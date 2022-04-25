#!/bin/bash

terraform apply -auto-approve

gcloud container clusters get-credentials --region=$(terraform output -raw zone) $(terraform output -raw kubernetes_cluster_name)
