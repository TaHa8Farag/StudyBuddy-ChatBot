from io import BytesIO
from extract_text_from_pdf import extract_text_from_pdf
from preprocess_page import preprocess_page
from save_to_database import save_to_database, get_from_database
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Prompt the user to enter their choice
choice = input("Are you a doctor (1) or a student (2)? ")

if choice == "1":
    # Prompt the user to choose whether to add a new course or add materials to an existing course
    add_choice = input("Do you want to add a new course (1) or add materials to an existing course (2)? ")

    if add_choice == "1":
        # Future work for adding a new course
        pass

    elif add_choice == "2":
        # Prompt the user to choose the course code to add materials to
        course_code = input("Enter the course code to add materials to: ")

        # Check if the course folder exists, and create it if it doesn't
        if not os.path.exists(course_code):
            os.makedirs(course_code)

        # Open a file browsing window and prompt the user to choose the file to add
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        file_path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

        # Read the selected file into memory as bytes
        with open(file_path, 'rb') as f:
            file_data = BytesIO(f.read())

        # Save the file to the course folder
        file_name = input("Enter a name for the file: ")
        with open(os.path.join(course_code, file_name), 'wb') as f:
            f.write(file_data.getvalue())

        # Call the extract_text_from_pdf function with the file data
        page_dict = extract_text_from_pdf(file_data)

        # Preprocess the text for each page and update the page_dict
        for page_number, page_text in page_dict.items():
            preprocessed_text = preprocess_page(page_text)
            page_dict[page_number] = preprocessed_text

        # Save to database
        save_to_database(course_code, file_name, page_dict)

        # Retrieve from database
        data_from_db = get_from_database(course_code, file_name)

        # Print the processed text for each page
        if data_from_db:
            for page_number, page_text in data_from_db.items():
                print(f'Page {page_number}: {page_text}')
        else:
            print('Data not found in database')

    else:
        print("Invalid choice. Please enter 1 or 2.")

else:
    print("Invalid choice. Please enter 1 or 2.")
