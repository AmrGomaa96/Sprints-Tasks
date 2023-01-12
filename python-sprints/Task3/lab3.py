
def is_balanced(string):
    while True:
        if '()' in string:
            string = string.replace('()', '')
        elif '{}' in string:
            string = string.replace('{}', '')
        elif '[]' in string:
            string = string.replace('[]', '')
        else:
            return "YES" if not string else "NO"

test1 = "{[()]}"
print(is_balanced(test1))

test2 = "{[(]}"
print(is_balanced(test2))

test3 = "{{[[(())]]}}"
print(is_balanced(test3))
