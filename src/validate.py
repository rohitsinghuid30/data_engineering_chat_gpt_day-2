import pandas as pd


def validate_employees(emp_df, dept_df):

    merged_df=emp_df.merge(
        dept_df,
        on="department_id",
        how="left"
    )

    valid_df=merged_df[
        merged_df["department_name"].notna()
        ].copy()

    rejected_df=merged_df[
        merged_df["department_name"].isna()
    ].copy()


    rejected_df["rejection_reason"]="INVALID_DEPARTMENT"

    return valid_df, rejected_df

