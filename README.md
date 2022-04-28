# TLDR;
This is the code produced during the testing for the project on life-cycle management of stateful applications on top of Kubernetes.


# Life-cycle management of stateful applications on top of Kubernetes.

## Frameworks
For this project 4 different frameworks:

### 1. Operator Framework
### 2. KUDO
### 3. Kopf
### 4. Shell Operator

will be implemented using the same operator template:




## Infrastructure

The testing environment will run on [GKE - Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine).

For building Infrastructure, [Terraform](https://www.terraform.io/) is used. Terraform will create the necessary infrastructure for running the frameworks on **GKE**. This means that the infrastructure will be consistent and reproduceable.

For more information on how to use Terraform to build infrastructure see either [My Terraform Repository](https://github.com/carste98/stateful/tree/main/terraform) or [Official Terraform Tutorial for Google](https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build
).


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

### PostgreSQL Operator
https://github.com/zalando/postgres-operator/blob/master/docs/quickstart.md
