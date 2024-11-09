import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the page config
st.set_page_config(page_title="Bipolar Type-2", layout="wide")

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

st.title("Bipolar Type II")


# Create buttons for each page
Factors_button = st.sidebar.button("Risk Factors")
Symptoms_button = st.sidebar.button("Symptoms")
Treatment_button = st.sidebar.button("Treatment")
Prevention_button = st.sidebar.button("Prevention")


# Initialize content display

if Factors_button:
    st.subheader("Bipolar II Risk Factors")
    st.write("""
        Virtually anyone can have bipolar II disorder. About 2.5% of the U.S. population has some form of bipolar disorder – nearly 6 million people.

        Most people are in their teens or early 20s when symptoms of bipolar disorder first start. Nearly everyone with bipolar II disorder gets it before age 50. 
             People with an immediate family member who has bipolar are at higher risk.
             """)
elif Symptoms_button:
    st.subheader("Bipolar II Symptoms")
    st.write("""
        **Bipolar II disorder** is a mental illness where a person experiences mood swings between hypomanic and depressive episodes. During a hypomanic episode, a higher mood can show up as either euphoria (feeling "high") or crankiness.
        
        **Symptoms of hypomanic episodes include:**
        - Flying suddenly from one idea to the next
        - Having exaggerated self-confidence
        - Rapid, "pressured" (uninterruptible) and loud speech
        - Increased energy, hyperactivity, and less need for sleep
        
        People in hypomanic episodes are often very pleasant to be around. They can seem like the "life of the party", making jokes, taking an intense interest in other people, and infecting others with their positive mood.

        **What's so bad about hypomania?**
        - While hypomania can seem enjoyable, it can also lead to erratic and unhealthy behaviors. Hypomanic episodes can sometimes progress to full mania, as seen in **bipolar I disorder**. In mania, individuals may engage in impulsive or risky behaviors with dangerous consequences.

        Most people with bipolar II disorder experience depressive symptoms more frequently than hypomanic ones. Depression can occur soon after hypomania subsides, or much later. Some people cycle back and forth between hypomania and depression, while others experience long periods of normal mood in between.

        **Untreated hypomania** can last anywhere from a few days to several months. The symptoms most commonly continue for a few weeks to a few months.

        **Depressive episodes in bipolar II disorder** are similar to clinical depression, with symptoms including:
        - Depressed mood
        - Loss of pleasure or interest
        - Low energy and activity levels
        - Feelings of guilt or worthlessness
        - Thoughts of suicide

        These depressive symptoms can last weeks, months, or even years in rare cases.
    """)
    
elif Treatment_button:
    st.subheader("Bipolar II Treatment")
    st.write("""
        

        Hypomania in bipolar II disorder often seems like happiness and relentless optimism. When hypomania doesn't cause unhealthy behavior, it often goes unnoticed, remaining untreated. In contrast, full mania requires treatment, often involving medications or hospitalizations.

        People with bipolar II disorder benefit from preventive drugs that help level out moods long term. These medications prevent the negative consequences of hypomania and also help prevent depressive episodes.

        **Mood Stabilizers:**
        - **Lithium (Eskalith, Lithobid):** A widely used treatment for bipolar disorder, effective at controlling mood swings, particularly the highs. It requires regular monitoring of blood and organ function.
        - **Carbamazepine (Tegretol):** An anti-seizure medication that is helpful in treating mania but less well-established for bipolar depression.
        - **Lamotrigine (Lamictal):** FDA-approved for maintaining bipolar disorder treatment and particularly effective in preventing depressive episodes.
        - **Valproate (Depakote):** Another anti-seizure drug used to stabilize moods, often quicker than lithium.

        **Antipsychotics:**
        - Drugs such as **Aripiprazole (Abilify)**, **Olanzapine (Zyprexa)**, and **Risperidone (Risperdal)** may be used in treating hypomanic symptoms or for depressive episodes.

        **Benzodiazepines:**
        - Medications like **Alprazolam (Xanax)** and **Lorazepam (Ativan)** may be used for short-term control of symptoms like insomnia or agitation.

        **Antidepressants:**
        - **Seroquel (Seroquel XR)** is FDA-approved for bipolar II depression. Other antidepressants like **Fluoxetine (Prozac)** and **Sertraline (Zoloft)** are used, but with careful monitoring for potential triggers of hypomania.

        **Ongoing Medication Management:**
        - Treatment often requires ongoing medication, even when symptoms are not present, to prevent relapse. Medication adherence is crucial to maintaining long-term stability.

        **Side Effects:**
        - Common side effects include nausea, tremors, sexual problems, weight gain, and liver damage. Regular check-ups with your doctor are essential to monitor side effects and adjust medication as needed.

        **Medication Tips:**
        - Consistency is key. Take your medications at the same time daily and discuss any missed doses with your doctor.
        - Do not stop or change medications without consulting your doctor, as it could lead to a relapse.

        **Maintenance Therapy:**
        - Maintenance treatment helps prevent episodes from becoming more frequent or severe. Even when feeling well, continuing medication may prevent the return of depressive or hypomanic episodes.

        Remember, the right treatment plan is unique for each individual, and your doctor will help guide the process of finding what works best for you.
    """)
elif Prevention_button:
    st.subheader("Bipolar II Prevention")
    st.write("""

        The exact causes of bipolar II disorder are not well understood, and it is not clear if the disorder can be entirely prevented. However, it is possible to reduce the risk of future episodes of hypomania or depression once bipolar disorder has developed.

        **Steps to reduce risk of future episodes include:**

        - **Regular therapy sessions**: Engaging in consistent therapy with a psychologist or social worker can help individuals recognize early warning signs of relapse and work on emotional stabilization.
        - **Medication adherence**: Ensuring proper medication management is crucial to help prevent future episodes. Medication helps to balance mood and reduce the frequency of episodes.
        - **Psychotherapy**: Regular psychotherapy, such as Cognitive Behavioral Therapy (CBT), helps individuals manage the emotional challenges of bipolar disorder, recognize relapse triggers, and address coping strategies.
        - **Lifestyle management**: Adopting healthy lifestyle practices, such as regular sleep patterns, exercise, and avoiding alcohol or drug use, can further reduce the risk of mood episodes.

        By incorporating these preventive strategies, many individuals with bipolar II disorder can experience fewer hospitalizations and an improved overall quality of life.
    """)
else:
    
    st.write("""
        **Bipolar II disorder** (pronounced "bipolar two") is a form of mental illness. Bipolar II is similar to bipolar I disorder, with moods cycling between high and low over time.  
        
        However, in bipolar II disorder, the "up" moods never reach full-blown mania. The less-intense elevated moods in bipolar II disorder are called hypomanic episodes, or hypomania.

        A person affected by bipolar II disorder has had at least one hypomanic episode in their life. Most people with bipolar II disorder have episodes of depression more often. This is where the term "manic depression" comes from.
    """)
