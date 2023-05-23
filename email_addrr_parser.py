import re

pattern_email = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

to_parse = input("Enter path to a file to be analized:\n")

with open(to_parse,'r') as source:   
    result = re.findall(pattern_email,source.read())
    print(result)

with open('output.txt','w') as output:
    for i in result:
        output.write(i+'\n')

