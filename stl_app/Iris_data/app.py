import streamlit as st
import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns
import altair as alt
st.title("Iris ")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล **Palmer\'s Penguins** กัน แบบเดียวกับ **Iris dataset**')

choices = ['sepal.length',
           'sepal.width',
           'petal.length',
           'petal.width']

selected_x_var = st.selectbox('เลือก แกน x', (choices))
selected_y_var = st.selectbox('เลือก แกน y', (choices))

iris_file = st.file_uploader("เลือกไฟล์ CSV", type=['csv'])




if iris_file is not None:
    iris_df = pd.read_csv(iris_file)
else:
    st.stop()

st.subheader('ข้อมูลตัวอย่าง')
st.write(iris_df)

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid')
markers = {"Setosa": "v", "Versicolor": "s", "Virginica": 'o'}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='variety', markers=markers, style='variety')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Palmer's Penguins Data")
st.pyplot(fig)




# alt_chart=(
#     alt.Chart(data=iris_df,title='Scatterplot of Plamer ')
#     .mark_circle()
#     .encode(
#         x=selected_x_var,y=selected_y_var
#     )
#     .interactive()
# )
# st.altair_chart(alt_chart,use_container_width=True)