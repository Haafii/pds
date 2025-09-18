import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# ----------- Base Class -----------
class DataHandler:
    def __init__(self, dataframe):
        self.df = dataframe

    def show_info(self):
        """Show basic info about DataFrame"""
        print("DataFrame Info:")
        print(self.df.info())
        print("\nFirst 5 rows:\n", self.df.head())


# ----------- Derived Class -----------
class DataAnalyzer(DataHandler):
    def __init__(self, dataframe):
        super().__init__(dataframe)  # Call parent constructor

    # ---------- Preprocessing ----------
    def preprocess(self, method="fillna_mean"):
        """Handle missing values and duplicates with different strategies"""
        self.df = self.df.drop_duplicates()

        if method == "fillna_mean":
            self.df = self.df.fillna(self.df.mean(numeric_only=True))
        elif method == "fillna_median":
            self.df = self.df.fillna(self.df.median(numeric_only=True))
        elif method == "fillna_mode":
            self.df = self.df.fillna(self.df.mode().iloc[0])
        elif method == "dropna":
            self.df = self.df.dropna()
        elif method == "fillna_zero":
            self.df = self.df.fillna(0)

        print(f"\nAfter Preprocessing ({method}):")
        print(self.df.head())

    # ---------- Descriptive Stats ----------
    def describe_data(self):
        """Print statistics of numeric columns"""
        print("\nStatistical Summary:")
        print(self.df.describe())

    # ---------- Matplotlib Visualizations ----------
    def plot_histogram(self):
        self.df.hist(figsize=(10, 6))
        plt.suptitle("Histograms of Numerical Columns")
        plt.show()

    def plot_bar(self, column):
        self.df[column].value_counts().plot(kind="bar", figsize=(8, 5))
        plt.title(f"Bar Chart of {column}")
        plt.show()

    def plot_pie(self, column):
        self.df[column].value_counts().plot(kind="pie", autopct='%1.1f%%', figsize=(6, 6))
        plt.title(f"Pie Chart of {column}")
        plt.ylabel("")  # Hide y-label
        plt.show()

    # ---------- Plotly Visualizations ----------
    def plot_scatter(self, x, y, size=None, color=None):
        fig = px.scatter(self.df, x=x, y=y, size=size, color=color,
                         title=f"Bubble Chart / Scatter Plot ({x} vs {y})")
        fig.show()

    def plot_treemap(self, path, values):
        fig = px.treemap(self.df, path=path, values=values,
                         title="Treemap Visualization")
        fig.show()

    def plot_interactive_bar(self, x, y):
        fig = px.bar(self.df, x=x, y=y, title="Interactive Bar Chart")
        fig.show()

    def plot_interactive_histogram(self, column):
        fig = px.histogram(self.df, x=column, title=f"Interactive Histogram of {column}")
        fig.show()


# ---------- Main Program ----------
if __name__ == "__main__":
    # Step 1: Read Excel file into DataFrame
    file_path = "input.xlsx"   # <-- put your Excel file name here
    df = pd.read_excel(file_path)

    # Step 2: Pass DataFrame to base/derived classes
    base = DataHandler(df)
    base.show_info()

    derived = DataAnalyzer(df)

    # Try different preprocessing techniques
    derived.preprocess(method="fillna_mean")
    derived.describe_data()

    # Matplotlib plots
    derived.plot_histogram()
    derived.plot_bar(column="Category")       # replace with your column
    derived.plot_pie(column="Category")       # replace with your column

    # Plotly plots
    derived.plot_scatter(x="Sales", y="Profit", size="Quantity", color="Category")  # replace col names
    derived.plot_treemap(path=["Region", "Category"], values="Sales")               # replace col names
    derived.plot_interactive_bar(x="Category", y="Sales")
    derived.plot_interactive_histogram(column="Sales")
