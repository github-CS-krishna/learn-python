#explore variables

# Store All Data Type
phone = 1234567890
pi    = 3.14
name  = "krishna"
using_python = True
simple_list  = [1,2,3]
simple_dict  = {"name":"krishna"}
simple_set   = {1,1,1,1,1.0};
simple_tuple = (1,2,3)

print("number     = ",phone)
print("float      = ",pi)
print("boolean    = ",using_python)
print("list       = ",simple_list)
print("dictionary = ",simple_dict)
print("set        = ",simple_set)
print("tuple      = ",simple_tuple)

# Type Function
# This function show variable data type
print(type(phone))
print(type(pi))
print(type(using_python))
print(type(simple_list))
print(type(simple_dict))
print(type(simple_set))
print(type(simple_tuple))

# Type Casting
value = 1
numbers = [1,2,3]
print("type casting int     : ",type(int(value)))
print("type casting float   : ",type(float(value)))
print("type casting string  : ",type(str(value)))
print("type casting boolean :",type(bool("True")))
print("type casting list    : ",type(list(numbers)))
print("type casting set     : ",type(set(numbers)))
print("type casting tuple  :",type(tuple(numbers)))

# Delete Variable
temp = 1
print("test del temp value : ",temp)
del temp
#print(temp) #throw NameError : temp not defined

# Variable Address
temp = "hi"
print("address of temp variable : ",id(temp))

# Global And Local Variable
# Global Variable
test = "pass"
print("test global variable :",test)
def dummy():
    print("test global variable :",test)
dummy()

# Local Variable
# function variable store in stack memory
def namePrint(nameString):
    Name = nameString
    print("test local variable print name :",Name)

namePrint("tux")
#print("test local variable print name : ",Name) #throw NameError not defined

# Global Keyword
# global keyword create reference for global variable in function scope
a = 1;

print("global keyword test a = ",a)
def addition():
    global a
    a = 20

addition()
print("global keyword test a = ",a)

# Constance
# no special keyword
# mutable constance(just naming convention to saw it constance)
PI = 3.14

#immutable constance
from collections import namedtuple
const = namedtuple("const",["PI"])
math = const(3.14)
print("namedtuple PI = ",math.PI)
print("namedtuple type =",type(math))
#constance.PI = 3.0 #AttributeError can't set attribute error

# Explicit data type hints
def area_of_circle(radius :float) -> float:
    PI :float = 3.14
    return PI * (radius * radius)

print("explicit type hint calculate area of circle = ",area_of_circle(2))

# Other data types
# Range
print("test range type")
a = range(3)

for i in a:
    print("i = ",i)
print(type(a))

# Frozenset - set and immutable behaviour
simple_list = [1,2,3,1]
test_frozenset = frozenset(simple_list)
#print(test_frozenset[0]) #show TypeError object not subscriptable
for i in test_frozenset:
    print("frozen set item :",i)

# Number complex
n = 3+5j
print("complex example :",n);
print("complex type print : ",type(n))
#casting
print("casting complex type :",complex(1))


# memoryview - this function efficient to access binary datatype and process largedataset audio,video,images
# memoryview function realtime usecase networking or image processing
# Bytes
# immutable property
b1 = bytes([1,2,3,4])
bo = memoryview(b1)

print("byte example :",b1[0])
print("memoryview   :",bo[0:2])
print("memoryview datatype :",type(bo))
# b1[0] += 10 #thow TypeError

# ByteArray
# mutable property
b2 = bytearray(b"aaaa")
bo = memoryview(b2)
print("byte array example :",b2)
bo[1] = 98
bo[2] = 99
bo[3] = 100
print("byte array example :",b2);

# None
name = None;
print("None example :",name)
print("type of None :",type(name))
