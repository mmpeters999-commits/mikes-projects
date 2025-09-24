import streamlit as st
import base64


if 'is_submitted' not in st.session_state:
    st.session_state['is_submitted'] = False

if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''
if 'adressed' not in st.session_state:
    st.session_state['adressed'] = ''


if not st.session_state['is_submitted']:
    # This form is the first thing the user will see.
    with st.form(key='user_info_form'):
        st.header("WELCOME!! to MICHEAL PETERS' Portfolio and Resume")
        
        # These are the input fields.
        name_input = st.text_input('Hi there!, Can you please provide your name😊?')
        adressed_input = st.selectbox('How would you love to be addressed?', options=['Mr', 'Miss', 'Mrs', 'Master', 'Mistress', 'Sir', 'Ma'])
        
        # This is the submit button for the form.
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state['user_name'] = name_input
            st.session_state['adressed'] = adressed_input
            
            st.session_state['is_submitted'] = True
          
            st.success(f"Hi  {st.session_state['adressed']} {st.session_state['user_name']} 🤗 Welcome to my portfolio and resume.")
        

elif st.session_state['is_submitted']:
    
    st.header("MICHEAL PETERS' Portfolio and Resume")
    
    with st.sidebar:
        st.header("MICHEAL PETERS")
     
        st.write(f" ### Welcome to my portfolio and resume {st.session_state['adressed']} {st.session_state['user_name']}.")
        
        st.markdown("---")
        
        select_option = st.radio("Go to", ("Resume", "Portfolio", "About", "Contact"))
        
        st.markdown("---")
        
        st.subheader("Settings")
        st.write("Pick a theme color:")
        selected_color = st.color_picker("", "#0000FF")
        st.markdown(f"<h1 style='color:{selected_color};'>My Title</h1>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.subheader("📫 Contact Me")
        st.markdown("Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or connect on [https://www.linkedin.com/in/petersmicheal/](https://www.linkedin.com/)")

    #gender_mapping = {'male': 'Mr', 'female':'Miss'}
    #gender_encoded = gender_mapping[gender]

    if select_option == "Resume":
        
        st.write(f"Hi {st.session_state['adressed']} {st.session_state['user_name']}!, WELCOME!!! to my resume😍.")
        def get_base64_image(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        
        profile_image_base64 = get_base64_image("My Profile Pics.jpg")
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)


        #profile_image_path = 'My Profile Pics.jpg' 
        #profile_image_base64 = get_base64_image(profile_image_path)
        
        #if profile_image_base64:
            #st.markdown(
            # f'<img src="data:image/png;base64,{profile_image_base64}" alt="Michael Peters Profile" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: block; margin-left: auto; margin-right: auto;">',
            # unsafe_allow_html=True
            #)
            #st.markdown("---") 
        
        st.title("My Resume")
        st.markdown("### MICHEAL PETERS")
        st.markdown(
            """
            - Address: 3, Lalubu Street, Okeilewo, Abeokuta, Ogun State, Abeokuta North, Ogun State
            - Phone: 08146399129
            - Email: mmpeters626@gmail.com
            - LinkedIn: https://www.linkedin.com/in/petersmicheal/
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
            f"""
            Hi! {st.session_state['adressed']} {st.session_state['user_name']} Welcome to my portfolio! Here you will find some of my key projects and work. 
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
        st.markdown(f"### Hello {st.session_state['adressed']} {st.session_state['user_name']}!!, This a brief overview about me")
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
        st.markdown("- Studying")
        st.markdown("- Making Researches")
        st.markdown("- Praying")

    elif select_option == "Contact":
        st.title("Contact")
        st.markdown(
            f"""
            Thank you for visiting my portfolio and resume! {st.session_state['adressed']} {st.session_state['user_name']} 🙏👏🤗🤩
            Please feel free to connect with me via.
            """
        )
        st.markdown(
            """
            - **Email:** mmpeters626@gmail.com
            - **Phone:** 08146399129 0r 08112398005
            - **LinkedIn:** https://www.linkedin.com/in/petersmicheal/
            """
        )


st.markdown("---")
st.markdown(r"""
                 
                **_Built Using Python and Streamlit_**
                """)
st.markdown("### _Micheal Peters_")

st.markdown("---")