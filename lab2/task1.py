money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
cnt_months = 1
money_capital = money_capital - (spend - salary)
while money_capital + salary >= spend * increase + spend:
    spend = spend + spend * increase
    money_capital = money_capital - (spend - salary)
    cnt_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", cnt_months)