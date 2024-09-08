import re
import nltk
from nltk.tokenize import word_tokenize
import pymorphy2

nltk.download('punkt')

def clean_text(text):
    # Удаление служебных символов
    cleaned_text = re.sub(r'[^а-яА-Я0-9 ]', '', text)
    
    # Токенизация текста на слова
    words = word_tokenize(cleaned_text)
    
    morph = pymorphy2.MorphAnalyzer()
    
    cleaned_words = []
    for word in words:
        # Получение основы слова
        base_form = morph.parse(word)[0].normal_form
        
        # Исключение предлогов и союзов
        if morph.parse(base_form)[0].tag.POS not in ['PREP', 'CONJ']:
            cleaned_words.append(base_form)

    cleaned_words = set(cleaned_words)
    
    cleaned_text = ' '.join(cleaned_words)
    
    return cleaned_text



def text_before_model(text):

  return clean_text(text)
