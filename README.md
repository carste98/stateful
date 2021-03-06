# Life-cycle management of stateful applications on top of Kubernetes.


## Operator Template
1. Monitor and wait for a specific custom resource to be inserted into the cluster.
2. Create a StatefulSet of X pods with X Persistent Volumes where X is the replicas specified by the Custom Resource. The base image for the pods should be a stateful application. 


![This is an image](https://github.com/carste98/stateful/blob/main/OperatorTemplate.drawio.png?raw=true)


In this case the chosen stateful application is the official postgres image from docker hub.


## Frameworks
For this project 4 different frameworks:

### 1. [Operator Framework](https://operatorframework.io/)
### 2. [KUDO](https://github.com/kudobuilder/kudo)
### 3. [Kopf](https://github.com/nolar/kopf)
### 4. [Shell Operator](https://github.com/flant/shell-operator)

will be implemented using the same operator template.

## Infrastructure

The testing environment will run on [GKE - Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine).

For building Infrastructure, [Terraform](https://www.terraform.io/) is used. Terraform will create the necessary infrastructure for running the frameworks on **GKE**. This means that the infrastructure will be consistent and reproduceable.

For more information on how to use Terraform to build infrastructure see either [My Terraform Repository](https://github.com/carste98/stateful/tree/main/terraform) or [Official Terraform Tutorial for Google](https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build
).


## Metrics

[Amount Documentation](https://github.com/carste98/stateful/tree/main/testing#measure-documentation-done-2022-05-03) - Measured 2022-05-03
```console
kopf-docs 2320730 bytes
kudo-docs 455792 bytes
operator-sdk-docs 3348450 bytes
shell-operator.git 2742108 bytes
```

## Side notes

### OLM - [Operator Lifecycle Manager](https://olm.operatorframework.io/)

Handle life-cycle of operators themselves by utilizing part of Operator Framework.

#### OLM - Own operator

I used this tutorial: https://sdk.operatorframework.io/docs/building-operators/ansible/tutorial/#3-deploy-your-operator-with-olm

Did not get the OLM tutorial to fully work at first, but replaced make bundle-build bundle-push with the corresponding commands in this link:
https://docs.openshift.com/container-platform/4.7/operators/operator_sdk/osdk-working-bundle-images.html which worked.

This problem likely occured due to me using Docker hub. There is a mismatch between the name of the accessible image registry `hub.docker.com` and where the images are retrieved `docker.io/`. This meant that the life-cycle manager tried to pull the image from `hub.docker.com/<thepath>` instead of `docker.io/<thepath>`.


#### OLM - community operator

Tutorial
https://olm.operatorframework.io/docs/getting-started/

### [Operator Hub](https://operatorhub.io/)

There are a lot of operators already created and maintained. Try to choose one from operator hub and install it with OLM with your own configuration.
