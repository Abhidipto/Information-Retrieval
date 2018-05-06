INSTALLATIONS( for Windows environment):

1)Download python 2.7.x from https://www.python.org/downloads/
2)Add two variables to path variable, as <home-directory of python>;<home-directory of python>/Scripts
3)Open command prompt or power shell and type the following "python -m pip install -U pip"   without the double quotes

EXECUTION:

CONTENTS OF FOLDER:

 page_rank.py --> python source file with the code for calculating page rank based on a given graph

 G1.txt--> text file representing the in-link graph for BFS crawl(might not open in notepad in windows because of size,but works fine with notepad++)
 
 G2.txt--> text file representing the in-link graph for DFS crawl(might not open in notepad in windows because of size,but works fine with notepad++)
 
 Simple_statistics_for_G1_G2.txt --> text file containing number of sink and source nodes in graph G1 and G2 

 Perplexity_Values --> text file containing Perplexity values which are recorded for each iteration,which were required to achieve convergence, for  both G1 and G2
 
 Task_2C_i.txt--> text file containing discussion on how a reduced damping factor of 0.55 would be affect the ranking process and the resulting ranks of the pages                        compared to Baseline

 Task_2C_ii.txt--> text file containing discussion on how would the ranking process and the resultant ranking ranking be affected if the page ranking algorithm is                         executed for 4 iterations only compared to the Baseline

 Task_2C_iii.txt-->text file containing top 10 pages sorted based on Page Rank on G1 and G2 and top 10 pages sorted based on raw in-link count of G1 and G2 and pros                    and cons for considering in-link count as an alternative for Page Ranking

 Top-50-pages-G1.txt: --> text file containing top 50 pages of G1 graph, sorted on the basis of the following variations
                      i) Page Rank
                      ii) Raw Inlink Count
		              iii)Page Rank with Damping factor of 0.55
                      iv) Page Rank with 4 iterations 

 Top-50-pages-G2.txt: --> text file containing top 50 pages of G2 graph, sorted on the basis of the following variations
                      i)  Page Rank
                      ii) Raw Inlink Count
		              iii)Page Rank with Damping factor of 0.55
                      iv) Page Rank with 4 iterations 


		
		
 
 
EXECUTION--> Steps for executing the program in windows environment:

1)go inside the the directory which has the python source file i.e. "page_rank.py" and "G1.txt" and "G2.txt" and copy the file location
2)open windows powershell or command prompt and type the command cd <file location copied in previous step>
3) To execute:
 i) Task2B for G1, enter "G1.txt" as parameter to "collect_info_from_graph" method inside " def main()" ,save the .py file and type python page_rank.py and hit enter       
 ii) Task2B for G2 ,enter "G2.txt" as parameter to "collect_info_from_graph" method inside " def main()", save the .py file and type python page_rank.py and hit enter 


CITATION:
 
1) https://www.crummy.com/software/BeautifulSoup/  -- BeautifulSoup is used for parsing and extracting contents from a page

  
  
  
  