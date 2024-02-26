def func1():
    print(" holaaX ")
def func2():
    print(" holaa D")

def main():
    listaLoca = [func1, func2]
    for f in listaLoca:
        f()

main()