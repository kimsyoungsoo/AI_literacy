import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import csv
import streamlit as st


def indata():
    fields = ['id','model','year','transmission','mileage','fuelType','tax','mpg','engineSize']
    data ={}

    # 데이터 입력
    for i in fields:
        #value = input(f'{i} : ')
        value = st.text_input(f'{i} : ')
        data[i] = value

    filename = 'used_car_x_test1.csv'
    with open(filename,'w',newline='') as f:     
        w = csv.DictWriter(f,fieldnames=fields)
        w.writeheader()   #열 제목을 파일에 작성7469
        w.writerow(data)

    return filename    

def model(filename):
#데이터 불러오기=========================================================
    df_X_train = pd.read_csv('aidata/used_car_x_train.csv')
    #df_X_test = pd.read_csv('data/used_car_x_test.csv')
    df_X_test = pd.read_csv(filename)
    df_y_train = pd.read_csv('aidata/used_car_y_train.csv')

    #전처리================================================================
    # 1. 범주형, 숫자형 데이터로 분리
    #범주형 데이터 만 불러오기(원핫인코딩)
    df_X_train['model'] = df_X_train['model'].str.replace(" ","") #공백 없애기 str.replace
    X_train_wold = df_X_train[['model','transmission','fuelType']]
    X_test_wold = df_X_test[['model','transmission','fuelType']]

    #수치형 데이터 (스케일링)       axis 열을지우는것
    X_train_num = df_X_train.drop(['id','model','transmission','fuelType'],axis=1)
    X_test_num = df_X_test.drop(['id','model','transmission','fuelType'],axis=1)


    #2. 데이터 스케일링(수치형데이터,표준화)
    # 개체생성
    scaler = MinMaxScaler()
    # 학습
    X_train_num_scale = scaler.fit_transform(X_train_num)  # fit 적용 다한다
    X_test_num_scale = scaler.transform(X_test_num)   #fit 시키지 않고 적용만 한다

    # 데이터프레임 설정
    df_train_num = pd.DataFrame(X_train_num_scale, columns=X_train_num.columns)
    df_test_num = pd.DataFrame(X_test_num_scale, columns= X_test_num.columns)

    #3. 원핫 인코딩(범주형데이터->숫자)  
    df_train_word = pd.get_dummies(X_train_wold)
    df_test_word = pd.get_dummies(X_test_wold)


    # 원핫인 코딩 후에 훈련데이터랑 테스트 데이터 열(칼럼) 체크

    # 훈련 데이터 목록
    train_cols= set(df_train_word.columns)   # set - 연산이 된다,집합으로 만들어 진다, {},키값없는 딕셔너리

    # 테스트 데이터 목록
    test_cols= set(df_test_word.columns)

    missing_test = train_cols-test_cols    # train_cols에만 있는것
    missing_train = test_cols-train_cols

    if len(missing_test) > 0 : # 길이(len)    #
        for i in missing_test :
            df_test_word[i] = 0

    if len(missing_train) > 0 : # 길이(len)
        for i in missing_train :
            df_train_word[i] = 0     


    #4. 수치형 데이터, 범주형 데이터 병합
    df_train = pd.concat([df_train_num,df_train_word],axis=1)
    df_test = pd.concat([df_test_num,df_test_word],axis=1)        

    # 모델링=====================================================================
    # 머신러닝- 지도학습
    #1. 독립변수(X), 종속변수(y)
    X= df_train
    y= df_y_train['price']

    #2. 훈련데이터 7:3으로 나누기
    X_train, X_val, y_train, y_val = train_test_split(X,y,test_size=0.3, random_state=0)

    #3. 회귀예측 모델 생성 및 학습
    # 3-1. 모델 개체 생성
    RForest_model = RandomForestRegressor(random_state=0)

    # 3-2. 학습
    RForest_model.fit(X_train, y_train)

    # 3-3. 평가- score (테스트독립변수, 테스트종속변수)
    st.write("R2 score:", RForest_model.score(X_train, y_train))

    #      평가 - RMSE
    x_predict = RForest_model.predict(X_val)
    st.write('RandomForestRegressor:', root_mean_squared_error(y_val,x_predict))  #예측값

    #활용=================================
    #print(X_train.columns)  #train 데이터와 test 데이터 칼럼이 다를때 train 칼럼즈만 불러와
    df_test= df_test[['year', 'mileage', 'tax', 'mpg', 'engineSize', 'model_A1', 'model_A2',
        'model_A3', 'model_A4', 'model_A5', 'model_A6', 'model_A7',        
        'model_A8', 'model_Q2', 'model_Q3', 'model_Q5', 'model_Q7',        
        'model_Q8', 'model_R8', 'model_RS3', 'model_RS4', 'model_RS5',     
        'model_RS6', 'model_RS7', 'model_S3', 'model_S4', 'model_S5',      
        'model_S8', 'model_SQ5', 'model_SQ7', 'model_TT',
        'transmission_Automatic', 'transmission_Manual',
        'transmission_Semi-Auto', 'fuelType_Diesel', 'fuelType_Hybrid', 'fuelType_Petrol']]
    
    y_predict = RForest_model.predict(df_test)  #가격만
    #df_result = pd.DataFrame(df_X_test['id'],columns=['id'])
    #print(y_predict)
    #df_result['price'] = y_predict
    #print(df_result)
    #파일로 만들기
    #df_result.to_csv('car_precidct_result.csv')
    st.write(f'예상 가격은 : {y_predict[0]} 입니다' )

def aiml_main():
    filename = indata()   #호출-예측한 filename을 받아서 indata에 넣어 model 넣기
    if st.button("예측")==True:     # if st.button("예측")==True:
       model(filename)     

if __name__=='__main__':
    aiml_main()
    #indata()
