import streamlit as st
from plotly import express as px
import weather_data

st.title("Weather Forecast App")
place = st.text_input(label = "Place", key="Place")
no_of_days =  st.slider(label = "Forecast Days", min_value=1, max_value=5)
datatype = st.selectbox(label="Select Data to View", options=["Sky", "Temperature"])

if place and datatype:
    st.subheader(f"{datatype} for next {no_of_days} days in {place}")
    date, temp, weather = weather_data.get_weather_data(place, no_of_days)
    temp = [x-273.15 for x in temp]
    fig = px.line(x = date, y = temp, labels={"x": "Date", "y": "Temp"})
    if datatype=="Temperature":
        st.plotly_chart(fig)
    else:
        curr_date = None
        icons = []
        captions = []
        for i, j in zip(weather, date):
            if curr_date == None:
                curr_date = j.date()
            if curr_date != j.date():
                st.write(f'<b><p style="text-align:center;">{curr_date.strftime("%a, %d %b")}</p></b>', unsafe_allow_html=True)
                st.image(icons, captions, width=100)
                curr_date = j.date()
                icons = []
                captions = []
            icon = i['icon']
            icons.append(f'https://openweathermap.org/img/wn/{icon}@2x.png')
            caption = f"**{j.strftime('%H : %M %p')}** {i['main'].title()}: {i['description'].title()}"
            captions.append(caption)
        st.write(f'<b><p style="text-align:center;">{curr_date.strftime("%a, %d %b")}</p></b>', unsafe_allow_html=True)
        st.image(icons, captions, width=100)