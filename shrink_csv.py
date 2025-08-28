import pandas as pd
import os

# Path to your original CSV (make sure file exists here)
input_file = "data/train.csv"
output_file = "data/train_small.csv"

# Load the CSV
print("Loading dataset...")
df = pd.read_csv(input_file)

# Show original size
print(f"Original rows: {len(df)}, Columns: {df.shape[1]}")

# ✅ Step 1: Keep only first 20,000 rows (adjust if needed)
df_small = df.head(20000)

# ✅ Step 2 (Optional): Drop very large text columns if not needed
# df_small = df_small.drop(columns=['content'])

# Save reduced dataset
df_small.to_csv(output_file, index=False)

# Show new size
new_size = os.path.getsize(output_file) / (1024*1024)  # in MB
print(f"Saved {output_file} with {len(df_small)} rows.")
print(f"New file size: {new_size:.2f} MB (should be < 100 MB for GitHub)")

# Optional: Replace original train.csv with smaller one
replace = input("Do you want to replace original train.csv with smaller file? (y/n): ")
if replace.lower() == "y":
    os.remove(input_file)
    os.rename(output_file, input_file)
    print("Replaced old train.csv with smaller version ✅")
