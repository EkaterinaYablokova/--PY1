from pprint import pprint

result = []
for i in range(16):
    num = {
        'bin': bin(i),
        'dec': i,
        'hex': hex(i),
        'oct': oct(i)
    }
    result.append(num)

pprint(result)
