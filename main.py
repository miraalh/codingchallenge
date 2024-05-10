import sys
import os
# ./mygrep [query] [path]

output = []

arguments = sys.argv
query  = sys.argv[1]
path = sys.argv[2]
cwd = os.getcwd()

subs = os.listdir(path)
os.chdir(path)

for s in subs:
    if(os.path.isfile(s)):
        with open(s) as myFile:
            for num, line in enumerate(myFile, 1):
                if query in line:
                    # print('found at line:', num)
                    output.append(cwd + s  +':' + str(num) + '\t' + line)
        # print("file")
    elif os.path.isdir(s):

        print("dir")
print(output)
#
# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# subdirs = [x[0] for x in os.walk('.')]
#
# for f in files:
#     print(f)
#
# for s in subdirs:
#     print(s)
