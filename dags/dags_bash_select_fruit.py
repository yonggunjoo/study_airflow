
from __future__ import annotations

import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# 분,시,일,월,요일
with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"  # 오타 수정
    )
    t2 = BashOperator(
        task_id="t2_avocado",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh AVOCADO"  # 오타 수정
    )