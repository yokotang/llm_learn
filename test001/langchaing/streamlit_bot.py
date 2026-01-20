import streamlit as st
import requests


#设计界面
backend_url="http://127.0.0.1:6166/chat"
st.set_page_config(page_title="聊天机器人",page_icon="🤖")
#设计聊天对话框
st.title("🤖TT")
def clear_chat_history():
    st.session_state.history=[]
with st.sidebar:
    st.title("ChatBot")
    sys_prompt=st.text_input("系统提示词:",value="You are a helpful assistant.")
    history_len=st.slider("保留历史记录对话的数量:",min_value=1,max_value=10,value=1,step=1)
    temperature=st.slider("temperature:",min_value=0.01,max_value=2.0,value=0.5,step=0.01)
    top_p=st.slider("top_p:",min_value=0.01,max_value=1.0,value=0.5,step=0.01)
    max_tokens=st.slider("max_tokens:",min_value=256,max_value=4096,value=1024,step=8)
    stream=st.checkbox("stream",value=True)
    st.button("清除聊天历史记录",on_click=clear_chat_history())

if "history" not in st.session_state:
    st.session_state.history=[]
#显示聊天历史
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#显示输入框和发送按钮
#:=海象运算符，用于检查赋值的内容是否为空
if prompt:=st.chat_input("来聊天"):
    #显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)
    #构建请求数据
    data={
        "query":prompt,
        "sys_prompt":sys_prompt,
        "history_len":history_len,
        "temperature":temperature,
        "top_p":top_p,
        "max_tokens":max_tokens,
        "stream":stream

    }
    #发送请求到后端
    response=requests.post(backend_url,json=data,stream=True)
    if response.status_code==200:
        assistant_placeholder=st.chat_message("assistant")
        assistant_text=assistant_placeholder.markdown("")
        chunks=""
        if stream:
            for chunk in response.iter_content(chunk_size=None,decode_unicode=True):
                #处理相应的内容，并累加
                chunks +=chunk
                #实时显示和更新消息
                assistant_text.markdown(chunks)
        else:
            for chunk in response.iter_content(chunk_size=None,decode_unicode=True):
                chunks +=chunk
            assistant_text.markdown(chunks)
    st.session_state.history.append({"role":"user","content":prompt})
    st.session_state.history.append({"role":"assistant", "content": chunks})