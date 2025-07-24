# Reddit Data Engineering Pipeline on AWS

An end-to-end modern data engineering project, including deployment of an ETL pipeline on AWS.The pipeline leverages a combination of tools and services including Apache Airflow, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Architecture
<img width="1258" alt="Project Architecture" src="https://github.com/user-attachments/assets/3cab990d-21d1-4d34-9ece-2e45426ae24c">


## Technology Stack
Languages: 
* Python
* SQL

AWS Platform: 
* Amazon S3
* AWS Glue
* Amazon Athena
* Amazon Redshift

Data Source:
* Reddit API

## Data Storage
The raw data and output files are too large to store in the repository. They are stored on Google Drive.

- **Raw data** link : https://drive.google.com/file/d/1NetxSDnmTlw_foWr8GYJPEz-xEt8Fy53/view?usp=sharing

## Data Modeling
![Uber Data Model](https://github.com/user-attachments/assets/7ced58c2-7210-42ac-98d6-b0d73a353b80)

## Airflow Pipeline
<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/48feae94-1c53-4c0c-822c-8ae6db28ad24">

## Glue ETL

<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/b4621c07-6b6c-4713-a536-de047350a858">

###

<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/a55772ed-c89d-441e-b6e5-ef83fb3f7f57">



## Output

<img src="https://github.com/user-attachments/assets/8ce24728-3f82-4ce9-a346-0886b8da24f5" style="padding-right:30px;" alt="status" height="365" width="375"/>

###

<img src="https://github.com/user-attachments/assets/5511c4f9-5e98-4ac8-92b7-132c2e20b164" alt="status"/>

## ❄️ Setup

1. Clone this repository :
```bash
git clone https://github.com/supakunz/ETL-Reddit-Pipeline-AWS.git
```

2. Navigate to the project folder and Set up the environment variables :
```
cd ETL-Reddit-Pipeline-AWS
```
- Create a `config.conf` file into config folder.
   
- Adding variables to `config.conf` must be consistent with the format of `config.sample.conf` by following the same structure and replacing the required values correctly.

3. Starting the containers :
```
docker-compose up -d
```

4. Launch the Airflow web UI :
```
open http://localhost:8080
```

## 🙋‍♂️ Contact

Developed by **Supakun Thata**  
📧 Email: supakunt.thata@gmail.com  
🔗 GitHub: [SupakunZ](https://github.com/SupakunZ)
