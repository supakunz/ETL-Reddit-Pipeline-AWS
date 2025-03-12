import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY


def connect_to_s3():
  try:
      s3 = s3fs.S3FileSystem(anon=False,
                             key = AWS_ACCESS_KEY_ID,
                             secret= AWS_SECRET_KEY)
      print("connected to aws s3!")
      return s3
  except Exception as e:
     print(e)

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket:str) :
  try:
    # ใช้ s3.exists(bucket) เพื่อตรวจสอบว่า bucket มีอยู่แล้วหรือไม่
    if not s3.exists(bucket): # ถ้า ไม่มี (False) → สร้าง bucket
      s3.mkdir(bucket)
      print("Bucket created")
    else : # ถ้า มีอยู่แล้ว (True) → ข้ามไป
      print("Bucket already exists")
  except Exception as e: # ถ้ามีข้อผิดพลาด
      print(e)

def upload_to_s3(s3: s3fs.S3FileSystem, file_path:str, bucket:str, s3_file_name: str):
  try:
      # 📌 อัปโหลดไฟล์ไปยัง S3
      s3.put(file_path, bucket+'/raw/'+s3_file_name) 
      # file_path → ไฟล์ที่ต้องการอัปโหลดจากเครื่อง
      # bucket+'/raw/'+s3_file_name' → ไฟล์จะถูกเก็บใน S3 โฟลเดอร์ raw/
      print("File uploaded to s3")
  except FileExistsError: # ❌ ถ้าไฟล์ต้นทาง (file_path) ไม่เจอ
      print('The file was not found')