#!/usr/bin/env python3

from aws_cdk import core

from inacap_lab.inacap_lab_stack import InacapLabStack


app = core.App()
InacapLabStack(app, "inacap-lab")

app.synth()
