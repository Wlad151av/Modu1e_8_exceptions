def add_everything_up(a1,a2):

    try:
        a1 = int(a1)
        a2 = int(a2)
        return(a1+a2)
    except:
        if type(a1) == int:
            a1 = str(a1)
        elif type(a2) == int:
            a2 = str(a2)
        return(str(a1)+str(a2))

p1 = input("Введите первый операнд:")
p2 = input("Введите второй операнд:")

print(add_everything_up(p1,p2))

