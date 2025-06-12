import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Descargar el lexicon de VADER
nltk.download('vader_lexicon')

# Configuración básica de la app
st.set_page_config(page_title="Análisis de Sentimiento con VADER", page_icon="💬")
st.title("💬 Análisis de Sentimiento con VADER")

texto = st.text_area("✍️ Escribe el texto que deseas analizar:")

if st.button("🔍 Analizar Sentimiento"):
    if texto.strip() == "":
        st.warning("Por favor, ingresa un texto primero.")
    else:
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(texto)
        st.write("📊 **Puntajes:**", scores)

        compound = scores["compound"]

        if compound >= 0.05:
            st.success("😊 Sentimiento positivo")
        elif compound <= -0.05:
            st.error("😠 Sentimiento negativo")
        else:
            st.info("😐 Sentimiento neutral")

