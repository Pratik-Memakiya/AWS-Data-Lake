Work Flow of datalake with automated stack:
step 1: create lambda function with [IAMFullAccess, AmazonS3FullAccess, CloudWatchFullAccess, AWSGlueServiceRole, AWSGlueConsoleFullAccess, AWSCloudFormationFullAccess] iam role permission and attached create_cloudformation_stack.py file's code.
step 2: after lambda function created and stack successfully created without any error
step 3: upload aws-glue-etl-job-data-tranform-script.py file on s3 which are used in aws glue etl job data transformation
step 4: upload data file to "original" s3 bucket which we want to tranform using aws glue
step 5: run original data crawler 
step 6: check new table is generated or not
step 7: after table generated run etl job
step 8: after etl job successfully executed run result data crawler
step 9: open athena console and fire query for select result table data
