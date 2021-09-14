#case 1: Display all the lines that has either camera or video or both
file=open("log.txt","r")
import re
lines=file.readlines()
print(len(lines))
for line in lines:
     pattern1 = re.compile(r'video|Camera|Camera video')
     result = re.search(pattern1, line)
     if (result != None):
         print(line, end="")

file.close()