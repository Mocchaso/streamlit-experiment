import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('タイトル: Streamlitをお試し')
st.write('テキストを書き込む。markdown, LaTeXも記述可能。')
st.markdown('## DataFrameの表示')


st.markdown('### 動的な表としてDataFrameを表示する')
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': [10, 20, 30, 40, 50]
})
# 引数 ->  width: 横方向の長さ[px], height: 縦方向の長さ[px]
# st.dataframe(...) では、表の縦横の長さを指定することが出来る
# st.write(...) では、表の細かい設定は出来ない
st.dataframe(df)
# 列または行における最大値にハイライトをつけることも可能
st.markdown('### 列または行における最大値にハイライトを付けてDataFrameを表示する')
st.dataframe(df.style.highlight_max(axis=0))
# 静的な表を作りたい時には、st.table(...) を使用する
st.markdown('### 静的な表としてDataFrameを表示する')
st.table(df)

"""
### マジックコマンドでmarkdownを記述することも可能です

```python
print('コードブロックも記述できます。')
```
"""


st.markdown('## グラフのプロット')
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.markdown('### 折れ線グラフ')
'拡大・縮小等のインタラクティブな操作や、グラフの画像保存も出来る。'
st.line_chart(df2)
st.markdown('### 面グラフ')
st.area_chart(df2)
st.markdown('### 棒グラフ')
st.bar_chart(df2)

st.markdown('### マップ\n\n名古屋駅周辺の座標情報を生成して、表示してみる。')
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.17, 136.88],
    columns=['latitude', 'longitude']
)
st.map(df3)

st.markdown('''
## 画像の表示

use_column_width: 実際のレイアウトの横幅に合わせて表示する。  
別の関数を使えば、音声や動画も表示させることが可能。
''')
img = Image.open('images/cloud.webp')
st.image(img, caption='cloud', use_column_width=True)


st.markdown('## インタラクティブなウィジェット')
'ユーザが入力した値によって、表示内容を動的に変化させることも可能。'

st.markdown('### チェックボックス')
if st.checkbox('表示を有効化'):
    img2 = Image.open('images/sephiroth_cloud.jpg')
    st.image(img2, caption='sephiroth_cloud', use_column_width=True)

st.markdown('### セレクトボックス（プルダウンリスト）')
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

st.markdown('### テキスト入力')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

st.markdown('### スライダー')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition


st.markdown('## レイアウトを整える')

st.markdown('### サイドバーの追加')
st.sidebar.write('ここはサイドバーです。')
text2 = st.sidebar.text_input('あなたの趣味を教えてください。2')
condition2 = st.sidebar.slider('あなたの今の調子は？2', 0, 100, 10)
'あなたの趣味2：', text2
'コンディション2：', condition2

st.markdown('### 2カラムレイアウトにする')
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラムです。')

st.markdown('### expanderの追加（アコーディオン）')
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

st.markdown('### プログレスバーの表示')
button2 = st.button('プログレスバーの動作を始める')
if button2:
    'Start!!'

    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)
    
    'Done!!'
