import re

str='Welcome @ To %% Python'

regex=re.compile('@%')

if (regex.search(str)==None):
    print("No Special Characters were found in the given string")
else:
    print("Special Characters found")