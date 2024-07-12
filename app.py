import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('model.pkl', 'rb'))

def run():
    # img1 = Image.open('static\img.jpg')
    # img1 = img1.resize((156,145))
    # st.image(img1,use_column_width=False)
    st.title("Bank Loan Prediction using Machine Learning")

    ## Full Name
    fn = st.text_input('Full Name')
    
    ## Account No
    account_no = st.text_input('Account number (Loan ID)')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependents
    dep_display = (0,1,2,3,'3+')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Yes','No')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Self Employed",emp_options, format_func=lambda x: emp_display[x])
    
    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan Amount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## loan duration
    dur_display = [12,36,60,84,120,180,240,300,360,480]
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    ## For Credit History
    cred_display = (0,1)
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit History",cred_options, format_func=lambda x: cred_display[x])
    
    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

    if st.button("Submit"):
        duration=dur_display[dur]
        
        features = [[gen, mar, dep, edu, emp, mon_income+co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you will get the loan from Bank'
            )

run()
