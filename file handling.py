
'''File Handling'''
import os
with open("nikhi.txt","w") as f:
    s=f.read()
    print(s)
    f.close()

s=s.replace("introduction","bellary")

with open("fiil.txt","r") as f:
    print(f.tell())
    f.seek(-35,2)
    print(b"#")
    print(f.read().decode('utf-8'))
    f.close()