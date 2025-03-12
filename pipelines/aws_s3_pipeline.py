import s3fs
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME


def upload_s3_pipeline(ti):
  # ดึง file_path จาก xcoms ของ reddit_pipeline
  file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value') # /opt/airflow/data/output/output.csv

  s3 = connect_to_s3()
  create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
  upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1]) # file_path.split('/')[-1] => output.csv
