# Trabajo
# Arquitectura actual
# Arquitectura propuesta
# deploy aplicacion

Crear entorno virtual y activarlo
```bash
cd /path/of/repository/streamlit_agent
python3 -m venv venv
source ./venv/bin/activate
```
Instalar dependencias
```bash
cd /path/of/repository
pip3 install -r requirements.txt
```
Correr aplicativo localmente
```bash
cd /path/of/repository
streamlit run ./streamlit_agent/courses.py 
```
# fuente
Documentacion
- acerca de chroma, [link](https://python.langchain.com/docs/integrations/vectorstores/chroma)
- aligment en LLM, [link](https://www.linkedin.com/pulse/importance-alignment-llms-nilesh-barla/)
- integrar con wsp, [link](https://python.langchain.com/docs/integrations/chat_loaders)
- frontend para langchain con streamlit, [link](https://python.langchain.com/docs/integrations/callbacks/streamlit), [link](https://streamlit.io/generative-ai)
- como usar SQLite con vscode, [link](https://www.youtube.com/watch?v=QDP_PTg6BcQ)
- agent + vector store, [link](https://python.langchain.com/docs/modules/agents/how_to/agent_vectorstore#use-the-agent-solely-as-a-router)
- Creating a SQLite database with Python code, [link](https://www.sqlitetutorial.net/sqlite-python/creating-database/)

Solucion a problemas
- como solucionar el problema que se presenta al usar Chroma y desplegar el aplicativo a streamlit app, [link](https://discuss.streamlit.io/t/issues-with-chroma-and-sqlite/47950/5), [link](https://stackoverflow.com/questions/76958817/streamlit-your-system-has-an-unsupported-version-of-sqlite3-chroma-requires-sq/76959262#76959262)
- resolver el problema con WebBaseLoader,
[link](https://github.com/langchain-ai/langchain/issues/11095)


todas las dependencias se tomaron del archivo pyproject.toml

