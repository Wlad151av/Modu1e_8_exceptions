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
        try:
            return(personal_sum(numbers)/len(numbers))
        except ZeroDivisionError:
            print("Исключение делёжки на нуль обработано")
            return(0)
    
