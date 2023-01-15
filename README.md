# [Project Doenca](https://project-doenca.streamlit.app/)

This project is submitted for [Treasure Hacks 3.0](https://treasure-hacks-3-0.devpost.com/)

---

**Alzheimer** is known the most for the causes of **dementia**. It takes $2/3$ of the whole dementia population, while the cause is still unknown.
According to papers from Lancet neurology, even the old theory such as neural inflations, which was disregarded as the cause compared to tau-protein, beta-amyloids, and genetic factors.
The **World Health Organization** Trusted Source says that **47.5 million people** around the world are living with dementia.
The **National Institutes of Health** estimate that more than **5 million people** in the United States have Alzheimer’s disease.
Although younger people can and do get Alzheimer's, the symptoms generally begin after age 60.
There are degrees of severity in Alzheimer.
- **Very mildly demented**: This is the stage where patient starts to forget where they put their stuff, other people's names recently, etc. It is hard to detect through cognitive ability test.
- **Mildly demented**: This is the stage where patients don't remember the words, can't find their way to the destination, loss of focus and work-abilities. This is also the stage where patients even forget that they are losing memory. From this stage, with cognitive testing, it can be found.
- **Moderately demented**: Starts to forget the recent activities, important old histories, have hard time calculating the budget, hard to go outside alone, and loss of empathy.

There are 3 more stages in the moderately dementia, which in the terminal stage, the patient can't move on their own, while they lose the ability to speak.
Knowing these stages are important because the faster the stage the patient is at, the treatment will have higher effect in terms of slowing the process. If the dementia is found during the moderately demented stage, it is known that the patient will pass away in 3 years.
**Thus, having an AI that detects alzheimer dementia in the early stage can allow longer life expectancy from the patient as well as higher life quality overall from the slowdown of dementia.**
As Alzheimer can not only be found with cognitive ability testing, but also through MRI or CT by looking at the ventricles of the brain and cortical atrophy, the theoretical foundation on this project is solid. Doctors find the patient with Alzheimer's have a brain that have enlarged ventricles (that lies in the center of the brain) as well as thinner cortical grey area of the brain.

---

# Technology Stack Used:

<a href="#" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>

- Streamlit
- Machine Learning

### APIs used

- [Google maps API for places](https://maps.googleapis.com): Our website will calculate latitude and longitude values of current location and it will fetch all nearby 
doctors with specialize in Alzheimer.

---

## How it works?

Our application utilizes machine learning to predict whether this person's brain image shows Alzheimer signs.
        
If the person have Alzheimer, than our application will also provide what stage the patient is, **it may be used as a supportive tool for doctors to diagnose Alzheimer's Disease**. It brings some light in the practical world as it may find early stages of AD, which can increase life expectancy as well as increased life quality with supportive treatments.

We then recommend you specialized doctors in your nearby areas,based on your current location.

---

## Installation/Execution

1. Create a virtual environment

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment

    for Linux and Mac:

    ```bash
    source venv/bin/activate
    ```

    for Windows:

    ```bash
    venv\Scripts\activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app

    ```bash
    streamlit run ./About.py
    ```
    
    ---
    
## Challenges we ran into 
1. Fetching, Installing Dependencies and Fixing Backend Errors.
2. Creating a model for detecting Alzheimer.

## Accomplishments that we're proud of 
We were able to successfully create an application to solve problems for those who are suffering from **Alzheimer's Disease**. Team Work was something we were really proud of specially when we had errors we worked together to fix them.

## What's next for Doenca?
We plan to finish this challenge and create a complete web application and help the user to experience the best out of it.

## Team Members:
<a href="https://github.com/coder12git/Treasure-Hacks-3.0/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=coder12git/Treasure-Hacks-3.0"/>
</a>


## Show your support

Please ⭐ this repository if this project helped you!
