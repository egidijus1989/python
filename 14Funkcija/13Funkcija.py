# LEGB

sk = 5
def fun1():
    global sk
    sk += 1
    def fun2():
        global sk
        sk += 5
        print(f'fun2 = {sk}') #su klaidomis
    fun2()
    print(f'fun1 = {sk}') #su klaidomis
fun1()
print(f'Virsus = {sk}') #su klaidomis

a = None
for i in range(5):
    a = i
    print(i * i)
    
print(i)
print(a)