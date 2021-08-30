import time
import datetime
import subprocess


def wait_for(timeout_seconds, condition_script):
    start_time = datetime.datetime.now()
    while True:
        if subprocess.call(condition_script, shell=True) == 0:
            return True
        elif (datetime.datetime.now() - start_time).total_seconds() > timeout_seconds:
            return False
        else:
            time.sleep(1)
