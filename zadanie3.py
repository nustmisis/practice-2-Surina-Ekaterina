import re
s = input("Nomer - ")
if re.fullmatch('\d{4}[A-Z]{3}', s): 
    print ("new")
elif re.fullmatch('[A-Z]{3}\d{3}', s):
    print("old")
else: 
    print ("not number")