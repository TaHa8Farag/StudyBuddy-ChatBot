from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy
import string
import unicodedata

# Load the stop words
stop_words = set(stopwords.words('english'))

# Define the lemmatizer
lemmatizer = WordNetLemmatizer()

nlp = spacy.load("en_core_web_lg")


def preprocess_page(page_text):
    """
    Preprocess the page text by removing punctuation, stop words, numbers, and lemmatizing the words.

    Args:
        page_text (str): Text for a single page.

    Returns:
        list: Preprocessed words for the page.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # Remove punctuation and special characters
    text = page_text.translate(str.maketrans("", "", string.punctuation))


    # Remove non-ASCII characters
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')


    # Tokenization
    words = word_tokenize(text)

    # Remove stop words and words that are too long or too short
    words = [word.lower() for word in words if word.lower() not in stop_words and len(word) > 2 and len(word) < 15]

    # Remove numbers
    words = [word for word in words if not word.isdigit()]

    # Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]

    return words

