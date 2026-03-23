import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.title("데이터 시각화 페이지")

st.header("샘플 데이터 소개")
st.write("이 페이지에서는 다양한 데이터 시각화 예제를 보여줍니다. 샘플 데이터를 사용하여 막대 그래프, 선 그래프, 산점도, 히스토그램 등을 시각화합니다.")

# 샘플 데이터 생성
data = {
    '카테고리': ['A', 'B', 'C', 'D', 'E'],
    '값': [10, 20, 15, 25, 30]
}
df_bar = pd.DataFrame(data)

time_data = {
    '시간': pd.date_range(start='2023-01-01', periods=10, freq='M'),
    '값': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
}
df_line = pd.DataFrame(time_data)

scatter_data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [2, 4, 1, 3, 5, 7, 6, 8, 9, 10],
    '크기': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df_scatter = pd.DataFrame(scatter_data)

hist_data = pd.DataFrame({'값': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]})

st.header("1. 막대 그래프 (Bar Chart)")
st.write("카테고리별 값을 보여주는 막대 그래프입니다.")
fig_bar = px.bar(df_bar, x='카테고리', y='값', title='카테고리별 값')
st.plotly_chart(fig_bar)

st.header("2. 선 그래프 (Line Chart)")
st.write("시간에 따른 값의 변화를 보여주는 선 그래프입니다.")
fig_line = px.line(df_line, x='시간', y='값', title='시간에 따른 값 변화')
st.plotly_chart(fig_line)

st.header("3. 산점도 (Scatter Plot)")
st.write("두 변수 간의 관계를 보여주는 산점도입니다. 점의 크기는 추가적인 차원을 나타냅니다.")
fig_scatter = px.scatter(df_scatter, x='X', y='Y', size='크기', title='X와 Y의 관계')
st.plotly_chart(fig_scatter)

st.header("4. 히스토그램 (Histogram)")
st.write("데이터의 분포를 보여주는 히스토그램입니다.")
fig_hist = px.histogram(hist_data, x='값', title='값의 분포')
st.plotly_chart(fig_hist)

st.header("5. Matplotlib을 사용한 그래프")
st.write("Matplotlib을 사용하여 간단한 선 그래프를 그립니다.")
fig, ax = plt.subplots()
ax.plot(df_line['시간'], df_line['값'])
ax.set_title('Matplotlib 선 그래프')
ax.set_xlabel('시간')
ax.set_ylabel('값')
st.pyplot(fig)

st.write("이 예제들은 기본적인 데이터 시각화 기법을 보여줍니다. 실제 데이터를 사용하여 더 복잡한 시각화를 만들 수 있습니다.")
