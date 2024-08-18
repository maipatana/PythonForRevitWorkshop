
### Variables ตัวแปร ###
x = 10
y = 2
print(x+y)
### --------------- ###
x = 3
print(x+y)

x += 1
print(x+y)
"""
!!! Exercise 1 !!!
ให้สร้างตัวแปร z โดยให้ assign จำนวนเต็มเท่าใดก็ได้เข้าไป
print ค่า x+y-z
"""
### Variables ตัวแปร ###

### Data Types ประเภทข้อมูล ###
string = 'this is a string'  ## ตัวอักษร  (String) อยู่ใน '' หรือ ""
number = 12345               ## จำนวนเต็ม (Integer) ไม่มี . ทศนิยม
f_number = 1.2345            ## จำนวนจริง (Float/Double) มี . ทศนิยม
Is_conditioned = True        ## จริง/ไม่จริง (Boolean) มีแค่ True หรือ False
### --------------- ###
room_names = ['Bed Room', 'Bath Room', 'Living Room']  ## List มีข้อมูลอยู่ใน [] เว้นกันด้วย ,
print(room_names[0])  ## [<จำนวนเต็ม>] ต่อท้าย list คือเลข Index ในการเลือกข้อมูล Index เริ่มที่ 0

room_names[0] = 'New Bed Room'  ## สามารถแทนค่าเดิมใน List ได้
print(room_names[0]) 

room_names.append('Kitchen')  ## การเพิ่ม item เข้าไปใน List ใช้ List.append(<สิ่งที่ต้องการจะเพิ่ม>)
print(room_names[-1])  ## index -1 หมายถึง item สุดท้ายของ List

immutable_room_names = ('Bed Room', 'Bath Room')  ## Tuple คือ Immutable List
print(immutable_room_names[0])

immutable_room_names[0] = 'New Bed Room'  ## ไม่สามารถแทนค่าใหม่ใน Immutable List ได้
"""
List มีส่วนสำคัญอย่างมากในการทำงานด้วย Revit API 
เป็น Data Type หลักของการทำงาน 
"""

data = [
    'ข้อมูล', 
    ['ห้องน้ำ', 3, 2.4, False], 
    ['ห้องนอน', 35, 2.7, True]
    ]
"""
List สามารถอยู่ใน List ได้ และสามารถผสมข้อมูลหลายประเภทใน List เดียวกันได้
"""
print(data[1])
print(data[1][0])  ## การใช้ Index เลือกข้อมูลที่ซ้อนกันอยู่

"""
!!! Exercise 2 !!!
ให้เปลี่ยนชื่อ 'ห้องนอน' ใน data เป็น 'Bed Room' 
และเปลี่ยนตารางเมตรห้องนอนเป็น 40.2 
data[][] = 'Bed Room'
print(data[][])

data[][] = 
print(data[])
"""
### --------------- ###
from datetime import date

### Dictionary สามารถพลิกแพลงใช้ได้หลากหลาย แต่โดยทั่วไปไม่ค่อยได้ใช้ นอกจากทำอะไรพิเศษจริงๆ
dict_data = {
    "rooms": 
    [
        {
            "name": 'Bath Room', 
            "area": 3, 
            "ceiling_height": 2.4,
            "is_conditioned": False
        },
        {
            "name": 'Bed Room', 
            "area": 40.2, 
            "ceiling_height": 2.7,
            "is_conditioned": True
        },
    ],
    'updated': date.today().strftime("%d/%m/%Y")
}

print(dict_data)
print(dict_data['rooms'])
print(dict_data['rooms'][0])


dict_data['rooms'].append(
    {
        "name": 'Living Room', 
        "area": 15, 
        "ceiling_height": 2.7,
        "is_conditioned": True
    }
)  

print(dict_data['rooms'])

"""
List ที่อยู่ใน Dictionary ทำงานเหมือน List ทั่วไป โดยข้อมูลทุกรุปแบบ มีพฤติกรรมเหมือนเดิม แม้อยู่ใน List หรือ Dictionary
"""

"""
!!! Exercise 3 !!!
แสดงข้อมูลของ Index ที่ 1 ใน data['rooms']
แสดงข้อมูลพื้นที่ของห้องน้ำ
แสดงวันที่ updated 
เปลี่ยนห้องน้ำเป็นติดแอร์
เปลี่ยนฝ้าเพดานห้องนอนเป็น 2.5
"""
### Data Types ประเภทข้อมูล ###


### Conditions ###
"""
if ใช้เยอะมาก

Syntax
if <ConditionA>:
    ## Code จะ Execute ถ้า ConditionA เป็นจริง
else:
    ## Code จะ Execute ถ้า ConditionA ไม่เป็นจริง

if <ConditionA>:
    ## Code จะ Execute ถ้า ConditionA เป็นจริง
elif <ConditionB>:
    ## Code จะ Execute ถ้า ConditionA ไม่เป็นจริง แต่ ConditionB เป็นจริง
elif <ConditionC>:
    ## Code จะ Execute ถ้า ConditionA และ B ไม่เป็นจริง แต่ ConditionC เป็นจริง
else:
    ## Code จะ Execute ถ้า ConditionA, B และ C ไม่เป็นจริง

สัญลักษณ์ที่ใช้ได้

"""
if dict_data['rooms'][1]['ceiling_height'] < 2.7:
    print('ฝ้าเพดานต่ำเกินไป')
else:
    print("ฝ้าเพดานสูงพอดี")

### Conditions ###

### Loops ###
"""
For Loop ใช้เยอะมาก

Syntax:
for <ชื่อ item> in <List>:
    ## Code Block
"""
for i in range(10):  ## range(<จำนวนเต็ม n>) จะให้ค่าตั้งแต่ 0 ถึง n-1
    print(i)

for room in ['Bed Room', 'Bath Room', 'Living Room']:
    print(room)

areas = [30,3,14,9]
for room, area in zip(room_names, areas):
    print(room, area)
"""
การ zip(ListA, ListB) เป็นการ iterate ทั้ง 2 List ไปพร้อมกัน
แต่ความยาวของ List จะต้องเท่ากันด้วย
"""

for i, room in enumerate(room_names):
    print(room, areas[i])
"""
enumerate จะให้ค่า index มาด้วย ซึ่งสามารถนำไปใช้เป็น index ของ List ได้
"""

for i in range(len(room_names)):
    print(room_names[i], areas[i])
"""
len(<List>) จะให้จำนวน item ใน List ซึ่งสามารถนำไปผนวกกับ range() และสามารถใช้ i เป็น index ของ List ได้
"""

for room in dict_data['rooms']:
    if room['name'] == 'Bed Room':
        print(room['name'], room['area'])

"""
!!! Exercise 4 !!!
นับจำนวนห้องใน dict_data['rooms'] ที่มีความสูงฝ้าเพดานต่ำกว่า 3 เมตร
"""
room_count = 0
for room in dict_data['rooms']:
    if room['ceiling_height'] < 3:
        room_count += 1
print(room_count)

### --------------- ###
"""
While Loop อย่าใช้ นอกจากจะรู้ว่าตัวเองทำอะไรอยู่

Syntax:
while <True>:
    ## Code Block
"""
run = True
index = 0
while run:
    if dict_data['rooms'][index]['name'] == 'Living Room':
        run = False
    print(dict_data['rooms'][index]['name'])
    index += 1

### Loops ###


### Functions ###
"""
Function จะใช้ตอนเขียน Code ให้เป็นระเบียบ
แยกส่วนการทำงาน เพื่อให้ Function ถูกนำไปใช้ซ้ำได้หลายๆครั้ง

Syntax:
def <ชื่อ function>(<ชื่อ argument ที่จะใช้ใน function>):
    ## Code
"""
def addNumber(a, b):
    return a+b

print(addNumber(10,20))

def getRoomData(room):
    print("{} {}sqm".format(room['name'], room['area']))

for room in dict_data['rooms']:
    getRoomData(room)

"""
!!! Exercise 5 !!!
เขียน Function เช็คว่าห้องใน dict_data['rooms'] ติดแอร์หรือไม่
ถ้าติด ให้ print ชื่อห้องออกมา และนับจำนวน
"""
### Functions ###



### Classes/Objects ###
"""
เราคงจะไม่ค่อยได้สร้าง Class เองเท่าไหร่ นอกจากว่าพิเศษมากๆ
แต่เราจะทำงานกับ Class ตลอดเวลาใน Revit 
สิ่งสำคัญคือรู้ว่าอะไรคือ Property อะไรคือ Method
"""

class Room:
    def __init__(self, name, area, ceiling_height, is_conditioned):
        self.name = name
        self.area = area
        self.ceiling_height = ceiling_height
        self.is_conditioned = is_conditioned
    
    def getArea(self):
        return "{} {}sqm".format(self.name, self.area)

bed_room = Room('Bed Room', 40.2, 2.7, True)
print(bed_room.getArea())

print(bed_room.name)

"""
!!! Exercise 6 !!!
เพิ่ม property ชื่อ width และ length ใน Class Room
เพิ่ม method ชื่อ getVolumn ที่ให้ปริมาตรของห้อง Hint: พื้นที่ x ความสูง
method getVolumn จะ return ค่าเป็น string โดยแสดงชื่อห้อง และปริมาตรของห้อง
"""
### Classes/Objects ###