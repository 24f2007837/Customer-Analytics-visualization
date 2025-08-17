import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------
# 1. Generate synthetic data
# --------------------------
np.random.seed(42)
channels = ["Email", "Chat", "Phone", "Social Media"]
data = {
    "Channel": np.random.choice(channels, 400),
    "Response Time (minutes)": np.concatenate([
        np.random.normal(30, 10, 100),   # Email
        np.random.normal(10, 3, 100),    # Chat
        np.random.normal(20, 7, 100),    # Phone
        np.random.normal(15, 5, 100),    # Social Media
    ])
}
df = pd.DataFrame(data)

# --------------------------
# 2. Styling
# --------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# --------------------------
# 3. Plot violinplot
# --------------------------
fig = plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
sns.violinplot(x="Channel", y="Response Time (minutes)", data=df, palette="muted")

plt.title("Customer Support Response Time Distribution", fontsize=14)
plt.xlabel("Support Channel", fontsize=12)
plt.ylabel("Response Time (minutes)", fontsize=12)

# --------------------------
# 4. Save exact size 512x512
# --------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
