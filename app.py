import streamlit as st
from googletrans import LANGUAGES
from googletrans import Translator

translator = Translator()

st.title(":red[Arun] Arunisto :male-technologist:")
st.title("Translator - 翻译 - يترجم")

col1, col2 = st.columns(2)

with col1:
    s_lang = st.text_input("", placeholder="Destination Language >>>", disabled=True)
with col2:
    d_lang = st.selectbox(" ", [i+"-"+LANGUAGES[i] for i in LANGUAGES])

col3, col4 = st.columns(2)

with col3:
    s_lang_text = st.text_area(label="")
if st.button("Translate"):
    with col4:
        des = d_lang[:2]
        t_text = translator.translate(s_lang_text.lower(), dest=des)
        d_lang_text = st.text_area(label=" ", value=t_text.text)
else:
    with col4:
        d_lang_text = st.text_area(label=" ", disabled=True)
