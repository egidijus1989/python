# LEGB

txt = "Globali sritis"
def fun1():
    txt = "Enclosing sritis"
    def fun2():
        txt = "Lokali stritis"
        print(f'fun2 = {txt}')
    fun2()
    print(f'fun1 = {txt}')
fun1()
print(f'Virsus = {txt}')