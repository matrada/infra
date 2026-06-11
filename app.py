#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infra.cpu_tasks import CpuTasks


app = cdk.App()
env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
cpu_tasks = CpuTasks(app, "CpuTasks", env=env)
cdk.Tags.of(cpu_tasks).add("project", "cpu-tasks")

app.synth()
