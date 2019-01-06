import os
from influxdb import InfluxDBClient
from operator import itemgetter
from Dictionary_creation import dict_creation
import nltk
import sys
import csv
import re
import string
import os
import datetime
import time as t
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer, word_tokenize, wordpunct_tokenize

try:
    client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='gis')
except:
    print("Influxdb Error")
loc_data=[]
def first(corpus):
     line_out=[]
     cluster_count=0
     with open('testabc.txt','w')as myFile:
         lines=corpus.split("\n")
         for line in lines:
             word=line.split("%")
             if cluster_count==0:
                 cluster_count=int(word[5])
             if line!="" and word[4]!="50":
                 date_time=str(word[0]).strip().split(" ")
                 in_date=date_time[0].strip().split("-")
                 f_date=in_date[2]+"/"+in_date[1]+"/"+in_date[0]
                 time=str(date_time[1]).strip()
                 time=time[:5]
                 #print("time",time)
                 line_out.append(str(word[3]).rstrip())
                 rec=str(f_date)+" "+str(time)+" "+str(word[1])+" "+str(word[2])+" "+str(word[5])+" "+str(word[3])+"\n"                 

##         squery='select time,lat,long,cluster,text from filtered'
##         result=client.query(squery)
##         text=list(result.get_points(measurement='filtered'))
##         text=sorted(text,key=itemgetter('cluster'))
##         for i in range(len(text)):
##             time=str(text[i]['time'])
##             time=time[:10]+" "+time[11:16]
##             rec=time+" "+str(text[i]['lat'])+" "+str(text[i]['long']).strip()+" "+str(text[i]['cluster'])+" "+str(text[i]['text'])
##             rec=rec+"\n"
##                 print("rec",rec)
                 myFile.write(rec)
     with open('testabc.txt','r')as myFile:
         str1=myFile.read()
         punctuation = ['!', '"', '..', '  ', '#', '$', '%', '&', '(', ')', '*', ',', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'] 
         for i in punctuation:
             str1 = str1.replace(i,"")
     #sys.stdout=open("st2.txt","w")
     with open("st2.txt","w")as myFile:
         myFile.write(str1+"\n")
     #sys.stdout.close()
     os.remove('testabc.txt')
     with open("st2.txt") as f:
         reader=csv.reader(f,delimiter=" ")
         d=list(reader)
     dn=[x for x in d if x]
     dlen=len(dn)
     f.close()
     for i in range(0,dlen-1):
         for k in range(i+1,dlen):
             if dn[k][1]!="" and dn[i][1]!="":
                 time_ini=datetime.datetime.strptime(dn[i][1], '%H:%M')
                 time_ini=time_ini-datetime.timedelta(minutes=5)
                 time_out=datetime.datetime.strptime(dn[k][1], '%H:%M')
                 if time_out>=time_ini:
                     lat_diff=abs(float(dn[i][2])-0.00002)
                     lat_add=abs(float(dn[i][2])+0.0002)
                     long_diff=abs(float(dn[i][3])-0.00002)
                     long_add=abs(float(dn[i][3])+0.0002)
                     if float(dn[k][2])<lat_add and float(dn[k][2])>lat_diff and float(dn[k][3])<long_add and float(dn[k][3])>long_diff:
                         dn[k][0]=""
                         dn[k][1]=""
                         dn[k][2]=""
                         dn[k][3]=""
                         dn[k][4]=""
##                 else:
##                     break
     file=open("testabc1.txt","w")
     for i in range(0,len(dn)):
         for j in d[i]:
             file.write(j)
            # print(j, end=" ")
             file.write(" ")
         if(i<len(dn)-1):
             if(d[i+1][0]!=""):
                 file.write("\n")
                 #print("\n")
     file.close()
     os.remove('st2.txt')
     with open('testabc1.txt','r') as inf, open("m.txt",'w') as m:
         for i in inf:
             i= i.replace("   "," ")
             i = i.replace("  "," ")
             m.write(i)
     inf.close()
     m.close()
     os.remove('testabc1.txt')
     #sys.stdout=open("t.txt","w")
     with open('t.txt', 'w') as t_input:
         with open('m.txt', 'r') as fileinput:
            for line in fileinput:
                line = line.rstrip().lower()
                #print(line)
                word=line.split(" ")
                #print(word[5:])
                rec=""
                other_data=""
                for i in range(0,5):
                    other_data=other_data+word[i]+" "
                for i in range(5,len(word)):
                    rec=rec+word[i]+" "
                rec.rstrip()
                rec=rec+"\n"
                loc_data.append(other_data)
##                #print(rec)
                t_input.write(rec)
     #sys.stdout.close()
     os.remove('m.txt')
     return line_out,cluster_count

def second():
     lst = []
     result = []
     ndc = []
     mlist = []
     synonyms = []
     casu_syn = []
     p=1
     ndc1=""
     word_index=[]
     num=[]
     words=[]
     punctuation = ['!', '"', '..', '  ', '#', '$', '%', '&', '(', ')', '*', ',', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '.', ':']
     #print("loc_data")
     with open('dcw.txt') as q:
         for s in q:
             for e in nltk.word_tokenize(s):
                 lst.append(e)
                 for syn in wordnet.synsets(e):
                         for l in syn.lemmas():
                             synonyms.append(l.name())
     for line in set(synonyms):
         result.append(line)
     c = len(lst)
     with open("temp.txt","w") as temp_input:
         with open('t.txt', 'r') as inf, open ('Final_output.txt', 'a') as of:
             count_loc=0  
             for i in inf:
                 ndc[:]=[]
                 words[:]=[]
                 num[:]=[]
                 word_index[:]=[]
                 for x in range(c):
                    mlist.append(0)
                 v=0
                 temp_input.write("\n")
                 temp_input.write("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                 temp_input.write("\t\t\t\t\tMessage no:"+str(p))
                 temp_input.write("\n\t\tInput message\n")
                 temp_input.write(i)
                 temp_input.write("Total Disaster Content Words present ")
                 words = nltk.word_tokenize(i)
                 for k in nltk.word_tokenize(i):
                 #for k in words:
                     for w in lst:
                        if(k==w and k in result):
                             temp_input.write(k+" ")
                             v=lst.index(w)
                             #print(v)
                             mlist[v] = mlist[v]+1
                     if( k not in result and k not in punctuation):
                         ndc.append(k)
                         #print(k)
                 #print("mlist",mlist)
                 for d in range(len(mlist)):
                     if(mlist[d]>0):
                         if( lst[d] not in ndc):
                             ndc.append(lst[d])
                 temp_input.write("\nThe Counting array is as follows")
                 temp_input.write(str(mlist))
                 p=p+1
                 mlist[:]=[]
                 temp_input.write("\nOutput Message\n")
                 #print(ndc)
                 z=len(ndc)
                 loc=loc_data[count_loc]
                 loc1=loc.split(" ")
                 #print("loc",loc)
                 #print("loc[0] and [1]",loc1[0],loc1[1])
                 ndc=[str(loc1[1])]+ndc
                 ndc=[str(loc1[0])]+ndc
                 ndc1=ndc1+str(ndc)+"\n"
                 of.write(str(ndc)+"\n")
                 count_loc+=1
     #inf.close()
     #sys.stdout.close()
     os.remove('temp.txt')
     os.remove('t.txt')
     print("Content Filtration Done")
     ndc1=ndc1.rstrip()
     return ndc1

def cf(corpus,snap_time,tw_flag):
    
    if tw_flag==0:
        print("snapshot_timestamp= ",snap_time)
        with open('/home/pi/Test_15/fold/report.txt','a') as rec:
            rec.write(snap_time+"\n")
     #smooth_str="2018-08-27%18:33:04%22.57378518%88.41767695%dead%500%1\n2018-08-27%17:35:04%22.57378518%88.41767695%injured%540%1\n2018-08-27%17:53:04%22.57378518%88.41767695%dead%550%1\n2018-08-27%17:33:04%22.57378518%88.41767695%dead%100%2"
    loc_data=[]
    line_out,cluster_count=first(corpus)
    ndc=second()
    print("Cluster Count",cluster_count)
    pdf_report=dict_creation(ndc,line_out,cluster_count)
    return pdf_report
    
     
#content_filtration()
