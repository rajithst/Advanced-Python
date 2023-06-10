

b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = 'This is a string'
print(s)

# Decode bytes to string
b2 = b.decode('utf-8')
print(s + b2)

# Encode string to bytes
s2 = s.encode('utf-8')
print(b+s2)

