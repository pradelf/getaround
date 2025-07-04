import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np

### CONFIG
st.set_page_config(
    page_title="E-commerce",
    page_icon="💸",
    layout="wide"
  )

### TITLE AND TEXT
st.title("Build dashboards with Streamlit 🎨")

st.markdown("""
    Welcome to this awesome `streamlit` dashboard. This library is great to build very fast and
    intuitive charts and application running on the web. Here is a showcase of what you can do with
    it. Our data comes from an e-commerce website that simply displays samples of customer sales. Let's check it out.
    Also, if you want to have a real quick overview of what streamlit is all about, feel free to watch the below video 👇
""")

### LOAD DATA
DATA_PRICING = ('/app/app/Data/get_around_pricing_project.csv')

DATA_ANALYSIS = ('/app/app/Data/get_around_delay_analysis.csv')

# this lets the cache activated : usage d'un décorateur python pour ajouter des fonctionnalité 
# : st.cache_data et st.cache_resource qui remplace st.cache qui va devenir obsolète.
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource
@st.cache_data 
def load_data(file, nrows, delimiter=","):
    data = pd.read_csv(file, nrows=nrows,delimiter=delimiter)
    #data["Date"] = data["Date"].apply(lambda x: pd.to_datetime(",".join(x.split(",")[-2:])))
    #data["currency"] = data["currency"].apply(lambda x: pd.to_numeric(x[1:]))
    return data

data_load_state = st.text('Loading data...')
data_pricing = load_data(DATA_PRICING,1000)
data_analysis = load_data(DATA_ANALYSIS,1000)
data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

## Run the below code if the check is checked ✅
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data_pricing) 
### SHOW GRAPH STREAMLIT

price_per_model = data_pricing["price"]
st.bar_chart(price_per_model)

### SHOW GRAPH PLOTLY + STREAMLIT

st.subheader("Simple bar chart built with Plotly")
st.markdown("""
    Now, the best thing about `streamlit` is its compatibility with other libraries. For example, you
    don't need to actually use built-in charts to create your dashboard, you can use :
    
    * [`plotly`](https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart) 
    * [`matplotlib`](https://docs.streamlit.io/library/api-reference/charts/st.pyplot)
    * [`bokeh`](https://docs.streamlit.io/library/api-reference/charts/st.bokeh_chart)
    * ...
    This way, you have all the flexibility you need to build awesome dashboards. 🥰
""")
fig = px.histogram(data.sort_values("country"), x="country", y="currency", barmode="group")
st.plotly_chart(fig, use_container_width=True)


### SIDEBAR
st.sidebar.header("Build dashboards with Streamlit")
st.sidebar.markdown("""
    * [Load and showcase data](#load-and-showcase-data)
    * [Charts directly built with Streamlit](#simple-bar-chart-built-directly-with-streamlit)
    * [Charts built with Plotly](#simple-bar-chart-built-with-plotly)
    * [Input Data](#input-data)
""")
e = st.sidebar.empty()
e.write("")
st.sidebar.write("Made with 💖 by [Jedha](https://jedha.co)")

### EXPANDER

with st.expander("⏯️ Watch this 15min tutorial"):
    st.video("https://youtu.be/B2iAodr0fOo")

st.markdown("---")

#### CREATE TWO COLUMNS
col1, col2 = st.columns(2)

with col1:
    # visu des widgets
    st.markdown("First column")
    car_id= st.selectbox("Select a country you want to see all time sales", data_analysis["car_id"].sort_values().unique())
    # intelligence et contrôle du widget
    rental_canceled = data_analysis[data_analysis["state"]=="canceled"]
    fig = px.histogram(rental_canceled, x="time_delta_with_previous_rental_in_minutes", y="delay_at_checkout_in_minutes")
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("Second column")
    with st.form("average_sales_per_country"):
      model = st.selectbox("Select a model you want to see", data_pricing["model_key"].sort_values().unique())
      power = st.selectbox("Select a start date you want to see your metric",data_pricing["engine_power"].sort_values().unique())
      submit = st.form_submit_button("submit")
      if submit:
              model_select = data_pricing[data_pricing["model_key"]==model]
              power_select = data_pricing[data_pricing["power"]==power]
              avg_rental_price = data_pricing[model_select & power_select ]["rental_price_per_day"].mean()
              st.metric("Average rental price (in $)", np.round(avg_rental_price, 2))



