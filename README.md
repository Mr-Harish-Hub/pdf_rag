## **PDF Question Answering System**
This project is a small implementation of a system that allows asking questions over a PDF document and getting answers only from that document.
The idea behind this project was to understand how document ingestion and retrieval work in a Retrieval Augmented Generation (RAG) setup, and to implement those parts manually instead of relying entirely on existing frameworks.

## **System workflow**
The system works by first taking a PDF document and reading all the text from it. This text is then broken into smaller parts so it can be searched efficiently. When a user asks a question, the system looks through the document to find only the parts that are most relevant to that question, instead of scanning the entire file. These relevant parts are then given to the model, which generates an answer strictly based on what is present in the document. If the document does not contain the answer, the system clearly says “Not found” instead of guessing.

## Technical Components Used

- **Python**  
  Used as the main programming language to build the complete pipeline.

- **pdfplumber**  
  Used to extract readable text from PDF documents.

- **Regular Expressions (re)**  
  Used to clean the extracted text by removing unnecessary whitespace and formatting noise.

- **Custom Text Chunking Logic**  
  Used to split large document text into smaller overlapping chunks for efficient embedding and retrieval.

- **Sentence Transformers (all-MiniLM-L6-v2)**  
  Used to generate embeddings for both document chunks and user queries to enable semantic similarity search.

- **FAISS**  
  Used as a vector database to store embeddings and perform fast similarity search.

- **Custom Retrieval Logic**  
  Used to dynamically select relevant chunks based on similarity distance instead of a fixed Top-K value.

- **Flan-T5 Base**  
  Used as a lightweight open-source language model to generate answers from the retrieved document context.

- **Hugging Face Transformers**  
  Used only for loading and running embedding and language models locally.

- **Git and GitHub**  
  Used for version control and project management.
