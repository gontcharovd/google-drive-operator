# Apache Airflow Google Drive Operator

Upload a local file to your Google Drive account. Read the full guide on [Medium](https://medium.com/towards-data-science/how-to-upload-files-to-google-drive-using-airflow-73d961bbd22).

This repository contains code that covers uploading files to Google Drive using Airflow in four steps:

1. Configuring the Google Drive API and a creating service account on GCP
2. Configuring Domain-wide Delegation on our Google Workspace
3. Writing the code for our custom GoogleDriveOperator
4. Testing a minimal DAG that uploads a text file to our Google Drive account
