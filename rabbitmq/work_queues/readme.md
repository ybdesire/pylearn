# How to run the program



* (1) Install rabbitmq at win by steps [here](../install_rabbitmq_win.md)
* (2) Run 2 rcv.py (workers) at 2 cmds. Those programs will enter a never-ending loop that waits for data
* (3) Run send_task.py msg 
* (4) We can run send_task.py msg many times, and we can see RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the same number of messages

* http://www.rabbitmq.com/tutorials/tutorial-two-python.html

