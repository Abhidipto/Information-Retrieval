import os
from bs4 import BeautifulSoup
import re

'''Location of crawled files'''
CRAWLED_FILES_LOCATION="BFSFiles"
CORPUS_FOLDER_NAME="corpus"

'''Function for generating the corpus'''
def corpus_generator(case_folding,punctuation):
    path=os.path.join(os.getcwd(),CRAWLED_FILES_LOCATION)
    for f in os.listdir(path):
        
        filePath=os.path.join(path,f)
        generate_article(filePath,case_folding,punctuation)

     
''' Function for extracting content form each crawled files, processing them ,and finally calls another functions to create the corpus'''    
def generate_article(filePath,case_folding,punctuation):
        fh=open(filePath,"r")
        title=fh.readline()
        title=get_title_from_url(title)
        title=title[:-2]
#        print(title)
        content=fh.read()
        '''Eliminates refences section of the wikipedia page'''
    
        if('<span class="mw-headline" id="References">'in content):
            pos=content.index('<span class="mw-headline" id="References">')
            content=content[:pos]
        
        ''' Eliminates the See Also section of the wikipedia page, if present'''
         
        if('<span class="mw-headline" id="See_also">' in content):           
            pos=content.index('<span class="mw-headline" id="See_also">')
            content=content[:pos]
            
            
        ''' Eliminates the Notes section of the wikipedia page, if present'''
            
        if('<span class="mw-headline" id="Notes">' in content):           
            pos=content.index('<span class="mw-headline" id="Notes">')
            content=content[:pos]
            
        soup=BeautifulSoup(content,"html5lib")
        fh.close()
        content=soup.find("div",attrs={"id":"bodyContent"})
        
        
        ''' Eliminates the Content links  section of the wikipedia page, if present'''
        
        if(content.find("div",attrs={"class":"toc","id":"toc"})):
            content.find("div",attrs={"class":"toc","id":"toc"}).decompose()
            
          
        ''' Eliminates the Mathematical formulas of the wikipedia page, if present'''
            
        if(content.find("annotation",attrs={"encoding":"application/x-tex"})):
            for elem in content.findAll("annotation",attrs={"encoding":"application/x-tex"}):
                elem.decompose()
                
        ''' Eliminates the "table" tags of the wikipedia page, if present'''
                                
        if(content.find("table")):
            for elem in content.findAll("table"):
                elem.decompose()
                
                
        ''' Eliminates the images from  of the wikipedia page, if present'''
                        
        if(content.find("img")):
            for elem in content.findAll("img"):
                elem.decompose()

        content=content.get_text().encode("utf-8").split()
            
        content_string=""
        for word in content:
            ''' checks for non ASCHII characters or spaces or "-" or "--"   '''
            if(not all(ord(char) < 128 for char in word) or word=="-" or word=="--" or word==" "):
                continue
            
            '''punctuation are eliminated if required'''
            
            if(punctuation):
                if(word.isdigit()):
                    p=re.compile('[^\d.,]')
                    word=p.sub("",word)
                else:
                    p=re.compile('[^\w-]')
                    word=p.sub("",word)
                    
            ''' case-folding is done if required'''        
            
            if(case_folding):
                word=word.lower()
                
            content_string+=word+" "
        ''' Functions call to create the corpus''' 
        create_file(title,content_string)       
      
        
        
''' creates a file for each page crawled where the main textual content is stored and is stored inside a 
    folder called "corpus",which is present in the current directory'''
            
def create_file(title,content_string):
    file_name=title+".txt"
    file_location=open(os.getcwd()+"\\"+CORPUS_FOLDER_NAME+"\\"+file_name,"a")
    
    file_location.write(title+"\n")
    for s in content_string.split():
        file_location.write(s+"\n")
    file_location.close()


''' Function to extract the title form url of each page'''

def get_title_from_url(url):
    title=""
    for i in range(len(url)-1,-1,-1):
        if(url[i]=="/"):
            break
        title+=url[i]
    title=title[::-1]
    return title
        
          
def main():
    corpus_generator(True,True)
    
    
if __name__=="__main__":main()