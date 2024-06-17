from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from preprocess_page import preprocess_page

def train_chatbot(course_code, file_name, page_dict):
    # Create a chatbot instance
    bot = ChatBot('Buddy')

    # Create a list of preprocessed sentences
    sentences = []
    for page_number, page_text in page_dict.items():
        sentences.extend(preprocess_page(page_text))

    # Create a trainer and train the chatbot
    trainer = ListTrainer(bot)
    trainer.train(sentences)

    # Save the trained chatbot to a file
    bot_path = f'{course_code}_{file_name}_chatbot.pickle'
    bot.save(bot_path)
    print(f'Chatbot trained and saved to {bot_path}')

