"""Python code used to generate random values based on probabilities using a Monte Carlo simulation and calculate cash flows for each outcome:"""

import numpy as np

# Simulation parameters
n_simulations = 10000
discount_rate = 0.15
initial_investment = -17000

# Probabilities and values for hire days
hire_days_probs = [0.2, 0.3, 0.5]
hire_days_values = [125, 150, 175]
hire_rate = 150

# Probabilities and values for maintenance costs
maintenance_year1_probs = [0.4, 0.5, 0.1]
maintenance_year1_values = [1200, 2500, 4000]
maintenance_year2_probs = [0.2, 0.6, 0.2]
maintenance_year2_values = [1200, 2500, 4000]

# Probabilities and values for salvage value
salvage_value_probs = [0.7, 0.3]
salvage_value_values = [5000, 7000]

# Function to simulate one year of cash flow
def simulate_cash_flow():
    # Simulate hire days
    hire_days = np.random.choice(hire_days_values, p=hire_days_probs)
    revenue = hire_days * hire_rate

    # Simulate maintenance costs
    maintenance_year1 = np.random.choice(maintenance_year1_values, p=maintenance_year1_probs)
    maintenance_year2 = np.random.choice(maintenance_year2_values, p=maintenance_year2_probs)

    # Simulate salvage value
    salvage_value = np.random.choice(salvage_value_values, p=salvage_value_probs)

    # Calculate cash flows
    year1_cash_flow = revenue - maintenance_year1
    year2_cash_flow = revenue - maintenance_year2 + salvage_value

    # Discount cash flows
    year1_discounted = year1_cash_flow / (1 + discount_rate)
    year2_discounted = year2_cash_flow / ((1 + discount_rate) ** 2)

    # Calculate NPV
    npv = initial_investment + year1_discounted + year2_discounted
    return npv

# Run simulations
npv_results = [simulate_cash_flow() for _ in range(n_simulations)]

# Analyze results
npv_mean = np.mean(npv_results)
npv_std = np.std(npv_results)
npv_percentiles = np.percentile(npv_results, [5, 50, 95])

# Print results
print("Net Present Value (NPV) Analysis Results:")
print("-----------------------------------------------")
print(f"Mean NPV: £{npv_mean:.2f}")
print(f"Standard Deviation of NPV: £{npv_std:.2f}")
print("NPV Percentiles:")
print(f"  5th percentile: £{npv_percentiles[0]:.2f}")
print(f"  50th percentile: £{npv_percentiles[1]:.2f}")
print(f"  95th percentile: £{npv_percentiles[2]:.2f}")


import matplotlib.pyplot as plt

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(npv_results, bins=50, color='skyblue', edgecolor='black', alpha=0.7)

# Add vertical lines for key statistics
plt.axvline(np.mean(npv_results), color='red', linestyle='--', label=f"Mean NPV: £{np.mean(npv_results):.2f}")
plt.axvline(np.percentile(npv_results, 50), color='green', linestyle='--', label=f"Median NPV: £{np.percentile(npv_results, 50):.2f}")
plt.axvline(np.percentile(npv_results, 5), color='orange', linestyle='--', label=f"5th Percentile: £{np.percentile(npv_results, 5):.2f}")
plt.axvline(np.percentile(npv_results, 95), color='blue', linestyle='--', label=f"95th Percentile: £{np.percentile(npv_results, 95):.2f}")

# Add titles and labels
plt.title("NPV Distribution from Simulation")
plt.xlabel("NPV (£)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)

# Show the plot
plt.show()

