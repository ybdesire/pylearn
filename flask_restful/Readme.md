# the sample way to build python rest api 


* (1) pip install modules

```
pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```

* (2) run server by `python rest_server.py`

* (3) access the api at web-browser

```
http://127.0.0.1:5002/employees shows ids of all the employees 
http://127.0.0.1:5002/tracks shows tracks details
http://127.0.0.1:5002/employees/3 shows details of employee whose employeeid is 3
```

# RESTful API by HTTP GET & POST

1. api server : [post_get_para/api_server.py](post_get_para/api_server.py)
2. get and post request : [post_get_para/api_usage.py](post_get_para/api_usage.py)


# ref

* [1] https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq







