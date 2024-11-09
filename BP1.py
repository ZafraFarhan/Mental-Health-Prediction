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

st.title("Bipolar Type I")


# Create buttons for each page
Factors_button = st.sidebar.button("Risk Factors")
Symptoms_button = st.sidebar.button("Symptoms")
Treatment_button = st.sidebar.button("Treatment")
Prevention_button = st.sidebar.button("Prevention")


# Initialize content display

if Factors_button:
    st.subheader("Bipolar I Risk Factors")
    st.write("""
        Virtually anyone can have bipolar I disorder. About 2.5% of the U.S. population has some form of bipolar disorder – nearly 6 million people.

        Most people are in their teens or early 20s when symptoms of bipolar disorder first start. Nearly everyone with bipolar II disorder gets it before age 50. 
             People with an immediate family member who has bipolar are at higher risk.
             """)
elif Symptoms_button:
    st.subheader("Bipolar I Symptoms")
    st.write("""
        During a manic episode in someone with bipolar disorder, the elevated mood can manifest as either euphoria (feeling "high") or irritability.

        ### Abnormal behavior during manic episodes includes:
        - **Flying suddenly from one idea to the next**
        - **Rapid, "pressured" (uninterruptible), and loud speech**
        - **Increased energy** with hyperactivity and a decreased need for sleep
        - **Inflated self-image** or grandiosity
        - **Excessive spending** far beyond one's means
        - **Hypersexuality** and risky behaviors
        - **Substance abuse**
             
        People in manic episodes may spend money far beyond their means, have sex with people they wouldn't otherwise, or pursue grandiose, unrealistic plans. In severe manic episodes, a person loses touch with reality. They may become delusional and behave bizarrely.

        Untreated, an episode of mania can last anywhere from a few days to several months. Most commonly, symptoms continue for a few weeks to a few months. Depression may follow shortly after, or not appear for weeks or months.

        Many people with bipolar I disorder experience long periods without symptoms in between episodes. A minority has rapid-cycling symptoms of mania and depression, in which they may have distinct periods of mania or depression four or more times within a year. People can also have mood episodes with "mixed features," in which manic and depressive symptoms occur simultaneously, or may alternate from one pole to the other within the same day.

        Depressive episodes in bipolar disorder are similar to "regular" clinical depression, with depressed mood, loss of pleasure, low energy and activity, feelings of guilt or worthlessness, and thoughts of suicide. Depressive symptoms of bipolar disorder can last weeks or months, but rarely longer than one year.
        
    """)
    
elif Treatment_button:
    st.subheader("Bipolar I Treatment")
    st.write("""
        Manic episodes in bipolar I disorder require treatment with drugs, such as mood stabilizers and antipsychotics, and sometimes sedative-hypnotics which include benzodiazepines such as clonazepam (Klonopin) or lorazepam (Ativan).
        People with bipolar II disorder benefit from preventive drugs that help level out moods long term. These medications prevent the negative consequences of hypomania and also help prevent depressive episodes.

        **Mood Stabilizers:**
        Lithium (Eskalith, Lithobid): This simple metal in pill form is especially effective at controlling mania that involves classical euphoria rather than mixtures of mania and depression simultaneously. Lithium has been used for more than 60 years to treat bipolar disorder. Lithium can take weeks to work fully, making it better for maintenance treatment than for sudden manic episodes. Blood levels of lithium as well as tests to measure kidney and thyroid functioning must be monitored to avoid side effects.

        Valproate (Depakote): This antiseizure medication also works to level out moods. It is faster acting than lithium for an acute episode of mania. It is also often used "off label" for prevention of new episodes. As a mood stabilizer that can be used by a "loading dose" method -- beginning at a very high dose -- valproate allows the possibility of significant improvement in mood as early as four to five days.

        Some other anti-seizure drugs, notably carbamazepine (Tegretol) and lamotrigine (Lamictal), can have value in treating or preventing manias or depressions. Other antiseizure medicines that are less well-established but still sometimes used experimentally for the treatment of bipolar disorder, such as oxcarbazepine (Trileptal). 
       
        **Antipsychotics:**          
        For severe manic episodes, traditional antipsychotics (such as Haldol, Loxapine, or Thorazine) as well as newer antipsychotic drugs -- also called atypical antipsychotics -- may be necessary. Cariprazine (Vraylar) is a newly approved antipsychotic to treat manic or mixed episodes. Aripiprazole (Abilify), asenapine (Saphris), clozapine (Clozaril), lumateperone (Caplyta), olanzapine (Zyprexa), quetiapine (Seroquel), risperidone (Risperdal), and ziprasidone (Geodon) are often used, and many other drugs are available. The antipsychotic lurasidone (Latuda) is approved for use -- either alone or with lithium or valproate (Depakote) -- in cases of bipolar I depression. Antipsychotic medicines are also sometimes used for preventive treatment.

        **Benzodiazepines:**
        This class of drugs, referred to as minor tranquilizers, includes alprazolam (Xanax), diazepam (Valium), and lorazepam (Ativan). They are sometimes used for short-term control of acute symptoms associated with mania such as agitation or insomnia, but they do not treat core mood symptoms such as euphoria or depression. They can also become habit-forming so need to be closely monitored.

        **Antidepressants:**
        Common antidepressants such as fluoxetine (Prozac), paroxetine (Paxil), and sertraline (Zoloft) have not been shown to be as effective for treating depression in bipolar I disorder as in unipolar depression. In a small percentage of people, they can also set off or worsen a manic episode in a person with bipolar disorder. However, studies have shown that for bipolar II depression, some antidepressants (such as Prozac and Zoloft) may be safe and more helpful than in bipolar I depression. For these reasons, the first-line treatments for depression in bipolar disorder involve medicines that have been shown to have antidepressant properties but also no known risk for causing or worsening mania. The five FDA-approved treatments for bipolar depression are lumateperone (Caplyta), lurasidone (Latuda), olanzapine-fluoxetine (Symbyax) combination, quetiapine (Seroquel) or quetiapine fumarate (Seroquel XR), and cariprazine (Vraylar). Other mood-stabilizing treatments that are sometimes recommended for treating acute bipolar depression include lithium, Depakote, and  lamotrigine (Lamictal) (although none of these latter three medicines is FDA-approved specifically for bipolar depression). If these fail, after a few weeks a traditional antidepressant or other medicine may sometimes be added. Psychotherapy, such as cognitive-behavioral therapy, may also help.

        People with bipolar I disorder (mania or depression) have a high risk for recurrences and usually are advised to take medicines on a continuous basis for prevention.

    """)
elif Prevention_button:
    st.subheader("Bipolar I Prevention")
    st.write("""
        The causes of bipolar disorder are not well understood. It's not known if bipolar I disorder can be prevented entirely.

        It is possible to lower the risk of episodes of mania or depression once bipolar disorder has developed. Regular therapy sessions with a psychologist or social worker can help people to identify factors that can destabilize mood (such as poor medication adherence, sleep deprivation, drug or alcohol abuse, and poor stress management), leading to fewer hospitalizations and feeling better overall. Taking medicine on a regular basis can help to prevent future manic or depressive episodes.
    """)
else:
    
    st.write("""
        **Bipolar I disorder** (pronounced "bipolar one") and also known as manic-depressive disorder or manic depression) is a form of mental illness. A person affected by bipolar I disorder has had at least one manic episode in their life. A manic episode is a 
             period of abnormally elevated or irritable mood and high energy, accompanied by abnormal behavior that disrupts life.

        Most people with bipolar I disorder also suffer from episodes of depression. Often, there is a pattern of cycling between mania and depression. This is where the term "manic depression" comes from. In between episodes of mania and depression, many people with 
             bipolar I disorder can live normal lives.
    """)