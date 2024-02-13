
# user_input_cash = input().split()
# user_input_taxrate = input().split()
"Зададим налоги и доходы компании для примера"
user_input_cash = ['200', '100', '400', '300']
user_input_taxrate = ['10', '20', '30', '40']
user_input_cash = list(map(int, user_input_cash))

user_input_taxrate = list(map(int, user_input_taxrate))
user_input_cash = list(map(int, user_input_cash))
user_input_taxrate = list(map(int, user_input_taxrate))
if len(user_input_taxrate) < len(user_input_cash):
    user_input_taxrate.extend([13] * (len(user_input_cash) - len(user_input_taxrate)))

cash_sort = sorted(user_input_cash)
tax_sorted = sorted(user_input_taxrate, reverse=True)
result = sum(x * (y/100) for x, y in zip(cash_sort, tax_sorted))


# Выводим результат
print(result)
