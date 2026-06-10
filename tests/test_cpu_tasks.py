import aws_cdk as cdk
import pytest
from aws_cdk.assertions import Template

from infra.cpu_tasks import CpuTasks


@pytest.fixture(scope="module")
def template():
    app = cdk.App()
    stack = CpuTasks(
        app,
        "CpuTasks",
        env=cdk.Environment(account="123456789012", region="eu-central-1"),
    )
    return Template.from_stack(stack)


def test_fargate_compute_environment(template):
    template.has_resource_properties(
        "AWS::Batch::ComputeEnvironment",
        {
            "ComputeEnvironmentName": "cpu-tasks",
            "ComputeResources": {"Type": "FARGATE_SPOT"},
        },
    )


def test_job_queue_wired_to_compute_environment(template):
    template.has_resource_properties(
        "AWS::Batch::JobQueue",
        {"JobQueueName": "cpu-tasks"},
    )
