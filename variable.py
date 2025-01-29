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
