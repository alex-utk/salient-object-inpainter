import streamlit as st
import time
import random
from inference.infer import run_infer
import cv2

caption = [
    'Маска',
    'Опоясывающий полигон',
    'Результат'
]
st.header('Демо')
uploaded_file = st.file_uploader("Картинка на вход", accept_multiple_files=False, key='uploader')
if uploaded_file is not None:
    st.image(uploaded_file.getvalue(),
                            caption='Input', width=300, use_column_width=None,
                            clamp=False, channels="BGR", output_format="auto")
    mask, poly, result = run_infer(uploaded_file.getvalue())
    time.sleep(random.uniform(2.5, 3.5))
    st.image([mask, poly, result], caption=caption, width=200, use_column_width=None,
                            clamp=False, channels="BGR", output_format="auto")
