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


dt = {"key1":"value1", "key2":"value2", "key3":"value3"}

celery.send_task(TASK_NAME, args=[dt])

