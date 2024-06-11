# STRINGS
# Creating a String
letter = "P"
greeting = "Hello, World!"
print("letter: ", letter)
print("greeting: ", greeting)

# Multiline String
multiline_greeting1 = '''
    Toi ten la Hung
    Toi 25 tuoi
    Toi la sinh vien
'''
multiline_greeting2 = """
    Toi ten la Nghi
    Toi 24 tuoi
    Toi la quan ly
"""
print("multiline_greeting: ", multiline_greeting1)
print("multiline_greeting: ", multiline_greeting2)

# String Concatenation
first_name = "Tong"
last_name = "Hung"
space = " "
fullName = first_name + space + last_name
print("Full name: ", fullName)

# Escape Sequences in Strings
# \n xuong dong
print("My name is \n Hung")
# \t tao khoang cach 8 ky tu
print("How are \t you")
# \\ viết một dấu chéo
print("MiniCapstones is very good for students (\\)")
# \' \" viết một dấu ' " được hiển thị ra output
print("I like python\'")

# String formating 
# String only - %s gọi một chuỗi khác và chuỗi hiện tại
a = "Hung"
b = "Quang"
fullName_format = "I am %s %s" %(a, b)
print(fullName_format)
# String & numbers - %d gọi một số nguyên - %....f: ... là lấy bao nhiêu số 0, số thực
radius = 10
pi = 3.14
area = pi * radius**2
formated_String = 'The area of circle with a radius %d is %.2f' %(radius, area)
print(formated_String)

# String formating - new
# Sử dụng {}
c = "Hung"
d = "Quang"
fullName_cd = "I am {} {}".format(c, d)
print(fullName_cd)
# Bổ sung
e = 2
f = 5
print('{} + {} = {}'.format(e, f, e + f))
print('{} / {} = {:.2f}'.format(f, e, f / e)) # giới hạn lấy bao nhiêu số sau dấu ,

# String interpolation
# sử dụng f ở đầu chuỗi
g = 5
h = 8
print(f'{g} + {h} = {g + h}')

# Python Strins as Sequence character
language = 'Python'
first_language = language[0]
# right end
last_language = language[-1]
print(last_language)

# Slicing Python Strings
# cắt chuỗi từ 0 đến 3 nhưng ko bao gồm 3
slice1 = language[0:3]
print(slice1)
# cách khác
slice2 = language[-3:]
print(slice2)

# Reversing a String
# -1 là lấy 1 ký tự dưới lên
# -2 là lấy cách 2 ký tự dưới lên
country = "abcdefghi"
print(country[::-2])

