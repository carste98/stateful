# This is in the works..


## Terraform GCP tutorial

https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build



## Operator Framework

Did not get the OLM tutorial to fully work, replaced make bundle-build bundle-push with the corresponding commands in this link.
`https://docs.openshift.com/container-platform/4.7/operators/operator_sdk/osdk-working-bundle-images.html`

Main tutorial

https://sdk.operatorframework.io/docs/building-operators/ansible/tutorial/

### OLM - community operator

#### Build operator

1. create and apply operator group yaml
2. create and apply subscription yaml
3. should now be able to `kubectl get operatorgroup <og>` or other resource to verify existence of operator.

#### Delete operator
1. `kubectl delete operatorgroup <og>`
2. `kubectl delete subscription <sub>`
3. `kubectl delete csv <csv>`
