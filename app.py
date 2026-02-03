#!/usr/bin/env python3
import os

import aws_cdk as cdk

from infra.batch_extract import BatchExtract


app = cdk.App()
BatchExtract(app, "BatchExtract",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
