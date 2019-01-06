import nltk
from num2words import num2words
import re
import copy

def num_ext(corpus):
    dcw=['dead','dying','die','died','perish','perished','decease','deceased','expire','expired','kill','killing','killed','missing','injured','hurt']
    grammar = '''
        NP: {<DET>? <ADJ>* <NOUN>*}
        P: {<PREP>}
        V: {<VERB.*>}
        ADJP: {<ADJ>*}
        PP: {<PREP> <NOUN>}
        VP: {<VERB> <NOUN|PREP>*}
        '''
    #sentence = "1002 crocodiles have escaped from crocodile park at chennai and 899 people dead and 789 injured."
    #sentence = "chennai airport is shutdown / 188 dead  but still national media like @ibnlive doesn't even consider it as a news !!"
    #sentence = "1002 people dead from landslides in Nepal."
    #sentence="people dead in nepal. numbers estimated to be 20 and 30 injured for help contact 9547745926. Also 59 children missing. Volunteers injured. numbers estimated to be 553."

    print(corpus)
    digit_list=[int(s) for s in re.findall(r'\b\d+\b',sentence)]
    for i in digit_list:
        if i>=6000000000 and i<=10000000000:
            digit_list.remove(i)
            sentence=sentence.replace(str(i),"")
    #print(digit_list)
    temp_digit_list=copy.deepcopy(digit_list)
    temp_dcw=[]
    if digit_list:
        for i in digit_list:
            digit_word=num2words(i)
            digit_word=digit_word.replace(' and','').replace(" ","-")
            sentence=sentence.replace(str(i),digit_word) 

    #print(sentence)
    tokens = nltk.word_tokenize(sentence)
    tagged_sent = nltk.pos_tag(tokens, tagset='universal')
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged_sent)

    #result.draw()
    phrase_list=[]
    flag=0
    dcwflag=0
    numeric_report={}
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
                        print("DCW found")
                        temp_dcw.append(subtree_leaves[i][0])
                        for sent_word in subtree_leaves:
                            for digit in digit_list:
                                digit_word=num2words(digit)
                                digit_word=digit_word.replace(' and','').replace(" ","-")
                                if digit_word in sent_word:
                                    temp_dcw.remove(subtree_leaves[i][0])
                                    temp_digit_list.remove(digit)
                                    print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                    try:
                                        numeric_report[subtree_leaves[i][0]]+=digit
                                    except:
                                        numeric_report[subtree_leaves[i][0]]=digit
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
                                                temp_dcw.remove(subtree_leaves[i][0])
                                                temp_digit_list.remove(digit)
                                                print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                                try:
                                                    numeric_report[subtree_leaves[i][0]]+=digit
                                                except:
                                                    numeric_report[subtree_leaves[i][0]]=digit
                                            else:
                                                if len(digit_list)==1:
                                                    temp_dcw.remove(subtree_leaves[i][0])
                                                    temp_digit_list.remove(digit_list[0])
                                                    print("Fatality report {} {}".format(subtree_leaves[i][0],digit_list[0]))
                                                    try:
                                                        numeric_report[subtree_leaves[i][0]]+=digit_list[0]
                                                    except:
                                                        numeric_report[subtree_leaves[i][0]]=digit_list[0]

                            if ft:
                                for subtree_next in pt:
                                    subtree_next_leaves=subtree_next.leaves()
                                    for k in subtree_next_leaves:
                                        #print(k)
                                        for digit in digit_list:
                                            digit_word=num2words(digit)
                                            digit_word=digit_word.replace(' and','').replace(" ","-")
                                            if digit_word==k[0]:
                                                temp_dcw.remove(subtree_leaves[i][0])
                                                temp_digit_list.remove(digit)
                                                print("Fatality report {} {}".format(subtree_leaves[i][0],digit))
                                                try:
                                                    numeric_report[subtree_leaves[i][0]]+=digit
                                                except:
                                                    numeric_report[subtree_leaves[i][0]]=digit
                                            else:
                                                if len(digit_list)==1:
                                                    temp_dcw.remove(subtree_leaves[i][0])
                                                    temp_digit_list.remove(digit_list[0])
                                                    print("Fatality report {} {}".format(subtree_leaves[i][0],digit_list[0]))
                                                    try:
                                                        numeric_report[subtree_leaves[i][0]]+=digit_list[0]
                                                    except:
                                                        numeric_report[subtree_leaves[i][0]]=digit_list[0]

        
    ##print("Len",len(result))
    ##print("Index",pos)
    ##print(temp_dcw)
    ##print(temp_digit_list)
    ##print(digit_list)
    if len(temp_dcw)==len(temp_digit_list):
        for i in range(len(temp_dcw)):
            print("Fatality report {} {}".format(temp_dcw[i],temp_digit_list[i]))
            try:
                numeric_report[temp_dcw[i]]+=temp_digit_list[i]
            except:
                numeric_report[temp_dcw[i]]=temp_digit_list[i]
                
        
    #print(numeric_report)
    return numeric_report
