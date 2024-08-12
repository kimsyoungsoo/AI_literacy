import streamlit as st
import electric_car as ec  # electric_car.py 파일에 있는 함수를 불러오는 것
import pybasic  as pb
import food_main as fm

#로그인 화면
st.sidebar.title(">> 로그인")    #왼쪽 title 글자크기
user_id=st.sidebar.text_input("아이디(ID) 입력",value='abc',max_chars=10) #value 값이 저장
user_pw=st.sidebar.text_input('패스워드 입력',value='',type='password')  

if user_id == 'abc' and user_pw =='1234' :
   st.sidebar.title('>> 0soo의 포트폴리오')
  #st.image('data\mojiseuyangjang5.jpg')

   menu=st.sidebar.radio('메뉴선택',['파이썬기초','탐색적 분석 : 전기자동차 분석','머신러닝','파이썬기초 미니프로젝트'],index=None)
   st.sidebar.write(menu)

   if menu == '탐색적 분석 : 전기자동차 분석':
     ec.elec_exe()
   elif menu == "머신러닝" :
     st.header("공사중")    
   elif menu == '파이썬기초':  
     pb.basic()                #함수 불러오기
   elif menu == '파이썬기초 미니프로젝트': 
     fm.food_main()
  
                     