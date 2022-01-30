string_1 = "supercalifragilisticexpialidocious" #will print letter by letter in for loop

list_linux = ["ubuntu", "redhat", "centos", "raspi"] #will print each list item in for loop

text_file = 'apples\npears\nbananas\nstrawberries'.splitlines() #will print line by line in for loop

#"character" can be anything
for character in string_1:
    print(character)

for item in list_linux:
    print(item)
    
for lines in text_file:
    print(lines)