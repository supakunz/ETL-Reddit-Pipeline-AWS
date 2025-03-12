from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta 
import os
import sys

# เพิ่มไดเรกทอรีของโปรเจคลงใน sys.path เพื่อให้ Python สามารถ import โมดูลที่อยู่ในไดเรกทอรีหลักของโปรเจคได้
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'Supakun Thata',
    'depends_on_past': False,
    'start_date': datetime(year= 2025, month= 3, day= 5),
    # 'retries': 2,
    # 'retry_delay': timedelta(minutes=5)
    }

# สร้าง string ที่แสดงวันที่ปัจจุบันในรูปแบบ YYYYMMDD
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline']
)

# extraction from reddit
extrack = PythonOperator(
    task_id ="reddit_extraction", # ชื่อ task
    python_callable = reddit_pipeline, # fuction ที่เรียกใช้
    op_kwargs = { # arg ที่่ส่งไปให้ใน fuction
      'file_name': f'reddit_{file_postfix}',
      'subreddit': 'dataengineering',
      'time_filter': 'day',
      'limit': 100
    },
    dag = dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id = "s3_upload",
    python_callable = upload_s3_pipeline,
    dag = dag
)

extrack >> upload_s3