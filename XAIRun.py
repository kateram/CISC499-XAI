import OpenAIconnector
import PostgresConnector
import os

def read_python_files(folder_name):
    """
    Reads all Python files and converts their content to strings.

    :param folder_name: Name of the folder containing Python files.
    :return: A dictionary where keys are file names and values are the file contents as strings.
    """
    # Get the folder path relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, folder_name)
    
    file_contents = {}

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Open and read the file
            with open(file_path, "r") as file:
                file_contents[filename] = file.read()
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return file_contents


if __name__ == "__main__":
    # Connect to openai and database
    # api_key = ADD IN API KEY  -------------------------------
    connector = OpenAIconnector.OpenAIConnector(api_key=api_key, model="gpt-4o", temperature=0.0)
    #db = PostgresConnector.PostgresDB(ADD IN DB CONNECTION STRING) -------------------------------
    db.connect()


    # Read each file containing the initial program 
    folder_name = "moretests"  
    python_files = read_python_files(folder_name)

    
    for file_name, program in python_files.items():
        # Get GPT to explain the given code
        explanation = connector.explain_code(program)

        # Get GPT to generate code using the given explanation
        generated_code = connector.generate_code(explanation)

        # Store results in the database
        query = """
                INSERT INTO runresults (initial_program, explanation,generated_program, filename )
                VALUES (%s, %s, %s, %s)
                """
        
        data = (program,explanation,generated_code,file_name)
        db.execute_query(query,data)
        print(file_name, "is done")

    db.close()
    print("Done!")
    

