import streamlit as st
import pandas as pd
from datetime import datetime

# 구글 시트 주소 (공유 링크 붙여넣기)
# 예: https://docs.google.com/spreadsheets/d/시트ID/edit?usp=sharing
SHEET_URL = "https://docs.google.com/spreadsheets/d/1r6t0szBZbrOf30CTjQLeGcs-ZX3R1qhDapsvJXbkg-Y/edit?gid=0#gid=0"
CSV_URL = SHEET_URL.replace("/edit?usp=sharing", "/export?format=csv")

st.set_page_config(page_title="주식 매매 엔진", layout="wide")
st.title("📊 데이터 영구보관 매매 일지")

# 데이터 불러오기 함수
def load_data():
    try:
        return pd.read_csv(CSV_URL)
    except:
        st.error("구글 시트 연결 실패. 주소와 공유 권한을 확인하세요.")
        return pd.DataFrame()

df = load_data()

tab1, tab2 = st.tabs(["🚀 기록하기", "🔍 결과 분석"])

with tab1:
    with st.form("input_form"):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input("날짜", datetime.now())
            stock = st.text_input("종목명")
        with col2:
            trade_type = st.selectbox("구분", ["매수", "매도", "추매"])
            price = st.number_input("단가", step=100)
            
        reason = st.text_area("매수 이유 (분석 근거)", placeholder="예: 248,000원 지지 후 반등 기대")
        
        if st.form_submit_button("시트에 기록 저장"):
            # 구글 시트 연동 앱은 배포 후 'st.write' 대신 구글 API를 사용하거나 
            # 단순히 시트를 웹 게시하여 데이터를 확인하는 용도로 쓰기 좋습니다.
            st.info("데이터 저장을 위해 구글 시트 앱이나 웹에서 직접 입력하는 것이 모바일에서 가장 안정적입니다.")

with tab2:
    st.subheader("매매 내역 분석")
    st.dataframe(df, use_container_width=True)