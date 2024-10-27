class Car():


  def __is_valid_vin(self,vin):
    if not isinstance(vin,int):
      raise IncorrectVinNumber("Некорректный тип vin номера")
      return(False)

    elif vin<1000000 or vin > 9999999:
      raise IncorrectVinNumber("Неверный диапазон для vin номера")
      return(False)

    else:
      return(True)

  def __is_valid_numbers(self,gosnums):
    if not isinstance(gosnums,str):
      raise IncorrectCarNumbers("Некорректный тип данных для номеров")
      return(False)

    elif len(gosnums) < 6 or len(gosnums) > 6:
      raise IncorrectCarNumbers("Неверная длина номера")
      return(False)

    else:
      return(True)

  def __init__(self,model,vin,gosnums):
    if self.__is_valid_vin(vin):
      self.__vin = vin
    if self.__is_valid_numbers(gosnums):
      self.__numbers = gosnums

    self.model = model




class IncorrectVinNumber(Exception):
  def __init__(self,msg):
    self.message = msg


class IncorrectCarNumbers(Exception):
  def __init__(self, msg):
    self.message = msg







try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')