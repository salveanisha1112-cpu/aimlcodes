import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("heart.csv")
print(df.head())

# 2. Data cleaning
df = df.drop_duplicates() 

# 3. Handle missing values
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values:")
print(df.isnull().sum())

# 4. Statistical analysis
print(df.describe())

# 5. Separate input and output
X = df.drop("target", axis=1)
y = df["target"]

# 6. Encoding categorical features
X = pd.get_dummies(X, drop_first=True, dtype=int)

# 7. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# 9. Histogram of Age
plt.figure(figsize=(10, 5))
plt.hist(df["age"].dropna(), bins=20, edgecolor="black")
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 10. Histogram of Cholesterol
plt.figure(figsize=(10, 5))
plt.hist(df["chol"].dropna(), bins=20, edgecolor="black")
plt.title("Histogram of Cholesterol")
plt.xlabel("Cholesterol")
plt.ylabel("Frequency")
plt.show()

# 11. Boxplot of Age
plt.figure(figsize=(10, 5))
sns.boxplot(x=df["age"])
plt.title("Boxplot of Age")
plt.xlabel("Age")
plt.show()

# 12. Boxplot of Cholesterol
plt.figure(figsize=(10, 5))
sns.boxplot(x=df["chol"])
plt.title("Boxplot of Cholesterol")
plt.xlabel("Cholesterol")
plt.show() 