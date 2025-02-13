# Explore string methods and usage
message = "Hello, world i use Python"

# Find length -> len()
print("length :",len(message))

# Upper - change uppercase
print("change to uppercase :",message.upper())

# Lower - change lowercase
print("change to lowercase :",message.lower())
print()

# Strip - remove whitespace
strip_demo = "  hello   "
print("strip example")
print(strip_demo)
print(strip_demo.strip())
print()

# Replace - replace string
print("replace string :",message.replace('w','W'))
print()

# Split - split a string string -> list
splitString = message.split(" ")
print("split string :",splitString)
print()


# String Slicing
print("slice message[7:12]           :",message[7:12])
print("slice from start message[:12] :",message[:12])
print("slice from end message[19:]   :",message[19:])
print("slice using negative index message[-25:-13] :",message[-25:-13])
print()

# Format string
pi = 3.141593
#why format
#print("pi value is"+pi) #TypeError can't concate str to float
#preferable method
print(f"format string example PI = {pi}")
temp = "{ 1+1 }"
print(f"perform math operation {temp} = {1+1}")
print(f"try modification {pi} and {pi:.2f}")
print()
