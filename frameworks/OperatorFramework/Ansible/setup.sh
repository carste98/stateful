#!/bin/bash


if [ "${1}" = "download" ] || [ "${2}" = "download" ] ; then
    # download operator-sdk
    export ARCH=$(case $(uname -m) in x86_64) echo -n amd64 ;; aarch64) echo -n arm64 ;; *) echo -n $(uname -m) ;; esac)
    export OS=$(uname | awk '{print tolower($0)}')

    export OPERATOR_SDK_DL_URL=https://github.com/operator-framework/operator-sdk/releases/download/v1.20.0
    curl -LO ${OPERATOR_SDK_DL_URL}/operator-sdk_${OS}_${ARCH}

    gpg --keyserver keyserver.ubuntu.com --recv-keys 052996E2A20B5C7E

    curl -LO ${OPERATOR_SDK_DL_URL}/checksums.txt
    curl -LO ${OPERATOR_SDK_DL_URL}/checksums.txt.asc
    gpg -u "Operator SDK (release) <cncf-operator-sdk@cncf.io>" --verify checksums.txt.asc

    grep operator-sdk_${OS}_${ARCH} checksums.txt | sha256sum -c -

    # Remove temp files
    rm checksums.txt
    rm checksums.txt.asc
    rm operator-sdk_linux_amd64
fi


if [ "${1}" = "init" ] || [ "${2}" = "init" ] ; then

    # init operator project
    operator-sdk init --plugins=ansible --domain hub.docker.com

    # create api
    operator-sdk create api --group db --version v1alpha1 --kind Psql --generate-role

    cp editedFiles/main.yml roles/psql/tasks/main.yml

    # write default value for the size, which is good practice
    printf "---
    # defaults file for Psql
    size: 1" >> roles/psql/defaults/main.yml

    # insert the example CR into the samples folder
    cp editedFiles/db_v1alpha1_psql.yaml config/samples/db_v1alpha1_psql.yaml

    # Replace Makefile with correct IMG tags
    cp editedFiles/Makefile Makefile
fi

# Build image
make docker-build docker-push

# Deploy operator into cluster
make deploy