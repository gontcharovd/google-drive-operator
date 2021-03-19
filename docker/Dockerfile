FROM apache/airflow:2.0.1-python3.8

WORKDIR ${AIRFLOW_HOME}

RUN mkdir ${AIRFLOW_HOME}/tmp

COPY airflow-to-drive-308020-f4e5a3186f4d.json .

RUN pip install --upgrade pip \
  && pip install 'apache-airflow-providers-google'

USER airflow
