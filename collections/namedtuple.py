from collections import namedtuple

# original tuple
raw_data = ('Sohu', 'Beijing', '100')

named_data = namedtuple('OwnInfo', ['name', 'address', 'people'])

# tuple to a named tuple
new_data = named_data._make(raw_data)

# show new data
print(new_data)# OwnInfo(name='Sohu', address='Beijing', people='100')

# access new data
print(new_data.name)
print(new_data.address)
print(new_data.people)
