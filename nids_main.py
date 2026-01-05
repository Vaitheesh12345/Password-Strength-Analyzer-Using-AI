import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI NIDS",
    layout="wide",
    page_icon="🛡️"
)


st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.main {
    background-color: #0f172a;
}

h1 {
    color: #38bdf8;
    text-align: center;
}

h3 {
    color: #facc15;
}

.upload-box {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #38bdf8;
}

.success-box {
    background-color: #052e16;
    color: #86efac;
    padding: 15px;
    border-radius: 10px;
}

.info-box {
    background-color: #1e3a8a;
    color: #bfdbfe;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>🛡️ AI-based Network Intrusion Detection System</h1>", unsafe_allow_html=True)

st.markdown(
    "<h3>Upload Network Traffic Dataset (CSV)</h3>",
    unsafe_allow_html=True
)


st.markdown('<div class="upload-box">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

st.markdown('</div>', unsafe_allow_html=True)


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown(
        '<div class="success-box">✅ Dataset uploaded successfully</div>',
        unsafe_allow_html=True
    )

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    col1, col2 = st.columns(2)
    col1.metric("📄 Rows", df.shape[0])
    col2.metric("📌 Columns", df.shape[1])

else:
    st.markdown(
        '<div class="info-box">ℹ️ Please upload a CSV file to continue</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    "<center style='color:#94a3b8'>Cybersecurity with Generative AI – Academic Project</center>",
    unsafe_allow_html=True
)
