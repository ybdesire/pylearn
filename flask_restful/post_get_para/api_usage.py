import requests

headers={
    'Content-type':'application/json;charset=UTF-8',
    'Accept':'application/json'
}


# GET
r = requests.get('http://localhost:8002/todos?task=jobs', headers=headers)
print(r.status_code)
x = r.json()
print(x)

# GET
params = {'task':'jobs'}
r = requests.get('http://localhost:8002/todos', params=params, headers=headers)
print(r.status_code)
x = r.json()
print(x)


# POST
r = requests.post('http://localhost:8002/todos', json={"task": "jobs"})
print(r.status_code)
x = r.json()
print(x)


