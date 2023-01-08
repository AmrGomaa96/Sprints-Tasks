
def replace_1(string, position, character):
    i=list(string)
    i[position]=character
    string=''.join(i)
    print(string)

x = input("please enter a string \n")
y = int(input("please enter the position of the char to replace \n"))
z = input("please enter the character \n")
replace_1(x,y,z)
