import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_resource
def load_data():
    data = pd.read_csv("../dataset/Bike-sharing-dataset/hour.csv")
    return data

data = load_data()

st.title("Bike Rental Dashboard")

st.sidebar.title("Dataset Bike Rental")

if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view)")

col1, col2 = st.columns(2)

# st.subheader("Hourly Bike Rental")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Bike Rental per Hour")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# st.subheader("Relationship between Humidity and The Number of Bike Rentals")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Relationship between Humidity and The Number of Bike Rentals")
st.plotly_chart(fig_humidity_chart)

# Temperature vs. Bike Share Count
# st.subheader("Relationship between Temperature and The Number of Bike Rentals")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Relationship between Temperature and The Number of Bike Rentals")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)

st.write("This analysis focuses on understanding the patterns and trends of bicycle rentals during the spring season of 2011. By examining rental data during this specific timeframe, users can gain insights into factors such as rental frequency, peak hours, popular rental locations, and overall demand for bicycles during the spring months of that year.")

st.write("The relationship between temperature and the number of bicycle rentals, the warmer it gets, the more rentals there are. This statement suggests a positive correlation between temperature and bicycle rentals, indicating that as temperatures increase, the number of bike rentals also tends to rise. This relationship is often observed in various locations where warmer weather is associated with more favorable conditions for outdoor activities, including cycling. ")

# Show data source and description
st.sidebar.title("About Us")
st.sidebar.info("This dashboard contains a dataset of bike rentals from 2011 to 2012. This data is used to conduct analysis on the business questions that have been posed.")
