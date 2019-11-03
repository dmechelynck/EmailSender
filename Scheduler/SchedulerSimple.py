from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import time

user="dmechelynck"


path_to_vitual_env="/home/"+user+"/Builds/EmailSender/python/bin/python"

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



dag = DAG("EmailSenderSimple", default_args=default_args, schedule_interval='0 1 * * *')


t1 = BashOperator(
    task_id='SendEmailPerson1',
    bash_command = path_to_vitual_env + ' /home/'+ user +'/Builds/EmailSender/code/EmailSender/EmailSender.py' + " " + 'diego@agilytic.be' + " " + '"Hellooo Youuuuuuu"',
    dag=dag)

t2 = BashOperator(
    task_id='SendEmailPerson2',
    bash_command = path_to_vitual_env + ' /home/'+ user +'dmechelynck/Builds/EmailSender/code/EmailSender/EmailSender.py' + " " + 'diego.mechelynck@gmail.com'  + " " + '"Hellooo Youuuuuuu"',
    dag=dag)

t3 = BashOperator(
    task_id='DoneMessage',
    bash_command='echo "done"',
    trigger_rule=TriggerRule.ALL_SUCCESS, #ALL_SUCCESS is the value by default
    dag=dag)


t3.set_upstream([t1, t2])
