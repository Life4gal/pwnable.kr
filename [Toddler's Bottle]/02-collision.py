from struct import pack
from os import system

hashcode = 0x21DD09EC
# 输入一个 20 个字符的字符串,分五次视作整形读取(每次读取四个字符)
# 直接分成五份
part = hashcode // 5
pad = hashcode - 5 * part

# 把余数加在最后面
"""
	@ native native
	= native standard
	< little-endian standard
	> big-endian standard
"""
print((4 * pack('<i', part) + pack('<i', part + pad)))

# -n     do not output the trailing newline
# -e     enable interpretation of backslash escapes
system("echo -n -e '\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xcc\xce\xc5\x06'")
