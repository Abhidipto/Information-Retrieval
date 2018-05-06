import os
from math import log
import operator
import traceback
import re
import shutil

CORPUS_LOCATION="corpus"
INDEX_FILE_NAME="unigram_inverted_index.txt"
QUERYFILE_LOCATION="query.txt"
SCORES_FOLDER_PATH=os.path.join(os.getcwd(),"scores")
QUERY_LIST=[]



UNIGRAM_INVERTED_INDEX={}
DOCUMENT_LENGTH_DICT={}




def generate_index():       
    global UNIGRAM_INVERTED_INDEX
    global DOCUMENT_LENGTH_DICT
     
    ''' Generting length of each document in corpus in a dictionary called  DOCUMENT_LENGTH_DICT'''
    
    path=os.path.join(os.getcwd(),CORPUS_LOCATION)
    for f in os.listdir(path):        
        filePath=os.path.join(path,f)
        fh=open(filePath,"r")
        length_of_doc=len(fh.readlines())
        doc_name=f[:-4]
        DOCUMENT_LENGTH_DICT[doc_name]=str(length_of_doc)
    print(len(DOCUMENT_LENGTH_DICT))
    fh.close()
    
    
    ''' Generating the index in a dictionary called UNIGRAM_INVERTED_INDEX'''
    
               
    file_path=os.path.join(os.getcwd(),INDEX_FILE_NAME)         
    fh=open(file_path,"r")
    for line in fh.readlines():
        line=line[:-1]
        term=line[:line.find(":")]
        UNIGRAM_INVERTED_INDEX[term]={}
        line=line[len(term)+2:-1]
        doc_id_list=line.split()
        doc_info=UNIGRAM_INVERTED_INDEX[term]
        for i in doc_id_list:
            doc_id=i[:i.find(":")]                             
            freq=i[len(doc_id)+1:]               
            doc_info[doc_id]=freq
   
        UNIGRAM_INVERTED_INDEX[term]=doc_info
    fh.close()
    print(len(UNIGRAM_INVERTED_INDEX.keys()))
 
def generate_BM25_score():
    global QUERY_LIST
    global UNIGRAM_INVERTED_INDEX
    global DOCUMENT_LENGTH_DICT
        
    query_term_freq_dict=generate_query_term_frequency_dict()
    
#    query_list=query_term_freq_dict.keys()
    
    sum=0
    for k,v in DOCUMENT_LENGTH_DICT.items():
        sum+=int(v)
        
    avdl=float(sum)/float(len(DOCUMENT_LENGTH_DICT.keys()))   
    query_id=0
    for query in QUERY_LIST:
        term_freq_dict=query_term_freq_dict[query]
        query_id+=1       
        generate_score(query_id,query,term_freq_dict,avdl)
        
        
        
def generate_score(query_id,query,query_freq_dict,avdl):
    global UNIGRAM_INVERTED_INDEX
    global DOCUMENT_LENGTH_DICT
    doc_score={}
    print("curent query",query)
    
    '''Parameters'''
    
    N=len(DOCUMENT_LENGTH_DICT)
    R=0
    r=0
    n=0
    k1=1.2
    k2=100
    b=0.75
    
    '''Iterating for each term in query'''
    
    for term in query.split():
        if(UNIGRAM_INVERTED_INDEX.has_key(term)):
            n=len(UNIGRAM_INVERTED_INDEX[term].keys())
                              
        qf=query_freq_dict[term]
        
        '''Calculating score for each document'''
           
        for doc in DOCUMENT_LENGTH_DICT.keys():
            dl=DOCUMENT_LENGTH_DICT[doc]
            f=0
            doc_dict=UNIGRAM_INVERTED_INDEX[term]
            if(doc_dict.has_key(doc)):
                f=int(doc_dict[doc])                
                                  
            K=k1*((1-b)+b*(float(dl)/float(avdl)))
            x=log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))
            y=((k1+1)*f)/(K+f)
            z=((k2+1)*qf)/(k2+qf)
            score=x*y*z
            if(doc_score.has_key(doc)):
                doc_score[doc]+=score 
            else:
                doc_score[doc]=score
                
    sorted_docs=sorted(doc_score.items(),key=operator.itemgetter(1),reverse=True)
    create_file(query_id,query,sorted_docs)
    
    
    
def create_file(query_id,query,sorted_docs):
    global SCORES_FOLDER_PATH
    try:
        if(not os.path.exists(SCORES_FOLDER_PATH)):
            os.mkdir(SCORES_FOLDER_PATH)
            
        p=re.compile('[\s]') 
        query=p.sub("_",query)
        
        file_name=query+"_BM25.txt"
        
        file_location=open(SCORES_FOLDER_PATH+"\\"+file_name,"a")
        
        for i in range(0,len(sorted_docs)):
            file_location.write(str(query_id)+" Q0 "+sorted_docs[i][0]+" "+str(sorted_docs[i][1])+" "+str(i+1)+" BM25_Model"+"\n")
            if(i==99):
                break
        
        file_location.close()
    except Exception as e:
        print(traceback.format_exc()) 
            
  
def generate_query_term_frequency_dict():
    global QUERY_LIST
    query_term_freq_dict={}
    qeury_file_path=os.path.join(os.getcwd(),QUERYFILE_LOCATION)
    f=open(qeury_file_path,"r")
    for query in f.readlines():
        if(query[-1]=="\n"):
            query=query[:-1]
        QUERY_LIST.append(query)
        query_term_freq_dict[query]={}
        term_list=query.split()
        term_freq_dict=query_term_freq_dict[query]
        for term in term_list:            
            if(term_freq_dict.has_key(term)):
                term_freq_dict[term]+=1
            else:
                term_freq_dict[term]=1
        query_term_freq_dict[query]=term_freq_dict
    print(QUERY_LIST)
    return query_term_freq_dict
        

        
                

    
      
     
def main():    
    
    if(os.path.exists(SCORES_FOLDER_PATH)):
        shutil.rmtree(SCORES_FOLDER_PATH)
        
    generate_index()
    generate_BM25_score()
    
    
if __name__=="__main__":main()

