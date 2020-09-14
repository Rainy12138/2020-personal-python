import json
import collections
# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
file = open("papers.json", 'r', encoding='utf-8')

papers = []
data=[]

idlist=[0 for i in range(20000)]
idcount=0
numlist=[0 for i in range(20000)]

pushnnum=0
commentnum=0
issuesnum=0
pullnum=0



for line in file.readlines():
    dic = json.loads(line)
    papers.append(dic)


data=sorted(papers,key=lambda x:x['actor']['id']) 

for key in data:
    if idlist[idcount]!=key['actor']['id']:
        numlist[idcount]=pushnnum
        numlist[idcount+1]=commentnum
        numlist[idcount+2]=issuesnum
        numlist[idcount+3]=pullnum
        pushnnum=0
        commentnum=0
        issuesnum=0
        pullnum=0
        idlist[idcount]=key['actor']['id']
        idcount+=4
    if key['type']=='PushEvent':
        pushnnum+=1
    elif key['type']=='IssueCommentEvent':
        commentnum+=1
    elif key['type']=='"IssuesEvent':
        issuesnum+=1
    elif key['type']=='PullRequestEvent':
       pullnum+=1
           
while idcount!=0:
    idcount-=4 
    print(idlist[idcount])
    print("PushEvent:",numlist[idcount-4])
    print("IssueCommentEvent:",numlist[idcount-3])
    print("IssuesEvent:",numlist[idcount-2])
    print("PullRequestEvent:",numlist[idcount-1],"\n")
      




