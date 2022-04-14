#!/bin/bash

psql -h ${1} -p 5432 -d postgres -U "user" -W
    
# Patch size 
# kubectl patch statefulsets <stateful-set-name> -p '{"spec":{"replicas":<new-replicas>}}'