money = float(input("Сумма вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for i in per_cent:
    deps_1 = float(money * (per_cent[i]) / 100)
    deposit.append(deps_1)
print('deposit=', deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))
