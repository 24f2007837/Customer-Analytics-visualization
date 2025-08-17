import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# 2. Generate synthetic customer support response time data
np.random.seed(42)
channels = ["Email", "Phone", "Chat", "Social Media"]

data = {
    "Channel": np.repeat(channels, 200),  # 200 samples per channel
    "ResponseTime": np.concatenate([
        np.random.normal(loc=12, scale=4, size=200),   # Email (slower)
        np.random.normal(loc=8, scale=3, size=200),    # Phone
        np.random.normal(loc=5, scale=2, size=200),    # Chat (faster)
        np.random.normal(loc=10, scale=3.5, size=200)  # Social Media
    ])
}

df = pd.DataFrame(data)

# Clip negative values (no negative response times)
df["ResponseTime"] = df["ResponseTime"].clip(lower=0.5)

# 3. Create the violinplot
plt.figure(figsize=(8, 8))  # 512x512 pixels with dpi=64
ax = sns.violinplot(
    x="Channel",
    y="ResponseTime",
    data=df,
    palette="Set2",
    inner="quartile"
)

# 4. Style the plot
ax.set_title("Customer Analytics: Response Time Distribution by Support Channel", fontsize=14, weight="bold")
ax.set_xlabel("Support Channel", fontsize=12)
ax.set_ylabel("Response Time (minutes)", fontsize=12)

# 5. Save chart as PNG (exact 512x512)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
