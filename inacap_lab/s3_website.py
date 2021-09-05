from aws_cdk import (
    aws_s3 as s3,
    aws_certificatemanager as acm, 
    aws_cloudfront as cf,
    core
)

chickyshop_certificate = "arn:aws:acm:us-east-1:844626608976:certificate/89f01ad1-ee05-4c6d-a55f-9d47ffb679d9"

class S3ReactWebsiteStack(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "websitebucket",website_index_document="index.html")

        #certificado  = acm.Certificate.from_certificate_arn(self, 'certificado', chickyshop_certificate)

        cf.CloudFrontWebDistribution(self, "CDN",
                                     price_class=cf.PriceClass.PRICE_CLASS_100,
                                     alias_configuration=cf.AliasConfiguration(
                                         names=["recover.chickyshop.cl"],
                                         acm_cert_ref=chickyshop_certificate,
                                         ssl_method=cf.SSLMethod.SNI,
                                         security_policy=cf.SecurityPolicyProtocol.TLS_V1_2_2018
                                     ),
                                     default_root_object='index.html',
                                     origin_configs=[
                                         cf.SourceConfiguration(
                                             behaviors=[
                                                 cf.Behavior(
                                                     is_default_behavior=True)
                                             ],
                                             s3_origin_source=cf.S3OriginConfig(
                                                 s3_bucket_source=bucket
                                             )
                                         )
                                     ]
                                     )