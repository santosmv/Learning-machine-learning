# To run the code: streamlit run app-dashboard.py

import streamlit as st
from datetime import datetime
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import investpy as ip

countries = ['united states']
# 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
intervals = ['1d', '1wk', '1mo']

start_date = datetime.today() - pd.to_timedelta(arg='30 days')
end_date = datetime.today()

@st.cache_data
def consulta_acao(stock, from_date, to_date, interval):
    df = yf.download(tickers=stock, start=formato_data(from_date), end=formato_data(to_date), interval=interval)
    return df

def formato_data(dt, format='%Y-%m-%d'):
    return dt.strftime(format)

def PlotCandle(df):
    data = [go.Candlestick(x=df.index,
                           open=df.Open,
                           close=df.Close,
                           high=df.High,
                           low=df.Low)]
    layout = go.Layout()
    fig = go.Figure(data=data, layout=layout)
    cs = fig.data[0]
    cs.increasing.fillcolor = '#3D9970'
    cs.increasing.line.color = '#3D9970'
    cs.decreasing.fillcolor = '#FF4136'
    cs.decreasing.line.color = '#FF4136'
    fig.update_layout(xaxis_rangeslider_visible=False)

    return fig

barra_lateral = st.sidebar.empty()
country_select = st.sidebar.selectbox('Selecione o país:', countries)
acoes = ip.get_stocks_list(country=country_select)
stock_select = st.sidebar.selectbox('Selecione o ativo:', acoes)

from_date = st.sidebar.date_input('De:', start_date)
to_date = st.sidebar.date_input('Até:', end_date)
interval_select = st.sidebar.selectbox('Selecione o intervalo:', intervals)

carregar_dados = st.sidebar.checkbox('Carregar dados')

st.title('Stock Monitor')
st.header('Ações')
st.subheader('Gráfico')

grafico_candle = st.empty()
grafico_line = st.empty()

if from_date > to_date:
    st.sidebar.error('Data de início maior que data final!')

else:
    df = consulta_acao(stock=stock_select, from_date=from_date, to_date=to_date, interval=interval_select)
    df.index = df.index.date
    df.index.name = 'Date'

    try:
        fig = PlotCandle(df)
        grafico_candle = st.plotly_chart(fig)
        grafico_line = st.line_chart(df.Close)

        if carregar_dados:
            st.subheader('Dados')
            dados = st.dataframe(df)
    except Exception as e:
        st.error(e)