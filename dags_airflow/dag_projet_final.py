from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.email import EmailOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python import BranchPythonOperator


directory ="/mnt/c/Users/Mansour3GUEYE/Desktop/DBTATOSPROJET/airbnb"

def process_data(**context):
    data = context['task_instance'].xcom_pull(task_ids="runseed")
    context['task_instance'].xcom_push(key="status_seed",value=data)

def process_data_test(**context):
    data = context['task_instance'].xcom_pull(task_ids="runtest")
    context['task_instance'].xcom_push(key="status_test",value=data)



def status_seed_to_dict(input):
    if input:
        words = input.split()
        results = {}
        for word in words:
            if '=' in word:
                key, value = word.split('=')
                results[key] = int(value)
        return results
    return {}

def branch_func(**kwargs):
    ti = kwargs['ti']
    xcom_value = ti.xcom_pull(task_ids="status_seed")
    status_results = status_seed_to_dict(xcom_value)
    error_count = status_results.get("ERROR",0)

    if int(error_count) == 0:
        return "runtest"
    else:
        return "send_email_error"

def branch_func_test(**kwargs):
    ti = kwargs['ti']
    xcom_value = ti.xcom_pull(task_ids="status_test")
    status_results = status_seed_to_dict(xcom_value)
    error_count = status_results.get("ERROR",0)

    if int(error_count) == 0:
        return "runseed1"
    else:
        return "send_email_error"

    

with DAG(
    dag_id="dbt_final_projet",
    default_args={
        "retries": 1,
    },
    description="Lancement job chaque 8h",
    schedule="0 8 * * *",
    start_date=datetime(2023, 9, 6),
    catchup=False,

) as dag:
    start_dag = EmptyOperator(task_id="start_dag")


    runseed = BashOperator(
        task_id="runseed",
        bash_command=f'cd {directory} && dbt seed',
    )
    
    runtest = BashOperator(
        task_id="runtest",
        bash_command=f'cd {directory} && dbt test',
    )
    

    python_task = PythonOperator(
        task_id='python_task',
        python_callable=process_data,
        provide_context=True
    )


    branch = BranchPythonOperator(
        task_id="branch_task",
        python_callable=branch_func,
    )
    branch_test = BranchPythonOperator(
        task_id="branch_task_test",
        python_callable=branch_func_test,
    )

    send_email_error = EmailOperator(
    task_id='send_email_error',
    to='sorogueye93@gmail.com',
    subject='error',
    html_content="Date: {{ ds }}",
    )
    send_email_succes = EmailOperator(
    task_id='send_email_succes',
    to='sorogueye93@gmail.com',
    subject='success',
    html_content="Date: {{ ds }}",
    )
    runseed1 = BashOperator(
        task_id="runseed1", 
        bash_command= f'cd {directory} && dbt run',  
    )
    start_dag >> runseed >> python_task >>branch >> [send_email_error,runtest]
    runtest >> branch_test >> [send_email_error,runseed1] 
    runseed1 >>send_email_succes    
  
