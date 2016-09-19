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
