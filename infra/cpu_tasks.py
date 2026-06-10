from aws_cdk import (
    Stack,
    aws_batch as batch,
    aws_ec2 as ec2
)
from constructs import Construct

NAME = "cpu-tasks"
MAXV_CPUS = 16

class CpuTasks(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # vpc
        vpc = ec2.Vpc.from_lookup(
            self,
            "Vpc",
            is_default=True
        )

        # compute environment
        compute_env = batch.FargateComputeEnvironment(
            self,
            "FargateEnv",
            compute_environment_name=NAME,
            vpc=vpc,
            maxv_cpus=MAXV_CPUS,
            spot=True,
        )

        # job queue
        job_queue = batch.JobQueue(
            self,
            "JobQueue",
            job_queue_name=NAME,
            compute_environments=[
                batch.OrderedComputeEnvironment(
                    compute_environment=compute_env,
                    order=1,
                )
            ],
        )
