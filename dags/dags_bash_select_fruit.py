
from __future__ import annotations

import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# 분,시,일,월,요일
with DAG(
    dag_id="dags_conn_test",
    schedule=None,
    start_date=pendulum.datetime(2024, 10, 6, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="t1_orange",
        basg_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )
    t2 = BashOperator(
        task_id="t2_avocado",
        basg_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO"
    )