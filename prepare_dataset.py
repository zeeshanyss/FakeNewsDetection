import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df_fake = pd.read_csv("data/news_sample.csv")
df_true = pd.read_csv("data/news_sample.csv")

# Add labels: Fake=0, True=1
df_fake["label"] = 0
df_true["label"] = 1

# Combine & shuffle
df = pd.concat([df_fake, df_true], axis=0).sample(frac=1, random_state=42).reset_index(drop=True)

# Split into train/test (80/20)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df["label"])

# Save processed data
train_df.to_csv("data/news_sample.csv", index=False)
test_df.to_csv("data/news_sample.csv", index=False)

print(f"Training samples: {len(train_df)}, Test samples: {len(test_df)}")
