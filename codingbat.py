# STRING 1

def hello_name(name):
    return "Hello " + name + "!"

print hello_name("Elijah")

def make_abba(a, b):
    return a + b + b + a

print "--"
print make_abba("Hi", "Bye")

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print "--"
print make_tags("i", "Yay")

def make_out_word(out, word):
    return out[:2] + word + out[2:]

print "--"
print make_out_word('<<>>', 'Yay') # '<<Yay>>
print make_out_word('<<>>', 'WooHoo') # '<<WooHoo>>'
print make_out_word('[[]]', 'word') # '[[word]]'

def extra_end(str):
    return (str[-2:] * 3)

print "--"
print extra_end('Hello') # 'lololo'
print extra_end('ab') # 'ababab'
print extra_end('Hi') # 'HiHiHi'

def first_two(str):
    if len(str) < 2:
        return str
    return str[:2]

print "--"
print first_two('Hello') # 'He'
print first_two('abcdefg') # 'ab'
print first_two('ab') # 'ab'
print first_two('a') # 'a'

def first_half(str):
    half = (len(str) / 2)
    return str[:half]

print "--"
print first_half('WooHoo') # 'Woo'
print first_half('HelloThere') # 'Hello'
print first_half('abcdef') # 'abc'

def without_end(str):
    str2 = str[1:]
    return str2[:-1]

print "--"
print without_end('Hello') # 'ell'
print without_end('java') # 'av'
print without_end('coding') # 'odin'

def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else: return b + a + b

print "--"
print combo_string('Hello', 'hi') # 'hiHellohi'
print combo_string('hi', 'Hello') # 'hiHellohi'
print combo_string('aaa', 'b') # 'baaab'

def non_start(a, b):
    return a[1:] + b[1:]

print "--"
print non_start('Hello', 'There') # 'ellohere'
print non_start('java', 'code') # 'avaode'
print non_start('shotl', 'java') # 'hotlava'

def left2(str):
    str2 = str[:2]
    return str[2:] + str2

print "--"
print left2('Hello') # 'lloHe'
print left2('java') # 'vaja'
print left2('Hi') # 'Hi'

#STRING 2

def double_char(str):
    result = ''
    for char in str:
        result += char * 2
    return result

print "--"
print double_char('The') # 'TThhee'
print double_char('AAbb') # 'AAAAbbbb'
print double_char('Hi-There') # 'HHii--TThheerree'

def count_hi(str):
    result = 0
    for char in range(len(str)-1):
        if str[char:char+2] == 'hi':
            result += 1
    return result

print "--"
print count_hi('abc hi ho') # 1
print count_hi('ABChi hi') # 2
print count_hi('hihi') # 2

def cat_dog(str):
    cat = 0
    dog = 0
    for char in range(len(str)-1):
        if str[char:char+3] == 'cat':
            cat += 1
        if str[char:char+3] == 'dog':
            dog += 1
    return cat == dog

print "--"
print cat_dog('catdog') # True
print cat_dog('catcat') # False
print cat_dog('1cat1cadodog') # True
