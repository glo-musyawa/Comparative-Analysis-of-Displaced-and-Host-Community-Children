# Comparative Analysis of Displaced and Host Community Children – OECD-UNHCR Datathon 2025

This repository contains a comparative analysis of displaced and host community children in **Northern South Sudan** and **Bangladesh**, conducted as part of the **OECD-UNHCR Datathon 2025**. The goal of this project is to uncover data-driven insights that inform inclusive policies, ensuring that **no child is left behind**, regardless of displacement status.

## Repository Structure

- `Northern_South_Sudan_Comparative_Analysis/`
  - Jupyter notebooks with detailed analysis for South Sudan`

- `Bangladesh_Comparative_Analysis/`
  - Jupyter notebooks with detailed analysis for Bangladesh
  
Here’s a clearer, more polished version of that section for your README:

---

-`datasets_and_visuals_functions/`

This folder contains:

#### Dataset Subfolders:

* **`Bangladesh_Comparative_Analysis/`**

  * `UNHCR_BGD_2023_msnahost_datai_anon_v.2.1.csv`
  * `UNHCR_BGD_2023_msnaref_datai_anon_v.2.1.csv`

* **`Northern_South_Sudan_Comparative_Analysis/`**

  * `UNHCR_SSD_2023_FDS_data_caregiver.csv`
  * `UNHCR_SSD_2023_FDS_data_roster.csv`

Each subfolder includes the datasets used for respective regional analyses.

#### Visualization Function Files:

* `bangladesh_visuals.py`:
  Contains plotting functions for the notebook
  **`Bangladesh_Comparative_Analysis_On_Host_and_Refugees_Children_.ipynb`**

* `south_sudan_visuals_function.py`:
  Supports visuals for
  **`South_Sudan_FDS_Children_Cargivers_dataset.ipynb`**

* `south_sudan_visuals_function2.py`:
  Supports visuals for
  **`South_Sudan_FDS2Rooster_dataset.ipynb`**

> To keep the notebooks clean and maintainable, all complex visualization code has been modularized into these separate Python files.

---


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

For a quick walkthrough of our findings, check out the interactive storytelling presentation at this link: https://public.flourish.studio/story/3071110/
