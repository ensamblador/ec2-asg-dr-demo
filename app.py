#!/usr/bin/env python3

from aws_cdk import core

from inacap_lab.inacap_lab_stack import InacapLabStack


region = 'us-east-1'

app = core.App()
vpc_stack = InacapLabStack(app, "inacap-lab", env={'region': region})
app.synth()


