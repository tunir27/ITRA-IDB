import os
import numpy as np
import pandas as pd
import csv
import operator

     
def exp_smoothing(smooth_str,snapshot_timestamp,tw_flag):
     #print(smooth_str)
     #print(snapshot_timestamp)
     #Program to do exponential smoothing
     cluster_count=[1]
     lines=smooth_str.split("\n")
     if tw_flag==0:
          with open('/home/pi/Test_15/fold/smooth.txt','a') as rec:
               rec.write(snapshot_timestamp+"\n")
               rec.close()
##     for line in lines:
##          if line!="":
##               word=line.split("%")
##               if int(word[6]) not in cluster_count:
##                    cluster_count.append(int(word[6]))
     f1=[]
     f2=[]
     f3=[]
     f4=[]
     f5=[]
     f6=[]
     f7=[]
     pdf_out=""
     for line in lines:
          line=line.replace("\n","")
          if line!="":
               word=line.split("%")
               #print(word)
               f1.append(str(word[0]))
               f2.append(str(word[1]))
               f5.append(str(word[2]))
               f6.append(str(word[3]))
               f3.append(str(word[4]))
               f4.append(int(word[5]))
               f7.append(str(word[6]))
     #print("f4",f4)
     if f4==[]:
          return
     #print(f7)
##          data=pd.read_csv('num_extract.csv')
##          data.head()
##          f1=data['Date'].values
##          f2=data['Time'].values
##          f5=data['Latitude'].values
##          f6=data['Longitude'].values
##          f3=data['Keyword'].values
##          f4=data['Quantity'].values
##          f7=data['Cluster'].values
     f=[]
     sm=[]
     cnt=0
     X=np.array(list(zip(f4)))
     '''print'length of data        ',len(X)
     for i in range(1,len(X)):
         print i,'\t\t',f1[i-1]'''
     cnt=cnt+1
     j=f4[0]
     sm.append(j)
     #print ('Enter the damping factor')
     #dmp=input('Damping Factor:')
     dmp=0.8
     for i in range(1,len(X)):
         k=int((dmp*X[i])+((1-dmp)*sm[i-1]))
         sm.append(k)
         cnt=cnt+1
     gg=open('exponential_output.csv','w',newline="")
     writer=csv.writer(gg)
    # print ('Date        Time     word    number      Smoothed Values')
     #print ('----        ----     ----    ------      ---------------')
     writer.writerow(['Date','Time','Latitude','Longitude','Keyword','number','Smoothed Values','Cluster'])
     for i in range(len(X)):
        # print (f1[i],'  ',f2[i],'  ',f3[i],'   ',f4[i],'             ',sm[i],'\n')
         writer.writerow([f1[i],f2[i],f5[i],f6[i],f3[i],f4[i],sm[i],f7[i]])
         jj=f2[i]
     gg.close()
     da=pd.read_csv('exponential_output.csv')
     fi=open('exp_store.txt','w')
     writer2=csv.writer(fi)
     writer2.writerow(['Date','Time','Latitude','Longitude','word','number','Smoothed Values','Cluser'])
    # print ('values to consider')
     #print (da.groupby('Keyword').tail(1))
     #print(da)
     kt=da.groupby('Keyword').tail(1)
     st=kt.values
     #st=np.array2string(st)
     #print(st[0][0])
     with open('/home/pi/Test_15/fold/smooth.txt','a') as rec:
          for text in st:
               print("text",text)
               pdf_out+=str(text[4])+' '+str(text[6])+'\n'
               temp=str(text[4])+'%'+str(text[6])+'%'+str(text[7])+'\n'
               rec.write(temp)
     kt.to_csv('final_filtered_exponential_outputp.csv')


     with open("final_filtered_exponential_outputp.csv","r",newline="") as source:
         rdr= csv.reader( source )
         with open("final_smooth_result.csv","a",newline="") as result:
             wtr= csv.writer( result )
             for r in rdr:
                 wtr.writerow( (r[1], r[2], r[3], r[4],r[5],r[6],r[7],r[8]) )
         result.close()
     source.close()
     fi.close()
     os.remove('final_filtered_exponential_outputp.csv')
     os.remove('final_smooth_result.csv')
     os.remove('exp_store.txt')
     os.remove('exponential_output.csv')
     print("Smoothing Done")
     return pdf_out
     
##def master():
##     import os
##     import sys
##     exp_smoothing()
##     
##master()
