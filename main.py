import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time

"""
# My first Streamlit app
"""

homePressed = st.sidebar.button('HOME')
chartPressed = st.sidebar.button('CHARTS')

if homePressed:
  'Starting a long computation...'

  # Add a placeholder
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range(5):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

  '...and now we\'re done!'

  st.image("media/isle_of_dog.gif", caption="My lovely dog")

  st.latex(r'''e^{i\pi} + 1 = 0''')
elif chartPressed:
  # Chart
  df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
  })

  df

  # Line Chart
  chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])

  st.line_chart(chart_data)

  # Map
  map_data = pd.DataFrame(
      np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
      columns=['lat', 'lon'])

  st.map(map_data)

  # Conditional
  if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

      chart_data
else:


  # option = st.sidebar.selectbox(
  #     'Which number do you like best?',
  #      df['first column'])

  # 'You selected:', option

  # st.multiselect('Options', ['a', 'b', 'c', 'd'])

  # Layout
  left_column, right_column = st.columns(2)
  pressed = left_column.button('Press me?')
  if pressed:
    right_column.write("Woohoo!")

  expander = st.expander("FAQ")
  expander.write("Here you could put in some really, really long explanations...")