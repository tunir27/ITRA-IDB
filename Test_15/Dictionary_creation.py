import nltk
import sys
import string
import re
import nltk.corpus
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from collections import Counter
import collections
import ast

from report_generation import report_generation
##
##with open('setnepal.txt','r') as f:
##    f1 = f.read()
##
##list = open("setnepal.txt").readlines()
##
##
##f2=open('pnepalset.txt','w+') 
##    

list1 = []

def extract_words(s):
    return [re.sub('^@[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]

def dict_creation(ndc,line_out,cluster_count):
    #print("ndc",ndc)
    #print("line_out",str(line_out))
##    for i in list:
##        counter = 0
##        st = str(i)
##        list1 = extract_words(st)
##        for j in list1:
##            st = str(j)
##            if (counter ==0):
##                if (st.startswith('@')):
##                    counter = counter +1
##                    continue
##                elif(st.startswith('#')):
##                    for c in st:
##                        if (c == '#'):
##                            st1=st.lstrip(c)
##                            f2.write(st1)
##                            f2.write(' ')
##                            counter=counter+1
##                else:
##                    f2.write(st)
##                    f2.write(' ')
##                    counter = counter +1
##            else:
##                if(st.startswith('@') | st.startswith('#') | st.startswith('+') | st.startswith('(')):
##                    for c in st:
##                        if ((c == '#') | (c == '@') | (c == '+') | (c == '(')):
##                            st1=st.lstrip(c)
##                            f2.write(st1)
##                            f2.write(' ')
##                            break
##
##                elif (st.startswith('http:') |st.startswith('https:')):
##                    continue
##                else:
##                    f2.write(st)
##                    f2.write(' ')
##        f2.write('\n')
##    f2.close()
    #Buillding corpus 

    #corpusdir = 'E:/'
    #newcorpus = PlaintextCorpusReader(corpusdir, ['short.txt'])
    #raw = open('C:\Program Files (x86)\Python36-32\short.txt').read() 
    #abstract = nltk.Text(newcorpus.words('short.txt'))
    #st = str(abstract)
    #print(st)
    #tokens = nltk.word_tokenize(raw)
    #text = nltk.Text(tokens)
    #t = text.collocations()
    #print(t)

    #POS TAG 
    datadic = dict()
    conjdic = dict()

##    with open('pnepalset.txt','r') as f:
##        f1 = f.read()
##
##    list = open("pnepalset.txt").readlines()
    

    list1=[]
    listtag = []
    dict_data=""
    counter = 0
    c = 0
    report_input=""
##    f3=open('dictionary.txt','w+') 


    temp_pos={}
    for i in line_out:
        token = word_tokenize(i)
        T = nltk.pos_tag(token)
        for j in T:
            j=str(j)
            if j in temp_pos:
                temp_pos[j]+=1
            else:
                temp_pos[j]=1
    od = collections.OrderedDict(sorted(temp_pos.items()))
    #print(od)
    temp_list=[]
    flag=0
    for k, v in od.items():
        key_tags=ast.literal_eval(k)
        max_value=v
        for t_k, t_v in od.items():
            t_k_tags=ast.literal_eval(t_k)
            if key_tags[0].lower()==t_k_tags[0].lower() and key_tags[0].lower().strip():
                if t_v>max_value:
                    max_value=t_v
                    key_tags=ast.literal_eval(t_k)

        if key_tags[0].strip().lower() not in temp_list:
            #print(key_tags[0].strip().lower()+"  "+key_tags[1].strip())
            dict_data=dict_data+str(key_tags[0].strip().lower()+"  "+key_tags[1].strip()+"\n")
##            f3.write(key_tags[0].strip().lower()+"  "+key_tags[1].strip()+"\n")
            temp_list.append(key_tags[0].lower().strip())
    dict_data=dict_data.rstrip()
    #print("dict_data",dict_data)

##    for i in temp_pos.keys():
##        key_tags=ast.literal_eval(i)
##        
##
##    for i in list:                                          
##        list1 = extract_words(i)
##        #print(c)
##        counter+=1
##        for j in list1:
##            #del listtag[:]
##            listtag=[]
##            if (j.lower() not in datadic):
##                for k in list:
##                    token = word_tokenize(k)
##                    T = nltk.pos_tag(token)
##                    for a,b in T:                               
##                        if (a.lower() == j.lower()):
##                            listtag.append(b)
##                    tag = Counter(listtag).most_common(1)
##                    #print(tag)
##                    for w in tag:
##                        datadic.update({j.lower():w[0]})
##            #print(datadic)
##            if ((len(datadic) == 1) & (c == 0)):
##                #f3=open('dictionary.txt','w+')
##                #print(datadic)
##                for k, v in datadic.items():
##                    report_input+=k+ " "+ v + "\n"
##                    #print(k+v)
##                    f3.write(k + '  ' + v)
##                    f3.write('\n')
##                        
##                datadic.clear()
##                #f3.close()
##                c = 1
##
##            elif(len(datadic) == 100):
##                #f3=open('dictionary.txt','a+')
##                #print(datadic)
##                for k, v in datadic.items():
##                    report_input+=k+ " "+ v + "\n"
##                    #print(k+v)
##                    f3.write(k + '  ' + v)
##                    f3.write('\n')
##                datadic.clear()
##                #f3.close()

            
                    
##    print("Report",report_input)
##    with open('dabi.txt','r') as f3:
##        f12 = f3.read()
##
##    list = open("dabi.txt").readlines()

    in_ndc=ndc.split("\n")
    inputpos=""

##    with open('dictionary.txt','r') as f:
##        f1 = f.read()

    #list1 = open("dictionary.txt",'r').readlines()
    list1=dict_data.split("\n")
    #fpos = open('inputpos.txt', 'a+' )

    listpos = []
    c =0
    v = 0
    for i in in_ndc:
        st = str(i)
        j = re.sub('[^A-Za-z]+', '  ', i)
        k = extract_words(j)
        for q in k:
            qstr = str(q)
            for w in list1:
                st = str(w)
                k1 = extract_words(w)
                k1str = str(k1[0])
                if(qstr.lower() == k1str):
                    c = 1
                    t = k1[1]
            if(c == 1):
                listpos.append((qstr,t))
                c = 0
        #print(listpos)
        if (v ==0):
            v = 1
##            fpos = open('inputpos.txt', 'w+' )
##            fpos.write(str(listpos))
##            fpos.write('\n')
            inputpos=inputpos+str(listpos)+"\n"
        else:
##            fpos = open('inputpos.txt', 'a+' )
##            fpos.write(str(listpos))
##            fpos.write('\n')
            inputpos=inputpos+str(listpos)+"\n"
            
        listpos.clear()

##    fpos.close()
    inputpos=inputpos.rstrip()
    #print("inputpos",inputpos)
    print("Dictionary Created")
    pdf_report=report_generation(dict_data,inputpos,line_out,cluster_count)
    return pdf_report  
    
