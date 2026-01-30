PDF Question Answering System
This project is a small implementation of a system that allows asking questions over a PDF document and getting answers only from that document.
The idea behind this project was to understand how document ingestion and retrieval work in a Retrieval Augmented Generation (RAG) setup, and to implement those parts manually instead of relying entirely on existing frameworks.

System workflow
The system works by first taking a PDF document and reading all the text from it. This text is then broken into smaller parts so it can be searched efficiently. When a user asks a question, the system looks through the document to find only the parts that are most relevant to that question, instead of scanning the entire file. These relevant parts are then given to the model, which generates an answer strictly based on what is present in the document. If the document does not contain the answer, the system clearly says “Not found” instead of guessing.

Technical Components Used
Below are the main technologies used in the project and why they are used.
Python
Used as the main programming language to build the complete pipeline.
pdfplumber
Used to extract readable text from PDF documents.
Regular Expressions (re)
Used to clean the extracted text by removing unnecessary whitespace and formatting issues from PDFs.
Custom Chunking Logic
Used to split large document text into smaller overlapping chunks so that they can be embedded and searched efficiently.
Sentence Transformers (all-MiniLM-L6-v2)
Used to convert both document chunks and user queries into numerical embeddings that capture semantic meaning.
FAISS
Used as a vector database to store embeddings and perform similarity search between the query and document chunks.
Custom Retrieval Logic
Used to dynamically select relevant chunks based on similarity distance instead of using a fixed number of chunks.
Flan-T5 Base
Used as a lightweight open-source language model to generate answers from the retrieved document context.
Hugging Face Transformers
Used only for loading and running models locally.
Git and GitHub
Used for version control and project management.

<img width="832" height="513" alt="image" src="https://github.com/user-attachments/assets/396fa200-4db7-4ac4-af75-24da9168d2cb" />

