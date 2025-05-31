import streamlit as st
import openai

# Streamlit app
st.title("Text Generation App")
st.write("Enter your OpenAI API key and prompt to generate text.")

# Input fields
api_key = st.text_input("OpenAI API key", type="password")
prompt = st.text_input("Prompt", "")
max_tokens = st.slider("Max Tokens", 10, 2048, 100)

# Generate button
if st.button("Generate"):
    if api_key:
        try:
            client = openai.api_key(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7
            )
            generated_text = response.choices[0].message.content
            st.write(generated_text)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter your OpenAI API key")
