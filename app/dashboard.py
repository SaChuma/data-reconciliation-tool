import streamlit as st
import pandas as pd

from api import get_api_data
from db import get_db_data
from compare import compare_data


st.set_page_config(
    page_title="Data Reconciliation Dashboard",
    layout="wide"
)

st.title("📊 Data Reconciliation Dashboard")

api_data = get_api_data()
db_data = get_db_data()

results = compare_data(api_data, db_data)

df = pd.DataFrame(results)

st.subheader("Mismatch Summary")

st.metric("Total Mismatches Found", len(results))

st.subheader("Mismatch Details")

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.success("No mismatches found 🎉")