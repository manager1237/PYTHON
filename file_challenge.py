# File Read & Write Challenge with Error Handling

def modify_content(content):
    """
    Function to modify file content.
    For this example, we will convert the text to uppercase.
    """
    return content.upper()

def main():
    # Ask the user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Define output filename
        output_file = "modified_" + filename

        # Write the modified content to new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"File processed successfully! Modified content saved in '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
