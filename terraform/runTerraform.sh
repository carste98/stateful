#!/bin/bash

terraform apply

gcloud container clusters get-credentials --region=europe-north1-a dark-blade-342011-gke
