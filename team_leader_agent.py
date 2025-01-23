from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from typing import List
import os
import glob


class TeamLeaderAgent:
    def __init__(self, docs_path: str, openai_api_key: str):
        print(f"Initializing TeamLeaderAgent with docs_path: {docs_path}")  # Debug print
        self.openai_api_key = openai_api_key
        self.docs_path = docs_path
        self.vectorstore = None
        self.llm = None
        self.prompt = None
        if not os.path.exists(docs_path):
            raise FileNotFoundError(f"Documents directory not found: {docs_path}")
        self.setup_rag_pipeline()


    def load_documents(self) -> List:
        # Get all .txt files in the knowledge_base directory
        txt_files = glob.glob(f"{self.docs_path}/*.txt")
        print(f"Found text files: {txt_files}") 
        
        if not txt_files:
            raise FileNotFoundError(f"No .txt files found in {self.docs_path}")
        
        documents = []
        for file_path in txt_files:
            try:
                print(f"Loading file: {file_path}")
                loader = TextLoader(file_path, encoding='utf-8')
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading file {file_path}: {str(e)}")
        
        if not documents:
            raise ValueError("No documents were successfully loaded")
        
        print(f"Successfully loaded {len(documents)} documents")
        return documents


    def setup_rag_pipeline(self):
        try:
            # Get documents
            documents = self.load_documents()

            # Turn documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            splits = text_splitter.split_documents(documents)
            print(f"Created {len(splits)} text chunks")

            # Create embeddings and vector store
            embedding = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
            
            # Initialize Chroma with persist_directory
            persist_directory = "chroma_db"
            self.vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=embedding,
                persist_directory=persist_directory
            )
            print("Vector store initialized successfully")

            # Initialize LLM
            self.llm = ChatOpenAI(
                openai_api_key=self.openai_api_key,
                model_name="gpt-3.5-turbo-0125",
                temperature=0.65
            )

            # Create the RAG prompt template
            self.prompt = ChatPromptTemplate.from_messages([
                ("system", """You are an experienced team leader and senior software engineer. 
                Use the following context to provide guidance and answers based on your knowledge in the style of a senior technical leader.
                
                Context: {context}
                
                Remember to:
                1. Be clear and concise
                2. Provide technical reasoning when needed
                3. Give recommendations based on your experience
                4. Consider best practices and team dynamics
                5. Share relevant examples when appropriate"""),
                ("human", "{question}")
            ])
            
        except Exception as e:
            print(f"Error in setup_rag_pipeline: {str(e)}")
            raise


    def get_response(self, question: str) -> str:
        # Search for relevant documents
        docs = self.vectorstore.similarity_search(question, k=4)
        context = "\n".join([doc.page_content for doc in docs])

        # Create the chain and run it
        chain = self.prompt | self.llm

        response = chain.invoke({
            "context": context,
            "question": question
        })

        return response.content 