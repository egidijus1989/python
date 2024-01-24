x = 5
def fun1():
    x = 121212
    def fun2():
        nonlocal x
        x = 100000
        print(x)
    fun2()
    print(x)
fun1()
print(x)