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

# Skipping Characters While Slicing
# 0: điểm bắt đầu, 6: là điểm kết thúc, 2: là step
language1 = 'Python'
pto = language1[0:2:6]
print(pto)

# String method
# capitalize: ghi hoa chữ đầu
ab = "quang Hung"
print(ab.capitalize())

# count: đếm cụm từ có bao nhiêu trong chuỗi, và đếm từ khoảng bao nhiêu
ac = "Hello, how are you today"
print(ac.count('o'))
print(ac.count('o', 4, 14))

# endswith: kiểm tra từ đó có phải kết thúc ở từ được chọn
ad = "abcdefghqj"
print(ad.endswith('j'))

# expandtabs: thêm dấu \t ở mỗi cụm từ muốn ngăn cách 
ae = "Toi\tTen\tHung"
print(ae.expandtabs())

# find: tìm ký tự ở vị trí nào
af = "a b c d e j h h f w a"
print(af.find('b'))

# rfind: tìm ký tự nhưng lại tìm từ dưới lên trên
ag = "a b d c d e f a"
print(af.rfind("a"))

# rindex: lấy giá trị tìm thấy ở vị trí sau cùng
ah = "Toi ten la Hung, toi nam nay 25 tuoi"
print(len(ah))
print(ah.rindex('i'))

# isalnum: kiểm tra chuỗi đó phải chuỗi ký tự *( bao gồm chữ và số)
ai = "ToitenHung"
print(ai.isalnum())

# isalpha: kiểm tra chuỗi đó phải từ a - z, A - Z
aj = "ToiTenHung"
print(aj.isalpha())

# isdecimal: kiểm tra chuỗi đó phải ký tự thập phân không
aq = "123123123.3"
print("isdecimal: ", aq.isdecimal())

# isdigit: 
