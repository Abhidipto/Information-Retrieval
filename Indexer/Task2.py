
import os
import operator
CORPUS_FOLDER_NAME="corpus"

'''Function to create unigram inverted index, uses  dictionary data structure to make the index, and fetches
 the textual contents from a folder called 'corpus' which is present in the current folder'''
def generate_unigram_index():
    inverted_index_unigram={}
    path=os.path.join(os.getcwd(),CORPUS_FOLDER_NAME)
    for f in os.listdir(path):
        doc_id=f[:-4]
        
        file_location=os.path.join(path,f)
        fh=open(file_location,"r")
        words=fh.read()
        fh.close()
        for w in words.split("\n"):
            if(w=="" or w==" "):
                continue
            if(inverted_index_unigram.has_key(w)):
                doc_count=inverted_index_unigram[w]
                if(doc_count.has_key(doc_id)):                   
                    doc_count[doc_id]+=1
                else:
                    doc_count[doc_id]=1                   
                inverted_index_unigram[w]=doc_count
                             
            else:
                  
                inverted_index_unigram[w]={doc_id:1}
                
                
    '''calls  function to create unigram term inverted index '''
                
    create_inverted_index("unigram_inverted_index.txt",inverted_index_unigram)
                
    '''calls  function to create unigram term frequenct table '''
                
    create_term_frequency_tables("unigram_term_frequency_table.txt",inverted_index_unigram)
    
    '''calls  function to create unigram document frequenct table '''
    
    create_document_frequency_tables("unigram_document_frequency_table.txt",inverted_index_unigram)
      
    
    

'''Function to create bigram inverted index, uses  dictionary data structure to make the index, and fetches
 the textual contents from a folder called 'corpus' which is present in the current folder'''

def generate_bigram_index():
    inverted_index_bigram={}
    path=os.path.join(os.getcwd(),CORPUS_FOLDER_NAME)
    for f in os.listdir(path):
        doc_id=f[:-4]
        file_location=os.path.join(path,f)
        fh=open(file_location,"r")
        words=fh.read()
        fh.close()
        words=words.split("\n")
        for i in range (0,len(words)-1):
            term=words[i]+" "+words[i+1]
            if(term=="- -" or term=="-"):
                continue
            if(inverted_index_bigram.has_key(term)):
                doc_count=inverted_index_bigram[term]
                if(doc_count.has_key(doc_id)):                   
                    doc_count[doc_id]+=1
                else:
                    doc_count[doc_id]=1                   
                inverted_index_bigram[term]=doc_count
                            
            else:                 
                inverted_index_bigram[term]={doc_id:1}


    '''calls  function to create bigram term inverted index '''
                
    create_inverted_index("bigram_inverted_index.txt",inverted_index_bigram)

    ''' calls  function to create bigram term frequenct table '''
                
    create_term_frequency_tables("bigram_term_frequency_table.txt",inverted_index_bigram)
    
    ''' calls  function to create bigram document frequenct table '''
    
    create_document_frequency_tables("bigram_document_frequency_table.txt",inverted_index_bigram)


'''Function to create bigram inverted index, uses  dictionary data structure to make the index, and fetches
 the textual contents from a folder called 'corpus' which is present in the current folder'''

def generate_trigram_index():
    inverted_index_trigram={}
    path=os.path.join(os.getcwd(),CORPUS_FOLDER_NAME)
    for f in os.listdir(path):
#        print(f)
        doc_id=f[:-4]
        file_location=os.path.join(path,f)
        fh=open(file_location,"r")
        words=fh.read()
        fh.close()
        words=words.split("\n")
        for i in range (0,len(words)-2):
            term=words[i]+" "+words[i+1]+" "+words[i+2]
            
            if(inverted_index_trigram.has_key(term)):
                doc_count=inverted_index_trigram[term]
                if(doc_count.has_key(doc_id)):                   
                    doc_count[doc_id]+=1
                else:
                    doc_count[doc_id]=1                   
                inverted_index_trigram[term]=doc_count
                            
            else:                 
                inverted_index_trigram[term]={doc_id:1}
                
                
    '''calls  function to create trigram term inverted index '''
                
    create_inverted_index("trigram_inverted_index.txt",inverted_index_trigram)

    ''' calls  function to create trigram term frequenct table '''
    
    create_term_frequency_tables("trigram_term_frequency_table.txt",inverted_index_trigram)
    
    ''' calls  function to create trigram document frequenct table '''
    
    create_document_frequency_tables("trigram_document_frequency_table.txt",inverted_index_trigram)
    


'''Function to create unigram inverted index which stores term position, uses  dictionary data structure to make the index, and fetches
 the textual contents from a folder called 'corpus' which is present in the current folder'''


def generate_unigram_index_with_position():
    inverted_index_unigram_with_pos={}
    path=os.path.join(os.getcwd(),CORPUS_FOLDER_NAME)
    for f in os.listdir(path):
#        print(f)
        doc_id=f[:-4]
        file_location=os.path.join(path,f)
        fh=open(file_location,"r")
        words=fh.read()
        fh.close()
        words=words.split("\n")
        for w in range(0,len(words)):
            term=words[w]
            if(term=="" or term==" "):
                continue
                       
            if(inverted_index_unigram_with_pos.has_key(term)):
                doc_count=inverted_index_unigram_with_pos[term]
                if(doc_count.has_key(doc_id)):                   
                    doc_count[doc_id].append(w)
                else:
                    doc_count[doc_id]=[w]                   
                inverted_index_unigram_with_pos[term]=doc_count
                           
            else:
                d={doc_id:[w]}
                inverted_index_unigram_with_pos[term]=d
                
    '''calls  function to create trigram term inverted index '''
                
    create_inverted_index("unigram_inverted_index_with_pos.txt",inverted_index_unigram_with_pos)


    
    

def create_inverted_index(file_name,inv_index):
    fw=open(file_name,"a")
    if(file_name=="unigram_inverted_index_with_pos.txt"):
        for k,v in inv_index.items():
            s=k+":"+"("
            for i in v.keys():
                pos_str=""
                for j in v[i]:
                    pos_str+=str(j)+" "               
                s+=i+":"+"["+pos_str+"]"+" "
            s+=")"+"\n"
            fw.write(s)
            
        
    else:
        for k,v in inv_index.items():
            s=k+":"+"("
            for i in v.keys():
                s+=i+":"+str(v[i])+" "
            s+=")"+"\n"
            fw.write(s)
    fw.close()
        
    
    

''' the following function takes an inverted index represented by a dictionary and the title of a 
   page and creates a file with a supplied name and which store the occurrence 
   of each unique term across the entire corpus. '''  

def create_term_frequency_tables(table_name,inv_index):
    term_freq_dict={}
    for k,v in inv_index.items():
        sum=0
        for i in v.keys():
            sum+=v[i]
        term_freq_dict[k]=sum
    
    sorted_term_freq=sorted(term_freq_dict.items(),key=operator.itemgetter(1),reverse=True)   
               
    fh=open(table_name,"a")
    for i in sorted_term_freq:
        fh.write(i[0]+"     "+str(i[1])+"\n")
    fh.close()
    
''' the following function takes an inverted index represented by a dictionary and the title of a 
   page and creates a file with a supplied name and which stores the how many and which documents holds a particular term'''
   
    
def create_document_frequency_tables(table_name,inv_index):
    doc_freq_dict={}
    for k,v in inv_index.items():
        doc_info=[]
        doc_id_list=""
        for i in v.keys():
            doc_id_list+=i+" "
        doc_info.append(doc_id_list)
        doc_info.append(str(len(v.keys())))
        doc_freq_dict[k]=doc_info

    sorted_document_freq=sorted(doc_freq_dict.items(),key=operator.itemgetter(0))
    fh=open(table_name,"a")
    for i in sorted_document_freq:
        t=i[0]
        doc_list=i[1][0]
        doc_count=i[1][1]        
        fh.write(t+"   "+"["+doc_list+"]"+"   "+doc_count+"\n")
    fh.close()
         
            
        
        
    
 
    


     
      
def main():
    generate_unigram_index()  
    generate_bigram_index() 
    generate_trigram_index()  
    generate_unigram_index_with_position()
    
    
    

if __name__=="__main__":main()    
