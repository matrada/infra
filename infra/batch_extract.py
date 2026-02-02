from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
    aws_ecr as ecr,
    aws_ec2 as ec2
)
from constructs import Construct

NAME = "batch-extract"

class BatchExtract(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # vpc
        vpc = ec2.Vpc.from_lookup(
            self, 
            "Vpc", 
            is_default=True
        )

        # storage
        bucket = s3.Bucket(
            self,
            "DataBucket",
            bucket_name=f"{NAME}-{self.account}-{self.region}",
            removal_policy=RemovalPolicy.RETAIN,  
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        # ecr
        repository = ecr.Repository(
            self,
            "ExtractRepo",
            repository_name=NAME,
            removal_policy=RemovalPolicy.RETAIN,
            image_scan_on_push=True,
        )