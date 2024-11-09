import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the page config
st.set_page_config(page_title="Bipolar Type-1", layout="wide")

st.markdown("""
    <head>
        <meta charset="UTF-8">
        <title>All Navigation Menu Hover Animation | CodingLab</title> 
        <style>
            [data-testid=stSidebar] {
                background-color: #000000;
            }
            body {
                background-color: #2E2E2E;  /* Black background color */
                
            }
            .stApp {
                background-color: #2E2E2E;  /* Set background to black for the app */
                
            }
            h1, h2, h3, h4, h5, h6, p, li, a {
                color: #ffffff;  /* Set font color to white for all text elements */
            }


            .stButton button {
                background-color: #FF7F27;
                color: #ffffff !important;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                width: 100%;
            }
                
        </style>
    </head>
    """, unsafe_allow_html=True)

st.title("Depression")


# Create buttons for each page
Factors_button = st.sidebar.button("Types")
Symptoms_button = st.sidebar.button("Symptoms")
Treatment_button = st.sidebar.button("Treatment")
Prevention_button = st.sidebar.button("Prevention")


# Initialize content display

if Factors_button:
    st.subheader("Depression Types")
    st.write("""
        The American Psychiatric Association’s Diagnostic Statistical Manual of Mental Disorders, Fifth Edition (DSM-5) classifies depressive disorders as the following:

        - **Clinical depression (major depressive disorder):** A diagnosis of major depressive disorder means you’ve felt sad, low or worthless most days for at least two weeks while also having other symptoms such as sleep problems, loss of interest in activities or change in appetite. This is the most severe form of depression and one of the most common forms.
        
        - **Persistent depressive disorder (PDD):** Persistent depressive disorder is mild or moderate depression that lasts for at least two years. The symptoms are less severe than major depressive disorder. Healthcare providers used to call PDD dysthymia.
        
        - **Disruptive mood dysregulation disorder (DMDD):** DMDD causes chronic, intense irritability and frequent anger outbursts in children. Symptoms usually begin by the age of 10.
        
        - **Premenstrual dysphoric disorder (PMDD):** With PMDD, you have premenstrual syndrome (PMS) symptoms along with mood symptoms, such as extreme irritability, anxiety or depression. These symptoms improve within a few days after your period starts, but they can be severe enough to interfere with your life.
        
        - **Depressive disorder due to another medical condition:** Many medical conditions can create changes in your body that cause depression. Examples include hypothyroidism, heart disease, Parkinson’s disease and cancer. If you’re able to treat the underlying condition, the depression usually improves as well.

        There are also specific forms of major depressive disorder, including:

        - **Seasonal affective disorder (seasonal depression):** This is a form of major depressive disorder that typically arises during the fall and winter and goes away during the spring and summer.
        
        - **Prenatal depression and postpartum depression:** Prenatal depression is depression that happens during pregnancy. Postpartum depression is depression that develops within four weeks of delivering a baby. The DSM refers to these as “major depressive disorder (MDD) with peripartum onset.”
        
        - **Atypical depression:** Symptoms of this condition, also known as major depressive disorder with atypical features, vary slightly from “typical” depression. The main difference is a temporary mood improvement in response to positive events (mood reactivity). Other key symptoms include increased appetite and rejection sensitivity.
        
             People with bipolar disorder also experience episodes of depression in addition to manic or hypomanic episodes.
                    """)
elif Symptoms_button:
    st.subheader("Depression Symptoms")
    st.write("""
        The symptoms of depression can vary slightly depending on the type and can range from mild to severe. In general, symptoms include:

        - **Feeling very sad, hopeless or worried. Children and adolescents with depression may be irritable rather than sad.**
        
        - **Not enjoying things that used to bring joy.**
        
        - **Being easily irritated or frustrated.**
        
        - **Eating too much or too little, which may result in weight gain or weight loss.**
        
        - **Trouble sleeping (insomnia) or sleeping too much (hypersomnia).**
        
        - **Having low energy or fatigue.**
        
        - **Having a difficult time concentrating, making decisions or remembering things.**
        
        - **Experiencing physical issues like headache, stomachache or sexual dysfunction.**
        
        - **Having thoughts of self-harm or suicide.**
    """)
    
elif Treatment_button:
    st.subheader("Depression Treatment")
    st.write("""
        Depression is one of the most treatable mental health conditions. Approximately 80% to 90% of people with depression who seek treatment eventually respond well to treatment.

        Treatment options include:

        - **Psychotherapy:** Psychotherapy (talk therapy) involves talking with a mental health professional. Your therapist helps you identify and change unhealthy emotions, thoughts and behaviors. There are many types of psychotherapy — cognitive behavioral therapy (CBT) is the most common. Sometimes, brief therapy is all you need. Other people continue therapy for several months or years.
        
        - **Medication:** Prescription medicine called antidepressants can help change the brain chemistry that causes depression. There are several different types of antidepressants, and it may take time to figure out the one that’s best for you. Some antidepressants have side effects, which often improve with time. If they don’t, talk to your healthcare provider. A different medication may work better for you.
        
        - **Complementary medicine:** This involves treatments you may receive along with traditional Western medicine. People with mild depression or ongoing symptoms can improve their well-being with therapies such as acupuncture, massage, hypnosis and biofeedback.
        
        - **Brain stimulation therapy:** Brain stimulation therapy can help people who have severe depression or depression with psychosis. Types of brain stimulation therapy include electroconvulsive therapy (ECT), transcranial magnetic stimulation (TMS) and vagus nerve stimulation (VNS).
        
        
        There are also things you can do at home to help improve depression symptoms, including:

        - Getting regular exercise.
        - Getting quality sleep (not too little or too much).
        - Eating a healthy diet.
        - Avoiding alcohol, which is a depressant.
        - Spending time with people you care about.
    """)
elif Prevention_button:
    st.subheader("Depression Prevention")
    st.write("""
        You can’t always prevent depression, but you can help reduce your risk by:

        - Maintaining a healthy sleep routine.

        - Managing stress with healthy coping mechanisms.

        - Practicing regular self-care activities such as exercise, meditation and yoga.

        If you’ve had depression before, you may be more likely to experience it again. If you have depression symptoms, get help as soon as possible.
    """)
else:
    
    st.write("""
        Depression is a **mood disorder** that causes a persistent feeling of sadness and loss of interest in things and activities you once enjoyed. It can also cause difficulty with thinking, memory, eating and sleeping.
             
        It’s normal to feel sad about or grieve over difficult life situations, such as losing your job or a divorce. But depression is different in that it persists practically every day for at least two weeks and involves other symptoms than sadness alone.

        There are several types of depressive disorders. Clinical depression, or major depressive disorder, is often just called “depression.” It’s the most severe type of depression.

        Without treatment, depression can get worse and last longer. In severe cases, it can lead to self-harm or death by suicide. The good news is that treatments can be very effective in improving symptoms.


    """)