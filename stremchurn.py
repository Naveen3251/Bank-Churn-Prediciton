'''CustomerId
Surname
CreditScore
Geography
Gender
Age
Tenure
Balance
NumOfProducts
HasCrCard
IsActiveMember
EstimatedSalary
Exited-->dependent
'''
import pickle as pk
import streamlit as st
model=pk.load(open('Churn.pkl','rb'))
st.title("BANK CHURN PREDICITON")
st.image('churn.jpg')
def run():
    #cusid
    id=st.text_input("Enter the Customer ID")
    #surn
    name=st.text_input("Enter SurName")
    #Credit score
    credit=st.number_input("Enter Credit Score",value=0)
    #Geography
    g=("France","Germany","Spain")
    op1=list(range(len(g)))
    geo=st.selectbox("Enter Geographical Area",op1,format_func=lambda x:g[x])
    #Gender
    ge=("Female","Male")
    op2=list(range(len(ge)))
    gender=st.selectbox("Enter Gender",op2,format_func=lambda x:ge[x])
    #age
    age=st.number_input("Enter Age",value=0)
    #tenure
    ten=st.number_input("Enter Tenure",value=0)
    #Balance
    bal=st.number_input("Enter the Balance")
    #num of prod
    product=st.number_input("Enter Number of Product",value=0)
    #hascard
    ca=("No","Yes")
    op3=list(range(len(ca)))
    has=st.selectbox("Has Credit Card",op3,format_func=lambda x:ca[x])
    #is active
    ac=("No","Yes")
    op4=list(range(len(ac)))
    active=st.selectbox("Is Active Number",op4,format_func=lambda x:ac[x])
    #estimated salary
    estimate=st.number_input("Enter Salary")
    if st.button("SUBMIT"):
        atri=[[credit,geo,gender,age,ten,bal,product,has,active,estimate]]
        prediction=model.predict(atri)
        lc=[str(i) for i in prediction]
        ans=int("".join(lc))
        if ans==0:
            st.balloons()
            st.success("The Customer "+name)
            st.success("ID: "+id)
            st.success("Not Leaving the Bank!!!")
        else:
            st.error("The Customer " + name)
            st.error("ID: " + id)
            st.error("Leaving the bank!!!")
run()