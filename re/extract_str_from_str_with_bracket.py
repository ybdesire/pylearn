import re

text = '''LinuxOS_Network{NET("10.0.0.1"f) & NET("10.0.0.2"f) & NET("10.0.0.3"f)}+version("666")'''
found = re.findall('NET\("(.+?)"f\)', text)
print(found)# ['10.0.0.1', '10.0.0.2', '10.0.0.3']