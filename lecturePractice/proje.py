import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import spearmanr

# Define the parameters based on the extracted equations
parameters = ["Lambda", "Beta", "Alpha", "Mu", "Gamma", "Delta", "Xi"]

# Generate random samples for each parameter (assuming normal distribution)
num_samples = 100  # Number of simulations
param_values = np.random.uniform(0.1, 1.0, (num_samples, len(parameters)))  # Uniform distribution [0.1,1.0]

# Simulate a basic model output (for example, total infected population I)
# Here, we assume a simple function based on extracted equations
output_I = (param_values[:, 1] * param_values[:, 0]) / (1 + param_values[:, 2]) - param_values[:, 4] * param_values[:, 5]

# Compute PRCC using Spearman's rank correlation
prcc_values = [spearmanr(param_values[:, i], output_I).correlation for i in range(len(parameters))]

# Convert to a DataFrame for visualization
prcc_df = pd.DataFrame({"Parameter": parameters, "PRCC": prcc_values})

# Plot the PRCC values
plt.figure(figsize=(8, 5))
sns.barplot(x="PRCC", y="Parameter", data=prcc_df, palette="coolwarm")
plt.xlabel("Partial Rank Correlation Coefficient (PRCC)")
plt.ylabel("Model Parameters")
plt.title("PRCC Analysis for Model Parameters")
plt.axvline(0, color="black", linestyle="--")  # Vertical line at zero for reference
plt.show()