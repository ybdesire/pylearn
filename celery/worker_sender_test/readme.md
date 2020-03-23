# how to run

the demo is based on celery and rabbit-mq.

1. run worker

```
celery worker -A celery_worker -l INFO --concurrency=1
```

we can also run multi-workers at multi-servers.


2. run sender

```
python celery_sender
```

