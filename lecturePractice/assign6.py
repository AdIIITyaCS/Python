# # q1
# import math
# class PowerCalculator:
#     def __init__(self, base):
#         self.base = base
#     def calculate(self, exponent):
#         return self.base ** exponent
# class DivisionCalculator:
#     def __init__(self, dividend):
#         self.dividend = dividend
#     def calculate(self, divisor):
#         if divisor == 0:
#             return "Cannot divide by zero"
#         return self.dividend / divisor
# class LogCalculator:
#     def __init__(self, x):
#         self.x = x
#     def calculate(self, base):
#         return math.log(self.x, base)
# class RadiansDegreesConverter:
#     def __init__(self, angle):  
#         self.angle = angle
#     def to_radians(self):
#         return math.radians(self.angle)
#     def to_degrees(self):
#         return math.degrees(self.angle)
# # Example usage:
# base_num = 10

# power_calc = PowerCalculator(base_num)
# result_power = power_calc.calculate(3)
# print(f"{base_num} ^ 3 = {result_power}")
# division_calc = DivisionCalculator(base_num)
# result_division = division_calc.calculate(2)
# print(f"{base_num} / 2 = {result_division}")
# log_calc = LogCalculator(base_num)
# result_log = log_calc.calculate(2)
# print(f"log2({base_num}) = {result_log}")
# angle = 45  # in degrees
# angle_converter = RadiansDegreesConverter(angle)
# radians = angle_converter.to_radians()
# degrees = angle_converter.to_degrees()
# print(f"{angle} degrees to radians = {radians}")
# print(f"{angle} radians to degrees = {degrees}")

#or can be solved by this way

#  import math
# class Power():
#     def __init__(self,base,exponent):
#         self.e= exponent
#         self.b= base
#     def power(self):
#         return self.b**self.e        
# class Division():
#     def __init__(self,dividend,divisor):
#         self.div= dividend
#         self.dir= divisor
#     def division(self):
#         return self.div/self.dir
# class Log():
#     def __init__(self,base,argu):
#         self.ba= base
#         self.ar= argu
#     def log(self):
#         return  math.log(self.ba,self.ar)   # log inbuilt function first take no. then argument
# class Radian_To_Degree():
#     def __init__(self,radian):
#         self.r= radian
#     def radian_to_degree(self):
#         return (self.r)*180/(22/7)          
# a=Power(2,3)
# b=Division(25,5)
# c=Radian_To_Degree((22/7)*2)
# d=Log(4,2)
# e=Log(2,4)
# print(a.power())
# print(b.division())
# print(c.radian_to_degree())
# print(d.log())
# print(e.log())

# # q2
# class Rectangle():
#     def calcAreaRectangle(self):
#         return int(self.height*self.width)
# class Square():
#     def calcAreaSquare(self):
#         return int(self.side*self.side)
# class Parallelepiped(Rectangle,Square):
#     def calcVolume(self):
#         if(i==2):
#             return int(self.side*self.side*self.length)
#         elif(i==3):
#             return (self.height*self.width*self.length)
#         else:
#             None
# r=Rectangle()
# s=Square()
# p=Parallelepiped()
# i=int(input("PUT NO. OF INPUTS YOU WANT TO GIVE:"))
# if (i==2):
#     p.side=int(input("SIDE OF SQUARE::"))
#     Area_Square=p.calcAreaSquare()
#     print("Area_Square:",Area_Square)
#     p.length=int(input("LENGTH OF PARALLELOPIPED::"))
#     Volume_Parallelopiped=p.calcVolume()
#     print("Volume_Parallelopiped:",Volume_Parallelopiped)
# elif (i==3):
#     p.height=int(input("HEIGHT OF RECTANLE::"))
#     p.width=int(input("WIDTH OF RECTANGLE::"))
#     Area_Rectangle=p.calcAreaRectangle()
#     print("Area_Rectangle:",Area_Rectangle)
#     p.length=int(input("LENGTH OF PARALLELOPIPED::"))
#     Volume_Parallelopiped=p.calcVolume()
#     print("Volume_Parallelopiped:",Volume_Parallelopiped)
# else:
#     print("invalid no.of inputs!!!!!!!")    

