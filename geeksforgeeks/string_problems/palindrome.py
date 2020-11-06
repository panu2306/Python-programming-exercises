# Python program to check if a string is palindrome or not

        
def using_for(sent_string):
    s = ""
    for c in sent_string:
        s = c + s
    return s

def using_reversed(sent_string):
    s = "".join(reversed(sent_string))
    return s

def using_recursion(sent_string):
    if(len(sent_string) == 0):
        return sent_string
    else:
        return using_recursion(sent_string[1:]) + sent_string[0]         

def using_slice(sent_string):
    return sent_string[::-1]

if __name__ == "__main__":
    sent_string = "121"

    returned_string = using_for(sent_string)
    returned_string = using_reversed(sent_string)
    returned_string = using_recursion(sent_string)
    returned_string = using_slice(sent_string)

    if(sent_string == returned_string):
        print("String is a Palindrome String")
    else:
        print("String is not a Palindrome String")