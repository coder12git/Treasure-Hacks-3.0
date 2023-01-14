from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Alzheimer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_disease = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_gkgqj2yq.json"
)
img_alzheimer = Image.open("./images/alzheimer.jpg")
img_alz = Image.open("images/alzheimer2.jpg")
img_doctor = Image.open("images/doctor.jpg")

st.title("Learn More")
st_lottie(lottie_disease, height=300, key="disease")
st.subheader("Read articles about Alzheimer's disease")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Alzheimer")
        """
        Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink (atrophy) and brain cells to die. Alzheimer's disease is the most common cause of dementia — a continuous decline in thinking, behavioral and social skills that affects a person's ability to function independently.

        Approximately 5.8 million people in the United States age 65 and older live with Alzheimer's disease. Of those, 80% are 75 years old and older. Out of the approximately 50 million people worldwide with dementia, between 60% and 70% are estimated to have Alzheimer's disease.

        The early signs of the disease include forgetting recent events or conversations. As the disease progresses, a person with Alzheimer's disease will develop severe memory impairment and lose the ability to carry out everyday tasks.

        Medications may temporarily improve or slow progression of symptoms. These treatments can sometimes help people with Alzheimer's disease maximize function and maintain independence for a time. Different programs and services can help support people with Alzheimer's disease and their caregivers.

        There is no treatment that cures Alzheimer's disease or alters the disease process in the brain. In advanced stages of the disease, complications from severe loss of brain function — such as dehydration, malnutrition or infection — result in death.
        
        **Symptoms**

        Memory loss is the key symptom of Alzheimer's disease. Early signs include difficulty remembering recent events or conversations. As the disease progresses, memory impairments worsen and other symptoms develop.

        At first, a person with Alzheimer's disease may be aware of having difficulty remembering things and organizing thoughts. A family member or friend may be more likely to notice how the symptoms worsen.

        Brain changes associated with Alzheimer's disease lead to growing trouble with:

        - Memory
        - Thinking and reasoning
        - Making judgments and decisions
        - Planning and performing familiar tasks
        - Changes in personality and behavior
        - Preserved skills

        **When to see a doctor**

        A number of conditions, including treatable conditions, can result in memory loss or other dementia symptoms. If you are concerned about your memory or other thinking skills, talk to your doctor for a thorough assessment and diagnosis.

        If you are concerned about thinking skills you observe in a family member or friend, talk about your concerns and ask about going together to a doctor's appointment.
        """
        st.write("##")
        st.write(
            "[**Learn More**](https://www.mayoclinic.org/diseases-conditions/alzheimers-disease/symptoms-causes/syc-20350447)"
        )
        with right_column:
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.image(img_alz)
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.write("##")
            st.image(img_alzheimer)
            st.write("##")
            st.write("##")
            st.write("##")
            st.image(img_doctor)
