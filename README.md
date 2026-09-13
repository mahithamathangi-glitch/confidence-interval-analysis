# Confidence Interval Analysis

## Project Overview

This project demonstrates how confidence intervals can be used to estimate population parameters using sample data.

The analysis was performed using the California Housing Dataset and Python.

## Objective

The main objectives of this project are:

- Calculate confidence intervals for population means.
- Compare 90%, 95%, and 99% confidence levels.
- Understand uncertainty around statistical estimates.
- Visualize confidence intervals.
- Interpret statistical results in plain language.

## Dataset

The California Housing Dataset contains information about housing and demographic characteristics of California districts.

The variables analyzed in this project are:

- MedInc
- HouseAge
- AveRooms
- Population

## Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Google Colab

## Statistical Method

Confidence intervals were calculated using the t-distribution.

The confidence interval for a population mean is calculated as:

CI = Mean ± Critical Value × Standard Error

where:

Standard Error = Sample Standard Deviation / √Sample Size

## Confidence Levels

The following confidence levels were analyzed:

- 90%
- 95%
- 99%

## Key Findings

The analysis demonstrates that:

1. Higher confidence levels produce wider confidence intervals.
2. The 90% confidence interval is narrower than the 95% interval.
3. The 99% confidence interval is the widest.
4. Increasing confidence increases the margin of error.
5. Confidence intervals provide information about uncertainty rather than relying only on a point estimate.

## Results

Confidence intervals were calculated for four statistics:

- Median Income
- House Age
- Average Rooms
- Population

The results were visualized using error-bar plots and comparison charts.

## Conclusion

Confidence intervals are an important statistical technique for estimating unknown population parameters using sample data.

The project demonstrates how changing the confidence level affects the width of an interval. Higher confidence provides greater coverage but results in a wider interval.

## How to Run

Clone the repository:

```bash
git clone https://github.com/mahithamathangi-glitch/confidence-interval-analysis.git

## Version History

Version 1.0 - Initial confidence interval analysis project.

