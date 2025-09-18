import pandas as pd

# Base Class
class DataHandler:
    def __init__(self, dataframe):
        self.df = dataframe

    def show_info(self):
        """Show basic info about DataFrame"""
        print("DataFrame Info:")
        print(self.df.info())
        print("\nFirst 5 rows:\n", self.df.head())


# Derived Class
class DataAnalyzer(DataHandler):
    def __init__(self, dataframe):
        super().__init__(dataframe)  # Call parent constructor

    def preprocess(self):
        """Handle missing values and duplicates"""
        self.df = self.df.drop_duplicates()
        self.df = self.df.fillna(0)  # Replace NaN with 0
        print("\nAfter Preprocessing:")
        print(self.df.head())

    def describe_data(self):
        """Print statistics of numeric columns"""
        print("\nStatistical Summary:")
        print(self.df.describe())

    def plot_data(self):
        """Plot histograms of numeric columns"""
        import matplotlib.pyplot as plt
        self.df.hist(figsize=(10, 6))
        plt.suptitle("Histograms of Numerical Columns")
        plt.show()


# ---------- Main Program ----------
if __name__ == "__main__":
    # Step 1: Read Excel file into DataFrame
    file_path = "input.xlsx"   # <-- put your Excel file name here
    df = pd.read_excel(file_path)

    # Step 2: Pass DataFrame to base/derived classes
    base = DataHandler(df)
    base.show_info()

    derived = DataAnalyzer(df)
    derived.preprocess()
    derived.describe_data()
    derived.plot_data()