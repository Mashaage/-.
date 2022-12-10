from pprint import pprint
table = list()
for i in range(0, 16):
    dict = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    table.append(dict)
pprint(table)