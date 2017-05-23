# How to run the program



* (1) Install rabbitmq at win by steps [here](../install_rabbitmq_win.md)
* (2) Run send.py
* (3) Run rcv.py. This program will enter a never-ending loop that waits for data
* (4) We can run send.py many times, and each time we run send.py, we will get below output


```
(env_celery_test) E:\xxx\xxx\prog\pylearn\rabbitmq\send_receive_msg>python rcv.py
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
```