import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime  # Import datetime
import pickle



with open('rf_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def run():
    st.set_page_config(layout="wide")

    
   
    st.markdown("""
    <head>
        <meta charset="UTF-8">
        <title>All Navigation Menu Hover Animation | CodingLab</title> 
        <style>
            body {
                background-color: #000000;  /* Black background color */
                
            }
            .stApp {
                background-color: #000000;  /* Set background to black for the app */
                
            }
            h1, h2, h3, h4, h5, h6, p, li, a, label {
                color: #ffffff;  /* Set font color to white for all text elements */

            }
  
            .center::after, .upward::after, .forward::after {
                content: '';
                position: absolute;
                width: 100%;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: #fff;  /* Change underline color to white */
                transform: scaleX(0);
                transition: transform 0.3s ease;
            }
            .center::after {
                transform-origin: center;
            }
            .upward::after {
                transform-origin: bottom;
            }
            .forward::after {
                transform-origin: top right;
            }
            .nav-links li:hover::after {
                transform: scaleX(1);
            }
            
            .stSlider > div > div > div > div {
                background-color: #FF7F27;
            }
            .stSlider > div > div > div > input {
                background-color: #FF7F27;
                border: none;
            }
            .stButton button {
                background-color: #FF7F27;
                color: #ffffff !important;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
            }
                
        </style>
    </head>
    """, unsafe_allow_html=True)

    st.markdown(
    """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 18px;
        margin-bottom: 15px;
    }
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 18px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True
    )

    
    st.header("Mental Health Prediction")

    mapping = {
    'Seldom': 1,
    'Sometimes': 2,
    'Most-Often': 4,
    'Usually': 3
    }


        # Inputs for user data
    MoodSwings = st.radio("Mood Swings: Occurrences of sudden and unpredictable mood changes", ("YES", "NO"))
    Optimisim = st.slider("Optimisim: Level of positive outlook towards future outcomes", 1, 5, 1)
    SuicidalThoughts = st.radio("Suicidal Thoughts: Frequency of having thoughts about self-harm or suicide", ("YES", "NO"))
    Sadness = st.radio("Sadness: Frequency of experiencing feelings of unhappiness or despair", ('Seldom', 'Sometimes','Most-Often','Usually'))
    Sadness_value = mapping[Sadness]
    Euphoric = st.radio("Euphoria: Frequency of experiencing intense feelings of happiness or excitement", ('Seldom', 'Sometimes','Most-Often','Usually'))
    Euphoric_value = mapping[Euphoric]
    AggressiveResponse = st.radio("Aggressive Response: Tendency to react with anger or hostility", ("YES", "NO"))
    SleepDisorder = st.radio("Sleep Disorder: Issues or disruptions in regular sleep patterns", ('Seldom', 'Sometimes','Most-Often','Usually'))
    SleepDisorder_value = mapping[SleepDisorder]
    Exhausted = st.radio("Exhaustion: Level of physical or mental tiredness experienced.", ('Seldom', 'Sometimes','Most-Often','Usually'))
    Exhausted_value = mapping[Exhausted]
    AuthorityRespect = st.radio("Authority Respect: Level of regard or compliance shown towards figures of authority", ("YES", "NO"))
    Concentration = st.slider("Concentration: Ability to focus and stay attentive on tasks", 1, 5, 1)
    SexualActivity = st.slider("Sexual Activity: Frequency of engaging in sexual behavior", 1, 5, 1)
    NervousBreakdown = st.radio("Nervous Breakdown: Experience of mental or emotional collapse due to stress", ("YES", "NO"))
    Anorxia = st.radio("Anorexia: Tendency to avoid or lose interest in eating", ("YES", "NO"))
    Overthinking = st.radio("Overthinking: Frequency of excessive or repetitive thoughts", ("YES", "NO"))
    TryExplanation = st.radio("Try-Explaining: Willingness to explain oneself in challenging situations", ("YES", "NO"))
    AdmitMistakes = st.radio("Admitting Mistakes: Openness to acknowledge personal errors or faults", ("YES", "NO"))
    IgnoreNMoveOn = st.radio("Ignore & Move-On: Tendency to overlook issues and move forward", ("YES", "NO"))



    def make_prediction(input_data):
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Print the input data for debugging
        print("Input Data:\n", input_df)
        
        # Make prediction using the loaded pipeline
        prediction = pipeline.predict(input_df)
        
        # Print the prediction for debugging
        print("Prediction:\n", prediction)
        
        return prediction


    input_data = {
        "Mood Swing": MoodSwings,
        "Optimisim": Optimisim,
        "Suicidal thoughts": SuicidalThoughts,
        "Sadness": Sadness_value,
        "Euphoric": Euphoric_value,
        "Aggressive Response": AggressiveResponse,
        "Sleep dissorder": SleepDisorder_value,
        "Exhausted": Exhausted_value,
        "Authority Respect": AuthorityRespect,
        "Concentration": Concentration,
        "Sexual Activity": SexualActivity,
        "Nervous Break-down": NervousBreakdown,
        "Anorxia": Anorxia,
        "Overthinking": Overthinking,
        "Try-Explanation": TryExplanation,
        "Admit Mistakes": AdmitMistakes,
        "Ignore & Move-On": IgnoreNMoveOn,

    }

    if st.button('Predict'):
        prediction = make_prediction(input_data)
        print("Prediction:", prediction)
        
        if prediction[0] == 'Normal':
            st.write("It has been predicted that, you are likely to be normal")
        elif prediction[0] == 'Bipolar Type-2':
            st.write("It has been predicted that you are likely to be experiencing Bipolar Type-2")
            st.markdown("""
            [Click here for more information about Bipolar Type-2 Disorder](https://mental-health-prediction-bp2.streamlit.app/)
            """)
        elif prediction[0] == 'Bipolar Type-1':
            st.write("It has been predicted that you are likely to be experiencing Bipolar Type-1")
            st.markdown("""
            [Click here for more information about Bipolar Type-2 Disorder](https://mental-health-prediction-bp1.streamlit.app/)
            """)
        else:
            st.write("It has been predicted that you are likely to be experiencing Depression")
            st.markdown("""
            [Click here for more information about Bipolar Type-2 Disorder](https://mental-health-prediction-depression.streamlit.app/)
            """)
            
run()
