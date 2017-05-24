# How to enable plugin rabbitmq_management and access the management webpage


* (1) Change directory to `rabbitmq_server-3.6.9\sbin` and run cmd below

```
rabbitmq-plugins enable rabbitmq_management
```


* (2) Modified (uncomment) config at rabbitmq_server-3.6.9\etc\rabbitmq.config

```
[{rabbit, [{loopback_users, []}]}],
```


* (3) Restart rabbitmq

```
rabbitmq-service stop
rabbitmq-service start
```


* (4) Access `http://localhost:15672`


