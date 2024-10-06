
from __future__ import annotations

import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

# 분,시,일,월,요일
with DAG(
    dag_id="dags_conn_test",
    schedule=None,
    start_date=pendulum.datetime(2024, 10, 6, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = EmptyOperator(
        task_id="t1"
    )
    t2 = EmptyOperator(
        task_id="t2"
    )
    t3 = EmptyOperator(
        task_id="t3"
    )
    t4 = EmptyOperator(
        task_id="t4"
    )
    t5 = EmptyOperator(
        task_id="t5"
    )
    t6 = EmptyOperator(
        task_id="t6"
    )
    t7 = EmptyOperator(
        task_id="t7"
    )
    t8 = EmptyOperator(
        task_id="t8"
    )
    
    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4,t7] >> t6 >> t8