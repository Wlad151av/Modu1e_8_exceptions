def add_everything_up(a1,a2):
    try:
        return(int(a1)+int(a2))
    except:
        return(str(a1)+str(a2))

p1 = input("Введите первый операнд:")
p2 = input("Введите второй операнд:")

print(add_everything_up(p1,p2))

