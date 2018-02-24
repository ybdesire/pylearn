import re
line = "should we use regex more often? let me know at  321dsasdsa@dasdsa.com"
match = re.search(r'[\w\.-]+@[\w\.-]+', line)
print(match.group(0))
# '321dsasdsa@dasdsa.com'
