I've created a complete Python script that covers all the tasks you requested. Let me walk you through what the code does:
Task 1: Load and Explore the Dataset
The script attempts to load the Titanic dataset from a GitHub URL, with a fallback to the Iris dataset if the URL is inaccessible. It then:

Displays the first 5 rows using .head()
Explores the structure with .info()
Checks for missing values
Cleans the dataset by filling missing numerical values with the median and categorical values with the mode

Task 2: Basic Data Analysis
The code performs several analytical tasks:

Computes basic statistics for numerical columns using .describe()
Groups data by a categorical column (either species for Iris or passenger class/sex for Titanic)
Identifies and highlights interesting patterns in the data, such as:

For Titanic: women had higher survival rates, 1st class passengers fared better
For Iris: clear separation between species based on petal dimensions



Task 3: Data Visualization
The script creates four different visualizations in a 2x2 grid:

Line chart: Shows trends across categories (species measurements or survival patterns)
Bar chart: Compares numerical values across categories (petal length by species or survival rate by class)
Histogram: Displays the distribution of a numerical column (sepal length or passenger age)
Scatter plot: Visualizes relationships between two numerical columns (sepal vs petal length or age vs fare)

All visualizations are properly customized with:

Clear titles
Appropriate axis labels
Legends where necessary
Grid lines for better readability

The script also includes proper error handling for loading the dataset and uses modern visualization techniques with both matplotlib and seaborn libraries.
