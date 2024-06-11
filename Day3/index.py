# Operators

x = 3
#----------------------
y = 5
y += 2
y -= 1
y *= 3
y /= 4
print("y = ", y)
#----------------------
# Lấy phần dư
z = 5
z %= 2
print("z = ", z)
#----------------------
# Lấy phần nguyên
a = 5
a //= 2
print("a = ", a)
#----------------------
# Mũ 
b = 5
b **= 2
print("b = ", b)
#----------------------
# Dạng nhị phân, sử dụng phép bitwise AND tương đương với a = a & b
c = 6
c &= 2
print("c = ", c)
#----------------------
# Dạng nhị phân, sử dụng phép bitwise OR tương đương với a = a | b
d = 5
d |= 2
print("d = ", d)
#----------------------
# Hoán đổi giá trị trị x và y mà không dùng biến tạm
e = 6
e ^= 2
print("e = ", e)
#----------------------
# Dịch qua phải "_" bao nhiêu bit đó
# Dịch qua trái "_" bao nhiêu bit đó
f = 4
f >>= 2
f <<= 2
print("f = ", f)