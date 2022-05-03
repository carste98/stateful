#!/bin/bash

# Uncomment this if you have not got subversion installed
# sudo apt-get install subversion

mkdir docs
cd docs
# operator sdk
svn checkout https://github.com/operator-framework/operator-sdk/trunk/website/content/en/docs
mv docs operator-sdk-docs
# kudo
svn checkout https://github.com/kudobuilder/kudo.dev/trunk/content/docs
mv docs kudo-docs
#kopf
svn checkout https://github.com/nolar/kopf/trunk/docs
mv docs kopf-docs

