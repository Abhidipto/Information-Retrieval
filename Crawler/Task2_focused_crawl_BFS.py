import urllib2
import time
import traceback
from bs4 import BeautifulSoup

'''Explanation for handling keyword variation:
This code crawls at most 1000 urls or till depth 6 whichever starts first from a given url.The urls are also filtered based on two keywords provides as inputs
"lunar" and "moon". While comparing both the keywords , url and the anchor text are converted to lower cases and each keyword is checked whether it is present in the url or the anchor textand if atleast
one of the keywords is present in either the url or the anchor text then only that particular url is selected.''' 




'''Global variable for maintaining number of files in the output list'''
FILE_NUMBER=1
'''Maximum number of pages allowed to be crawled'''
MAX_PAGES=1000
'''Maximum depth  allowed to be crawled'''
MAX_DEPTH=6

'''Main crawler method that takes the initial url as "seed" and a set of keywords and crawls urls matching the given keywords,
 using BFS algorithm'''
def crawler(seed,keywords):
    depth=1
    pages_to_be_crawled=[seed+str(depth)]
    pages_in_next_depth=[]
    pages_already_crawled=[]
    
    while(len(pages_to_be_crawled)>0 and len(pages_already_crawled)<MAX_PAGES and depth<=MAX_DEPTH):
        current_page=pages_to_be_crawled.pop(0)
        page_link_length=len(current_page)
        current_page=current_page[:page_link_length-1]
        if(current_page not in pages_already_crawled):
            urls=fetch_urls(current_page,depth,keywords)
            pages_already_crawled.append(current_page)
            for url in urls:
                if(url not in pages_in_next_depth):
                    pages_in_next_depth.append(url)
                    
            if(len(pages_to_be_crawled)==0):
                pages_to_be_crawled=pages_in_next_depth
                pages_in_next_depth=[]
                depth+=1
    return pages_already_crawled
    
            
'''write the current url into the output file called "focused_crawled_urls_BFS.txt" '''
            
def create_File(current_page,depth):
    global FILE_NUMBER
    bfs_url_fileHandle=open("focused_crawled_urls_BFS.txt","a")
    bfs_url_fileHandle.write(str(FILE_NUMBER)+")"+" "+current_page+" at depth:"+" "+str(depth)+"\n")
    bfs_url_fileHandle.close()
    FILE_NUMBER+=1
           
 
 
'''Takes an url as input and collects all urls within the page.This is done with BeautifulSoup.
Criteria for selecting an url:
1)has to be in a div having id as "bodyContent"
2)has to start with  "/wiki/"
3)no ":" present 
4)either of the given keywords are found in either the anchor text or the entire url
5)if a "#" is found, only the text prior to the "#" is taken

Finally all the urls are are appended in an list and returned '''
            
def fetch_urls(current_page,depth,keywords):
    list_of_urls=[]
    k1=keywords[0]
    k2=keywords[1]
    try:
        time.sleep(1)
        x=urllib2.urlopen(current_page)
        soup=BeautifulSoup(x,"html.parser")
        create_File(current_page,depth)
        content=soup.findAll("div",attrs={"id":"bodyContent"})
        for d in content:
            list_of_links=d.findAll("a")
            for links in list_of_links:
                href=links.get("href")
                if(href and href.startswith("/wiki/")):
                    if(":" in href):
                        continue
                    anchor_text=links.text.encode("utf8")
                    url="https://en.wikipedia.org"+href
                    if("#" in url):
                        url=url[:url.index("#")]
                    if(k1.lower() in anchor_text.lower() or k1.lower() in url.lower() or k2.lower() in anchor_text.lower() or
                       k2.lower() in url.lower()):
                        url+=str(depth)
                        #print(url)
                        list_of_urls.append(url.encode("utf8"))

                    else:
                        continue
                    
    except:
        print "some error in fetch urls"
        print traceback.format_exc()
    return list_of_urls
                        
                        
def main():
    #startTime=time.time()
    crawler("https://en.wikipedia.org/wiki/Solar_eclipse",["lunar","moon"])
    #endTime=time.time()
    #print("exec-time",(endTime-startTime)//60)
    #f=open("time_requiredBFS_focused.txt","w")
    #f.write(str((endTime-startTime)//60))
    #f.close()
    
if __name__=="__main__": main()
                    
                    
                    
            
            
            
        
        
            
        