

# class Car:
#     loaixe = "ô tô"
#     def __init__(self, tenxe, mausac, nguyenlieu):
#         self.tenxe = tenxe
#         self.mausac = mausac
#         self.nguyenlieu = nguyenlieu
# # instantiate the Car class
# toyota = Car("Toyota", "Đỏ", "Điện")
# lamborghini = Car("Lamborghini", "Vàng", "Deisel")
# porsche = Car("Porsche", "Xanh", "Gas")
# # access the class attributes
# print("Porsche là {}.".format(porsche.__class__.loaixe))
# print("Toyota là {}.".format(toyota.__class__.loaixe))
# print("Lamborghini cũng là {}.".format(lamborghini.__class__.loaixe))
# # access the instance attributes
# print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( toyota.tenxe, toyota.mausac, toyota.nguyenlieu))
# print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( lamborghini.tenxe, lamborghini.mausac,lamborghini.nguyenlieu))
# print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( porsche.tenxe, porsche.mausac, porsche.nguyenlieu))


# ------------------------ METHOD OOP --------------------------

# class Car:
# # thuộc tính đối tượng
#     def __init__(self, tenxe, mausac, nguyenlieu):
#         self.tenxe = tenxe
#         self.mausac = mausac
#         self.nguyenlieu = nguyenlieu
# # phương thức
#     def dungxe(self, mucdich):
#         return "{} đang dừng xe để {}".format(self.tenxe,mucdich)
#     def chayxe(self):
#         return "{} đang chạy trên đường".format(self.tenxe)
#     def nomay(self):
#         return "{} đang nổ máy".format(self.tenxe)
# # tạo các đối tượng
# toyota = Car("Toyota", "Đỏ", "Điện")
# lamborghini = Car("Lamborghini", "Vàng", "Deisel")
# porsche = Car("Porsche", "Xanh", "Gas")
# # Gọi các phương thức
# print(toyota.dungxe("nạp điện"))
# print(lamborghini.chayxe())
# print(porsche.nomay())

# print("use dict: ")
# print(lamborghini.__dict__)


# ---------------------- THỪA KẾ OOP ------------------------------

# # Lớp cha
# class Car:
# # Constructor
#     def __init__(self, hangxe, tenxe, mausac):
# # Lớp Car có 3 thuộc tính: tenxe, mausac, hang xe
#         self.hangxe = hangxe
#         self.tenxe = tenxe
#         self.mausac = mausac
# # phương thức
#     def chayxe(self):
#             print ("{} đang chạy trên đường".format(self.tenxe))
#     def dungxe(self, mucdich):
#         print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))
        
        
# # Lớp Toyota mở rộng từ lớp Car.
# class Toyota(Car):
#     def __init__(self, hangxe, tenxe, mausac, nguyenlieu):
# # Gọi tới constructor của lớp cha (Car)
# # để gán giá trị vào thuộc tính của lớp cha.
#         super().__init__(hangxe, tenxe, mausac)
#         self.nguyenlieu = nguyenlieu
# # Kế thừa phương thức cũ
#     def chayxe(self):
#         print ("{} đang chạy trên đường".format(self.tenxe))
# # Ghi đè (override) phương thức cùng tên của lớp cha.
#     def dungxe(self, mucdich):
#         print ("{} đang dừng xe để {}".format(self.tenxe, mucdich))
#         print ("{} chạy bằng {}".format(self.tenxe, self.nguyenlieu))
# # Bổ sung thêm thành phần mới
#     def nomay(self):
#         print ("{} đang nổ máy".format(self.tenxe))
        
# toyota1 = Toyota("Toyota", "Toyota Hilux", "Đỏ", "Điện")
# toyota2 = Toyota("Toyota", "Toyota Yaris", "Vàng", "Deisel")
# toyota3 = Toyota("Toyota", "Toyota Vios", "Xanh", "Gas")
# toyota1.dungxe("nạp điện")
# toyota2.chayxe()
# toyota3.nomay()

# -------------------------ĐÓNG GÓI OOP---------------------------

# class Computer:
#     def __init__(self):
#     # Thuộc tính private ngăn chặn sửa đổi trực tiếp
#         self.__maxprice = 900
#     def sell(self):
#         print("Giá bán sản phẩm: {}".format(self.__maxprice))
#     def setMaxPrice(self, price):
#         self.__maxprice = price
# c = Computer()
# c.sell()
# # thay đổi giá.
# print("Thay đổi giá cách 1:")
# c.__maxprice = 1000
# c.sell()
# # sử dụng hàm setter để thay đổi giá.
# print("Thay đổi giá cách 2:")
# c.setMaxPrice(1000)
# c.sell()

# ----------------------------Đa hình (Polymorphism)-------------------

# class Toyota:
#     def dungxe(self):
#         print("Toyota dừng xe để nạp điện")
#     def nomay(self):
#         print("Toyota nổ máy bằng hộp số tự động")
# class Porsche:
#     def dungxe(self):
#         print("Porsche dừng xe để bơm xăng")
#     def nomay(self):
#         print("Porsche nổ máy bằng hộp số cơ")
#     # phương thức chung để gọi
# def kiemtra_dungxe(car): car.dungxe()
# # tạo các object
# toyota = Toyota()
# porsche = Porsche()
# # passing the object
# kiemtra_dungxe(toyota)
# kiemtra_dungxe(porsche) 

# -----------------------Polymorphism và Inheritance:------------------

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# obj_bird = Bird()
# obj_spr = sparrow()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()


# ------------------------- BT 1--------------------------------------
# Create a Vehicle class with name, top_speed and engine_size, seating_capacity instance attributes.
# Create a Bus class that inherits from the Vehicle class. 
    # Bus class have Bus.seating_capacity() a default value of 50
    
    
class Vehicle:
    def __init__(self,name,top_speed,engine_size):
        self.name = name
        self.top_speed = top_speed
        self.engine_size = engine_size
        self.seating_capacity = 10

class Bus(Vehicle):
    def __init__(self,name,top_speed,engine_size):
        super().__init__(name,top_speed,engine_size)
        self.seating_capacity = 50
        
       
xebus = Bus("Vinfast","50KM/h","Large")

print(xebus.__dict__)

# --------------------------- BT2: suffle cards --------------------

# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#     def __repr__(self):
#         return "{} of {}".format(self.value, self.suit)
    
# class Deck:
#     def __init__(self):
#         suits = ['Heart','Diamond','Club','Spade']
#         values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         card = [Card(suit,value) for suit in suits for values in value]












