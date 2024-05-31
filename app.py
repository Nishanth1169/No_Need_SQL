from dotenv import load_dotenv
load_dotenv() #load all env variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text
    

#Retrieve query from database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The sql database has the name student and has the following columns - ID,NAME,YEAR,GROUPS AND MARKS
    the command will be something like Example: Tell me all the students studying in DataScience group?,
    The sql commands will be like this SELECT * FROM STUDENT WHERE GROUPS="DataScience";
    also the code should not have ''' in beginning or end and sql word in the output.
    """
]


st.set_page_config(page_title="Give the text and Get the data")
st.header("Give the text and get the result :")
question = st.text_input("Input :",key="input")
submit = st.button("Ask the Question")


if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)