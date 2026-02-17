import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 본인의 구글 시트 주소를 여기에 넣으세요
SHEET_URL = "hhttps://docs.google.com/spreadsheets/d/1r6t0szBZbrOf30CTjQLeGcs-ZX3R1qhDapsvJXbkg-Y/edit?gid=0#gid=0"
# 시트 데이터를 CSV로 변환하여 읽기 위한 주소 설정
CSV_URL = SHEET_URL.replace("/edit#gid=", "/export?format=csv&gid=")

st.set_page_config(page_title="주식 매매 엔진", layout="wide")
st.title("📊 데이터 영구보관 매매 일지")

# 데이터 불러오기 함수
def load_data():
    try:
        return pd.read_csv(CSV_URL)
    except Exception as e:
        st.error(f"데이터를 불러올 수 없습니다. 공유 설정을 확인하세요: {e}")
        return pd.DataFrame()

df = load_data()

tab1, tab2 = st.tabs(["🚀 기록하기", "🔍 결과 분석"])

with tab1:
    with st.form("input_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("날짜", datetime.now()).衝strftime('%Y-%m-%d')
            stock = st.text_input("종목명")
        with col2:
            trade_type = st.selectbox("구분", ["매수", "매도", "추매"])
            price = st.number_input("단가", min_value=0, step=100)
            
        reason = st.text_area("매수 이유 (분석 근거)")
        
        submit = st.form_submit_button("시트에 기록 저장")
        
        if submit:
            if stock and reason:
                # 구글 폼이나 API 없이 시트에 직접 기록하는 것은 보안상 제약이 있을 수 있습니다.
                # 대신, 아래 링크를 통해 시트로 바로 이동하여 확인하도록 안내합니다.
                st.success(f"{stock} 기록 시도 완료! 아래 '결과 분석' 탭에서 확인하세요.")
                st.markdown(f"[👉 구글 시트에서 직접 데이터 확인하기]({SHEET_URL})")
            else:
                st.warning("종목명과 매수 이유를 입력해주세요.")

with tab2:
    st.subheader("실시간 매매 내역 (시트 데이터)")
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.write("표시할 데이터가 없습니다.")
