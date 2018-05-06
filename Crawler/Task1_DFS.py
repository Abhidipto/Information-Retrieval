import urllib2
import time
import traceback
from bs4 import BeautifulSoup
'''Global variable for maintaining number of files in the output list'''
FILE_NUMBER=1
'''Maximum number of pages allowed to be crawled'''
MAX_PAGES=1000
'''Maximum depth  allowed to be crawled'''
MAX_DEPTH=6

'''Main crawler method that takes the initial url as "seed" and crawls from there using DFS algorithm'''
def crawler(seed):
    depth=1
    pages_to_be_crawled=[seed+str(depth)]
    pages_already_crawled=[]
    
    while(len(pages_to_be_crawled)>0 and len(pages_already_crawled)<MAX_PAGES):
        current_page=pages_to_be_crawled.pop(0)
        page_link_length=len(current_page)
        current_depth=int(current_page[-1])
        current_page=current_page[:page_link_length-1]
        if(current_page not in pages_already_crawled and current_depth<=MAX_DEPTH):                           
                current_depth+=1               
                urls=fetch_urls(current_page,current_depth)
                pages_already_crawled.append(current_page)
                for i in range(0,len(urls)):
                    pages_to_be_crawled.insert(i, urls[i])
        else:
            continue
    return pages_already_crawled
 
 
'''write the current url into the output file named as "crawled_urls_DFS.txt'''

def create_File(current_page,depth):
    global FILE_NUMBER
    bfs_url_fileHandle=open("crawled_urls_DFS.txt","a")
    bfs_url_fileHandle.write(str(FILE_NUMBER)+")"+" "+current_page+" at depth:"+" "+str(depth)+"\n")
    bfs_url_fileHandle.close()
    FILE_NUMBER+=1
            
'''Takes an url as input and collects all urls within the page.This is done with BeautifulSoup.
Criteria for selecting an url:
1)has to be in a div having id as "bodyContent"
2)has to start with  "/wiki/"
3)no ":" present 
4)if a "#" is found, only the text prior to the "#" is taken

Finally all the urls are are appended in an list and returned '''
             
def fetch_urls(current_page,depth):
    list_of_urls=[]
    try:
        time.sleep(1)
        x=urllib2.urlopen(current_page)
        soup=BeautifulSoup(x,"html.parser")
        create_File(current_page,depth-1)
        content=soup.findAll("div",attrs={"id":"bodyContent"})
        for d in content:
            list_of_links=d.findAll("a")
            for links in list_of_links:
                href=links.get("href")
                if(href and href.startswith("/wiki/")):
                    if(":" in href):
                        continue
                    url="https://en.wikipedia.org"+href
                    if("#" in url):
                        url=url[:url.index("#")]
                    url+=str(depth)                   
                    #print(url)
                    list_of_urls.append(url.encode("utf8"))

    except:
        print "some error in fetch urls"
        print traceback.format_exc()
    return list_of_urls
                        
                        
def main():
    #startTime=time.time()
    crawler("https://en.wikipedia.org/wiki/Solar_eclipse")
    #endTime=time.time()
    #print("exec-time",(endTime-startTime)//60)
    #f=open("time_required_dfs.txt","w")
    #f.write(str((endTime-startTime)//60))
    #f.close()
    
if __name__=="__main__": main()
                    
                       
        
