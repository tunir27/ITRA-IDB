import nltk
import sys
import string
import re
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import state_union
from nltk.corpus import stopwords
import copy
import ast

#list1=[('the', 'DT'), ('prime', 'NNP'), ('minister', 'NNP'), ('spoke', 'VBD'), ('west', 'NNP'), ('bengal', 'NNP'), ('chief', 'NNP'), ('minister', 'NNP'), ('mamataofficial', 'NNP'), ('situation', 'NN'), ('arising', 'VBG'), ('wake', 'NN'), ('shri', 'NNP'), ('rahul', 'NNP'), ('statement', 'NN'), ('massive', 'JJ'), ('today', 'NN'), ('my', 'PRP'), ('thoughts', 'NNS'), ('prayers', 'NNS'), ('people', 'NNS'),  ('to', 'TO'),('on', 'IN'), ('the', 'DT'),('in', 'IN'), ('the', 'DT'),('of', 'IN'), ('the', 'DT'),('affected', 'VBN'), ('massive', 'JJ'), ('nepal', 'NNP'), ('parts', 'NNS'), ('india', 'NNP'), ('earthquake', 'NN')]

def report_generation(dict_data,inputpos,line_out,cluster_count):
##    print("dict_data",dict_data)
##    print("inputpos",inputpos)
##    temp=""
##    for i in line_out:
##        temp+=i+"\n"
##    print("line_out",temp)
    count_skip=0
    
    input_file=inputpos.split("\n")
    for list1 in input_file:
        try:
            list1=ast.literal_eval(list1)
            #print("LIST1",list1)
            pos_list=[]
            Noun=[]
            Adjective=[]
            Pronoun=[]
            Adverb=[]
            Verb=[]
            Preposition=[]
            Combination=[]
            temp_list=[]


            print("COMMING HERE 1")
            #print(pos_list)

            for token in list1:
                if (token[1] in ['NN', 'NNS', 'NNP', 'NNPS']):
                    Noun.append(token)
                elif(token[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']):
                    Verb.append(token)
                elif(token[1] in ['JJ', 'JJR', 'JJS', 'CD','DT']):
                    Adjective.append(token)
                elif(token[1] in ['IN', 'TO']):
                    Preposition.append(token)
                elif(token[1] in ['RB', 'RBR', 'RBS']):
                    Adverb.append(token)
                elif (token[1] in ['PRP', 'PRP$ ', 'WP','WP$']):
                    Pronoun.append(token)
                else:
                    continue
    ##            print('Number of Nouns')
    ##            print(Noun)
    ##            print('Number of Verbs')
    ##            print(Verb)
    ##            print ('Number of Adjectives')
    ##            print(Adjective)
    ##            print('Number of Adverbs')
    ##            print(Adverb)
    ##            print('Number of Prepositions')
    ##            print(Preposition)
    ##            print('Number of Pronouns')
    ##            print(Pronoun)
            temp2_list=[]
            temp3_list=[]
            temp4_list=[]
    ##        dic_file=open('dictionary.txt', 'r').readlines()
            dic_file=dict_data.split("\n")
            temp_dic=[]
            for line1 in dic_file:
                line1=line1.replace("\n","").replace("  "," ")
                temp_dic.append(line1.split(" "))


            for line in line_out:
                tempi_list=[]
                tokenized = nltk.word_tokenize(line)
                    
                for token in tokenized:                                                                                  #Corpus Pos tagging from created dictonary (dictionary.txt)
                    for line1 in temp_dic:
                        if (token.lower()== line1[0]):
                            tempi_list.append((token, line1[1]))
                            break
                        else:
                            continue
                    
                temp_list.append(tempi_list)
                temp2_list.append(tempi_list)
                temp3_list.append(tempi_list)
                temp4_list.append(tempi_list)


    ##        file.close()

            #print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
            #print('After Correct Tagging of Each Word in Filtered list')
            #print (temp_list)
            print("COMMING HERE 1")

            def prefix_noun_pronoun(list11, count_list11):
                for line in temp3_list:
                    #print(line)
                    flag=0
                    temp1_list=[]
                    list2=[]
                    list3=[]
                    for w in line:
                        if (w[0].lower()==verb[0]):
                            flag=1
                            break
                        else:
                            temp1_list.append(w)
                    if (flag==1):
                        #print('hello')
                        #print(temp1_list)
                
                        for noun in Noun:
                            list2.append(noun[0])
                        #print(list2)
                        for pronoun in Pronoun:
                            list3.append(pronoun[0])
                        for w in reversed (temp1_list):
                            if ((w[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ'])& (w[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                                break
                            else:
                                if ((w[1] in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$','WP','WP$']) & ((w[0].lower() in list2  )| (w[0].lower() in list3))& (w not in operation_list)& (w not in list11)):
                                    operation_list.append(w)
                                    list11.append(w)
                                    count_list11=count_list11+1

                    del temp1_list
                    del list2
                    del list3
                operation_list.reverse()
                list11.reverse()
                operation_list.append(verb)
                list11.append(verb)
                count_list11=count_list11+1
                return list11, count_list11



            def suffix_noun_pronoun(list11, count_list11,temp_verb):
                 if (len(list11)<=1):
                    ##temp_verb=verb[0]
                    #print(temp_verb)
                    for line in temp_list:
                        list_p=[]
                        temps_list=[]
                        list_p.append (line)
                        c=0
                        for w in list_p:
                             for p in w:
                                 if(p[0].lower()!=temp_verb):
                                     c=c+1
                                     continue
                                 else:
                                    temps_list=w[c+1: ]
                                    #print('HI')
                                    #print(temps_list)
                                    list2 =[]
                                    list3=[]
                                    list22=[]
                                    for noun in Noun:
                                        list2.append(noun[0])
                                    for pronoun in Pronoun:
                                        list3.append(pronoun[0])
                                    for s in temps_list:
                                        if ((s[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ'])&(s[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                                            break
                                        else:
                                            if ((s[1] in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$','WP','WP$']) & ((s[0].lower() in list2)| (s[0].lower in list3))):
                                                list11.append(s)
                                    
                
                                        
                                        
                 else:
                    #temp_verb=verb[0]
                    #print(temp_verb)
                    for w in operation_list:
                        if (w[1] in ['NN', 'NNS', 'NNP', 'NNPS' ,'PRP', 'PRP$','WP','WP$']):
                            temp1=w[0]
                            for line in temp_list:
                                #print(line)
                                temps_list=[]
                                tempy_list=[]
                                list_p=[]
                                list_p.append(line)
                                #print("2nd")
                                #print(list_p)
                                c=0
                                for w in list_p:
                                    for p in w:
                                        if (p[0]!=temp1):
                                            c=c+1
                                            continue
                                        else:
                                            temps_list=w[c+1: ]
                                        j=0
                                        for r in temps_list:
                                            if (r[0]!=temp_verb):
                                                j=j+1
                                                continue
                                            else:
                                                tempy_list=temps_list[j+1: ]
                                                list2=[]
                                                list3=[]
                                                list22=[]
                                                for noun in Noun:
                                                    list2.append(noun[0])
                                                for pronoun in Pronoun:
                                                    list3.append(pronoun[0])
                                                
                                                for s in tempy_list:
                                                        if ((s[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ'])&(s[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                                                            break
                                                        else:
                                                            if ((s[1] in ['NN', 'NNS', 'NNP', 'NNPS' ,'PRP', 'PRP$','WP','WP$']) & ((s[0].lower() in list2)|(s[0].lower() in list3))):
                                                                list22.append(s)
                                                if (list11[count_list11: ]!=list22):
                                                    for w in list22:
                                                        if (w[0] not in list11[count_list11: ]):
                                                            list11.append(w)
                                                else:
                                                    continue
                                                
                                                
                                            
                                            del list2
                                            del list3
                        
                                #line=temps_list + w
                                del list_p
                                del temps_list
                                del tempy_list


                    
                 op_list=[]
                 prefixnoun_list=[]
                 Final_adj=[]
                 #print('After Suffix noun and pronoun list')
                 #print(list11)
                 op_list=list11
                 return list11




            def adjective_prefix_noun_pronoun(list11, op_list, temp_verb):
                prefixnoun_list=[]
                count_prefix_noun=0
                for w in op_list:
                    if (w[0].lower()==temp_verb):
                        break
                    else:
                        prefixnoun_list.append(w)
                        count_prefix_noun=count_prefix_noun+1
                #print(prefixnoun_list)
                c= count_prefix_noun
                #print(c)
                for x in prefixnoun_list:
                    loc=0
                    temp_noun=x[0]
                    #print(temp_noun)
                    for w in list11:
                        if(w[0].lower()!=temp_noun):
                            loc=loc+1
                    
                    for line in temp3_list:
                        flag=0
                        list_tempo=[]
                        temp_adj=[]
                        for w in line:
                        
                            if (w[0]!=temp_noun):
                                list_tempo.append(w)
                                
                            else:
                                flag=1
                                break
                        
                        if (flag==1):
                             list_tempo.reverse()
                             #print(list_tempo)
                             for w in list_tempo:
                                 if (w[1] in ['JJ', 'JJR', 'JJS', 'CD','DT']):
                                     temp_adj.append(w)
                                 elif (w[1] in ['NN', 'NNS', 'NNP', 'NNPS','PRP', 'PRP$','WP','WP$']):
                                      break
                                 else:
                                      break
                             #print(temp_adj)
                             if (temp_adj==[]):
                                 del list_tempo
                                 continue
                             else:
                                list2=[]
                                for adj in Adjective:
                                    list2.append(adj[0])
                                c=0
                                for w in list11:
                                    if (w[0]!=temp_noun):
                                        c=c+1
                                        continue
                                    elif(c==0):
                                        for y in temp_adj:
                                            if((y[0].lower()in list2)):
                                               list11.insert(c,y)
                                               c=c+1
                                    else:
                                        p1=loc-1
                                        for y in temp_adj:
                                            if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                                list11.insert(c, y)
                                                c=c+1
                                            else:
                                                continue
                                    break
                                del list2
                        del temp_adj
                        del list_tempo
                
                #print('After Adjective prefix of nouns and pronouns')
                #print(list11)
                return list11



                


            def adjective_suffix_noun_pronoun(list11, temp_verb):
                suffix_noun=[]
                #Final_adj_suffix=[]
                list11.reverse()
                #print(list11)
                count_suffix_noun=0
                for w in list11:
                    if (w[0].lower()==temp_verb):
                        break
                    else:
                        suffix_noun.append(w)
                        count_suffix_noun=count_suffix_noun+1
                suffix_noun.reverse()
                list11.reverse()
                #print(list11)
                #print(suffix_noun)
                #c=count_suffix_noun
                #print(c)

                for x in suffix_noun:
                    loc=0
                    temp_noun=x[0]
                    #print(temp_noun)
                    for w in list11:
                        if(w[0].lower()!=temp_noun):
                            loc=loc+1
                    for line in temp3_list:
                        flag=0
                        list_tempo=[]
                        temp_adj=[]
                        for w in line:
                        
                            if (w[0].lower()!=temp_noun.lower()):
                                list_tempo.append(w)
                                
                            else:
                                flag=1
                                break
                        
                        if (flag==1):
                             list_tempo.reverse()
                             #print(list_tempo)
                             #print(list_tempo)
                             for w in list_tempo:
                                 if (w[1] in ['JJ', 'JJR', 'JJS', 'CD','DT']):
                                     temp_adj.append(w)
                                 elif (w[1] in ['NN', 'NNS', 'NNP', 'NNPS','PRP', 'PRP$','WP','WP$']):
                                     if (w[0].lower() in suffix_noun):
                                         break
                                     else:
                                        temp_adj=[]
                                        break
                                 else:
                                      break
                             #print(temp_adj)
                             if (temp_adj==[]):
                                 #c=c-1
                                 del list_tempo
                                 continue
                             else:
                                list2=[]
                                for adj in Adjective:
                                    list2.append(adj[0])
                                c=0
                                for w in list11:
                                    if (w[0].lower()!=temp_noun):
                                        c=c+1
                                        continue
                                    elif(c==0):
                                        for y in temp_adj:
                                            if((y[0].lower()in list2)):
                                               list11.insert(c,y)
                                               c=c+1
                                    else:
                                        #print('Value of c')
                                        #print (c)
                                        p1=loc-1
                                        #print('Value of p1')
                                        #print(p1)
                                        for y in temp_adj:
                                            if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                                list11.insert(c, y)
                                                c=c+1
                                            else:
                                                continue
                                    break
                                
                                del list2
                        del temp_adj
                        del list_tempo
                
                #print('After Adjective suffix nouns and pronouns')
                #print(list11)
                return list11





            def adverb_prefix_verb(list11, temp_verb):
                Final_adv_prefix=[]
                for line in temp3_list:
                    flag=0
                    list_tempo1=[]
                    temp_adv=[]
                    for w in line:
                        
                        if (w[0].lower() != temp_verb):
                            list_tempo1.append(w)
                        else:
                            flag=1
                            break
                        

                    if(flag==1):
                        list_tempo1.reverse()
                        #print(list_tempo1)
                        for w in list_tempo1:
                            if (w[1]  in ['RB', 'RBR', 'RBS']):
                                temp_adv.append(w)
                            else:
                                break
                       # print(temp_adv)

                        if (temp_adv==[]):
                            del list_tempo1
                            continue
                        else:
                            list2=[]
                            for adv in Adverb:
                                list2.append(adv[0])
                                
                            c=0
                            for w in list11:
                                if (w[0].lower()!=temp_verb):
                                    c=c+1
                                    continue
                                else:
                                    p1=c-1
                                    for y in temp_adv:
                                        if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                            list11.insert(c, y)
                                            c=c+1
                                        else:
                                            continue
                                break
                            del list2
                    del temp_adv
                    del list_tempo1
                    
                #print('Adverb In prefix of verb')
                #print(list11)
                return list11





            def adverb_suffix_verb(list11, temp_verb):
                for line in temp2_list:
                    #line.reverse()
                    flag=0
                    list_tempo1=[]
                    temp_adv=[]
                    for w in reversed(line):
                
                        if (w[0].lower() != temp_verb):
                            list_tempo1.append(w)
                        else:
                            flag=1
                            break
                        

                    if(flag==1):
                        list_tempo1.reverse()
                        #print(list_tempo1)
                        for w in list_tempo1:
                            if (w[1]  in ['RB', 'RBR', 'RBS']):
                                temp_adv.append(w)
                            else:
                                break
                        #print(temp_adv)

                        if (temp_adv==[]):
                            del list_tempo1
                            continue
                        else:
                            list2=[]
                            for adv in Adverb:
                                list2.append(adv[0])
                                
                            c=0
                            for w in list11:
                                if (w[0].lower()!=temp_verb):
                                    c=c+1
                                    continue
                                else:
                                    c=c+1
                                    p1=c-1
                                    for y in temp_adv:
                                        if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                            list11.insert(c, y)
                                            c=c+1
                                        else:
                                            continue
                                break
                            del list2
                    del temp_adv
                    del list_tempo1

                #temp2_list=temp4_list
                #print('6th temp2 list')
                #print(temp2_list)
                #print('adverb in suffix of verb')
                #print(list11)
                return list11


            def adverb_prefix_adjective(list11, Adj_list11):
                for w in list11:
                    if (w[1] in ['JJ', 'JJR', 'JJS', 'CD']):
                        Adj_list11.append(w)
                
                #print(Adj_list11)

                for p in Adj_list11:
                    for line in temp3_list:
                        flag=0
                        list_tempo2=[]
                        temp_adv=[]
                        for w in line:
                            if (w[0].lower() != p[0].lower()):
                                list_tempo2.append(w)
                            else:
                                flag=1
                                break

                        if (flag==1):
                            list_tempo2.reverse()
                            for w in list_tempo2:
                                if (w[1]  in ['RB', 'RBR', 'RBS']):
                                    temp_adv.append(w)
                                else:
                                    break
                            if (temp_adv==[]):
                                del list_tempo2
                                continue
                            else:
                                list2=[]
                                for adv in Adverb:
                                    list2.append(adv[0])

                                c=0

                                for  w in list11:
                    
                                    if (w[0].lower()!=p[0].lower()):
                                        c=c+1
                                        continue
                                    else:
                                        p1=c-1
                                        for y in temp_adv:
                                             if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                                 list11.insert(c, y)
                                                 c=c+1
                                             else:
                                                continue
                                    break
                                del list2
                        del temp_adv
                        del list_tempo2

                
                return list11, Adj_list11






            def adverbs_suffix_adjective(list11, Adj_list11):
                for p in Adj_list11:
                    for line in temp3_list:
                        #line.reverse()
                        flag=0
                        list_tempo2=[]
                        temp_adv=[]
                        for w in reversed(line):
                            if (w[0].lower() != p[0].lower()):
                                list_tempo2.append(w)
                            else:
                                flag=1
                                break

                        if (flag==1):
                            list_tempo2.reverse()
                            for w in list_tempo2:
                                if (w[1]  in ['RB', 'RBR', 'RBS']):
                                    temp_adv.append(w)
                                else:
                                    break
                            if (temp_adv==[]):
                                del list_tempo2
                                continue
                            else:
                                list2=[]
                                for adv in Adverb:
                                    list2.append(adv[0])

                                c=0

                                for  w in list11:
                    
                                    if (w[0].lower()!=p[0].lower()):
                                        c=c+1
                                        continue
                                    else:
                                        p1=c-1
                                        for y in temp_adv:
                                             if((y[0].lower() in list2)& (y not in list11[p1:c])):
                                                 list11.insert(c, y)
                                                 c=c+1
                                             else:
                                                continue
                                    break
                                del list2
                        del temp_adv
                        del list_tempo2
                        
                #temp2_list=temp4_list
                #print(temp2_list)
                #print('8th temp2 list')
                #print(temp2_list)
                #print('Adverbs suffix of Adjectives')
                #print(list11)

                 #prepositional phrases prefix of nouns or pnouns / nouns or pronouns with modifiers
                #print('Final list is:')
                #print(list11)
                return list11


            for verb in Verb:
                operation_list=[]
                count_list11=0
                list11=[]
                list11, count_list11=prefix_noun_pronoun(list11, count_list11)
                #print('After arranging prefix nouns and pronouns')
                #print(list11)
                #print(count_list11)
                #print(verb[0])
                list11=suffix_noun_pronoun(list11, count_list11, verb[0])
                #print('After arranging suffix nouns and pronouns')
                #print(list11)
                operational_list=list11
                list11=adjective_prefix_noun_pronoun(list11, operational_list, verb[0])
                #print('After arranging adjectives prefix of nouns and pronouns')
                #print(list11)
                list11= adjective_suffix_noun_pronoun(list11, verb[0])
                #print('After arranging adjectives suffix of nouns and pronouns')
                #print(list11)
                list11=adverb_prefix_verb(list11, verb[0])
                #print('After arranging adverbs prefix of verbs')
                #print(list11)
                list11=adverb_suffix_verb(list11, verb[0])
                #print('After arranging adverbs suffix of verbs')
                #print(list11)
                Adj_list11=[]
                list11, Adj_list11=adverb_prefix_adjective(list11,Adj_list11)
                #print('After arranging adjectives prefix of adverbs')
                #print(list11)
                list11= adverbs_suffix_adjective(list11, Adj_list11)
                #print('After arranging adjectives suffix of adverbs')
                #print(list11)
                Combination.append(list11)
                #print(Combination)

            print("COMMING HERE 2")           
            #print('--------------------------------------------------------------------------------------The Final Combination List of statements-----------------------------')
            #print(Combination)
            #Elimination of overlapping for each combination of verb
            count_combination=0

            Redun_list=[]

            Final_comb_list=[]
            for w in Combination:
                count_combination=count_combination+1

            #print(count_combination)

            flag_lst=[]
            for line1 in Combination:
                suffix_list=[]
                for w in reversed (line1):
                    if (w[1] not in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']):
                        suffix_list.append(w)
                    else:
                        break
                suffix_list.reverse()
                for line2 in reversed (Combination):
                    prefix_list=[]
                    #print(line2)
                    if (line2 is line1):
                        continue
                    elif((line1, line2) in flag_lst):
                        continue
                    else:
                        for w in line2:
                            if (w[1] not in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']):
                                prefix_list.append(w)
                            else:
                                break

                    a_set=set(suffix_list)
                    b_set=set(prefix_list)
                    
                    #print(a_set)
                    #print(b_set)
                    if (b_set.issubset(a_set)):
                        list50=sorted (set (set(line2)- b_set),key=line2.index)
                        Redun_list.append(line1+list50)
                        #print(Redun_list)
                        flag_lst.append((line1, line2))
                        #flag_lst.append(line2)
                        #print(flag_lst)
                        #single_comb=[]
                        if (a_set - b_set):
                            single_comb=sorted(set (set(suffix_list)- b_set),key=line1.index)
                            Redun_list.append(line1+single_comb)
                            #del single_comb
                            
                    else:
                        continue

            #print(Redun_list)
            #print(flag_lst)

            Val=0

            if (flag_lst==[]):
                Val=1
                for line in Combination:
                    Redun_list.append(line)
            else:
                Val=2
                for line in Combination:
                    flag=0
                    #count_combination=count_combination-1
                    for line1, line2 in flag_lst:
                        if ((line1==line) |( line2==line)):
                            flag=1
                            break
                        else:
                            continue
                    if (flag==0):
                        Redun_list.append(line)
                    else:
                        continue

            list51=[]
            list52=[]

            if (Val==1 | Val==2):
                for line in Redun_list:
                    count=0
                    for w in line:
                        if (w[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']):
                            count=count+1
                        else:
                            continue
                    if(count> 1):
                        list52.append(line)
                        continue
                    else:
                        list51.append(line)


            Redun_list1=[]
            flag_lst1=[]




            if (len(list51)>1):
                for line1 in list51:
                    prefix_list1=[]
                    for w in line1:
                        if (w[1] not in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']):
                            prefix_list1.append(w)
                        else:
                            continue
                    for line2 in reversed(list51):
                        prefix_list2=[]
                        if (line2 is line1):
                            continue
                        elif((line1, line2)| (line2, line1) in flag_lst1):
                            continue
                        else:
                            for w in line2:
                                if (w[1] not in ['VB', 'VBD', 'VBG', 'VBN', 'VBZ','VBP']):
                                    prefix_list2.append(w)

                            if(prefix_list1 is prefix_list2):
                                Redun_list1.append(line1+ ('and', 'CC')+ line2)
                                flag_lst1.append((line1,line2))
                            else:
                                continue

            else:
                Final_comb_list=Redun_list


            if(Redun_list1 != []):
                for line in list52:
                    Final_comb_list.append(line)
                for line in Redun_list1:
                    Final_comb_list.append(line)

            #print('///////////////////////////////////////////////////////////////////////////////////////The Final list after combination is://///////////////////////////////////////////////////////////////////')
            #print(Final_comb_list)


            ##for i in temp4_list:
            ##    print(i)
            ##    print("====================================")
            #fixing of content word redudencies in each statement
            #prefix_fixing
            Final_list_after_prefix_fixing=[]
            list_of_verbs_each_statement=[]
            for each_statement in Final_comb_list:
                lower_bound=0
                verb_list=[]
                count=0
                prefix_words=[]
                list=[]
                #print("each_statement",each_statement)
                for word in each_statement[lower_bound:]:
                    if ((word[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']) &(word[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                        verb_list.append(word)
                        list.append(prefix_words)
                        lower_bound=count
                        prefix_words=[]
                        continue
                    else:
                        prefix_words.append(word)
                        count=count+1
                #print(list)
                #print("Verb_list",verb_list)
                #print("prefix_words",prefix_words)
                list_of_verbs_each_statement.append(verb_list)
                c=0
                #print("VERB_LIST",verb_list)
                #print("list",list)
                for prefix_list in list:
                    temp_prefix_list=[]
                    all_prefix=[]
                    for line in temp4_list:
                        if verb_list[c] not in line:
                            continue
                        else:
                            #print("Line",line)
                            #print("verb_list[c]",verb_list[c])
                            for chunk in line:
                                #print("chunk",chunk)
                                
                                if chunk != verb_list[c]:
                                    temp_prefix_list.append(chunk)
                                else:
                                    temph=[]
                                    for val in reversed(temp_prefix_list):
                                        if ((val[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ'])&(val[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                                            break
                                        else:
                                            temph.append(val)
                                            
                                    #print('8888888888888888888888888888888888888888888888888888')
                                    #print("TEMPH",temph)
                                    all_prefix.append(reversed(temph))
                                    temp_prefix_list=[]
                                    break
                    #print('-----------------------------------------------------------------------------------------------------------------------')
                    #print("ALL_PREFIX")
                    #print("PREFIX_LIST",prefix_list)
                    #print(len(all_prefix))
                    lst=[]
                    for val in all_prefix:
                        match_lst=[value for value in val if value in prefix_list]
                        #print("MATCH_LIST",match_lst)
                        lst.append(match_lst)
                    #print("LST",lst)
                    if (len(lst)==1):
                        for lst1 in lst:
                            lst1.insert(len(lst1), verb_list[c])
                            #print(lst1)
                            Final_list_after_prefix_fixing.append(lst1)
                    else:
                        Max=0
                        c1=0
                        for match_list in lst:
                            Max=len(match_list)
                            break
                        for match_list in lst:
                            if (len(match_list)>Max):
                                Max=len(match_list)
                                c1=c1+1
                            else:
                                continue
                        #print(lst[c1])
            ##            print("LST",lst)
            ##            print("LENGTH OF LST",len(lst))
            ##            print("C1",c1)
                        lst[c1].insert(len(lst[c1]), verb_list[c])
                        Final_list_after_prefix_fixing.append(lst[c1])
                    c=c+1
                            
                        


            #Merging of statements before suffix fixing

            Merge_list=[]
            new_list_after_merge=[]
            for val in list_of_verbs_each_statement:
                if (len(val)>1):
                    i=0
                    while(i<len(val)):
                          Merge_list=Merge_list+Final_list_after_prefix_fixing[i]
                          i=i+1
                    new_list_after_merge.append(Merge_list)
                    del Final_list_after_prefix_fixing[:len(val)]
                else:
                    new_list_after_merge.append(Final_list_after_prefix_fixing[0])
                    del Final_list_after_prefix_fixing[:1]



            #suffix Fixing


            for each_statement in Final_comb_list:
                suffix_fixing_list=[]
                all_suffix=[]
                suffix_verb=' '
                each_statement=reversed(each_statement)
                for word in each_statement:
                    if ((word[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']) &(word[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were'])):
                        suffix_verb=word[0]
                        break
                    else:
                        suffix_fixing_list.append(word)
                suffix_fixing_list.reverse()

                for line in temp4_list:
                    if(suffix_verb.lower() not in [x[0].lower() for x in line]):
                        #print('no')
                        continue
                    else:
                        #print('yes')
                        count_pos=0
                        for word in line:
                            if (word[0].lower() !=suffix_verb.lower()):
                                count_pos=count_pos+1
                                continue
                            else:
                                #print('111111111111111111111111111111111111111111111111')
                                #print(line[count_pos:])
                                temp_suffix_words=[]
                                for val in line[count_pos+1:]:
                                    if ((val[1] in ['VB', 'VBD', 'VBG','VBN', 'VBP', 'VBZ']) &(val[0].lower() not in ['am', 'is', 'are', 'been', 'be','being', 'have', 'has', 'had','was','were']) ):
                                        break
                                    else:
                                        temp_suffix_words.append(val)
                                all_suffix.append(temp_suffix_words)
                                break
                s_lst=[]
                for val in all_suffix:
                    match_lst=[value for value in val if value in suffix_fixing_list]
                    s_lst.append(match_lst)
                #print(s_lst)
                #break
                if(len(s_lst)==1):
                    c=0
                    for val in new_list_after_merge:
                        if (suffix_verb.lower() in [x[0].lower() for x in val]):
                            for lst in s_lst:
                                new_list_after_merge[c]=new_list_after_merge[c]+lst
                            #print(new_list_after_merge)
                        else:
                            c=c+1
                            continue
                else:
                    Max=0
                    c1=0
                    for match_list in s_lst:
                        Max=len(match_list)
                        break
                    for match_list in s_lst:
                        if (len(match_list)>Max):
                            Max=len(match_list)
                            c=c1+1
                        else:
                            continue
                    c=0
                    for val in new_list_after_merge:
                        if (suffix_verb.lower() in [x[0].lower() for x in val]):
                            new_list_after_merge[c]=new_list_after_merge[c]+s_lst[c1]
                        else:
                            c=c+1
                            continue

                #print('***************************************')
                #print(all_suffix)

                #print('**************************************************************************')
                #print(suffix_fixing_list)
                #print(suffix_verb)
                        
             #print(Final_list_after_prefix_fixing)
            #print(new_list_after_merge)
            report_file=[]
            for val in new_list_after_merge:
                for word in val:
                    report_file.append(word[0])
                report_file.append('......')

            print("REPORT",report_file)
                    
        
            print('------------------------------------------------------------------------------------------------------------------------------------')
            #print(Final_list_after_prefix_fixing)
            #print(list_of_verbs_each_statement)
            rep+=report_file+"\n"
    
        except:
            count_skip+=1            
            pass
    with open('/home/pi/Test_15/fold/report.txt','a') as report_text:
        report_text.write("Report Not Ready"+"%"+str(cluster_count)+"\n")

    print("Records Skipped",count_skip)
    return "Report Not Ready. Number of Records Skipped in Cluster "+str(cluster_count)+" are"+str(count_skip)+"\n"
