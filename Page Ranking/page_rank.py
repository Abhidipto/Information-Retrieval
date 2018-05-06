from math import log
import time
import operator


inlink_graph={}
page_list=[]
outlink_graph={}
sink_list=[]
total_number_of_pages=0
page_rank_dict={}
inlink_count_dict={}
d=0.85

''' The following method parses the given graph and creates the inlink graph,the outlink count graph,the list of all pages and the list of sink pages'''

def collect_info_from_graph(graph):
    global page_list
    global total_number_of_pages
    h=open(graph,"r")
    for line in h.readlines():
        titles_list=line.split()
        page_list.append(titles_list[0])
        create_inlink_graph(titles_list)
        create_outlink_graph(titles_list[1:])
    total_number_of_pages=len(page_list)  
    create_sink_list()    
    h.close()


''' The following method creates the in-link graph which is a dictionary and it stores  a page as a key and all the crawled
    pages that has links to this page as values'''      
        
def create_inlink_graph(titles_list):
    global inlink_graph
    key=titles_list[0]
    inlink_graph[key]=[]
    for i in range (1,len(titles_list)):
        inlink_graph[key].append(titles_list[i])
        
 
 
''' The following method created the outlink graph which is dictionary that holds all pages(except for sinks) and their
    respective out-link counts'''
        
def create_outlink_graph(titles_list):    
    global outlink_graph   
    for i in titles_list:
        if(i in outlink_graph.keys()):
            outlink_graph[i]+=1
        else:
            outlink_graph[i]=1   
    

''' The following method creates a list containing all the sink pages'''

def create_sink_list():
    global page_list
    global sink_list
    global outlink_graph
    
    for i in page_list:
        if(i not in outlink_graph.keys()):
            sink_list.append(i)
            
    
''' The following method calculates the perplexity value for the pages'''  
   
def calculate_perplexity(d):
    entropy=0
    for k,v in d.iteritems():
        entropy+=v*log(v,2)   
    entropy=-entropy
    return pow(2,entropy)
    
    
''' The following method   calculates the page rank of all the pages present in inlink graph till the values converge ,
      which is determined by the perplexity after each iteration'''
   
    
def calculate_page_rank():
    global page_rank_dict
    global sink_list
    global total_number_of_pages
    global inlink_graph
    global outlink_graph
    global page_list
    perplexity=0
    i=0
    '''Initiating the page rank dictionary by asigning an uniform rank to all pages'''
    for page in page_list:
        page_rank_dict[page]=float(1)/total_number_of_pages
    c=0
    ''' The while is repeated in loops of 4 iterations as the value of c reaches 4 only when the perplexity value remains less than 1
    for at least 4 consecutive iterations'''
    while(c<4):
        newPR={}
        sinkPR=0       
        for p in sink_list:
            sinkPR+=page_rank_dict[p]
            
        for p in page_list:
            newPR[p]=float (1-d)/total_number_of_pages
            newPR[p]+=d* float (sinkPR/total_number_of_pages)
            for q in inlink_graph[p]:
                newPR[p]+=d* float(page_rank_dict[q])/float(outlink_graph[q])
        for p in page_list:
            page_rank_dict[p]=newPR[p]
        new_perplexity=calculate_perplexity(page_rank_dict)
        if(abs(perplexity-new_perplexity)<1):
            c+=1
        else:
            c=0
        perplexity=new_perplexity
        i+=1
#        s="Perplexity for iteration "+str(i)+" is :"+str(perplexity)
#        print(s)
        
        '''Following is the code for getting the number of iterations required to converge and their
         respective perplexity values'''
        
#         perplexity_value_string="Perplexity for iteration "+str(i)+" is :"+str(perplexity)+"\n"               
#         perp_val_handle=open("G2_perplexity_values_with_4_iterations.txt","a")
#         perp_val_handle.write(perplexity_value_string)
#         perp_val_handle.close()
#         if(i==4):
#             break
 
 
''' Following method is used to get the raw inlink count for all the pages and store it in a dictionary called 'inlink_count_dict'.
    This is required for creating the statistics'''
 
        
# def get_inlink_count():
#     global inlink_graph
#     global inlink_count_dict
#     for k,v in inlink_graph.iteritems():
#         inlink_count_dict[k]=len(v)
 
''' Following method reverse sorts the  pages according to their Page Ranks and writes top 50 pages to a file 
    This is required for evaluating statistics'''
    
# def sort_pr_dictionary():
#     global page_rank_dict
#      
#     sorted_dict=sorted(page_rank_dict.items(),key=operator.itemgetter(1),reverse=True)
#     counter=1
#     f=open("Top_50_pages_G2_sorted_by_PR_with_4_iterations.txt","a")
#     while(counter<=50):        
#         f.write(str(counter)+")"+sorted_dict[counter-1][0]+": "+str(sorted_dict[counter-1][1])+"\n")
#         counter+=1
#     f.close()
#     
    

''' Following method reverse sorts pages according to their in link counts and writes top 50 pages to a file
    This is required for evaluating statistics'''   
    
# def sort_inlink_dictionary():
#     global inlink_count_dict
#     sorted_dict=sorted(inlink_count_dict.items(),key=operator.itemgetter(1),reverse=True)
#     counter=1
#     f=open("Top_50_pages_G2_sorted_by_Inlink.txt","a")
#     while(counter<=50):        
#         f.write(str(counter)+")"+sorted_dict[counter-1][0]+": "+str(sorted_dict[counter-1][1])+"\n")
#         counter+=1
#     f.close()
 

def main():
    collect_info_from_graph("G1.txt")
#    stime=time.time()
    calculate_page_rank()
#    etime=time.time()
#    print("exec time :",(etime-stime))
#   get_inlink_count()
#    sort_pr_dictionary()    
#    sort_inlink_dictionary()
  


if __name__ == "__main__": main()