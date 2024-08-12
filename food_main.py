 # Main
import streamlit as st
import k_food as kf
import fast_food as ff
import bunsik as bs

def food_main():
    while True:
        st.write("추천 맛집 종류예요: ")
        # st.write("*"*30)
        # st.write("1. 한식")
        # st.write("2. 패스트푸드")
        # st.write("3. 분식")
        # st.write("*"*30)

       #menu_number = st.number_input("번호를 입력하세요: ",value=0)
        menu_number = st.radio("음식추천", ["한식","패스트푸드","분식"],index=None)
        if menu_number == '한식':
            st.write("\"한식\"을 선택하셨네요!")
            if not kf.k_food():             # 예산에 맞는 메뉴가 없을 경우 앞 모듈의 False값을 받아
                st.write("다시 선택해 주세요")
            else:
                 break                       # 예산에 맞는 메뉴를 찾았으므로 반복문 중지
        elif menu_number == '패스트푸드':
            st.write("\"패스트푸드\"를 선택하셨네요!")
            if not ff.fast_food():
                st.write("다시 선택해 주세요")
            else:
                break
        elif menu_number == '분식':
            st.write("\"분식\"을 선택하셨네요!")
            if not bs.bunsik():
             st.write("다시 선택해 주세요")
            else:
               break
        else:
            st.write("잘못 입력하셨어요! 다시 선택해 주세요") 