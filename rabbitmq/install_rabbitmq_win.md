# Environment setup for rabbitmq at Win


* (1) Download and install "OTP 19.3 Windows 64-bit Binary File" from [here](http://www.erlang.org/downloads).
* (2) Set environment variable `ERLANG_HOME` to Erlang installation.
* (3) Download and install rabbitmq-server-3.6.9.exe from [here](https://www.rabbitmq.com/install-windows.html).
* (4) Start CMD as administrator.
* (5) Start rabbitmq from it's installation folder by command `rabbitmq-service start`.

```
E:\xxx\rabbitmq_server-3.6.9\sbin>rabbitmq-service start
F:\xxx\erl8.3\\erts-8.3\bin\erlsrv: Service RabbitMQ started.
```


* (6) If get error "Failed to start service RabbitMQ", then run the 3 cmds below
   * `rabbitmq-service remove`
   * `rabbitmq-service install`
   * `rabbitmq-service start`
   
   
   
# Check if rabbitmq installed correctly by python

* (1) run `rabbitmq-service start` as above.
* (2) `pip install pika`
* (3) rabbitmq success if below python code run without error.

```
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
```   