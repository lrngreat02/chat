#chat 2

def read_file(filename):  # 读取
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # sig 取消文档（txt，word）隐藏前缀
		for line in f:
			chat.append(line.strip())
	return chat

def analysis(chat):  # 分析
	allen_word_count = 0
	allen_sticker_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	for line in chat:
		s = line.split(' ')
		if s[1] == 'Allen':
			if s[2] == '贴图' or s[2] == '图片':  #这里不能写成'贴图' or '图片'
				allen_sticker_count += 1
			else:
				for each in s[2:]:  #s[:2], s[-2:], s[2,4]
					allen_word_count += len(each)
		elif s[1] == 'Viki':
			if s[2] == '贴图' or s[2] =='图片':  
				viki_sticker_count += 1
			else:
				for each in s[2:]:
					viki_word_count += len(each)
	print('Allen said', allen_word_count, 'words')
	print('Viki said', viki_word_count, 'words')
	print('Allen post', allen_sticker_count, 'images')
	print('Viki post', viki_sticker_count, 'images')		


def main():
	chat = read_file('-LINE-Viki.txt')
	analysis(chat)

main()

