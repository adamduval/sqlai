import openai
import streamlit as st


# load api key from secrets file
openai.api_key = st.secrets['pass']

# streamlit app configuration
query = st.text_input('Entry text to translate to Snowflake SQL')


def generate_sql(query: str) -> str:
    """
    """
    model_engine = "text-davinci-002"
    prompt = (
        f"Translate the following natural language query into Snowflake SQL:\n"
        f"{query}\n"
        f"SQL:"
    )

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    return response.choices[0].text.strip()


# streamlit app functionality
if st.button('Generate SQL query'):
    if len(query) > 0:
        response = generate_sql(query)
        st.write(response)
