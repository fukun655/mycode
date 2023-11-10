import random
import psycopg2
from sqlalchemy import create_engine, MetaData, Table, select

# Connect to your PostgreSQL database (replace with your database connection details)
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create an SQLAlchemy engine
engine = create_engine("postgresql://your_user:your_password@your_host/your_database")

# Define the table you want to shuffle columns in
table_name = "your_table"

# Retrieve column names dynamically
metadata = MetaData()
table = Table(table_name, metadata, autoload=True, autoload_with=engine)
column_names = [column.name for column in table.columns]

# Shuffle data in each column individually
for column_name in column_names:
    # Retrieve the data from the current column using SQLAlchemy's select
    select_query = select([table.c[column_name]])
    result = engine.execute(select_query)
    data = [row[0] for row in result]

    # Shuffle the data
    random.shuffle(data)

    # Update the column in the database with the shuffled data
    with engine.connect() as conn:
        conn.execute(table.update().values({column_name: data}))

# Close the database connection
conn.close()
