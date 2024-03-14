import streamlit as st


st.text('It is text')

st.write('Hello, *World!* :sunglasses:')

st.caption('Balloons. Hundreds of them... and it is caption')

st.text("Text content...")

st.markdown('''* first
 * second
* third''')


st.header('my header')

st.subheader('my_sub_header')

st.code('''
    for i in range(8):
        print(i)
''')

# LaTeX is a typesetting system commonly used for producing scientific and mathematical documents due to its ability to handle complex equations and formatting requirements.
#  It is widely used in academia for writing research papers, theses, and technical documents.
#  LaTeX uses markup tags to define the structure of a document, separating content from formatting.
#  Users write their documents in plain text, then use a LaTeX compiler to generate a PDF or other output format with the desired formatting.
st.latex(r''' e^{i\pi} + 1 = 0 ''')


st.image('https://miro.medium.com/v2/resize:fit:720/format:webp/1*0FqDC0_r1f5xFz3IywLYRA.jpeg')

st.video('https://youtu.be/80UVjkcxGmA?si=C8mWrN1O21Y_IbSp')

st.audio('./Recording.m4a')

import pandas as pd

df = pd.DataFrame({"Col1":[1,2,3],"Col2":['a','b','c']})

st.write(df)
st.table(df)
st.json(df.to_dict())
st.metric('My metric', 42, 2)