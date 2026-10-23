import pandas as pd

class DataSort:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, sep=",", engine="python", encoding='utf-8-sig',on_bad_lines='skip')  #file_path хранит путь к файлу на пк
                                                                      #sep-определяет вид разделителя(в данном случае ;)
                                                                       #encoding- кодировка текста
    def divide_save(self, column_name=None):  #разделение на два файла по определенному признаку
        if column_name is None or column_name not in self.df.columns:
            column_name = self.df.columns[-1]
        unique_values = self.df[column_name].unique() #сохранили все различные названия лиц в переменную уникально(то есть там будет всего два названия без повторений)
        for value in unique_values:
            sub_df = self.df[self.df[column_name] == value]  #выбираем из исходной таблицы только те строки, где в столбце column_name написано текущее значение value
            clean_value = str(value).replace(" ", "_")  #переводим значение в строку и заменяем пробелы на нижнее подчеркивание (из 'физ. лицо' делаем 'физ._лицо')
            file_name = f"{clean_value}.csv"  #формируем строку с полным именем будущего файла на диске с расширением .csv
            sub_df.to_csv(file_name, index=False, encoding='utf-8')  #Сохраняем выделенную таблицу,полученную из исходной, в отдельный файл.
            print(f"Файл успешно сохранен: {file_name} (строк: {len(sub_df)})")

    def __invert__(self):   #будем перегружать унарный оператор ~
        initial_count = len(self.df)   #Считаем и сохраняем начальное количество строк в нашей таблице перед удалением повторов
        self.df = self.df.drop_duplicates()  #метод для удаления одинаковых строк
        final_count = len(self.df)  # Считаем и сохраняем новое количество строк в таблице, которое осталось после так называемой фильтрации
        deleted_count = initial_count - final_count  #Математически находим разницу: вычитаем из исходного количества новое и получаем точное число удаленных дубликатов
        print(f"Количество повторяющихся строк в наборе данных: {deleted_count}")
        return self

    