import hdfs
from getpass import getuser

# 配置HDFSUrl
HDFSUrl = "http://master:50070"

# 配置HDFS文件所在的目录
inputpath = "/"

# 建立连接（以指定用户名的形式建立连接）
client = hdfs.InsecureClient(HDFSUrl, user='hyxy')
# 默认建立连接的方式，以本地主机的用户名去连接HDFS
# client = hdfs.Client(HDFSUrl)

# print(client.__dict__)
# print(client.__dir__())

# 获取当前的用户名
# print(getuser())
# print(clien)


# 获取指定目录下的文件
fs = client.list(inputpath)
print(fs)

# print(client.list('/in/'))

# print(client.parts('/input/'))

# 获取路径具体信息
# print(client.status(inputpath))

# 创建目录
# client.makedirs('/in/')

# 注
# 上传文件至hdfs
# client.upload('/input/', 'hello')
# client.upload('/input/', 'E:/bak.docx')
# print(client.status('/in/'))
# client.upload('/in/', 'E:/test/pg4300.txt')
# client.upload('/in/', 'E:/test/pg5000.txt')
# client.upload('/in/', 'E:/test/pg20417.txt')

# 写文件至hdfs
# print(client.write('/out/t1.txt', data="hello"))

# 重命名文件
# client.rename('/out/t1.txt', '/in/hello.txt')

# 读取文件
# with client.read('/input/t1.txt', encoding='utf8') as reader:
# with client.read('/input/t1.txt') as reader:
#     content = reader.read()
#     print(type(content))
#     print(content)

# 删除文件
# print(client.delete('/in', recursive=True))