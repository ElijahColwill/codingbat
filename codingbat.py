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
    a = a.lower()
    b = b.lower()
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

def sum3(nums):
    return nums[0] + nums[1] + nums[2]

print "--"
print sum3([1, 2, 3]) # 6
print sum3([5, 11, 2]) # 18
print sum3([7, 0, 0]) # 7

def rotate_left3(nums):
   return [nums[1], nums[2], nums[0]]

print "--"
print rotate_left3([1, 2, 3]) # [2, 3, 1]
print rotate_left3([5, 11, 9]) # [11, 9, 5]
print rotate_left3([7, 0, 0]) # [0, 0, 7]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

print "--"
print reverse3([1, 2, 3]) # [3, 2, 1]
print reverse3([5, 11, 9]) # [9, 11, 5]
print reverse3([7, 0, 0]) # [0, 0, 7]

def max_end3(nums):
    final = 0
    if nums[0] > nums[2]:
        final += nums[0]
    else: final += nums[2]
    nums[0] = final
    nums[1] = final
    nums[2] = final
    return nums

print "--"
print max_end3([1, 2, 3]) # [3, 3, 3]
print max_end3([11, 5, 9]) # [11, 11, 11]
print max_end3([2, 11, 3]) # [3, 3, 3]

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else: return nums[0] + nums[1]

print "--"
print sum2([1, 2, 3]) # 3
print sum2([1, 1]) # 2
print sum2([1, 1, 1, 1]) # 2

def middle_way(a, b):
    return [a[1], b[1]]

print "--"
print middle_way([1, 2, 3], [4, 5, 6]) # [2, 5]
print middle_way([7, 7, 7], [3, 8, 0]) # [7, 8]
print middle_way([5, 2, 9], [1, 4, 5]) # [2, 4]

def make_ends(nums):
    return [nums[0], nums[-1]]

print "--"
print make_ends([1, 2, 3]) # [1, 3]
print make_ends([1, 2, 3, 4]) # [1, 4]
print make_ends([7, 4, 6, 2]) # [7, 2]

def has23(nums):
    return 2 in nums or 3 in nums

print "--"
print has23([2, 5]) # True
print has23([4, 3]) # True
print has23([4, 5]) # False

# LIST 2

def count_evens(nums):
    result = 0
    for i in nums:
        if (i % 2) == 0:
            result += 1
    return result

print "--"
print count_evens([2, 1, 2, 3, 4]) # 3
print count_evens([2, 2, 0]) # 3
print count_evens([1, 3, 5]) # 0

def big_diff(nums):
    return max(nums) - min(nums)

print "--"
print big_diff([10, 3, 5, 6]) # 7
print big_diff([7, 2, 10, 9]) # 8
print big_diff([2, 10, 7, 2]) # 8

def centered_average(nums):
  result = 0
  for i in nums:
    result += i
  return (result - min(nums) - max(nums)) / (len(nums)-2)

print "--"
print centered_average([1, 2, 3, 4, 100]) # 3
print centered_average([1, 1, 5, 5, 10, 8, 7]) # 5
print centered_average([-10, -4, -2, -4, -2, 0]) # -3

def sum13(nums):
    if len(nums) == 0:
        return 0
    skipnext = False
    sum = 0
    for i in nums:
         if i == 13:
             skipnext = True
             continue
         if skipnext:
             skipnext = False
             continue
         else: sum += i
    return sum

print "--"
print sum13([1, 2, 2, 1])
print sum13([1, 1])
print sum13([1, 2, 2, 1, 13])
print sum13([1, 2, 2, 1, 13, 13, 13, 13, 1, 2])
