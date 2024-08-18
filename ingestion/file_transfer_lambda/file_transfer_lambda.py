import boto3
import requests
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError
from datetime import datetime

def fetch_and_store_csv_in_s3(year: int, bucket_name: str):
    s3_client = boto3.client('s3')

    url = f"https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{year}.csv"
    file_name = f"play_by_play_{year}.csv"
    s3_key = f"{file_name}"

    # Check to see if the file already exists in the s3 bucket
    try:
        s3_client.head_object(Bucket=bucket_name, Key=s3_key)
        print(f"{file_name} already exists in s3://{bucket_name}/{s3_key}. Skipping download.")
        return
    except ClientError as e:
        print(f"{file_name} does not exist in s3://{bucket_name}/{s3_key}. Continuing to fetch step.")
        pass

    try:
        response = requests.get(url)
        response.raise_for_status()

        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=response.content,
            ContentType='text/csv'
        )
        print(f"Successfully uploaded {file_name} to s3://{bucket_name}/{s3_key}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {file_name} from {url}. Error: {e}")
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Failed to upload {file_name} to S3. Check your AWS credentials. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def lambda_handler(event, context):
    YEAR = datetime.now().year - 1
    BUCKET_NAME = 'yearly-play-by-play-data'

    fetch_and_store_csv_in_s3(YEAR, BUCKET_NAME)

    return {
        'statusCode': 200,
        'body': f'Successfully processed data for {YEAR}'
    }
