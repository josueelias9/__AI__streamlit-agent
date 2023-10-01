# deploy aplicacion
```
cd /path/of/repository
pip3 install -r requirements.txt
```
# start aplicacion
```
cd /path/of/repository
streamlit run ./streamlit_agent/courses.py 
```
# fuente
- resolver el problema con WebBaseLoader,
[link](https://github.com/langchain-ai/langchain/issues/11095)
- acerca de chroma, [link](https://python.langchain.com/docs/integrations/vectorstores/chroma)
- aligment en LLM, [link](https://www.linkedin.com/pulse/importance-alignment-llms-nilesh-barla/)
- integrar con wsp, [link](https://python.langchain.com/docs/integrations/chat_loaders)
- frontend para langchain con streamlit, [link](https://python.langchain.com/docs/integrations/callbacks/streamlit), [link](https://streamlit.io/generative-ai)
- como usar SQLite con vscode, [link](https://www.youtube.com/watch?v=QDP_PTg6BcQ)
- agent + vector store, [link](https://python.langchain.com/docs/modules/agents/how_to/agent_vectorstore#use-the-agent-solely-as-a-router)
- Creating a SQLite database with Python code, [link](https://www.sqlitetutorial.net/sqlite-python/creating-database/)


todas las dependencias se tomaron del archivo pyproject.toml

