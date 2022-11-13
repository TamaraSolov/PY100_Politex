# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
dict_hex = {i: hex(i) for i in range(16)}
# for i in dict_hex:
#     dict_hex['hex'] = dict_hex.pop(i)
pprint(dict_hex)
dict_dec = {i for i in range(1, 16)}
pprint(dict_dec)
dict_bin = {i: bin(i) for i in range(16)}
pprint(dict_bin)
dict_oct = {i: oct(i) for i in range(16)}
