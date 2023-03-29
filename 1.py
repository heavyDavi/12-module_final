
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада...'))
depositList = []

for key in per_cent:
    value = per_cent[key]
    deposit = value* money / 100
    depositList.append(deposit)

max_deposit = max(depositList)
print(depositList)
print ("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))