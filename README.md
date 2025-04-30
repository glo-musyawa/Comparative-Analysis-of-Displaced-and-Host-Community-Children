# Comparative Analysis of Displaced and Host Community Children – OECD-UNHCR Datathon 2025

This repository contains a comparative analysis of displaced and host community children in **Northern South Sudan** and **Bangladesh**, conducted as part of the **OECD-UNHCR Datathon 2025**. The goal of this project is to uncover data-driven insights that inform inclusive policies, ensuring that **no child is left behind**, regardless of displacement status.

## Repository Structure

- `Northern_South_Sudan_Comparative_Analysis/`
  - Jupyter notebooks with detailed analysis for South Sudan
  - Original dataset: `UNHCR_FDS_SSD_2023.csv`

- `Bangladesh_Comparative_Analysis/`
  - Jupyter notebooks with detailed analysis for Bangladesh
  - Datasets:
    - `UNHCR_BGD_2023_msnahost_datai_anon_v.2.1.csv`
    - `UNHCR_BGD_2023_msnaref_datai_anon_v.2.1.csv`

  - A presentation summarizing the analysis for a quick walkthrough
    https://youtu.be/79wdKiXARuA

## Summary of the Analysis

The analysis draws on **weighted household survey data from 2023**, with datasets representing **refugee and host community children** in both regions. The primary focus is on:

- **Education**: School attendance, literacy, and enrollment
- **Healthcare**: Immunization coverage and access to services
- **Living Conditions**: Shelter type, sanitation, and basic amenities

By applying **population weights**, we ensured representative comparisons between refugee and host children, accounting for sampling design.

## Analytical Approach

1. **Data Preparation**: Variable mapping and alignment across datasets
2. **Descriptive Statistics**: Summarizing key metrics by population group
3. **Inferential Testing**: Using weighted Z-tests with 95% confidence intervals
4. **Visualization**: Charts, tables, and maps to illustrate disparities
5. **Insights & Recommendations**: Translating patterns into policy-relevant findings

## Tools & Libraries Used

- **Python**: Primary analysis language
- **Pandas, NumPy, GeoPandas**: Data manipulation and spatial analysis
- **Matplotlib, Seaborn**: Static data visualizations
- **Flourish**: Interactive data storytelling
- **Statsmodels**: Weighted statistical analysis using `DescrStatsW`

## Why This Matters

> Behind every row of data lies a child navigating the daily realities of displacement—trying to learn, stay healthy, and grow in uncertain conditions.

This project amplifies their stories by uncovering evidence that can drive **equity-focused action** across both refugee and host communities.

---

For a quick walkthrough of our findings, check out the interactive storytelling presentation in this link: https://public.flourish.studio/story/3071110/
