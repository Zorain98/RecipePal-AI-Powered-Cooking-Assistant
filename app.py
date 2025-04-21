import streamlit as st
import langchain
import warnings
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = st.secrets["OPENAI_API_KEY"]
warnings.filterwarnings("ignore")

template = """You are an experienced chef creates a recipe based on the ingredients provided by the user. 
                Here are the ingredients: {ingredients}
                Please suggest a recipe that can be made with these ingredients, including instructions.
                Recipe: 
                """

prompt = PromptTemplate(
    input_variables=["ingredients"], template=template
)

LLM = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo", api_key=api_key)

recipe_chain = LLMChain(
    llm=LLM,
    prompt=prompt
)
 
st.title("👨🏻‍🍳 RecipePal: AI Powered Cooking Assistant")
st.divider()
st.write("Enter the ingredients available in the kitchen and let RecipePal suggest a recipe!")
ingredients = st.text_input("Enter the ingredients you have (comma separated):")
st.divider()
if st.button("Get Recipe", type="primary"):
    if ingredients:
        with st.spinner("Creating recipe..."):
            st.snow()
            recipe = recipe_chain.run(ingredients)
            st.write(recipe)
    else:
        st.warning("Please enter ingredients.")

