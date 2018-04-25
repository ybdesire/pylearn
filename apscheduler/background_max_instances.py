from apscheduler.schedulers.background import BackgroundScheduler
import time,os,threading

def job():
    print('job thread_id-{0}, process_id-{1}'.format(threading.get_ident(), os.getpid()))
    time.sleep(50)

if __name__=='__main__':
    job_defaults = { 'max_instances': 20 }
    sched = BackgroundScheduler(timezone='MST', job_defaults=job_defaults)
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()
    
    while(True):
        print('main 1s')
        time.sleep(1)
