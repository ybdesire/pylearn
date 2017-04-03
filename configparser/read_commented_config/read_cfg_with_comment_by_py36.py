# python 3

import configparser

# init
cf = configparser.ConfigParser()
cf.read('config.ini')# read config file

# read parameter
ip = cf['network']['ip']
password = cf['auth']['password']

print('ip = {0}, password = {1}'.format(ip, password))

