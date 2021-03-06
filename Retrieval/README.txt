INSTALLATIONS( for Windows environment):

For python :

1)Download python 2.7.x from https://www.python.org/downloads/
2)Add two variables to path variable, as <home-directory of python>;<home-directory of python>/Scripts
3)Open command prompt or power shell and type the following "python -m pip install -U pip"   without the double quotes

For java:

1)Download and install jdk and jre(any latest version)
2)add the location of "bin" folders present inside jre and jdk folders to the "PATH" variable
3)Donload Lucene(preferably version 4.7.2)



CONTENTS OF FOLDER:

1) HW4.java --> java source file with the code for generating top 100 documents for the queries using lucene
2) Task2.py --> python source file with the code for generating top 100 documents for the queries using BM25model

3) comparisons-->Folder containing the comparisons between lucene and BM25 models for 10 queries in 10 different text files, which are named as 
   Comparison_Query<query_id>.txt
	
	
4)top-100-results--> A folder containing 20 text files

10 files containing names of 100 documents(maximum) generated by lucene.These are named as <query_name>_lucene.txt

10 files containing names of 100 documents(maximum) generated by BM25.These are named as <query_name>_BM25.txt

5)implementation.txt-->text file containing a very brief description of implementation of Task1 and Task2

	
	
	
EXECUTION--> Steps for executing the program in windows environment:

For HW4.java-->
1)Create a java project and add the following jars
     i)lucene-core-VERSION.jar
	 ii)lucene-queryparser-VERSION.jar
	 iii)lucene-analyzers-common-VERSION.jar.
	 
	Where VERSION is to be substituted with the version downloaded
3)Execute the program
4)3 absolute paths has to be provided to console when prompted:
    i)the path where the the index folder will be created
	ii)the path where the corpus is located
	iii)path to a text  file containing the queries.Each query in a single line
	
N.B. --> A processed(removed punctuation and case folded) corpus is used because, the default implementation of lucene does not remove the html tags
and thus the documents does not get ranked correctly.	 


		   
			   
For Task2.py-->

1)go inside the the directory which has the python source file i.e. "Task2.py" 

Make the following changes in the Task2.py files

	i)Store the path of the corpus in a variable called "CORPUS_LOCATION"

	ii)Store the path of the query file in a variable called "QUERYFILE_LOCATION"

	iii)Store the path of the inverted index generated in HW3 in a variable called "INDEX_FILE_NAME"

3)open windows powershell or command prompt and type the command cd <file location copied in previous step>

4) To execute: type "python Task2.py" without the quotes and hit enter
 

CITATION:
 
1) https://lucene.apache.org/core/documentation.html  -- Lucene is used for parsing queries and retrieving documents

  
  
  
  