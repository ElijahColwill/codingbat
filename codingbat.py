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

def count_code(str):
    result = 0
    for char in range(len(str) - 3):
        if str[char:char+2] == 'co':
            if str[char+3] == 'e':
                result += 1
    return result

print "--"
print count_code('aaacodebbb') # 1
print count_code('codexxcode') # 2
print count_code('cozexxcope') # 2

def end_other(a, b):
    a = a.lower(a)
    b = b.lower(b)
    return a.endswith(b) or b.endswith(a)

print "--"
print end_other('Hiabc', 'abc') # True
print end_other('AbC', 'HiaBc') # True
print end_other('abc', 'abXabc') # True

def xyz_there(str):
    xyzcount = 0
    xyz1count = 0
    for n in range(len(str)):
        if str[n:n+3] == 'xyz':
          xyzcount += 1
        if str[n:n+4] == '.xyz':
          xyz1count += 1
    return (xyzcount - xyz1count) > 0

print "--"
print xyz_there('abcxyz') # True
print xyz_there('abc.xyz') # False
print xyz_there('xyz.abc') # True

# LIST 1

def first_last6(nums):
    if nums[0] == 6:
        return True
    if nums[-1] == 6:
        return True
    else: return False

print "--"
print first_last6([1, 2, 6]) # True
print first_last6([6, 1, 2, 3]) # True
print first_last6([13, 6, 1, 2, 3]) # False

def same_first_last(nums):
    if len(nums) > 0:
        if nums[0] == nums[-1]:
            return True
        else: return False
    else: return False

print "--"
print same_first_last([1, 2, 3]) # False
print same_first_last([1, 2, 3, 1]) # True
print same_first_last([1, 2, 1]) # True

def make_pi():
    nums = [0, 1, 2]
    nums[0] = 3
    nums[1] = 1
    nums[2] = 4
    return nums

print "--"
print make_pi() # [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

print "--"
print common_end([1, 2, 3], [7, 3]) # True
print common_end([1, 2, 3], [7, 3, 2]) # False
print common_end([1, 2, 3], [1, 3]) # True    
