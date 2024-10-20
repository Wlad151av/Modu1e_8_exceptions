def personal_sum(numbers):
    n_sum = 0
    incorrect_data = 0
    for num in numbers:
        try:
            n_sum += num
        except TypeError:
            incorrect_data += 1
    return (n_sum,incorrect_data)


def calculate_average(numbers):
    n_sum = 0
    incorrect_data = 0
    for num in numbers:
        if type(num) == (int,float):
            n_sum += 1
    try:
        crct_num,incrt_num = personal_sum(numbers)
        return(crct_num/n_sum)
    except ZeroDivisionError:
        print("Исключение делёжки на нуль обработано")
        return(0)


print(personal_sum((2,5,'sdg',8)))
print(calculate_average((3,"dfsd",8,4,"ec")))
    
