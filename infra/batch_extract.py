from aws_cdk import (
    # Duration,
    Size,
    Stack,
    RemovalPolicy,
    aws_batch as batch,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_ec2 as ec2
)
from constructs import Construct

NAME = "batch-extract"
MAXV_CPUS = 16

# job definition
CPU = 1
MEMORY = 4096
TAG = "latest"
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
            bucket_name=f"{NAME}",
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

        # image
        #

        # execution role
        execution_role = iam.Role(
            self,
            "ExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonECSTaskExecutionRolePolicy"
                )
            ],
        )

        # job role
        job_role = iam.Role(
            self,
            "JobRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
        )
        bucket.grant_read_write(job_role)

        # security group
        # cdk creates automatically

        # compute environment
        compute_env = batch.FargateComputeEnvironment(
            self,
            "FargateEnv",
            compute_environment_name=f"{NAME}-compute",
            vpc=vpc,
            maxv_cpus=MAXV_CPUS,
        )

        # job queue
        job_queue = batch.JobQueue(
            self,
            "JobQueue",
            job_queue_name=f"{NAME}-queue",
            compute_environments=[
                batch.OrderedComputeEnvironment(
                    compute_environment=compute_env,
                    order=1,
                )
            ],
        )

        # job definition
        job_definition = batch.EcsJobDefinition(
            self,
            "JobDefinition",
            job_definition_name=f"{NAME}-job",
            container=batch.EcsFargateContainerDefinition(
                self,
                "Container",
                image=ecs.ContainerImage.from_ecr_repository(repository, tag=TAG),
                cpu=CPU,
                memory=Size.mebibytes(MEMORY),
                execution_role=execution_role,
                job_role=job_role,
            ),
        )