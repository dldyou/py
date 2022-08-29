f = open('./savefile.txt', 'r')

a = f.readline()
b = f.readline()

print(a)
print(b)
print(a+b)

f.close()