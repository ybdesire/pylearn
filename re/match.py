import re

rx = 'contacts.*'# regular expression

for s in ['contacts','contacts123','contacts.xx','con']:# check if strings match the re
    z = re.match(rx, s)
    print(z)

'''
<re.Match object; span=(0, 8), match='contacts'>
<re.Match object; span=(0, 11), match='contacts123'>
<re.Match object; span=(0, 11), match='contacts.xx'>
None
'''
