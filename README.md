# NPV Simulation Analysis for Cleaning Equipment Investment
## Overview
This project evaluates the financial viability of investing in specialized cleaning equipment using Net Present Value (NPV) analysis and Monte Carlo simulation. The goal is to assess the potential profitability of the investment under various scenarios and provide a data-driven recommendation.
---

### Objective
To calculate the NPV of purchasing and operating specialized cleaning equipment for two years, incorporating:
- Revenue from hire days.
- Maintenance costs.
- Resale value of the equipment.

### Key Factors Considered
- *Revenue:* Hire rate (£150/day) and probability-weighted hire days.
- *Maintenance Costs:* Yearly estimates with probabilities.
- *Salvage Value:* Resale value at the end of two years.
- *Discount Rate:* 15%.
- *Initial Investment:* £17,000.

---

## 2. Setup Instructions

### Prerequisites
- Python 3.7 or later.
- Libraries:
  - numpy
  - matplotlib

### Installation
1. Install Python dependencies:
   bash
   pip install numpy matplotlib
   

2. Clone or download the project files.

---

## 3. Simulation Process

### Methodology
- *Monte Carlo Simulation:*
  - Generate random values for hire days, maintenance costs, and salvage value based on given probabilities.
  - Calculate annual cash flows and their discounted values.
  - Repeat for 10,000 iterations to generate a distribution of possible NPVs.

---

## 4. Results

### Key Statistics
- *Mean NPV:* £21,864.56
- *Standard Deviation:* £4,919.83
- *Percentiles:*
  - *5th Percentile:* £13,198.49 (Pessimistic scenario).
  - *50th Percentile (Median):* £22,952.74.
  - *95th Percentile:* £27,886.58 (Optimistic scenario).

### Insights
- The investment has a high probability of positive returns, with a low risk of negative outcomes.
- The histogram shows most NPVs clustering around the mean, indicating consistent profitability.

---

## 5. Usage

### Modifying Inputs
You can adjust the probabilities, hire days, costs, or resale value in the simulation code. Example parameters to edit:
python
hire_days_probs = [0.2, 0.3, 0.5]
hire_days_values = [125, 150, 175]
hire_rate = 150

maintenance_year1_probs = [0.4, 0.5, 0.1]
maintenance_year1_values = [1200, 2500, 4000]

salvage_value_probs = [0.7, 0.3]
salvage_value_values = [5000, 7000]


### Running the Simulation
1. Run the simulation script:
   bash
   python simulation.py
   

2. View the results, including the NPV distribution graph and statistical summaries.

---
