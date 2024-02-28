write a python program which will do the following
import datetime

def create_timestamp_file():
    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create file name with timestamp
    file_name = f"{current_time}.txt"
    
    # Write content to the file
    with open(file_name, 'w') as file:
        file.write(current_time)

# Call the function to create the timestamp file
create_timestamp_file()

write another python function to read a text File
def read_text_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Display the content in the console
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
# Replace 'example.txt' with the name of the text file you want to read
read_text_file('example.txt')