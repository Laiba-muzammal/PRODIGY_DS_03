def regional_analysis(data):
    print("Regional Data Insights:\n")
    regions = data['Region'].unique()

    for region in regions:
        region_data = data[data['Region'] == region]

        if region_data['Income'].duplicated().any():
            print(f"Overlapping Income data in {region} region\n")
        if region_data['Expenditure'].duplicated().any():
            print(f"Overlapping Expenditure data in {region} region\n")
        print(f"Data for {region}: \n{region_data}\n")
