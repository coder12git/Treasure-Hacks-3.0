import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(
    page_title="Alzheimer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

lottie_health = load_lottieurl(
    "https://assets4.lottiefiles.com/packages/lf20_33asonmr.json"
)
lottie_welcome = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json"
)
lottie_healthy = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json"
)

st.title("Welcome to team Doenca!")
st_lottie(lottie_welcome, height=450, key="welcome")
# st.header("Alzheimer detection at your brain images.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            **Alzheimer** is known the most for the causes of **dementia**. It takes 2/3 of the whole dementia population, while the cause is still unknown.
            According to papers from Lancet neurology, even the old theory such as neural inflations, which was disregarded as the cause compared to tau-protein, beta-amyloids, and genetic factors.
            The **World Health Organization** Trusted Source says that **47.5 million people** around the world are living with dementia.
            The **National Institutes of Health** estimate that more than **5 million people** in the United States have Alzheimer’s disease.
            Although younger people can and do get Alzheimer’s, the symptoms generally begin after age 60.

            There are degrees of severity in Alzheimer.
            - **Very mildly demented**: This is the stage where patient starts to forget where they put their stuff, other people's names recently, etc. It is hard to detect through cognitive ability test.
            - **Mildly demented**: This is the stage where patients don't remember the words, can't find their way to the destination, loss of focus and work-abilities. This is also the stage where patients even forget that they are losing memory. From this stage, with cognitive testing, it can be found.
            - **Moderately demented**: Starts to forget the recent activities, important old histories, have hard time calculating the budget, hard to go outside alone, and loss of empathy.

            There are 3 more stages in the moderately dementia, which in the terminal stage, the patient can't move on their own, while they lose the ability to speak.
            Knowing these stages are important because the faster the stage the patient is at, the treatment will have higher effect in terms of slowing the process. If the dementia is found during the moderately demented stage, it is known that the patient will pass away in 3 years.
            **Thus, having an AI that detects alzheimer dementia in the early stage can allow longer life expectancy from the patient as well as higher life quality overall from the slowdown of dementia.**
            As Alzheimer can not only be found with cognitive ability testing, but also through MRI or CT by looking at the ventricles of the brain and cortical atrophy, the theoretical foundation on this project is solid. Doctors find the patient with Alzheimer's have a brain that have enlarged ventricles (that lies in the center of the brain) as well as thinner cortical grey area of the brain.
            """
        )
        st.write("##")
        st.write(
            "[**Learn More >**](https://en.wikipedia.org/wiki/Alzheimer%27s_disease)"
        )
    with right_column:
        st.write("##")
        st_lottie(lottie_health, height=900, key="check")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.header("How it works?")
        st.write(
        """
        Our application utilizes machine learning to predict whether this person's brain image shows Alzheimer signs.
        If the person have Alzheimer, than our application will also provide what stage the patient is, **it may be used as a supportive tool for doctors to diagnose Alzheimer's Disease**. It brings some light in the practical world as it may find early stages of AD, which can increase life expectancy as well as increased life quality with supportive treatments.
        We then recommend you specialized doctors in your nearby areas,based on your current location.

        """
        )
        st.write("##")
  with right_column:
        st.write("##")
        st_lottie(lottie_healthy, height=300, key="healthy")
