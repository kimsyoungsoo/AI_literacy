import streamlit as st
def bunsik(): 			# 분식함수 정의
    bunsik = [
        {
            "name": "김밥 천국",
            "menu": ["참치 김밥", "치즈 라볶이", "돈가스"],
            "price": [4500, 6500, 9000],
            "url": "https://maps.app.goo.gl/rr3GHDsZ1wz48MPd8"
        },
        {
            "name": "감탄 떡볶이",
            "menu": ["감탄 떡볶이 1인분", "순대 1인분", "튀김 5개"],
            "price": [3000, 4000, 4500],
            "url": "https://maps.app.goo.gl/JB94c1aV1a241obs9"
        },
        {
            "name": "이삭 토스트",
            "menu": ["햄치즈 토스트", "베이컨 베스트 토스트", "딥치즈 베이컨 토스트"],
            "price": [2900, 3900, 4600],
            "url": "https://maps.app.goo.gl/XafnhESs594QeuBf8"
        }
    ]

    while True:
        money = int(st.number_input("예산은 얼마인가요? "))
        kk = []
        available = False					        # available은 예산에 맞는 메뉴를 찾았는지를 추적하는 설정

        for i in range(len(bunsik)):
            rprice = bunsik[i]['price']		# 각 분식점의 메뉴 가격 읽어 리스트 만들기
            for k in range(len(rprice)):
                if money >= rprice[k]:		# 예산과 메뉴 가격을 비교해서 예산에 맞는 메뉴 리스트 만들기
                    kk.append((rprice[k], bunsik[i]['menu'][k], bunsik[i]['name'], bunsik[i]['url']))

        if kk:
            kk.sort(key=lambda x: x[0])		# 예산에 맞는 메뉴를 가격의 올림차순으로 정렬
            st.write("예산에 맞는 메뉴예요:")
            st.writet("*"*75)
            for item in kk:					      # 예산에 맞는 메뉴를 ‘가격, 메뉴 이름, 음식점 이름, 주소’ 내용으로
                print(f"{item[0]} \"{item[1]}\" {item[2]} {item[3]}")
            st.writet("*"*75)
            available = True              # 예산에 맞는 메뉴를 찾았음을 표시

        if available:
            return True  					        # 예산에 맞는 메뉴를 찾으면 True값으로 반복문 빠져나감
        else:
            st.write("예산에 맞는 메뉴가 없어요")	# 예산에 맞는 메뉴가 없으면 False값으로 메인화면 선택으로 되돌아감
            return False