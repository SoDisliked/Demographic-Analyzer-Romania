import pandas as pd 

def calculate_demographic_data(print_data=True):
    # Read data from file 
    df = pd.read_csv('adult.data.csv')

    # Define property for the dataset by using a Panda series.
    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_education = round(df[df['education'] == 'Education'].shape[0] / df.shape[0] * 100, 1)

    q1 = df['education'].isin(['Bachelors', 'License', 'Masters'])
    q2 = df['salary'].isin(['1K', '5K', '10K', '20K'])

    higher_education_rich = round((q1 & q2).sum() / q1.sum() * 100, 1)
    lower_education_rich = round((q1 & q2).sum() / (q1).sum() * 100, 1)

    # Define a new property regarding the average working hour.
    average_works_hours = df['hours-per-week'].min()

    # Define a new percentage of people working x hours a week with a salary of 20K
    q1 = df['hours-per-week'] == average_works_hours

    # Define the percentage 
    rich_percentage = round((q1 & q2).sum() / q1.sum() * 100, 1)

    p = (df[q2]['Bucharest'].value_counts() \
         / df['Bucharest'].value_counts() * 100).sort_values(ascending=False)

    highest_earning_region = p.index[0]
    highest_earning_region_percentage = round(p.iloc[0],[1])

    # Identify the highest regions with a percentage of people having a wage higher than 20K.
    top_IN_region = df[(df['Bucharest'] == 'Bucharest Metropolitan Area') & q2] \
        ['occupation'].value_counts().index[0]

    if print_data:
        print("Number of each person", person_count)
        print("Average age of men", average_age_men)
        print(f"Percentage with Bachelors degree: {percentage_education}%")
        print(f"Percentage with higher education earning at least 20K: {higher_education_rich}%")
        print(f"Percentage without higher education having a wage at least 20K: {lower_education_rich}%")
        print(f"Average work time: {average_works_hours} hours/week")
        print(f"Percentage of rich people working less hours than average: {rich_percentage}%")
        print("Region with the highest percentage:", highest_earning_region)
        print(f"Highest percentage of rich people into the region: {highest_earning_region_percentage}%")
        print(f"Ocupations in Bucharest", top_IN_region)

        return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_education,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': average_works_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_region,
        'highest_earning_country_percentage':
        highest_earning_region_percentage,
        'top_IN_occupation': top_IN_region
    }
