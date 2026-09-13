import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.datasets import fetch_california_housing


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Confidence Interval Analysis",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 Confidence Interval Analysis")

st.write(
    "Interactive analysis of confidence intervals "
    "using the California Housing Dataset."
)


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():

    housing = fetch_california_housing(as_frame=True)

    return housing.frame


df = load_data()


# --------------------------------------------------
# Variables
# --------------------------------------------------

variables = [
    "MedInc",
    "HouseAge",
    "AveRooms",
    "Population"
]


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Analysis Settings")

selected_variable = st.sidebar.selectbox(
    "Select a variable",
    variables
)

confidence = st.sidebar.select_slider(
    "Select confidence level",
    options=[0.90, 0.95, 0.99],
    value=0.95,
    format_func=lambda x: f"{int(x * 100)}%"
)


# --------------------------------------------------
# Statistical Calculation
# --------------------------------------------------

data = df[selected_variable].dropna()

n = len(data)

mean = data.mean()

std = data.std()

standard_error = std / np.sqrt(n)

alpha = 1 - confidence

t_critical = stats.t.ppf(
    1 - alpha / 2,
    df=n - 1
)

margin_of_error = t_critical * standard_error

lower_bound = mean - margin_of_error

upper_bound = mean + margin_of_error


# --------------------------------------------------
# Display Results
# --------------------------------------------------

st.subheader("Confidence Interval Results")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Sample Mean",
        f"{mean:.4f}"
    )


with col2:

    st.metric(
        "Lower Bound",
        f"{lower_bound:.4f}"
    )


with col3:

    st.metric(
        "Upper Bound",
        f"{upper_bound:.4f}"
    )


# --------------------------------------------------
# Statistical Information
# --------------------------------------------------

st.write(
    f"### {int(confidence * 100)}% Confidence Interval"
)

st.write(
    f"The confidence interval for the mean of "
    f"**{selected_variable}** is:"
)

st.success(
    f"({lower_bound:.4f}, {upper_bound:.4f})"
)


st.write(
    f"**Margin of Error:** {margin_of_error:.4f}"
)

st.write(
    f"**Sample Size:** {n}"
)


# --------------------------------------------------
# Visualization
# --------------------------------------------------

st.subheader("Confidence Interval Visualization")


chart_data = pd.DataFrame(
    {
        "Value": [
            lower_bound,
            mean,
            upper_bound
        ]
    },
    index=[
        "Lower Bound",
        "Mean",
        "Upper Bound"
    ]
)


st.bar_chart(chart_data)


# --------------------------------------------------
# Interpretation
# --------------------------------------------------

st.subheader("Interpretation")

st.write(
    f"At the {int(confidence * 100)}% confidence level, "
    f"the estimated population mean of {selected_variable} "
    f"is between {lower_bound:.4f} and "
    f"{upper_bound:.4f}."
)

st.info(
    "Increasing the confidence level generally produces "
    "a wider confidence interval because a larger margin "
    "of error is required to achieve greater confidence."
)


# --------------------------------------------------
# Dataset Preview
# --------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head(10))