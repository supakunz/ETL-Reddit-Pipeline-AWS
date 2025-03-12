import configparser
import os

# อ่านไฟล์คอนฟิก (config.conf) ที่อยู่ในโฟลเดอร์ config/ โดยใช้ configparser
parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'), encoding='utf-8')

# api_keys
SECRET = parser.get(section= 'api_keys', option= 'reddit_secret_key')
CLIENT_ID = parser.get(section= 'api_keys', option= 'reddit_client_id')

# database
DATABASE_HOST = parser.get(section= 'database',option= 'database_host')
DATABASE_NAME = parser.get(section= 'database',option= 'database_name')
DATABASE_POST = parser.get(section= 'database',option= 'database_port')
DATABASE_USERNAME = parser.get(section= 'database',option= 'database_username')
DATABASE_PASSWORD = parser.get(section= 'database',option= 'database_password')

# AWS
AWS_ACCESS_KEY_ID = parser.get(section= 'aws', option= 'aws_access_key_id')
AWS_SECRET_KEY = parser.get(section= 'aws', option= 'aws_secret_access_key')
AWS_SESSION_TOKEN = parser.get(section= 'aws', option= 'aws_session_token')
AWS_REGION = parser.get(section= 'aws', option= 'aws_region')
AWS_BUCKET_NAME = parser.get(section= 'aws', option= 'aws_bucket_name')

# file_paths
INPUT_PATH = parser.get(section= 'file_paths',option= 'input_path')
OUTPUT_PATH = parser.get(section= 'file_paths',option= 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)

