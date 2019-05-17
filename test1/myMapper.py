import sys

'''
统计文件中的单词数
'''
for line in sys.stdin:
    # 去除两头的空格
    line = line.strip()
    words = line.split()
    for word in words:
        print("%s\t%s" % (word, 1))


