from forex_python.converter import CurrencyRates

c = CurrencyRates()
list = ['USD', 'EUR', 'JPY', 'CHF', 'GBP', 'AUD', 'CAD']
v1 = 0


for loop_1 in list[1:]:
    v1 = c.get_rate(list[0], loop_1)
    for loop_2 in list[0:]:
        try:
            v2 = c.get_rate(loop_1, loop_2)
            r1 = v1 * v2
            if r1 >= 1:
                if loop_2 == list[0]:
                    print(list[0],loop_1, loop_2,r1)
        except Exception:
            print("")

