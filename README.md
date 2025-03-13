# Reddit Data Engineering Pipeline on AWS

An end-to-end modern data engineering project, including deployment of an ETL pipeline on Google Cloud Platform. The data is extracted from Supabase ( PostgreSQL ), processed and loaded into BigQuery for analysis, and finally visualized using Power BI to generate an insight dashboard

## Architecture
<img width="1258" alt="Project Architecture" src="https://github.com/user-attachments/assets/9d65b70c-e944-414e-acca-a062d84b4deb">


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
![Uber Data Model](https://github.com/user-attachments/assets/515ce74d-6feb-46c1-8db1-38e050c2ae12)

## Airflow Pipeline
<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/48feae94-1c53-4c0c-822c-8ae6db28ad24">

## Glue ETL
Job ETL:
<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/b4621c07-6b6c-4713-a536-de047350a858">

Crawler:
<img alt="ETL pipeline" src="https://github.com/user-attachments/assets/a55772ed-c89d-441e-b6e5-ef83fb3f7f57">



## Output
<img align="left" src="https://github.com/user-attachments/assets/8ce24728-3f82-4ce9-a346-0886b8da24f5" style="padding-right:30px;" alt="status" height="365" width="375"/>

&nbsp;&nbsp;&nbsp;&nbsp;

<img src="https://github.com/user-attachments/assets/5511c4f9-5e98-4ac8-92b7-132c2e20b164" alt="status"/>

## ❄️ Setup

1. Clone this repository :

```bash
git clone https://github.com/supakunz/Uber-Pipeline-GCP.git
```

2. Navigate to the project folder and Set up the environment variables :

```
cd Uber-Pipeline-GCP
```
- Create a `.env` file in the root directory.

- Add the following variables to the .env file, replacing the placeholder values with your own:

```
AIRFLOW_UID = 50000 # User ID for running Airflow in Docker
# raw_data_path = /opt/airflow/data/raw_uber_data.csv # Path if running on local Docker
raw_data_path = /home/airflow/gcs/data/raw_uber_data.csv # Path on GCS
final_data_path = /home/airflow/gcs/data/uber_data_final.csv # Processed output file path
```

## Contact
Supakun Thata (supakunt.thata@gmail.com)
