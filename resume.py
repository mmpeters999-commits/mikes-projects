

import streamlit as st

st.header("MICHEAL PETERS' Portfolio and Resume")

name = st.text_input('Hi there!!, Whats your name?', 'user')

# --- Set up the main page ---
if st.button('Submit'):
    st.write(f"Hi {name}, WELCOME!! to my portforlio")

    st.write("This Streamlit app showcases my Portfolio and my Resume.")

    # --- Create the sidebar using 'with' notation ---
#py -m streamlit run resume.py

    with st.sidebar:
        st.header("MICHEAL PETERS")
        st.write("Welcome to my portforlio and resume 😍.")
        
        select_option = st.radio("Go to", ("Resume", "Portfolio", "About", "Contact"))
        st.markdown("---")
        
        st.subheader("Settings")
        
        st.subheader("📫 Contact Me")
#Feel free to reach out via [Email](mailto:mmpeters626@gmail.com) or connect on [LinkedIn](#)

        color = st.color_picker("Pick a theme:")
    if select_option == "Resume":        
        st.markdown("### MICHEAL PETERS")
        st.markdown(
        r"""
        3, Lalubu Street, Okeilewo, Abeokuta, Ogun State Abeokuta North, Ogun State  
        Phone: 08112398005  
        Email: mmpeters626@gmail.com  
        LinkedIn: [Your LinkedIn Profile] (if available)  
        Portfolio Website: [Your Portfolio Link] (if available)

        """
    )
        st.markdown("---")

        st.markdown("### OBJECTIVE")
        st.markdown(
        r"""
        Enthusiastic and detail-oriented aspiring Data Scientist with a strong foundation 
        in statistical analysis, machine learning, and data visualization. Eager to apply 
        academic knowledge and technical skills to real-world projects through an internship, 
        aiming to contribute to data-driven decision-making and gain practical industry experience.

        """
    )

        st.markdown("---")

        st.markdown("### SKILLS")
        st.markdown(
        r"""
        - Programming: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
        - Data Analysis & Visualization  
        - Machine Learning Algorithms: Linear Regression, Logistic Regression, Decision Trees, Random Forest  
        - SQL & Databases  
        - Basic Knowledge of Big Data Tools (Spark, Hadoop)  
        - Statistical Analysis & Hypothesis Testing  

        """
    )

        st.markdown("---")

        st.markdown("### EDUCATION ")
        st.markdown(
        r"""
        Bachelor of Science in Education (BSc.Ed) in Technology Education (in view)
        University of Yaba, Lagos  
        Expected Graduation: August 2026  
        Relevant Coursework: Data Structures, Statistics, Machine Learning, Data Visualization, Databases



        """
    )

        st.markdown("---")

        st.markdown("### PROJECT ")
        st.markdown(
        r"""
        Customer Churn Prediction  
        - Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy.  
        - Performed data cleaning, feature engineering, and model evaluation.

        Employee Salary Prediction
        Sentiment Analysis of Social Media Data
        - Analyzed Twitter data to classify sentiment using NLP techniques and Python libraries.  
        - Visualized sentiment trends over time.

        Sales Data Visualization Dashboard
        - Created an interactive sales performance dashboard in Tableau to explore regional sales metrics.

        """
    )

        st.markdown("---")

        st.markdown("### CERTIFICATION AND COURSES ")
        st.markdown(
        r"""
        - Introduction to Data Science in Python – Coursera, University of Michigan  
        - Machine Learning – Coursera, Stanford University  
        - Data Analysis with Python – freeCodeCamp  


        """
    )

        st.markdown("---")

        st.markdown("### EXTRACURRICULAR ACTIVITIES")
        st.markdown(
        r"""
        - Member of [University Data Science Club]  
        - Participated in Kaggle competitions (if applicable)  
        - Volunteered for data analysis projects at [Organization Name]  


        """
    )

        st.markdown("---")

        st.markdown("### LANGUAGE")
        st.markdown(
        r"""
        - English (Fluent)  

        """
    )


        st.markdown("---")

   
    
    elif select_option == "Portfolio":
        
        st.write(f"hello {name}")
        st.markdown("### MICHEAL PETERS")
        
    

