# from utils.constants import CLIENT_ID, SECRET
import os
import sys
import pandas as pd
# from pandasgui import show

# เพิ่มไดเรกทอรีของโปรเจคลงใน sys.path เพื่อให้ Python สามารถ import โมดูลที่อยู่ในไดเรกทอรีหลักของโปรเจคได้
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 


from etls.reddit_etl import connect_reddit, extract_posts, tranform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter ='day', limit = None) :
   #connecting to reddit instance
   instance = connect_reddit(CLIENT_ID, SECRET, 'api_data_engineer')
   #extraction
   posts = extract_posts(instance, subreddit, time_filter, limit)
   post_df = pd.DataFrame(posts)
   #transformation
   transformation = tranform_data(post_df)
   
   #Loading to csv
   file_path = f'{OUTPUT_PATH}/output.csv'
   load_data_to_csv(transformation, file_path)

   return file_path # return file_path value ไปเก็บไว้บน xcoms ของ reddit_pipeline
