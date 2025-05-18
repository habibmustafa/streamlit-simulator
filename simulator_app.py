
import streamlit as st
import json
import requests

st.title("🚀 Hücum Trafiki Simulyatoru")
st.write("Aşağıdan hücum və ya normal trafik göndərə bilərsiniz.")

traffic_type = st.selectbox("Trafik Növü Seçin:", ["Normal", "Hücum"])
send = st.button("Trafiki Göndər")

if send:
    # Məlumat nümunəsi
    sample = {
        "Flow Duration": 2000000,
        "Total Fwd Packets": 15,
        "Total Backward Packets": 10,
        "Total Length of Fwd Packets": 1500,
        "Total Length of Bwd Packets": 1000,
        "Flow Bytes/s": 1250.0,
        "Flow Packets/s": 20.0,
        "Attack": 1 if traffic_type == "Hücum" else 0
    }

    # Online json store (demo məqsədilə)
    requests.post("https://json.extendsclass.com/bin/cyber-traffic", json=sample)
    st.success(f"{traffic_type} Trafiki Göndərildi!")
