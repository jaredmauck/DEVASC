#single line comment

print(1) #works after code
print(2)
'''does not work after code in the same line ^ '''


'''same as # comment
but can be used with multiple line
yep'''

#variable
address = "myaddress"

print(address)

#math
result = 1 + 3

print(result)

#different type of data

#string
string = "hello"

print(type(string))
print(string[1] + " == string[1] = 2nd character of 'hello'")
print(string[0:-1] + " == string[0:-1] = hell of 'hello'")
print(string[-1] + " == string[-1] = last character of 'hello'")

#integer
integer = 2 + 2

print(type(integer))

#float
float_1 = 1.1 + 2.2

print(type(float_1))

#boolean
boolean_true = True
boolean_false = False

print(type(boolean_true))
print(type(boolean_false))

#list
list_1 = [1, 2, 3]

print(type(list_1))
print(list_1[-1])
print("list_1[-1] = last item in list")
print(list_1[-2])
print("list_1[-2] = 2nd to last item in list")
print(list_1[0])
print("list_1[0] = 1st item in list")

#dictionary
dictionary_1 = {1 : "key"}

print(type(dictionary_1))



