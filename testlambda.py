from boto3 import resource, client
import botocore
from datetime import datetime

def lambda_handler(event, context):
    SOURCE_BUCKET_NAME = 'xxxx'
    FILE_NAME = 'temp.json'
    
    s3 = resource('s3')
    try:
        s3.Object(SOURCE_BUCKET_NAME, FILE_NAME).load()
        print("[SUCCESS]", "File Exists with name as",FILE_NAME)
        return {'status':'prevRunNotComplete'}
        
    except botocore.exceptions.ClientError as errorStdOut:
        
        if errorStdOut.response['Error']['Code'] == "404":
            a= errorStdOut.response['Error']['Code'] == "404"
            print("[ERROR]", "File does not exist")
            return {'status':'prevRunComplete'}
        else:
            print("[ERROR]",  "Something went wrong")
            return {'status':'unknown'}
