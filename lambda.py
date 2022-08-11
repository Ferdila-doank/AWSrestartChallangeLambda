import boto3
import os
import pandas as pd

def lambda_handler(event, context):
    
    bucket_name = "wordcounttesting"
    df = pd.DataFrame(columns=['file_name','last_modified'])
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket=bucket_name)['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
    
    for i in objs:
        row_append = {'file_name': i['Key'] , 'last_modified': i['LastModified']}
        df = df.append(row_append,ignore_index=True)

    filename = df.loc[df['last_modified'].idxmax()]['file_name']
    
    fileObj = s3.get_object(Bucket=bucket_name, Key=filename)
    file_content = fileObj["Body"].read().decode("utf-8")
    
    all_file_content = file_content.rstrip().split()
    
    print("The word count in the file " + filename + " is " + str(len(all_file_content)) + ".") 
    
    send_email = boto3.client('sns')
    response = send_email.publish(
        TopicArn="arn:aws:sns:us-east-1:048348913545:email",
        Message="The word count in the file " + filename + " is " + str(len(all_file_content)) + ".",
        Subject= "Word Count Result"
        )
