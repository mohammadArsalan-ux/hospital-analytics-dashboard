#  import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load data
# df = pd.read_csv("hospital_data.csv")

# st.title("🏥 Hospital Analytics Dashboard")

# # Sidebar filter
# column = st.selectbox("Select Column", df.columns)

# # KPI
# st.metric("Total Records", len(df))

# # Plot
# fig = px.histogram(df, x=column)
# st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import plotly.express as px 

# load data  
df = pd.read_csv("hospital_data.csv")
st.title("Hospital Analytics Dashboard")

# Sidebar filter
column = st.selectbox("Select Column",df.columns)

# KPI
st.metric("Total Records", len(df))

# Plot
fig = px.histogram(df, x = column)
st.plotly_chart(fig)
