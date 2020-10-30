from os import pipe, write
from socket import socket, AF_INET, SOCK_STREAM
from subprocess import Popen
from os import environ

processPath = './input'

# 第一关
# 要求参数个数为 100 个(除去进程本身的名字有 99 个)
# 其中第 65(ord('A')) 个参数要是 '\x00' 第 66(ord('B')) 个参数要是 '\x20\x0a\x0d'

argv = ['a'] * 100
argv[0] = processPath
argv[ord('A')] = ''  # \x00 是终止符....在这里卡了好久...
argv[ord('B')] = '\x20\x0a\x0d'
# 这是第五关的端口设置
argv[ord('C')] = '1145'

# Popen(argv)

# 第二关
"""
文件描述符在形式上是一个非负整数。实际上，它是一个索引值，指向内核为每一个进程所维护的该进程打开文件的记录表。
当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。在程序设计中，一些涉及底层的程序编写往往会围绕着文件描述符展开。
但是文件描述符这一概念往往只适用于UNIX、Linux这样的操作系统。

每个Unix进程（除了可能的守护进程）应均有三个标准的POSIX文件描述符，对应于三个标准流：

整数值	名称	<unistd.h>符号常量[1]	<stdio.h>文件流[2]
0	Standard input	STDIN_FILENO	stdin
1	Standard output	STDOUT_FILENO	stdout
2	Standard error	STDERR_FILENO	stderr
"""
# read 的第一个参数 fd 就是文件描述符(file descriptor)
# 从 stdin 读取四个字符,要求是 '\x00\x0a\x00\xff'
# 从 stderr 读取四个字符,要求是 '\x00\x0a\x02\xff'
# pipe[0] = READ pipe[1] = WRITE
pipeStdin = pipe()
pipeStderr = pipe()

write(pipeStdin[1], b'\x00\x0a\x00\xff')
write(pipeStderr[1], b'\x00\x0a\x02\xff')

# Popen(argv, stdin = pipeStdin[0], stderr = pipeStderr[0])

# 第三关
# char* getenv(const char* name)是查找程序环境列表中参数name的值
# 要求 env['\xde\xad\xbe\xef'] 是 '\xca\xfe\xba\xbe'
environ['\xde\xad\xbe\xef'] = '\xca\xfe\xba\xbe'

# 这里不知道为啥就是不对...
Popen(argv, stdin = pipeStdin[0], stderr = pipeStderr[0], env = environ)


# 第四关
# 打开一个叫 '\x0a' 的文件并且读取四个字符
# 要求内容是 '\x00\x00\x00\x00'
with open(r'\x0a', 'wb') as f:
	f.write(b'\x00\x00\x00\x00')

# 第五关
# 将 input 作为服务端,监听端口 argv[ord('C')] 转为整形(atoi)的值
# 要求给 input 的这个端口发送一个 4 字符信息,内容为 '\xde\xad\xbe\xef'

# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('127.0.0.1', int(argv[ord('C')])))
# sock.send(b'\xde\xad\xbe\xef')
# sock.close()

