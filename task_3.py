# Set Seaborn style
sns.set(style="whitegrid")

# Line chart: simulate time-series with cumulative sum
df['index'] = df.index
df_line = df.groupby('index').mean().cumsum()
plt.figure(figsize=(10, 6))
plt.plot(df_line)
plt.title("Cumulative Feature Trends Over Index")
plt.xlabel("Index")
plt.ylabel("Cumulative Sum")
plt.legend(df.columns[:-2], loc='upper left')
plt.show()

# Bar chart: average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram: distribution of sepal length
plt.figure(figsize=(8, 6))
plt.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: sepal length vs. petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
