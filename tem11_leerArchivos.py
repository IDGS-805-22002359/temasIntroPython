from io import open

file = open('file.txt', 'r')

content = file.read()
print(content)
print(type(content))

file.seek(0)
line = file.readline()
print(line)
print(type(line))

lines = file.readlines()
print(lines)
print(type(lines))

for l in lines:
  print(l)

file.close()

