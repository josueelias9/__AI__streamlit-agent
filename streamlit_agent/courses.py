import streamlit as st
from pathlib import Path

from langchain.callbacks import StreamlitCallbackHandler



st.set_page_config(page_title="Has tus preguntas", page_icon="laureate.png")

#image
from PIL import Image
image = Image.open("laureate.png")
st.image(image, caption='Sunrise by the mountains')

st.title("🤖🌐📚 Preguntas de curso")

# User inputs
radio_opt = ["Use sample database - Chinook.db", "Connect to your SQL database"]
selected_opt = st.sidebar.radio(label="Choose suitable option", options=radio_opt)
if radio_opt.index(selected_opt) == 1:
    db_uri = st.sidebar.text_input(
        label="Database URI", placeholder="mysql://user:pass@hostname:port/db"
    )
else:
    db_filepath = (Path(__file__).parent / "Chinook.db").absolute()
    db_uri = f"sqlite:////{db_filepath}"

openai_api_key = st.sidebar.text_input(
    label="OpenAI API Key",
    type="password",
)

# Check user inputs
if not db_uri:
    st.info("Please enter database URI to connect to your database.")
    st.stop()

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")
    st.stop()

# Setup agent
import os
os.environ['OPENAI_API_KEY'] = openai_api_key

from my_agent import MyAgent
myAgent = MyAgent()
agent = myAgent.initialize_agent2()



if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Buenos dias. ¿Como te puedo ayudar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="¡Pregunta lo que desees!")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
