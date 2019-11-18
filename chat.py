#chat

def read_file(filename):  # 读取
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # sig 取消文档（txt，word）隐藏前缀
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):  # 转换
	new_chat = []
	person = None  # Null，空，在if 中相当于False
	for c in chat:
		if c == 'Allen' or c == 'Tom':
			person = c
			continue
		if person:  # person 非空时，判定为True
			new_chat.append(person + ': ' + c)
	return new_chat

def write_in(file, chat):  # 写入
	with open(file, 'w', encoding='utf-8') as f:
		for c in chat:
			f.write(c + '\n')   # for loop不提供\n, 需要自己添加，否则是不会换行的，print执行完，会自动换行

def main():
	chat = read_file('chat.txt')
	chat = convert(chat)
	write_in('new_chat.txt', chat)

main()

