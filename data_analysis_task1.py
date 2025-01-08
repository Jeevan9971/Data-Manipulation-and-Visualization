import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#readiing data file
df = pd.read_csv(r'D:/Internship/NativeSoftTech/Project/Task 1/StudentsPerformance.csv')

#display first few rows of data
print(df.head())

#checking for missing values
print(df.isnull().sum())

#To get the summary of the data
print(df.describe())

# Data Manipulation

#1.Filtering
# filtering Data where  math score is above 80.

math_above_80 = df[df['math score'] > 80]
print(math_above_80)

# filtering Data where test preperation course is completed.

completed_course = df[df['test preparation course'] == 'completed']
print(completed_course)

# Combine filters 
filtered_df = df[(df['math score'] > 80) & (df['test preparation course'] == 'completed')]
print(filtered_df)

#2. Grouping data
# Grouping data by gender and calculating Average of math score, reading score and writing score.

avg_scores_by_gender = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
print(avg_scores_by_gender)


#Grouping data by parental level of education and calculating Average of math score, reading score and writing score.

avg_scores_by_parent_edu = df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
print(avg_scores_by_parent_edu)

#3.Aggregating data
# Calculate the total and average scores for each test.

total_avg_scores = df.agg({
    'math score': ['sum', 'mean'],
    'reading score': ['sum', 'mean'],
    'writing score': ['sum', 'mean']
})
print(total_avg_scores)

# Data Visualization
#1.Line Chart : Showing trends in math scores for the first 50 students

plt.plot(df['math score'][:50])
plt.title('Line Chart - Math Scores for First 50 Students')
plt.xlabel('Index')
plt.ylabel('Math Score')
plt.show()

# 2. Area Chart - Showing trends for scores

scores = df[['math score', 'reading score', 'writing score']][:50]
scores.plot(kind='area', alpha=0.5, figsize=(10, 6))
plt.title('Area Chart - Scores for First 50 Students')
plt.xlabel('Index')
plt.ylabel('Scores')
plt.grid(True)
plt.legend(title='Subjects')
plt.show()

#3. Bar chart : Comparing the count of students by gender

df['gender'].value_counts().plot(kind='bar', color=['blue', 'pink'])
plt.title('Bar Chart - Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#4. Histogram : Distribution of math scores

plt.hist(df['math score'], bins=10, color='green')
plt.title('Histogram - Math Score Distribution')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.show()

#5. Scatter plot : Showing Corelation between math and reading scores

sns.scatterplot(data=df, x='math score', y='reading score', hue='gender')
plt.title('Scatter Plot - Math vs Reading Scores')
plt.show()

#6. Bubble Chart: To Show and compare relationships between math and reading scores

scatter = plt.scatter(x=df['math score'], y=df['reading score'], c=df['writing score'], s=100, alpha=0.5, cmap='viridis')
plt.title('Bubble Chart - Math vs Reading Scores with Writing Scores')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.colorbar(scatter, label='Writing Score') 
plt.show()

#7. Pie Chart : Showing Proportion of student by lunch type:

df['lunch'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['orange', 'lightblue'])
plt.title('Pie Chart - Lunch Type Distribution')
plt.ylabel('') 
plt.show()

# 8. Gauge Chart : 

avg_math_score = df['math score'].mean()
fig = px.bar_polar(r=[avg_math_score], 
theta=['Math Score'],
color=['Math'],
title='Gauge Chart - Average Math Score',
template='plotly_dark')
fig.show()

# 9. Heat map : Showing correlation matrix for all numeric scores

correlation_matrix = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heat Map - Correlation Between Scores')
plt.show()



# to save any processed DataFrame as new csv file
filtered_df.to_csv('filtered_data.csv', index=False)

