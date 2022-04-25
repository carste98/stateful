#!/usr/bin/env bash

if [[ $1 == "--config" ]] ; then
  cat <<EOF
configVersion: v1
kubernetes:
- apiVersion: test.com/v1
  kind: psql
  executeHookOnEvent: ["Added"]
EOF
else
  type=$(jq -r '.[0].type' $BINDING_CONTEXT_PATH)
  if [[ $type == "Event" ]] ; then
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
fi