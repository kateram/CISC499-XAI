import psycopg2
import pandas as pd

class PostgresDB:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """Connect to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to the database!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def close(self):
        """Close the database connection."""
        if self.connection:
            try:
                self.connection.close()
                print("Connection closed.")
            except Exception as e:
                print(f"Error closing the connection: {e}")

    def execute_query(self, query, params=None):
        """
        Execute a SQL query.
        :param query: SQL query to be executed.
        :param params: Optional parameters for the query 
        :return: Result of the query (if any).
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                # Commit the changes for (INSERT, UPDATE, DELETE)
                if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    self.connection.commit()
                # Fetch results for SELECT queries
                elif query.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")

    def split_results(self, table_name, group_count):
        """
        Split results from a database table evenly among groups member and save them as CSV files.
        This was only used to divide results for evaluation

        :param table_name: Name of the database table to query.
        :param group_count: Number of groups to split the results into.
        """
        try:
            # Query to fetch all rows with a row number for splitting
            query = f"""
            SELECT *, ROW_NUMBER() OVER () AS row_num
            FROM {table_name};
            """
            
            # Execute the query
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                records = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]

            # Create a DataFrame manually from the fetched results
            df = pd.DataFrame(records, columns=column_names)

            # Split the data among groups
            for i in range(group_count):
                group_df = df[df['row_num'] % group_count == i]
                output_file = f"group_{i+1}_results.csv"  # File saved in the same directory as the script
                group_df.to_csv(output_file, index=False)
                print(f"Group {i+1} results saved to {output_file}")

        except Exception as e:
            print(f"Error during splitting: {e}")


