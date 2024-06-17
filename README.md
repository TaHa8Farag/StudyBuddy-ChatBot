# StudyBuddy ChatBot

## Description

This project, StudyBuddy ChatBot, automates the extraction, preprocessing, and storage of text from PDF documents intended for educational use. It supports functionalities like text extraction, cleaning and preprocessing, training chatbots with cleaned data, and saving the processed content to a SQLite database. This system is ideal for educational institutions looking to digitize course materials and enhance student interactions through AI-driven chatbots.

## Features

- **PDF Text Extraction:** Extracts text from PDF files, handling various layouts and encodings.
- **Text Preprocessing:** Cleans and preprocesses text by removing punctuation, stop words, numbers, and applying lemmatization.
- **Chatbot Training:** Trains custom chatbots using preprocessed text to facilitate interactive learning.
- **Database Integration:** Saves preprocessed text to a SQLite database and allows easy retrieval and management.

## Getting Started

### Prerequisites

- Python 3.8 or above
- Libraries:
  - `pdfminer.six`
  - `chatterbot`
  - `nltk`
  - `spacy`
  - `sqlite3` (included with Python)
- Spacy English Model: Download using `python -m spacy download en_core_web_lg`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TaHa8Farag/StudyBuddy-ChatBot.git
   cd StudyBuddy-ChatBot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Follow the instructions in `main.py` to start the application. Choose your role as either Doctor or Student, and proceed to add new course materials or manage existing ones.

### Code Overview

For a detailed explanation of each script's functionality, please refer to the individual files within the repository. They contain comments that describe their purpose and how to use them.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/TaHa8Farag/StudyBuddy-ChatBot](https://github.com/TaHa8Farag/StudyBuddy-ChatBot)
