import streamlit as st
import ollama
import time


def stream_data(text, delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)


#Input
prompt = st.chat_input("Ask...")

if prompt:
    #Display input prompt from user
    with st.chat_message("user"):
        st.write(prompt)
    
    #Processing
    with st.spinner("Thinking...."):
        try:
            result=ollama.chat(model="tinyllama", messages=[{
                "role": "user",
                "content": prompt
            }])
            response=result["message"]["content"]
        except Exception as e:
            st.error(f"An error occurred: {e}")
            response = ""
        

        #Display streamed response
        if response:
            with st.chat_message("bot"):
                message_placeholder=st.empty()
                streamed_response= ""
                for word in stream_data(response):
                    streamed_response += word
                    message_placeholder.markdown(streamed_response)
        
