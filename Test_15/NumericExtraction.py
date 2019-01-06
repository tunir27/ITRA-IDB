import nltk
from num2words import num2words
import re
import copy
from smoothing import exp_smoothing

def num_ext(corpus,tw_flag):
    dcw=['dead','dying','die','died','perish','perished','decease','deceased','expire','expired','kill','killing','killed','missing','injured','hurt']
    grammar = '''
        NP: {<DET>? <ADJ>* <NOUN>*}
        P: {<PREP>}
        V: {<VERB.*>}
        ADJP: {<ADJ>*}
        PP: {<PREP> <NOUN>}
        VP: {<VERB> <NOUN|PREP>*}
        '''
    
    #print(corpus)
    sentences=corpus.strip().rstrip("\n").split("\n")
    smooth_str=""
    snapshot_timestamp=""
    for unparsed_sentence in sentences:
        #print("unparsed_sentence",unparsed_sentence)
        unparsed_sentence=unparsed_sentence.strip()
        if len(unparsed_sentence)!=0:
            fields=unparsed_sentence.split("%")
            sentence=fields[3]
            if fields[4]=='5':
                digit_list=[int(s) for s in re.findall(r'\b\d+\b',sentence)]
                if digit_list==[]:
                    continue
                for i in digit_list:
                    if i>=6000000000 and i<=10000000000:
                        digit_list.remove(i)
                        sentence=sentence.replace(str(i),"")
                #print("digit_list",digit_list)
                #temp_digit_list=copy.deepcopy(digit_list)
                temp_digit_list=list(digit_list)
                temp_dcw=[]
                #print(sentence)
                if digit_list:
                    for i in digit_list:
                        digit_word=num2words(i)
                        digit_word=digit_word.replace(' and','').replace(" ","-")
                        #sentence=sentence.replace(str(i),digit_word)
                        regex=r"\b"+str(i)+r"\b"
                        sentence=re.sub(regex,digit_word,sentence)

                #print("sentence",sentence)
                tokens = nltk.word_tokenize(sentence)
                tagged_sent = nltk.pos_tag(tokens, tagset='universal')
                cp = nltk.RegexpParser(grammar)
                result = cp.parse(tagged_sent)

                #result.draw()
                phrase_list=[]
                flag=0
                dcwflag=0
                for index in range(len(result)):
                    node=result[index]
                    try:
                        st=node.subtrees()
                    except:
                        st=None
                    if st:
                        for subtree in st:
                            subtree_leaves=subtree.leaves()
                            for i in range(len(subtree_leaves)):
                                if subtree_leaves[i][0] in dcw:
                                    #print("DCW found")
                                    if not temp_digit_list:
                                        break
                                    #print(sentence)
                                    temp_dcw.append(subtree_leaves[i][0])
                                    for sent_word in subtree_leaves:
                                        for digit in digit_list:
                                            digit_word=num2words(digit)
                                            digit_word=digit_word.replace(' and','').replace(" ","-")
                                            if digit_word in sent_word:
                                                temp_dcw.remove(subtree_leaves[i][0])
                                                #print("temp_digit_list",temp_digit_list)
                                                temp_digit_list.remove(digit)
                                                #print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                                smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+\
                                                str(subtree_leaves[i][0])+"%"+str(digit)+"%"+fields[5]+"\n"
##                                                try:
##                                                    numeric_report[subtree_leaves[i][0]]+=digit
##                                                except:
##                                                    numeric_report[subtree_leaves[i][0]]=digit
                                                flag=1
                                    pos=index
                                    if flag==0:
                                        try:
                                            prev_node=result[pos-1]
                                        except:
                                            prev_node=None
                                        try:
                                            fol_node=result[pos+1]
                                        except:
                                            fol_node=None
                                        try:
                                            if prev_node:
                                                pt=prev_node.subtrees()
                                            else:
                                                pt=None
                                        except:
                                            pt=None
                                        try:
                                            if fol_node:
                                                ft=fol_node.subtrees()
                                            else:
                                                ft=None
                                        except:
                                            ft=None
                                        if pt:
                                            for subtree_prev in pt:
                                                subtree_prev_leaves=subtree_prev.leaves()
                                                for j in subtree_prev_leaves:
                                                    #print(j)
                                                    for digit in digit_list:
                                                        digit_word=num2words(digit)
                                                        digit_word=digit_word.replace(' and','').replace(" ","-")
                                                        if digit_word==j[0]:
                                                            try:
                                                                temp_dcw.remove(subtree_leaves[i][0])
                                                                temp_digit_list.remove(digit)
                                                            except:
                                                                pass
                                                            #print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                                            smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+str(subtree_leaves[i][0])+"%"+str(digit)+"%"+fields[5]+"\n"
##                                                            try:
##                                                                numeric_report[subtree_leaves[i][0]]+=digit
##                                                            except:
##                                                                numeric_report[subtree_leaves[i][0]]=digit
                                                        else:
                                                            if len(digit_list)==1 and temp_digit_list!=[]:
                                                                temp_dcw.remove(subtree_leaves[i][0])
                                                                temp_digit_list.remove(digit_list[0])
                                                                #print("Fatality report {} {}".format(subtree_leaves[i][0],digit_list[0]))
                                                                smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+str(subtree_leaves[i][0])+"%"+str(digit)+"%"+fields[5]+"\n"
##                                                                try:
##                                                                    numeric_report[subtree_leaves[i][0]]+=digit_list[0]
##                                                                except:
##                                                                    numeric_report[subtree_leaves[i][0]]=digit_list[0]

                                        if ft:
                                            for subtree_next in ft:
                                                subtree_next_leaves=subtree_next.leaves()
                                                for k in subtree_next_leaves:
                                                    #print(k)
                                                    for digit in digit_list:
                                                        digit_word=num2words(digit)
                                                        digit_word=digit_word.replace(' and','').replace(" ","-")
                                                        if digit_word==k[0]:
                                                            try:
                                                                temp_dcw.remove(subtree_leaves[i][0])
                                                                temp_digit_list.remove(digit)
                                                            except:
                                                                pass
                                                            #print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                                            smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+str(subtree_leaves[i][0])+"%"+str(digit)+"%"+fields[5]+"\n"
##                                                            try:
##                                                                numeric_report[subtree_leaves[i][0]]+=digit
##                                                            except:
##                                                                numeric_report[subtree_leaves[i][0]]=digit
                                                        else:
                                                            if len(digit_list)==1 and temp_digit_list!=[]:
                                                                temp_dcw.remove(subtree_leaves[i][0])
                                                                temp_digit_list.remove(digit_list[0])
                                                                #print("Fatality report {} {}".format(subtree_leaves[i][0],digit_list[0]))
                                                                smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+str(subtree_leaves[i][0])+"%"+str(digit)+"%"+fields[5]+"\n"
##                                                                try:
##                                                                    numeric_report[subtree_leaves[i][0]]+=digit_list[0]
##                                                                except:
##                                                                    numeric_report[subtree_leaves[i][0]]=digit_list[0]

                    
                ##print("Len",len(result))
                ##print("Index",pos)
                ##print(temp_dcw)
                ##print(temp_digit_list)
                ##print(digit_list)                                                    
                if len(temp_dcw)==len(temp_digit_list) and temp_digit_list!=[]:
                    for i in range(len(temp_dcw)):
                        #print("Fatality report {} {}".format(temp_dcw[i],temp_digit_list[i]))
                        smooth_str+=fields[0].split(" ")[0]+"%"+fields[0].split(" ")[1]+"%"+fields[1]+"%"+fields[2]+"%"+str(temp_dcw[i])+"%"+str(temp_digit_list[i])+"%"+fields[5]+"\n"
##                        try:
##                            numeric_report[temp_dcw[i]]+=temp_digit_list[i]
##                        except:
##                            numeric_report[temp_dcw[i]]=temp_digit_list[i]
            else:
                if tw_flag==0:
                    snapshot_timestamp=fields[0]
                
                        
    #print(smooth_str)
    print("Extraction Done")
    pdf_smooth=exp_smoothing(smooth_str,snapshot_timestamp,tw_flag)
    return pdf_smooth

