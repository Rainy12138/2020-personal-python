import json

# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
file = open("papers.json", 'r', encoding='utf-8')
papers = []
creatnum=0
pushnnum=0
releasenum=0
watchnum=0
for line in file.readlines():
    dic = json.loads(line)
    papers.append(dic)
    if dic['type']=='PushEvent':
       pushnnum+=1
    elif dic['type']=='ReleaseEvent':
        releasenum+=1
    elif dic['type']=='CreateEvent':
        creatnum+=1
    elif dic['type']=='WatchEvent':
        watchnum+=1
print(creatnum)
print(pushnnum)
print(releasenum)
print(watchnum)
