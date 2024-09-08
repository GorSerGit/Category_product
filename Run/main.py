
from Trans_text import text_before_model
import joblib

def find_key_by_value(file_path, value):
        # Чтение словаря из текстового файла
        with open(file_path, 'r', encoding="utf-8") as file:
            dictionary = eval(file.read())

        # Поиск ключа по значению
        for key, val in dictionary.items():
            if val == value:
                return key
        
        return None

def text_to_cat(a, file_path):

    vectorizer = joblib.load('vectorizer_4.pkl')
    svc = joblib.load('svm_model_2_4.pkl')

    text = text_before_model(a)
    text = vectorizer.transform([text])

    y_pred = svc.predict_proba(text)

    otvet = {}

    for i in range(len(y_pred[0])):

        mini = (sorted(list(y_pred[0]))[::-1][2])

        if y_pred[0][i] >= mini:

            # Значение, по которому нужно найти ключ
            search_value = i

            # Нахождение ключа по значению
            found_key = find_key_by_value(file_path, search_value)

            if found_key:
                #print(found_key, y_pred[0][i])
                otvet[found_key] = y_pred[0][i]
            else:
                print(f"Ключ для значения '{search_value}' не найден")

    print(otvet)
                
    return otvet

def main(path):

    # Путь к файлу с словарем
    file_path = 'num_to_class.txt'

    return text_to_cat(path, file_path)

