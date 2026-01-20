def exec_code():
    LOC="""
def f(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(f(4))
    """
    exec (LOC)
exec_code()