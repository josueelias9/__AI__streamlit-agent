__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

#-- import libraries
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.document_loaders import TextLoader
from langchain.document_loaders import WebBaseLoader
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain import SQLDatabase
from pathlib import Path

class MyAgent:

    
    def initialize_agent2(self):
        # LLM model
        llm = OpenAI(temperature=0)

        #-- path
        relevant_parts = []
        for p in Path(".").absolute().parts:
            relevant_parts.append(p)
            if relevant_parts[-3:] == ["langchain", "docs", "modules"]:
                break
        doc_path = str(Path(*relevant_parts) / "streamlit_agent/state_of_the_union.txt")

        #-- preparing text tool
        loader = TextLoader(doc_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        docsearch = Chroma.from_documents(texts, embeddings, collection_name="state-of-union")
        state_of_union = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=docsearch.as_retriever()
        )

        #-- preparing web tool
        loader = WebBaseLoader(["https://www.laureate.net/"])
        docs = loader.load()
        ruff_texts = text_splitter.split_documents(docs)
        ruff_db = Chroma.from_documents(ruff_texts, embeddings, collection_name="ruff")
        ruff = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=ruff_db.as_retriever()
        )

        #-- preparing db tool
        DB_PATH = (Path(__file__).parent / "cursos.db").absolute()
        db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
        db_chain = SQLDatabaseChain.from_llm(llm, db)

        #-- tools
        tools = [

            Tool(
                name="Web de Laureate",
                func=ruff.run,
                description="useful for when you need to answer questions about the Laureate school. Answer in spanish.",
            ),
            Tool(
                name="DB",
                func=db_chain.run,
                description="useful for when you need to find information about the offered courses. Answer in spanish."
            ),
        ]

        # memory
        agent_kwargs = {
            "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
        }
        memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

        #-- agent
        agent = initialize_agent(
            tools, 
            llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=True,
            agent_kwargs=agent_kwargs,
            memory=memory
        )
        return agent


if __name__ == "__main__":
    import os
    os.environ['OPENAI_API_KEY'] = "tu_api_key"

    obj = MyAgent()

    x = obj.initialize_agent2()

    a = x.run("¿Que cursos ofreces?")
    b = x.run("¿cuanto cuesta cada curso?")
    c = x.run("¿La institucion educativa es buena?")
    d = x.run("horario de atencion?")
    e = x.run("No se que curso me convenga estudiar")
    f = x.run("creo que escogere Data Mining")
    print("---------------------")
    print(a)
    print("---------------------")
    print(b)
    print("---------------------")
    print(c)
    print("---------------------")
    print(d)
    print("---------------------")
    print(e)
    print("---------------------")
    print(f)
    print("---------------------")
