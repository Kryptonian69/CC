# Data Science Viva Quick Reference (One-Liners)

This guide covers all key terms, acronyms, and concepts from Practicals 1-10.

## 1. Excel & Basic Analysis (Practical 1)
*   **VLOOKUP (Vertical Lookup):** A function used to search for a value in the first column of a table and return a value in the same row from another column.
*   **Pivot Table:** A data processing tool used to summarize, sort, reorganize, group, or total data stored in a table.
*   **Goal Seek:** A "What-If" analysis tool that finds the input value needed to achieve a specific desired output or goal.
*   **Conditional Formatting:** A feature that changes the appearance of cells (e.g., color, font) based on specific conditions or rules.

## 2. Data Pre-processing & Pandas (Practical 2)
*   **Pandas (Python Data Analysis Library):** A powerful library used for data manipulation and analysis, primarily through DataFrames.
*   **DataFrame:** A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
*   **CSV (Comma Separated Values):** A simple text file format that stores tabular data, where each line is a data record.
*   **JSON (JavaScript Object Notation):** A lightweight data-interchange format often used for storing hierarchical or nested data.
*   **NaN (Not a Number):** A special floating-point value used to represent missing or undefined data in a dataset.
*   **SimpleImputer:** A scikit-learn class used to handle missing values by replacing them with a specific strategy like the mean, median, or mode.
*   **Outlier:** A data point that differs significantly from other observations in the dataset, often identified using boxplots.

## 3. Feature Engineering & Scaling (Practical 3)
*   **Feature Scaling:** The process of transforming numerical features to a similar scale to prevent certain variables from dominating others during model training.
*   **Standardization (Z-score Normalization):** Rescaling data so it has a mean of 0 and a standard deviation of 1.
*   **Normalization (Min-Max Scaling):** Scaling data into a fixed range, usually between 0 and 1.
*   **Dummification (One-Hot Encoding):** The process of converting categorical variables into a numerical format by creating binary (0 or 1) columns for each category.
*   **Train-Test Split:** Dividing a dataset into two subsets: one for training the model and one for testing its performance on unseen data.

## 4. Statistical Testing & ANOVA (Practicals 4 & 5)
*   **Hypothesis Testing:** A statistical method used to decide whether there is enough evidence in a sample of data to support a particular belief about a population.
*   **Null Hypothesis ($H_0$):** A statement that there is no significant difference or effect; it is what we aim to test against.
*   **Alternative Hypothesis ($H_1$):** The statement we want to support, suggesting that there is a significant difference or effect.
*   **P-value (Probability Value):** The probability that the observed results occurred by chance; if $P < 0.05$, we typically reject the Null Hypothesis.
*   **T-test:** A statistical test used to compare the means of two groups (e.g., One-sample, Two-sample, or Paired).
*   **ANOVA (Analysis of Variance):** A statistical method used to compare the means of three or more groups to see if at least one is significantly different.
*   **Tukey HSD (Honestly Significant Difference):** A post-hoc test used after ANOVA to determine exactly which specific groups' means are different from each other.

## 5. Regression Analysis (Practical 6)
*   **Linear Regression:** A supervised learning algorithm used to predict a continuous numerical value based on the relationship between variables.
*   **Multiple Regression:** An extension of linear regression that uses two or more independent variables to predict a single dependent variable.
*   **MSE (Mean Squared Error):** A metric that measures the average of the squares of the errors—the average squared difference between estimated values and the actual value.
*   **$R^2$ (R-squared / Coefficient of Determination):** A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable.

## 6. Classification Models (Practical 7)
*   **Logistic Regression:** A classification algorithm used to predict the probability of a categorical dependent variable (usually binary like Yes/No).
*   **Decision Tree:** A flowchart-like structure used for classification and regression where each internal node represents a "test" on an attribute.
*   **Accuracy:** The ratio of correctly predicted observations to the total observations.
*   **Precision:** The ratio of correctly predicted positive observations to the total predicted positives (measures "exactness").
*   **Recall (Sensitivity):** The ratio of correctly predicted positive observations to all actual positives (measures "completeness").
*   **Classification Report:** A summary of the key evaluation metrics (Precision, Recall, F1-Score) for each class in a model.

## 7. Clustering & PCA (Practicals 8 & 9)
*   **K-Means Clustering:** An unsupervised learning algorithm that groups data points into $K$ clusters based on their similarity.
*   **WCSS (Within-Cluster Sum of Squares):** The sum of squared distances between each data point and the centroid of its assigned cluster; used to evaluate clustering.
*   **Elbow Method:** A heuristic used to find the optimal number of clusters ($K$) by plotting WCSS and looking for the "elbow" point.
*   **PCA (Principal Component Analysis):** A dimensionality-reduction technique that transforms large sets of variables into smaller ones while preserving as much information as possible.
*   **Explained Variance:** A measure that tells us how much information (variance) can be attributed to each of the principal components.

## 8. Data Visualization (Practical 10)
*   **Matplotlib:** The foundational library for creating static, interactive, and animated visualizations in Python.
*   **Seaborn:** A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.
*   **Plotly:** A library used to create interactive, web-based visualizations like histograms, scatter plots, and pie charts.
*   **Correlation Matrix:** A table showing correlation coefficients between variables, often visualized using a Heatmap.
