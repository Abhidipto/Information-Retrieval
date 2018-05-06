INSTALLATIONS( for Windows environment):

1)Download python 2.7.x from https://www.python.org/downloads/
2)Add two variables to path variable, as <home-directory of python>;<home-directory of python>/Scripts
3)Open command prompt or power shell and type the following "python -m pip install -U pip"   without the double quotes

EXECUTION:

CONTENTS OF FOLDER:

1) Task1.py --> python source file with the code for generating the corpus from previously crawled files
2) Task2.py --> python source file with the code for generating the unigram, bigram and trigram inverted indexes, and also the code for generating 
              the term and document frequency tables for each of the 3 indexes

3) unigram_inverted_index.txt-->text file storing the unigram inverted index
 structure:
	term:(doc_id1:term_frequency doc_id2:term_frequency doc_id3:term_frequency....)
	
	
	
	
 
4) bigram_inverted_index.txt-->text file storing the bigram inverted index
 
 structure:
	term:(doc_id1:term_frequency doc_id2:term_frequency doc_id3:term_frequency....)


5)trigram_inverted_index.txt-->text file storing the trigram inverted index
 
 structure:
	term:(doc_id1:term_frequency doc_id2:term_frequency doc_id3:term_frequency....)

			  
6)unigram_document_frequency_table.txt--> text file storing the unigram terms , the document id of document this term 
                                         is found in and the number of such documents
										 										 
 structure:
	term:[doc_id1 doc_id2 doc_id3....) doc_frequency

 
7)unigram_term_frequency_table.txt--> text file storing the all the unique unigram terms and their counts
 
 structure:
	term1:term1_frequency
	term2:term2_frequency
	.
    .
	.
 
 
 8)bigram_document_frequency_table.txt--> text file storing the bigram terms , the document id of document this term 
                                         is found in and the number of such documents
										 
structure:
	term:[doc_id1 doc_id2 doc_id3....) doc_frequency
 
 
 9)bigram_term_frequency_table.txt--> text file storing the all the unique bigram terms and their counts
 
 structure:
	term1:term1_frequency
	term2:term2_frequency
	.
    .
	.
 
10) trigram_document_frequency_table.txt--> text file storing the trigram terms , the document id of document this term 
                                         is found in and the number of such documents
										 
										 
structure:
	term:[doc_id1 doc_id2 doc_id3....) doc_frequency
	
 
11)trigram_term_frequency_table.txt--> text file storing the all the unique trigram terms and their counts

structure:
	term1:term1_frequency
	term2:term2_frequency
	.
    .
	.
 
12) Task_2C_3_Unigram_Stoplist.txt--> text file containing unigram stop-words and a brief discussion on the logic behind creating the list

13) Task_2C_3_Bigram_Stoplist.txt--> text file containing bigram stop-words and a brief discussion on the logic behind creating the list
 
14) Task_2C_3_Trigram_Stoplist.txt--> text file containing trigram stop-words and a brief discussion on the logic behind creating the list

15) unigram_inverted_index_with_pos.txt-->text file storing the unigram inverted index with term position the document and term count for each document
 structure:
	term:(doc_id1:[positions1 position2 position3....-->{term_frequency}] doc_id2:[positions1 position2 position3....-->{term_frequency}]....)
	
	
	
DESIGN CHOICES:
 1)All the inverted indexes are represented as python dictionaries.The major reason behind choosing this data structure is 
   to exploit the speed of retrieval provided by dictionaries which internally implements hash tables.
   
  For text processing following choices are incorporated:
   
  2)To eliminate navigational components, the following tags/sections of an wikipedia page are removed:
			i)Any content after the section called "See Also"
			ii)Any component after the section called "Notes"
			iii)Any component after the section called "References"
			iv)Components with class name as "toc"
			
  3)All the "annotation" with "encoding"value set as "application/x-tex" are removed to eliminate mathematical formulas
  
  4)All table and img tags are removed
  
  5)If punctuations parameter is set as True, all punctuations except "-" is removed
  
  6)If case-folding parameter is set as True, all terms are converted to lower case	
 
EXECUTION--> Steps for executing the program in windows environment:

For Task1.py-->

1)go inside the the directory which has the python source file i.e. "Task1.py"
2)store the path of the crawled files in the global variable called "CRAWLED_FILES_LOCATION" and copy the path of the directory
3)open windows powershell or command prompt and type the command cd <file location copied in previous step>
4) To execute: (i)enter required boolean values as paramters in the function called "corpus_generator(Boolean,Boolean)" The first parameter , when set to TRUE, will eliminate the 
               content of all punctuations, except for "-".  The second parameter set to TRUE will result in case-folding of the content.
               (ii)After setting the desired parameters, type "python Task1.py" without the double quotes and hit enter
			   
			   
For Task2.py-->

1)go inside the the directory which has the python source file i.e. "Task2.py"
2)This code assumes that there is a folder present in the current directory which stores the output obtained from Task1.py
Name of this folder("corpus" by default) is stored in a global variable called "CORPUS_FOLDER_NAME"
  Copy the current path location.
3)open windows powershell or command prompt and type the command cd <file location copied in previous step>
4) To execute: type "python Task2.py" without the quotes and hit enter
 

CITATION:
 
1) https://www.crummy.com/software/BeautifulSoup/  -- BeautifulSoup is used for parsing and extracting contents from a page

  
  
  
  