import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

st.set_page_config(page_title="Multi AI agent",layout='centered')
st.title("Multi AI agenty using Groq and Tavily")

system_prompt=st.text_area("Define you AI agent: ",height=70)
selected_model=st.selectbox("Select yout AI model: ",settings.ALLOWED_MODEL_NAMES)

allow_web_search=st.checkbox("Allow web search")

user_query=st.text_area("Enter your query: ",height=150)

API_URL= "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():

    payload={
        "name_of_model" : selected_model,
        "system_prompt" : system_prompt,
        "messages" : [user_query],
        "allow_search" : allow_web_search
    } 

    try:
        logger.info("Sending requests to backend")

        response=requests.post(API_URL,json=payload)

        logger.info(f"📡 Status Code: {response.status_code}")
        logger.info(f"📨 Raw Response: {response.text}")

        if response.status_code==200:
            agent_response=response.json().get("response")
            logger.info("Sucessfully received respobse from backend")
            logger.info(f"agent_response = {agent_response}")

            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n","<br>"),unsafe_allow_html=True)

        else:
            logger.error("Backend Error")
            st.error(f"Error with backend: {response.status_code}")
            st.text(response.text)

    except Exception as e:
        logger.error("Error occured while sending request to backend")
        logger.error(str(e))
        st.error(str(CustomException("Failed to communicate with backend", error_detail=e)))


