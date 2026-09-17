import pandas as pd
from sqlalchemy import create_engine



def extract_employees(engine):
    query="select * from employees"
    emp_df=pd.read_sql_query(query, engine)
    return emp_df


def extract_departments(engine):
    query="select * from departments"
    dept_df=pd.read_sql_query(query, engine)
    return dept_df