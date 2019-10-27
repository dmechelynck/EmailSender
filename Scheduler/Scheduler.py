from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import time


path_to_vitual_env="/home/dmechelynck/Builds/EmailSender/python/bin/python"

n=time.strftime("%Y,%m,%d")
v=datetime.strptime(n,"%Y,%m,%d")
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date':  "2019-10-26",
    'email': ['diego@agilytic.be'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),

}



dag = DAG("TimePrinter_Scheduler", default_args=default_args, schedule_interval='0 1 * * *')


t1 = BashOperator(
    task_id='SendEmailPerson1',
    bash_command = path_to_vitual_env + ' /home/dmechelynck/Builds/Dummy-Api/code/EmailSender/EmailSender.py' + 'diego@agilytic.be',
    dag=dag)

t2 = BashOperator(
    task_id='SendEmailPerson2',
    bash_command = path_to_vitual_env + ' /home/dmechelynck/Builds/Dummy-Api/code/EmailSender/EmailSender.py' + 'diego.mechelynck@gmail.com',
    dag=dag)

t3 = BashOperator(
    task_id='DoneMessage',
    bash_command='echo "done"',
    dag=dag)


t3.set_upstream([t1, t2])