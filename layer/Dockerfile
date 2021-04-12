# Adapted from: https://github.com/seanfdnn/weasyprint_lambda/blob/master/Dockerfile
#
# To convert SVG to PNG, we rely upon libcairo, which requires binary (.so) files
# built specifically for Amazon Linux.
# We cannot obtain them locally if we are, say, on an Ubuntu machine. We have
# to build the Lambda Layer with those files, publish it, and use it in our Lambda function.
FROM lambci/lambda:build-python3.8

# Based on https://aws.amazon.com/premiumsupport/knowledge-center/lambda-linux-binary-package/
RUN yum install -y yum-utils rpmdevtools
WORKDIR /tmp
RUN yumdownloader libffi libffi-devel cairo cairo-devel expat libuuid --resolve && rpmdev-extract *rpm
RUN file $(find . -name libexpat.so*)

RUN mkdir /opt/lib && rm -rf /opt/lib/*
WORKDIR /opt
RUN cp -R /tmp/*/usr/lib64/* /opt/lib

RUN zip --symlinks geopatterns_demo_lambda_layer.zip lib/*
