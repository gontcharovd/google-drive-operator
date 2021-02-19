from datetime import datetime
from airflow.models.dag import DAG
from airflow.providers.bash import BashOperator

from google_drive_operator import GoogleDriveOperator

dag = DAG(
    dag_id='upload_to_drive',
    description='Create spare parts analysis sheet in Google Drive',
    schedule_interval='@daily',
    start_date=datetime(2021, 2, 10),
    end_date=datetime(2021, 2, 13)
)

create_file = BashOperator(
    task_id='create_file',
    bash_command='echo {{ ds }} >> /tmp/my_file_{{ ds }}.txt',
    dag=dag
)

upload_file = GoogleDriveOperator(
    task_id='upload_file',
    local_path='/tmp/my_file_{{ ds }}.txt',
    drive_folder='/some_project/airflow_upload',
    gcp_conn_id='my_google_drive',
    delegate_to='denis@gontcharov.be',
)

create_file >> upload_file
