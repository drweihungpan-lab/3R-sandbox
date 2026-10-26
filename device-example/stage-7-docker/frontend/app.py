"""One-page Streamlit app: show each device's predicted limit date."""

import os

import requests
import streamlit as st

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

st.title("When does each device reach its usage limit?")

try:
    response = requests.get(f"{BACKEND_URL}/limits", timeout=10)
    response.raise_for_status()
except requests.RequestException as error:
    st.error(f"Could not reach the API at {BACKEND_URL}: {error}")
    st.stop()

body = response.json()
st.caption(f"Usage limit: {body['limit']:,} measurements per device (synthetic data).")
st.table(
    [
        {"Device": device["device_id"], "Reaches its limit on": device["limit_date"]}
        for device in body["devices"]
    ]
)
