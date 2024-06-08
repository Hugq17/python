# Python numbers
a = 5
b = 2.3
c = 3 + 4j
print("a is ", type(a))
print("b is ", type(b))
print("c is ", type(c))
#phần real
print("real c is ", c.real)
#phần ảo
print("Fake c is ", c.imag)

# ------------------------------------------------------- #

# Python strings
# String literals
x = "Hello world"
print(x)
# Multiline Strings
y = """Tôi tên là Hưng
        Hôm nay tôi học Python
        Mỗi ngày tôi sẽ học 1 bài
        Đừng ráng tiếp thu kiến thức quá nhiều
"""
print(y)
# Chuỗi là 1 mảng
print(y[30])

# ------------------------------------------------------- #

# Python Booleans
#true
print(3 > 2)
#false
# 0, None, "", (), set(), {}, False là các giá trị flase

# ------------------------------------------------------- #

# Python Lists
# List là một tập hợp được sắp xếp và có thể thay đổi. Trong python, List
# được viết bằng dấu ngoặc VUÔNG
thisList = ["Apple", "Banana", "Grape"]
print(thisList[1])
# Tạo một list mới từ hàm list() -- lưu ý sử dụng 2 dấu ngoặc tròn
thisNewList = list(("Táo", "Chuối", "Nho"))
print(thisNewList)

# ------------------------------------------------------- #

# Python Tuples
# Tuples là một tập hợp được sắp xếp theo thứ tự và không thể thay đổi, 
# không thể thêm, xóa, sửa !!!
thisTuple = ("Tv", "Tủ lạnh", "Bếp từ")
print(thisTuple)
print(thisTuple[0])
# Tạo bộ dữ liệu tuple chỉ có một phần tử thì phải thêm một dấu phẩy ở cuối !!!
thisTupleOne = ("Máy game",)
print(type(thisTupleOne))
print(thisTupleOne)
# Tạo một tuple mới từ tuple() -- lưu ý sử dụng 2 ngoặc tròn
thisNewTuple = tuple(("KFC", "Lotteria", "Pessi"))
print(thisNewTuple)

# ------------------------------------------------------- #

# Python Sets
# Set là một tập hợp không có thứ tự và không lập chỉ mục.
# Set được viết bằng dấu ngoặc nhọn
thisSet = {"Iphone", "Samsung", "Xiaomi"}
print(thisSet)
# lặp qua tập hợp các giá trị
for x in thisSet: 
    print(x)
# Kiểm tra phần tử có trong set không
print("Iphone" in thisSet)
# Tạo mới Set mới từ Set() -- lưu ý sử dụng 2 ngoặc tròn
thisNewSet = set(("KFC", "Lotteria", "Pessi"))
print(thisNewSet)

# ------------------------------------------------------- #
# Python Dictionaries
# dictionary là một tập hợp không có thứ tự, có thể thay đổi được và được lập chỉ mục
# Trong python dictionary được viết bằng dấu ngoặc nhọn và chúng có khóa và giá trị
thisDict = {
    "Ho Chi Minh" : "Tan Phu",
    "Ha Noi" : "Hai Ba Trung"
}
print(thisDict)
# Nested dictionary
thisNestDict = {
    "child1" : {
        "name" : "Hoa",
        "age" : 18
    }, 
    "child2" : {
        "name" : "Tuan",
        "age" : 25
    }
}
print(thisNestDict)
# Tạo mới dictionary từ dict() -- lưu ý từ khóa không phải chuỗi ký tự
thisNewDict = dict(brand="Ford", model="Mustang")
print(thisNewDict)