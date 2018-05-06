INSTALLATIONS( for Windows environment):

1)Download python 2.7.x from https://www.python.org/downloads/
2)Add two variables to path variable, as <home-directory of python>;<home-directory of python>/Scripts
3)Open command prompt or power shell and type the following "python -m pip install -U pip"   without the double quotes
4)Install BeautifulSoup by typing "pip install beautifulSoup4" without the double quotes

EXECUTION:

CONTENTS OF FILE:

 Task1_BFS.py --> python source file with the code for unfocused crawling using BFS algorithm
 
 Task1_DFS.py -->python source file with the code for unfocused crawling using DFS algorithm
 
 Task2_focused_crawl_BFS.py-->python source file with the code for focused crawling using BFS algorithm
 
 crawled_urls_BFS.txt--> text file containing 1000 urls with their depth,which were crawled using BFS algorithm
 
 crawled_urls_DFS.txt-->text file containing 1000 urls with their depth,which were crawled using DFS algorithm
 
 crawled_urls_BFS.txt-->text file containing 1000 urls with their depth,which were crawled using BFS algorithm and filtered with keywords "moon" and "lunar"
 
 Task1_G_Explanation.txt-->text file explaining comparisons between the BFS crawl and the DFS crawl in terms of overlapped urls,perceived quality,efficiency,coverage of given topic i.e. "Solar Eclipse"
 
  Task2_Explanation.txt --> text file explaining the execution procedure of Task2
 
 
EXECUTION--> Steps for executing the program in windows environment:

1)go inside the the directory which has the python source files i.e. "Task1_BFS.py", "Task1_DFS.py" and "Task2_focused_crawl_BFS.py" copy the file location
2)open windows powershell or command prompt and type the command cd <file location copied in previous step>
3) To execute the program:
a)To execute Task1 with BFS type python Task1_BFS.py and hit enter 
b)To execute Task1 with DFS type python Task1_DFS.py and hit enter
c)To execute Task2 type python Task2_focused_crawl_BFS.py and hit enter

MAXIMUM DEPTH REACHED:

BFS--> The crawler reaches till depth 4
DFS-->The crawler reaches till depth 6
BFS-Focused-->The crawler reaches till depth 4


CITATION:
 
1) https://www.crummy.com/software/BeautifulSoup/  -- BeautifulSoup is used for parsing and extracting contents from a page
2) https://www.udacity.com/course/intro-to-computer-science--cs101  


  
  
  
  