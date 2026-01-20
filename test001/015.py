with open ('test.txt','wt') as ix:
    ix.write("这就是我")
with open('test.txt','rt') as ox:
    outx=ox.read()
print(outx)