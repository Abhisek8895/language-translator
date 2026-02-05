import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer # type: ignore

# -------- CONFIG -------- #

MODEL_NAME = "facebook/m2m100_418M"

LANGUAGES = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "English": "en"
}

# -------- LOAD MODEL -------- #

@st.cache_resource
def load_model():
    tokenizer = M2M100Tokenizer.from_pretrained(MODEL_NAME)
    model = M2M100ForConditionalGeneration.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

# -------- TRANSLATION FUNCTION -------- #

def translate_text(text, target_language):
    tokenizer.src_lang = "en"  # default source (can change later)
    encoded = tokenizer(text, return_tensors="pt")

    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id(LANGUAGES[target_language])
    )

    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

# -------- UI -------- #

st.set_page_config(page_title="GenAI Translator", layout="centered")

st.title("🌍 Language Translator (Hugging Face Local)")

input_text = st.text_area("Enter text to translate", height=150)

target_language = st.selectbox(
    "Translate to",
    list(LANGUAGES.keys())
)

if st.button("Translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            result = translate_text(input_text, target_language)
        st.success("Translation")
        st.write(result)
    else:
        st.warning("Please enter some text.")
