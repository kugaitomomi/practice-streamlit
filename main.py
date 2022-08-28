import time
from random import sample
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit超入門')

st.write('Display Image')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )

st.write('プロブレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteratetion {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!!!!'


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1を書く')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2を書く')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ4を書く')

# text = st.sidebar.text_input(
#     'あなたの趣味を教えてください',
# )
# 'あなたの趣味は、', text, 'です。'

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション: ', condition


# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='TOmomi Kugai', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# dataframeは、widthとheightの指定ができる。
# st.dataframe(df.style.highlight_max(axis=1), width=200, height=200)
# st.dataframe(df.style.highlight_max(axis=0))
# ただ表を表示させたいときは「.table」
# st.table(df.style.highlight_max(axis=0))

# マークダウン記法
# """
# # 章
# # 節
# # 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """
