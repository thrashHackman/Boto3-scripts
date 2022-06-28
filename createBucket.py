import boto3

#Creates an S3 client.
s3_client = boto3.client('s3')

# Uploads the file to the Bucket
# In order to use the 'Bucket' attribute we need to create a resource of s3.
s3_resource = boto3.resource('s3')


s3_client.create_bucket(Bucket='YOUR BUCKET NAME')