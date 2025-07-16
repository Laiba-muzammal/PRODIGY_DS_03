import matplotlib.pyplot as plt

def plot_income_vs_expenditure(data):
    plt.figure(figsize=(11.5, 8))
    plt.hist(data['Income'], color='pink', alpha=0.5, edgecolor='black', label='Income')
    plt.hist(data['Expenditure'], color='lightgreen', alpha=0.5, edgecolor='black', label='Expenditure')
    plt.title("Income VS Expenditure\n")
    plt.xlabel("\nIncome & Expenditure")
    plt.ylabel("Frequency\n")
    plt.legend()
    plt.tight_layout()
    plt.show()
