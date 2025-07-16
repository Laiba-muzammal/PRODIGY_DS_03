from data_loader import load_and_clean_data
from plotter import plot_income_vs_expenditure
from analysis import regional_analysis

def main():
    original, cleaned = load_and_clean_data('Book1.csv')

    print(f"Original Data: \n{original}\n")
    print(f"Data After Cleaning: \n{cleaned}\n")
    print(f"Statistical Review: \n{cleaned.describe()}\n")

    plot_income_vs_expenditure(cleaned)
    regional_analysis(cleaned)

if __name__ == "__main__":
    main()
