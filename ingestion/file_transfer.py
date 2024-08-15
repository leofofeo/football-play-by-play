import boto3
import requests
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def fetch_and_store_csv_in_s3(start_year: int, end_year: int, bucket_name: str):
    s3_client = boto3.client('s3')

    for year in range(start_year, end_year + 1):
        url = f"https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{year}.csv"
        file_name = f"play_by_play_{year}.csv"
        s3_key = f"{file_name}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            # Upload the file to S3
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

if __name__ == "__main__":
    START_YEAR = 2004
    END_YEAR = 2023
    BUCKET_NAME = 'yearly-play-by-play-data'

    fetch_and_store_csv_in_s3(START_YEAR, END_YEAR, BUCKET_NAME)
