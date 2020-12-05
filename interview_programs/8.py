'''
Count number of words, characters, uppercase letters, vowels in given string.
'''


def count(s):
    word_count = vowel_count = char_count = upper_count = 0
    vowel_string = 'AaEeIiOoUu'

    word_count = len(s.split())
 
    for ele in s: 
        if(ele.isalpha()):
            char_count += 1
        if(ele.isupper()):
            upper_count += 1
        if(ele in vowel_string):
            vowel_count += 1

    return word_count, vowel_count, char_count, upper_count


s = input()
w, v, c, u = count(s)
print('Word Count:{}, Character Count:{}, Vowel Count:{}, Uppercase Count:{}'.format(w,c,v,u))


