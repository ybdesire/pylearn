from apscheduler.schedulers.background import BackgroundScheduler
import time

def job():
    print('job 3s')


if __name__=='__main__':

    sched = BackgroundScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()
    
    while(True):
        print('main 1s')
        time.sleep(1)
