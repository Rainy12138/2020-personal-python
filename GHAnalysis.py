import json
import collections
import os
import getopt
import sys

options,args= getopt.getopt(sys.argv[1:],'iu:r:e:',['init','user=','repo=','event='])
print ("options:",options)
print("args:",args)

for name,value in options:
     if name in ("-i","--init"):
         print ("初始化")
         file = open("jason/papers.json", 'r', encoding='utf-8')
         papers = []
         data=[]

         idlist=[0 for i in range(200000)]
         idcount=0
         numlist=[0 for i in range(200000)]

         pushnnum=0
         commentnum=0
         issuesnum=0
         pullnum=0
         count=0
         count2=0

         for line in file.readlines():
             dic = json.loads(line)
             papers.append(dic)
         data=sorted(papers,key=lambda x:(x['actor']['id'],x['type'])) 
         
         for key in data:
             if idlist[idcount]==key['actor']['id']:
                 if key['type']=='PushEvent':
                     pushnnum+=1
                 elif key['type']=='IssueCommentEvent':
                     commentnum+=1
                 elif key['type']=='IssuesEvent':
                     issuesnum+=1
                 elif key['type']=='PullRequestEvent':
                     pullnum+=1
             else:
                 numlist[idcount*4]=pushnnum
                 numlist[idcount*4+1]=commentnum
                 numlist[idcount*4+2]=issuesnum
                 numlist[idcount*4+3]=pullnum
                 pushnnum=0
                 commentnum=0
                 issuesnum=0
                 pullnum=0
                 idcount+=1
                 idlist[idcount]=key['actor']['id']
                 if key['type']=='PushEvent':
                     pushnnum+=1
                 elif key['type']=='IssueCommentEvent':
                     commentnum+=1
                 elif key['type']=='IssuesEvent':
                     issuesnum+=1
                 elif key['type']=='PullRequestEvent':
                     pullnum+=1


     if name in ("-u","--user",value):
         print ('查某用户的某事件数量运行格式',value)
         search=input()
         search=int(search)
         while idcount!=0:
             if search==idlist[idcount]:
             print(idlist[idcount])
             print("PushEvent:",numlist[idcount*4])
             print("IssueCommentEvent:",numlist[idcount*4+1])
             print("IssuesEvent:",numlist[idcount*4+2])
             print("PullRequestEvent:",numlist[idcount*4+3],"\n")
             idcount-=1   

     if name in ("-r","--repo"):
         print ('查询某项目的某事件数量运行格式',value)
     if name in ("-e","--event"):
         print ('查询某用户在某项目的某事件数量运行格式',value)
    

        







