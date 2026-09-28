"""Thin Streamlit host: inventory and photos remain inside the browser."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="物光 · 个人物品盘点", page_icon="◇", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>.block-container{padding:1rem 0.5rem;max-width:1200px}iframe{border:0}</style>""", unsafe_allow_html=True)
# Only embed trusted, bundled source. Never interpolate uploads or user input.
page = Path(__file__).with_name("inventory.html").read_text(encoding="utf-8")
components.html(page, height=1050, scrolling=True)
