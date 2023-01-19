per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = []
for v in per_cent.values():
	v = v*money/100
	deposit.append(v)
print(deposit)
print(max(deposit))

