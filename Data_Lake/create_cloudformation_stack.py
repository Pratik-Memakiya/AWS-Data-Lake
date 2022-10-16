import boto3
def lambda_handler(event, context):
    client = boto3.client('cloudformation')
    
    response = client.create_stack(
        StackName='sahil-data-lake-stack',
        TemplateURL='https://sahil-data-lake-cloud-formation-script.s3.ap-south-1.amazonaws.com/data_lake_cloudformation_infra_script.yml',
        DisableRollback=True,
        Capabilities=[
            'CAPABILITY_NAMED_IAM',
        ],
    )
    
    return response