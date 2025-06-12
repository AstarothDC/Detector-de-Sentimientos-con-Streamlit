# 💬 Análisis de Sentimientos con VADER y Streamlit

Este proyecto es una aplicación web simple para realizar análisis de sentimientos usando el analizador VADER de `nltk`, desplegada con la biblioteca `streamlit`.

VADER (Valence Aware Dictionary and sEntiment Reasoner) es un modelo basado en reglas, especialmente adecuado para textos cortos e informales como comentarios, redes sociales y reseñas.

---

## 🚀 Funcionalidades

- Analiza textos y proporciona una puntuación de sentimiento:
  - Positivo 😊
  - Negativo 😠
  - Neutral 😐
- Interfaz simple y amigable construida con Streamlit.
- Resultados inmediatos con un solo clic.

---

## 📦 Requisitos

- Python 3.7+
- pip

### 🧰 Instalación de dependencias

```bash
pip install streamlit nltk
Además, asegúrate de descargar el léxico de VADER (esto se hace automáticamente en la app, pero también puedes hacerlo manualmente):

python
Copiar
Editar
import nltk
nltk.download('vader_lexicon')
📝 Uso
Guarda el archivo principal como sentimientos.py.

Abre tu terminal en la carpeta del proyecto.

Ejecuta la aplicación con:

bash
Copiar
Editar
streamlit run sentimientos.py
Se abrirá una pestaña en tu navegador. Ingresa un texto y haz clic en "Analizar Sentimiento".

📋 Ejemplo
Entrada de texto:

r
Copiar
Editar
¡Este proyecto es increíble! Me encanta cómo funciona.
Resultado:

compound: 0.7783

Sentimiento: Positivo 😊

📁 Estructura del Proyecto
bash
Copiar
Editar
análisis-sentimientos-vader/
│
├── sentimientos.py        # Código principal de la app
└── README.md              # Este archivo
🧠 Notas
VADER está optimizado para inglés. Si deseas un análisis para español, se recomienda traducir el texto o utilizar otros modelos como BERT, TextBlob-es, o modelos entrenados con datasets en español.

Este proyecto está enfocado en la simplicidad y rapidez.

🧠 Créditos
Desarrollado por Ing. Dilan Cabas / GitHub