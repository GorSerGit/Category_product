Модель для классификации товаров по категориям.

Исходные данные - Json файл от интернет магазина со списком названий товаров их описанием и категорией
Товары содержат название, описание и категории. Некоторые товары принадлежат нескольким категориям.
 
Подход к решению: 
1. Удалить все пропущенные значения т.к. обучать модель на пропусках не получится
2. Объединить все текстовые признаки в один большой признак
3. Представить текстовый признак в виде основ слов и избавиться от служебных символов
4. Разделить записи с описанием и несколькими признаками на несколько записей с тем же описанием и каждым признаком
5. Преобразовать признаки в числовые значения (для работы модели) и сохранить расшифровку
6. Обучить модель vectorizer для преобразования текстовых признаков в числа
7. Обучить основную модель

Результаты: 
Лучшие результаты получила модель мультиноминальной логистической регрессии

Модели код для запуск представлены в папке run


