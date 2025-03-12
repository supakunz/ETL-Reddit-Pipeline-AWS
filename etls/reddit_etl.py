import praw
from praw import Reddit # ไลบรารี praw ซึ่งเป็นไลบรารีสำหรับเชื่อมต่อกับ Reddit API
import sys
import pandas as pd
import numpy as np
from utils.constants import POST_FIELDS

# fuction ที่เชื่อมต่อ Reddit API
def connect_reddit(client_id, client_secret, user_agent) -> Reddit: # -> Reddit #หมายถึงฟังก์ชันนี้ควรคืนค่าเป็นอ็อบเจ็กต์ของคลาส Reddit
    # try-except เหมือน try-catch
    try: 
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent,
                             username="gunbyboy02",
                             password="gun053795606"
                             )
        print("connected to reddit!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1) # บังคับให้โปรแกรมหยุดทำงานทันที โดยคืนค่า 1 (หมายถึง เกิดข้อผิดพลาด)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None) :
    
    # ตั้งค่า Reddit API
    reddit = praw.Reddit(
        client_id="9Y3cPg1Hv6OsWqIXt_6R_A",
        client_secret="4_12BUoui7hmFxcp9quAEeqemeYmTg",
        user_agent="api_data_engineer",
        username="gunbyboy02",
        password="gun053795606"
    )
    
    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)

    return post_lists

def tranform_data(post_df: pd.DataFrame):
    # แปลง created_utc เป็น datetime
    # unit='s' กำหนดให้ Pandas แปลงค่า timestamp ที่อยู่ในหน่วยวินาที (seconds) เป็น datetime
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s') # ถ้า colunm ชื่อเหมือนกันจะเอาไปแทนที่
    
    # np.whre เหมือน if-else --> np.where(condition, value_if_true, value_if_false)
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)

    # แปลงค่าในคอลัมน์ author ให้เป็นประเภทข้อมูล string (str) โดยใช้ astype(str)
    post_df['author'] = post_df['author'].astype(str) # เปลี่ยนค่าข้างในให้เป็น string ✅ แต่ dtype ยังคงเป็น object เพราะเป็น default ของ Pandas

    edited_mode = post_df['edited'].mode() # ค่าที่พบบ่อยๆที่จุด False
    
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]), 
                                 post_df['edited'], edited_mode).astype(bool)
    # เช็คว่าค่าใน post_df['edited'] เป็น True หรือ False หรือไม่
    # ถ้าใช่ → คงค่าเดิมไว้
    # ถ้าไม่ใช่ → แทนที่ด้วย edited_mode (ค่าที่พบบ่อยที่สุด -> False)
    # แปลงค่าทั้งหมดให้เป็น bool

    # แปลง type ใน DataFrame
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path ,index=False)