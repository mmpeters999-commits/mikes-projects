import streamlit as st
import base64


# --- Helper function to display local images ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# To use this function, you would need to have the image file locally.
# Example:
profile_image_base64 = get_base64_image("My Profile Pics.jpg")
st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)

# --- Set up the main page and a simple greeting ---
st.header("MICHEAL PETERS' Portfolio and Resume")
st.markdown("---")

#name = st.text_input('Hi there!, What is your name?')
#st.write(f"Hi {name}, welcome to my portfolio and resume.")

# --- Create the sidebar for navigation ---
with st.sidebar:
    st.header("MICHEAL PETERS")
    st.write("Welcome to my portfolio and resume. 😍")
    
    st.markdown("---")
    
    select_option = st.radio("Go to", ("Resume", "Portfolio", "About", "Contact"))
    
    st.markdown("---")
    
    # You can add a color picker or other settings here if needed
    st.subheader("Settings")
    st.write("Pick a theme color:")
    st.color_picker("", "#0000FF") # Default color is a nice blue
    
    st.markdown("---")
    st.subheader("📫 Contact Me")
    st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/)")

# --- Display content based on the radio button selection ---

if select_option == "Resume":
    st.title("My Resume")
    # --- Code to display the profile picture ---
    # NOTE: You must have a file named 'profile_pic.png' in the same directory.
    # Replace 'profile_pic.png' with your actual image filename.
    profile_image_path = 'My Profile Pics.JPG' 
    profile_image_base64 = get_base64_image(profile_image_path)
    
    if profile_image_base64:
        st.markdown(
            f'<img src="data:image/png;base64,{profile_image_base64}" alt="Michael Peters Profile" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: block; margin-left: auto; margin-right: auto;">',
            unsafe_allow_html=True
        )
        st.markdown("---") # Add a separator after the image
    
    
    st.markdown("### MICHEAL PETERS")
    st.markdown(
        """
        3, Lalubu Street, Okeilewo, Abeokuta, Ogun State, Abeokuta North, Ogun State
        Phone: 08112398005
        Email: mmpeters626@gmail.com
        LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/)
        Portfolio Website: [Your Portfolio Link](https://www.yourportfolio.com/)
        """
    )
    st.markdown("---")

    st.markdown("### OBJECTIVE")
    st.markdown(
        """
        Enthusiastic and detail-oriented aspiring Data Scientist with a strong foundation 
        in statistical analysis, machine learning, and data visualization. Eager to apply 
        academic knowledge and technical skills to real-world projects through an internship, 
        aiming to contribute to data-driven decision-making and gain practical industry experience.
        """
    )
    st.markdown("---")

    st.markdown("### SKILLS")
    st.markdown(
        """
        - Programming: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
        - Data Analysis & Visualization
        - Machine Learning Algorithms: Linear Regression, Logistic Regression, Decision Trees, Random Forest
        - SQL & Databases
        - Basic Knowledge of Big Data Tools (Spark, Hadoop)
        - Statistical Analysis & Hypothesis Testing
        """
    )
    st.markdown("---")

    st.markdown("### EDUCATION")
    st.markdown(
        """
        **Bachelor of Science in Education (BSc.Ed) in Technology Education (in view)**
        University of Yaba, Lagos
        *Expected Graduation: August 2026*
        *Relevant Coursework: Data Structures, Statistics, Machine Learning, Data Visualization, Databases*
        """
    )
    st.markdown("---")

    st.markdown("### PROJECTS")
    st.markdown(
        """
        **Customer Churn Prediction**
        - Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy.
        - Performed data cleaning, feature engineering, and model evaluation.

        **Employee Salary Prediction**

        **Sentiment Analysis of Social Media Data**
        - Analyzed Twitter data to classify sentiment using NLP techniques and Python libraries.
        - Visualized sentiment trends over time.

        **Sales Data Visualization Dashboard**
        - Created an interactive sales performance dashboard in Tableau to explore regional sales metrics.
        """
    )
    st.markdown("---")

    st.markdown("### CERTIFICATIONS AND COURSES")
    st.markdown(
        """
        - Introduction to Data Science in Python – Coursera, University of Michigan
        - Machine Learning – Coursera, Stanford University
        - Data Analysis with Python – freeCodeCamp
        """
    )
    st.markdown("---")

    st.markdown("### EXTRACURRICULAR ACTIVITIES")
    st.markdown(
        """
        - Member of [University Data Science Club]
        - Participated in Kaggle competitions (if applicable)
        - Volunteered for data analysis projects at [Organization Name]
        """
    )
    st.markdown("---")

    st.markdown("### LANGUAGES")
    st.markdown("- English (Fluent)")
    st.markdown("---")


elif select_option == "Portfolio":
    st.title("My Portfolio")
    st.markdown(
        """
        Welcome to my portfolio! Here you will find some of my key projects and work. 
        Each project showcases my skills in data science, machine learning, and data visualization.
        """
    )
    # Add your portfolio content here, e.g., using `st.columns` to lay out projects
    st.subheader("Project Showcase")
    
    st.markdown("#### Customer Churn Prediction App")
    st.write("- Developed a classification model to predict customer churn using Python and Scikit-learn, achieving 85% accuracy /n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Car Prices Prediction App")
    st.write("- Developed a Regression model to predict car prices using Python and Scikit-learn, achieving 81% accuracy /n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Student performance Prediction")
    st.write("- Developed a classification model to predict students perfomances using Python and Scikit-learn, achieving 85% accuracy /n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Diabetes Prediction")
    st.write("- Developed a classification model to predict the tendency of an individual to have diabetes due to some informations/n"
             "supplied by the individual as requested using Python and Scikit-learn, achieving 85% accuracy /n"
             "- Performed data cleaning, feature engineering, and model evaluation.")
    st.markdown("---")
    
    st.markdown("#### Weather App")
    st.write("- Built a Python application using Streamlit to provide real-time weather information for any location worldwide, here is the link to check out the app\n"
             "https://whether-app-mop.streamlit.app")
    st.markdown("---")
    
    
    


elif select_option == "About":
    st.title("About Me")
    st.markdown(
        """
        I am a passionate and driven aspiring data scientist with a knack for solving problems
        and uncovering insights from data. I am currently pursuing my Bachelor of Science in 
        Education (BSc.Ed) in Technology Education at the University of Yaba, Lagos. 
        My goal is to leverage my skills in data science and machine learning to contribute
        to meaningful, data-driven solutions.
        """
    )
    st.markdown("---")

    st.markdown("### My Hobbies")
    st.markdown("- Reading")
    st.markdown("- Hiking")
    st.markdown("- Photography")

elif select_option == "Contact":
    st.title("Contact")
    st.markdown(
        """
        Thank you for visiting my portfolio and resume! 
        Please feel free to connect with me.
        """
    )
    st.markdown(
        """
        - **Email:** mmpeters626@gmail.com
        - **Phone:** 08112398005
        - **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/)
        - **GitHub:** [Your GitHub Profile](https://github.com/)
        """
    )
















