import sys

def getFileName():
	try:
		fileName=sys.argv[1]
		return fileName
	except Exception as e:
		print("读文件错误")
		sys.exit()

def getFileText(fileName):
	try:
	    txt = open(fileName,"r",encoding="utf-8").read()
	    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
		    txt = txt.replace(ch," ")
	    return txt
	except IOError as e:
		print ("ERROR: %s"%str(e))
		sys.exit()

def countWords(txt):
	words = txt.split()
	counts={}
	for word in words:
		counts[word] = counts.get(word,0)+1

	items = list(counts.items())
	items.sort(key=lambda x :x[1],reverse=True)
	for i in range(20):
		word,count = items[i]
		print("{0:<10} {1:>5}".format(word,count))
	return len(items)


if __name__ == "__main__":
	filepath = "60489-0.txt"
	txt = getFileText(filepath)
	print("共%d 个单词"%countWords(txt))
