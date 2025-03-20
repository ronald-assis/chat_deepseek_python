import streamlit as st
from langchain_ollama import ChatOllama


llm = ChatOllama(model='deepseek-r1:1.5b', base_url='http://localhost:11434')

st.set_page_config(page_title='DeepSeek Chat', layout='centered')
st.title('Talk to DeepSeek')

if "messages" not in st.session_state:
    st.session_state.messages = []

messages = st.session_state.messages
for type, content in messages:
    chat = st.chat_message(type)
    chat.markdown(content)

prompt = st.chat_input('Send your message to DeepSeek:')

if prompt:
    messages.append(('human', prompt))
    chat = st.chat_message('human')
    chat.markdown(prompt)

    response = llm.invoke(messages)
    messages.append(('ai', response.content))

    chat = st.chat_message('ai')
    chat.markdown(response.content)
