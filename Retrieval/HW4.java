import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.util.ArrayList;
import java.io.BufferedWriter;
import java.io.FileWriter;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.core.SimpleAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopScoreDocCollector;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;

public class HW4  {
	
    private static Analyzer analyzer = new StandardAnalyzer(Version.LUCENE_47);
    private static Analyzer sAnalyzer = new SimpleAnalyzer(Version.LUCENE_47);
    
    private IndexWriter writer;
    private ArrayList<File> queue = new ArrayList<File>();

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out
		.println("Enter the FULL path where the index will be created: (e.g. /Usr/index or c:\\temp\\index)");
		
		String indexLocation = null;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		HW4 indexer = null;
		
		try {
		    indexLocation = s;
		    indexer = new HW4(s);
		} catch (Exception ex) {
		    System.out.println("Cannot create index..." + ex.getMessage());
		    System.exit(-1);
		}
		
		// ===================================================
		// read input from user until he enters q for quit
		// ===================================================
		while (!s.equalsIgnoreCase("q")) {
		    try {
			System.out
				.println("Enter the FULL path to add into the index (q=quit): (e.g. /home/mydir/docs or c:\\Users\\mydir\\docs)");
			System.out
				.println("[Acceptable file types: .xml, .html, .html, .txt]");
			s = br.readLine();
			if (s.equalsIgnoreCase("q")) {
			    break;
			}

			// try to add file into the index
			indexer.indexFileOrDirectory(s);
		    } catch (Exception e) {
			System.out.println("Error indexing " + s + " : "
				+ e.getMessage());
		    }
		}

		// ===================================================
		// after adding, we always have to call the
		// closeIndex, otherwise the index is not created
		// ===================================================
		indexer.closeIndex();
		
		
		// =========================================================
		// Now search
		// =========================================================
		IndexReader reader = DirectoryReader.open(FSDirectory.open(new File(
			indexLocation)));
		IndexSearcher searcher = new IndexSearcher(reader);
		TopScoreDocCollector collector = TopScoreDocCollector.create(100, true);
		
		try{
			File dir=new File(indexLocation);
			if(dir.isDirectory()) {
				for (File f : dir.listFiles()) {
					if(f.exists()) {
						f.delete();
					}
				}
			}		
			
		}catch(Exception e) {
			e.printStackTrace();
			System.exit(-1);
		}
			
		
		
		s = "";

	    try {
		System.out.println("Enter the FULL path to the query file : (e.g. /home/mydir/query or c:\\Users\\mydir\\query.txt)");
		s = br.readLine();
	
		ArrayList<String> querylist=new ArrayList<String>();
		try {
		
		File file = new File(s);
		BufferedReader b = new BufferedReader(new FileReader(file));
		String st;
		  while ((st = b.readLine()) != null) {
		    System.out.println(st);
		    querylist.add(st);
		  }
		  }
		catch(Exception e) {
			System.out.println(e);
	}
		
		for (int j=0;j<querylist.size();j++) {
			String current_query=querylist.get(j);
			
			Query q = new QueryParser(Version.LUCENE_47, "contents",
					sAnalyzer).parse(current_query);
			collector=TopScoreDocCollector.create(100,true);
				searcher.search(q, collector);
				ScoreDoc[] hits = collector.topDocs().scoreDocs;

				// 4. display results
				System.out.println("Found " + hits.length + " hits.");
				
			   	String file_name=current_query.replaceAll(" ", "_");
		    	file_name+="_Lucene.txt";
		    	BufferedWriter w = new BufferedWriter(new FileWriter(file_name));
		    	String query_id=Integer.toString(j+1);
		    	
		    	//Storing top 100 results in text files
		    	
				for (int i = 0; i < hits.length; ++i) {
				    int docId = hits[i].doc;
				    Document d = searcher.doc(docId);
				 
				    System.out.println((i + 1) + ". " + d.get("path")
					    + " score=" + hits[i].score);
				    
				    String doc_name=d.get("filename");
				    int l=doc_name.length()-4;
				    doc_name=doc_name.substring(0,l);
				    String output_string=query_id+" Q0 "+doc_name+" "+(i+1)+" "+hits[i].score+" Lucene_Model"+"\n";		    
				    
				    try {
				    	w.write(output_string);

				    }catch(Exception e) {
				    	System.out.println(e);
				    }
				    
				}
				w.close();
				
				// 5. term stats --> watch out for which "version" of the term
				// must be checked here instead!
				
				Term termInstance = new Term("contents", current_query);
				long termFreq = reader.totalTermFreq(termInstance);
				long docCount = reader.docFreq(termInstance);
				System.out.println(s + " Term Frequency " + termFreq
					+ " - Document Frequency " + docCount);
				}

			    } catch (Exception e) {
				System.out.println("Error searching " + s + " : "
					+ e.getMessage());
				e.printStackTrace();

			    }

			}
				
			
	  /**
     * Constructor
     * 
     * @param indexDir
     *            the name of the folder in which the index should be created
     * @throws java.io.IOException
     *             when exception creating index.
     */
    HW4(String indexDir) throws IOException {

	FSDirectory dir = FSDirectory.open(new File(indexDir));

	IndexWriterConfig config = new IndexWriterConfig(Version.LUCENE_47,
		sAnalyzer);

	writer = new IndexWriter(dir, config);
    }

    /**
     * Indexes a file or directory
     * 
     * @param fileName
     *            the name of a text file or a folder we wish to add to the
     *            index
     * @throws java.io.IOException
     *             when exception
     */
    public void indexFileOrDirectory(String fileName) throws IOException {
	// ===================================================
	// gets the list of files in a folder (if user has submitted
	// the name of a folder) or gets a single file name (is user
	// has submitted only the file name)
	// ===================================================
	addFiles(new File(fileName));

	int originalNumDocs = writer.numDocs();
	for (File f : queue) {
	    FileReader fr = null;
	    try {
		Document doc = new Document();

		// ===================================================
		// add contents of file
		// ===================================================
		fr = new FileReader(f);
		doc.add(new TextField("contents", fr));
		doc.add(new StringField("path", f.getPath(), Field.Store.YES));
		doc.add(new StringField("filename", f.getName(),
			Field.Store.YES));

		writer.addDocument(doc);
		System.out.println("Added: " + f);
	    } catch (Exception e) {
		System.out.println("Could not add: " + f);
	    } finally {
		fr.close();
	    }
	}

	int newNumDocs = writer.numDocs();
	System.out.println("");
	System.out.println("************************");
	System.out
		.println((newNumDocs - originalNumDocs) + " documents added.");
	System.out.println("************************");

	queue.clear();
    }

    private void addFiles(File file) {

	if (!file.exists()) {
	    System.out.println(file + " does not exist.");
	}
	if (file.isDirectory()) {
	    for (File f : file.listFiles()) {
		addFiles(f);
	    }
	} else {
	    String filename = file.getName().toLowerCase();
	    // ===================================================
	    // Only index text files
	    // ===================================================
	    if (filename.endsWith(".htm") || filename.endsWith(".html")
		    || filename.endsWith(".xml") || filename.endsWith(".txt")) {
		queue.add(file);
	    } else {
		System.out.println("Skipped " + filename);
	    }
	}
    }

    /**
     * Close the index.
     * 
     * @throws java.io.IOException
     *             when exception closing
     */
    public void closeIndex() throws IOException {
	writer.close();
    }
}

