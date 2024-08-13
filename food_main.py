 # Main
import streamlit as st
import k_food as kf
import fast_food as ff
import bunsik as bs

def food_main():
        st.write("추천 맛집 종류예요: ")
        menu_number = st.radio("음식추천", ["한식","패스트푸드","분식"],index=None)
        if menu_number == '한식':
            st.write("\"한식\"을 선택하셨네요!")
            kf.k_food()
        #   if not kf.k_food():            
        #      st.write("다시 선택해 주세요")
        #   else:
        elif menu_number == '패스트푸드':
            st.write("\"패스트푸드\"를 선택하셨네요!")
            ff.fast_food()
        #  if not ff.fast_food():
        #     st.write("다시 선택해 주세요")
        #   else:
        elif menu_number == '분식':
            st.write("\"분식\"을 선택하셨네요!")
            bs.bunsik()
         # if not bs.bunsik():
         #   st.write("다시 선택해 주세요")
             
