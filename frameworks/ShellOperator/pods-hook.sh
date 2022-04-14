#!/usr/bin/env bash

if [[ $1 == "--config" ]] ; then
  echo '{"configVersion":"v1", "onStartup": 1}'
else
  cat << EOF | kubectl apply -f -
  apiVersion: apps/v1
  kind: StatefulSet
  metadata:
    name: psql-deployment
    namespace: default
  spec:
    serviceName: "psql"
    selector:
      matchLabels:
        app: psql
    replicas: 4
    template:
      metadata:
        labels:
          app: psql
      spec:
        containers:
          - name: psql
            image: postgres:latest
            ports:
              - containerPort: 5432
            env:
            - name: POSTGRES_PASSWORD
              value: admin
            - name: POSTGRES_USER 
              value: user
            - name: POSTGRES_DB
              value: db
    volumeClaimTemplates:
    - metadata:
        name: www
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 1Gi
EOF
fi