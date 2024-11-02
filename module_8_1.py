def add_everything_up(a1,a2):

    try:
        res = a1+a2
    except:
        if type(a1) == int or type(a1) == float:
            a1 = str(a1)
            
        elif type(a2) == int or type(a2) == float:
            a2 = str(a2)
        res = a1+a2
    if type(res) == float:
        width = max(len(str(a1)),len(str(a2)))
        res = str(res)[:width]
    return(res)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
