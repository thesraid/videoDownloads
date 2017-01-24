import fileinput
import re
 
for line in fileinput.input():
    line = re.sub(r'\.(?=\d)', r',', line.rstrip())
    print(line)
