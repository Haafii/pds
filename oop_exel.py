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
        super().__init__(dataframe)

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

    # ---------- Matplotlib Visualizations (Saved) ----------
    def plot_histogram(self, column="Unit price", filename="histogram.png"):
        self.df[column].hist(bins=20, figsize=(8, 5))
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.savefig(filename)
        plt.close()

    def plot_bar(self, column="Product line", filename="barchart.png"):
        self.df[column].value_counts().plot(kind="bar", figsize=(8, 5))
        plt.title(f"Bar Chart of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.savefig(filename)
        plt.close()

    def plot_pie(self, column="Payment", filename="piechart.png"):
        self.df[column].value_counts().plot(kind="pie", autopct='%1.1f%%', figsize=(6, 6))
        plt.title(f"Pie Chart of {column}")
        plt.ylabel("")  # Hide y-label
        plt.savefig(filename)
        plt.close()

    # ---------- Plotly Visualizations (Saved) ----------
    def plot_scatter(self, x="Quantity", y="Total", size="Unit price", color="Product line",
                     filename="scatter.png"):
        fig = px.scatter(self.df, x=x, y=y, size=size, color=color,
                         title=f"Bubble/Scatter Plot ({x} vs {y})")
        fig.write_image(filename)

    def plot_treemap(self, path=["City", "Product line"], values="Total",
                     filename="treemap.png"):
        fig = px.treemap(self.df, path=path, values=values,
                         title="Treemap of Sales by City & Product Line")
        fig.write_image(filename)

    def plot_interactive_bar(self, x="Product line", y="Total", filename="interactive_bar.png"):
        fig = px.bar(self.df, x=x, y=y, title="Interactive Bar Chart of Total Sales by Product Line",
                     color=x, text_auto=True)
        fig.write_image(filename)

    def plot_interactive_histogram(self, column="Rating", filename="interactive_histogram.png"):
        fig = px.histogram(self.df, x=column, nbins=20,
                           title=f"Interactive Histogram of {column}", color_discrete_sequence=["blue"])
        fig.write_image(filename)


# ---------- Main Program ----------
if __name__ == "__main__":
    # Step 1: Read Excel file into DataFrame
    file_path = "supermarkt_sales.xlsx"   # <-- put your Excel file name here
    df = pd.read_excel(file_path)

    # Step 2: Pass DataFrame to base/derived classes
    base = DataHandler(df)
    base.show_info()

    derived = DataAnalyzer(df)

    # Try preprocessing
    derived.preprocess(method="fillna_mean")
    derived.describe_data()

    # ---------- Example Plots (Saved instead of showing) ----------
    derived.plot_histogram(column="Unit price", filename="hist_unitprice.png")
    derived.plot_bar(column="Product line", filename="bar_productline.png")
    derived.plot_pie(column="Payment", filename="pie_payment.png")

    derived.plot_scatter(x="Quantity", y="Total", size="Unit price",
                         color="Product line", filename="scatter_sales.png")
    derived.plot_treemap(path=["City", "Product line"], values="Total",
                         filename="treemap_sales.png")
    derived.plot_interactive_bar(x="Product line", y="Total",
                                 filename="bar_total_sales.png")
    derived.plot_interactive_histogram(column="Rating",
                                       filename="hist_rating.png")
