from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines
)
from stacks.pipeline_stage import PipelineStage

class PipelineStack(Stack):
    
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        #for gitlab
        pipeline = pipelines.CodePipeline(self, "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection("chanshih/apigw-http-api-lambda-dynamodb-python-cdk", "main",
                    connection_arn="arn:aws:codestar-connections:ap-southeast-2:381895544333:connection/8ab65b77-210c-4371-b600-e3bd818c5844"
                ),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                    ]
                )    
        )
        
        ##deploy_dev = PipelineStage(self,"Deploy")#
        deploy_stage = pipeline.add_stage(PipelineStage(self,"Prod"))
