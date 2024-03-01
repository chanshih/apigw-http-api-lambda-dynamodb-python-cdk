from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    Environment 
)
from stacks.pipeline_stage import PipelineStage

class PipelineStack(Stack):
    
    def __init__(self, scope: Construct, id: str,env=None, **kwargs) -> None:
        super().__init__(scope, id,env=env, **kwargs)
        #for gitlab
        pipeline = pipelines.CodePipeline(self, "Pipeline",
            cross_account_keys=True,
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.connection("chanshih/apigw-http-api-lambda-dynamodb-python-cdk", "main",
                    connection_arn="arn:aws:codestar-connections:ap-southeast-2:690155231179:connection/ce055da4-7d81-4b81-b52f-fffda975ad3a"
                ),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                    ]
                )    
        )
        
        ##deploy_dev = PipelineStage(self,"Deploy")#
        deploy_stage = pipeline.add_stage(PipelineStage(self,"Prod",env=Environment(account="381895544333",region="ap-southeast-2")))
