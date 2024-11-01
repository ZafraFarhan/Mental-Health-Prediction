import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the page config
st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

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
            }
                
        </style>
    </head>
    """, unsafe_allow_html=True)

# Load data
def load_data():
    data = pd.read_csv("df_new.csv")
    return data
df = load_data()



st.title("Mental Health Dashboard")


with st.sidebar:
    st.header("⚙️ Settings")
    
    feature = st.radio(
        "Select Feature",
        ('Sadness', 'Euphoric', 'Exhausted', 'Sleep dissorder', 'Mood Swing',
       'Suicidal thoughts', 'Anorxia', 'Authority Respect', 'Try-Explanation',
       'Aggressive Response', 'Ignore & Move-On', 'Nervous Break-down',
       'Admit Mistakes', 'Overthinking', 'Sexual Activity', 'Concentration',
       'Optimisim'),
    )


st.subheader(f"Distribution of {feature}")

# Generate chart based on selection
plt.figure(figsize=(10, 6), facecolor='#2E2E2E')  # Set the figure background color

# Calculate percentage of each category
counts = df[feature].value_counts()
percentages = counts / counts.sum() * 100

# Create the bar plot
bar_plot = sns.barplot(x=percentages.index, 
                       y=percentages.values, 
                       color='#FFA001')  # Set bar color

plt.xlabel(feature, color='white')  # Set x-label color
plt.ylabel("Percentage (%)", color='white')   # Set y-label color
plt.gca().set_facecolor('#2E2E2E') 
plt.xticks(color='white')  # Set x-tick color
plt.yticks(color='white')  # Set y-tick color
plt.ylim(0, 100)  # Set y-axis limits from 0 to 100

# Add percentage labels on top of the bars
for p in bar_plot.patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2, 
             height, 
             f'{height:.1f}%', 
             ha='center', 
             color='white', 
             fontsize=12, 
             va='bottom')  # va='bottom' to place text above the bar

st.pyplot(plt)

# Create a DataFrame to hold the percentage of each feature for each depression state
df_grouped = df.groupby('Expert Diagnose')[feature].value_counts(normalize=True).unstack(fill_value=0) * 100

# Generate charts for each depression state
plt.figure(figsize=(10, 6), facecolor='#2E2E2E')
df_grouped.plot(kind='bar', stacked=True, color=sns.color_palette("husl", len(df_grouped.columns)), ax=plt.gca())

st.subheader(f'Distribution of {feature} by Expert Diagnose')

plt.xlabel('Expert Diagnose', color='white')
plt.ylabel('Percentage (%)', color='white')
plt.gca().set_facecolor('#2E2E2E')
plt.xticks(color='white')  
plt.yticks(color='white')  
plt.ylim(0, 100)  

# Add percentage labels on top of the bars
for container in plt.gca().containers:
    plt.bar_label(container, fmt='%.1f%%', color='white', fontsize=12)


# Customizing x-axis tick labels
depression_labels = ['Bipolar Type-1', 'Bipolar Type-2', 'Depression', 'Normal']
plt.xticks(ticks=range(len(depression_labels)), labels=depression_labels, rotation=45, ha='right', color='white')

st.pyplot(plt)
