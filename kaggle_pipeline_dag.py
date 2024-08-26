from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from modules.kaggle_data_download import download_kaggle_dataset
from modules.kaggle_data_load_to_gcs import upload_to_gcs

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 26),
    'depends_on_past': False
}

dag = DAG('Kaggle_dataset_pipeline',
          default_args=default_args,
          description='Downloads a dataset from Kaggle and uploads it to GCS',
          schedule_interval='@daily',
          catchup=False)

download_kaggle_dataset_task = PythonOperator(
    task_id='download_kaggle_dataset_task',
    python_callable=download_kaggle_dataset,
    dag=dag
)

upload_to_gcs_task = PythonOperator(
    task_id='upload_to_gcs_task',
    python_callable=upload_to_gcs,
    dag=dag
)

download_kaggle_dataset_task >> upload_to_gcs_task