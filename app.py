'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

import aws_cdk as cdk
from aws_cdk import (
    Environment 
)
from stacks.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "ApigwHttpApiLambdaDynamodbPythonCdkStack-PipelineStack",Environment(account="690155231179",region="ap-southeast-2"))
app.synth()
