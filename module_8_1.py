def add_everything_up(a1,a2):

    try:
        if type(int(a1)) == int or type(int(a1)) == float:
            a1 = int(a1)
            if type(int(a2)) == int or type(int(a2)) == float:
                a2 = int(a2)
                return(a1+a2)
    except:
        return(str(a1)+str(a2))

p1 = input("Введите первый операнд:")
p2 = input("Введите второй операнд:")

print(add_everything_up(p1,p2))

