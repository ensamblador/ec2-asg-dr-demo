from aws_cdk import core
from inacap_lab.vpc_stack import CdkVpcStack
from inacap_lab.ec2_stack import CdkEc2Stack
from inacap_lab.s3_website import S3ReactWebsiteStack

class InacapLabStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        vpc_stack = CdkVpcStack(self, "cdk-vpc")
        ec2_stack = CdkEc2Stack(self, "cdk-ec2",vpc=vpc_stack.vpc)
        #s3_cloudfront = S3ReactWebsiteStack(self, "s3-website")
