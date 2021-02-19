FROM apache/airflow:2.0.1-python3.8

WORKDIR ${AIRFLOW_HOME}

RUN mkdir ${AIRFLOW_HOME}/tmp

RUN pip install --upgrade pip \
  && pip install 'apache-airflow-providers-google'

USER airflow
