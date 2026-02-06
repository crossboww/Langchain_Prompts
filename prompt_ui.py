from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

st.header("Researcher Tool")

# user_input = st.text_input("Enter your Prompt")

paper_input = st.selectbox("select Research Paper Name", ["Attention is all you need", "BERT: Pre-Training od Model", "GPT-3: Language Model are Few-Shot Learners", "Diffusion Models Beat GAN's on Image Synthesis"])

style_input = st.selectbox("Select Explaination style", ["Beginer Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraph)", "Medium (3-5 paragraph)", "Long (Detailed Paragraph)"])

template = load_prompt("template.json")


#Fill the Placeholders


if st.button("button"):
    chain = template | model
    result= chain.invoke({
    "paper_input" : paper_input,
    "style_input":  style_input,
    "length_input": length_input
    })

    st.write(result.content)