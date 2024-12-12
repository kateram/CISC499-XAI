import difflib
import OpenAIconnector

# Function to compare files
def compare_files(file1, file2):
    """
    Compares two files using the difflib module and returns differences in a String.

    :param file1: Name of original program file
    :param file2: Name of generated program file
    :return: A string containing line by line differences of the given two files
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    # Use difflib to generate the differences
    diff = difflib.unified_diff(
        file1_lines, file2_lines, fromfile='File1', tofile='File2', lineterm=''
    )
    diff_text = "\n".join(diff)
    return diff_text


# Main execution
if __name__ == "__main__":
    # Compare two files
    diff_text = compare_files('original.py', 'generated.py')

    #api_key = ADD API KEY HERE -------------------------------
    connector = OpenAIconnector.OpenAIConnector(api_key=api_key, model="gpt-4o", temperature=0.0)
    # Write the differences to a text file
    with open('differences.txt', 'w') as diff_file:
        diff_file.write("Differences:\n")
        diff_file.write(diff_text)
        diff_file.write("\n\n")
    
    # Get GPT explanation
    explanation = connector.explain_differences(diff_text)
    
    # Append the explanation to the same text file
    with open('differences.txt', 'a') as diff_file:
        diff_file.write("Explanation:\n")
        diff_file.write(explanation)
        diff_file.write("\n")

