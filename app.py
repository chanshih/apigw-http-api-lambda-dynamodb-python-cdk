'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
'''

import aws_cdk as cdk
from stacks.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "ApigwHttpApiLambdaDynamodbPythonCdkStack-PipelineStack")
app.synth()
