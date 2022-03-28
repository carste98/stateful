#!/bin/bash

terraform apply

gcloud container clusters get-credentials --region=europe-west1-b dark-blade-342011-gke
