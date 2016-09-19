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
