from celery import Celery

# celery based on rabbitmq
RABBIT_HOST = "rabbitmq-xxx.net"
RABBIT_PORT = 5672
RABBIT_USER = "your_username"
RABBIT_PWD = "your_password"
RABBIT_VHOST = "your_vhost"
CELERY_BACKEND = 'amqp'
BROKER_URL = 'amqp://%s:%s@%s:%d/%s' %(RABBIT_USER, RABBIT_PWD, RABBIT_HOST, RABBIT_PORT, RABBIT_VHOST)
TASK_NAME = "celery_worker.task_your"

celery = Celery("", backend=CELERY_BACKEND, broker=BROKER_URL)


@celery.task(name=TASK_NAME, ignore_result=True, serializer='json')
def task_your(dt):
    value1 = dt["key1"]
    value2 = dt["key2"]
    value3 = dt["key3"]

# how to run worker
# celery worker -A celery_worker -l INFO --concurrency=1