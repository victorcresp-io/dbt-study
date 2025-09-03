import pandas as pd
 
 # Creating tables that I will use in dbt part and saving them to csv file
def creating_tables():
    data_example_df_person = {
    "id_person": [1, 2, 3, 4, 5],
    "name": ['Victor Rodrigues', 'João Gusmão', 'Jorge Crespo', 'Pedro Bial', 'Fernando Amorim']
}

    data_example_df_age_person = {
        "id_person": [1, 2, 3, 4, 5],
        "age": [23, 25, 32, 36, 41]
    }

    df_person = pd.DataFrame(data = data_example_df_person)

    df_age = pd.DataFrame(data = data_example_df_age_person)

    df_person.to_csv('data_person_dbt_study.csv', index = False)

    df_age.to_csv('data_age_dbt_study.csv', index = False)

if __name__ == "__main__":
    creating_tables()