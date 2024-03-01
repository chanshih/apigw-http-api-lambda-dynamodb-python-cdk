from constructs import Construct
from aws_cdk import (
    Stage,
    Tags
)
from stacks.apigw_http_api_lambda_dynamodb_python_cdk_stack import ApigwHttpApiLambdaDynamodbPythonCdkStack

class PipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        stack = ApigwHttpApiLambdaDynamodbPythonCdkStack(self, 'ApigwHttpApiLambdaDynamodbPythonCdkStack', stage=str(id))
        Tags.of(stack).add("auto-delete","no")
