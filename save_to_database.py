import sqlite3

def save_to_database(course_code, file_name, page_dict):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create the course_files table if it does not exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS course_files (
        course_code TEXT,
        file_name TEXT,
        page_number INTEGER,
        page_text TEXT
    )
    ''')

    # Insert data into the table
    for page_number, page_text in page_dict.items():
        # Convert page_text to a string if it is a list
        if isinstance(page_text, list):
            page_text = ' '.join(page_text)
        c.execute('''
        INSERT INTO course_files (course_code, file_name, page_number, page_text)
        VALUES (?, ?, ?, ?)
        ''', (course_code, file_name, page_number, page_text))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def get_from_database(course_code, file_name):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Retrieve data from the table
    c.execute('''
    SELECT page_number, page_text FROM course_files
    WHERE course_code = ? AND file_name = ?
    ''', (course_code, file_name))
    data = c.fetchall()

    # Convert the data into a dictionary
    page_dict = {}
    for row in data:
        page_number, page_text = row
        page_dict[page_number] = page_text

    # Close the connection and return the data
    conn.close()
    return page_dict
