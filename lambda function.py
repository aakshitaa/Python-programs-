tuple1 = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
maximum = max(tuple1, key=lambda a: a[1])[1]
minimum = min(tuple1, key=lambda b: b[1])[1]
print("Maximum and minimum values of the said list of tuples:")
print("(%d,%d)" % (maximum, minimum))