import pandas as pd

def transform_employee(df):

    df = df.copy()


    df["name"]=(
        df["name"]
        .str.strip()
        .str.title()
        )

    df["department_name"]=(
        df["department_name"]
        .str.strip()
        .str.lower()
    )

    final_df=df[
        [
            "id",
            "name",
            "department_id",
            "department_name",
            "salary"

        ]
    ]
    return final_df
    