from var1 import DataSort

def main():
    file_name = "var1.csv" 
    print("Шаг 1: Загрузка исходной таблицы...")
    processor = DataSort(file_path=file_name)
    print("\nШаг 2: Очистка данных от повторов...")
    processor = ~processor  
    print("\nШаг 3: Разделение данных по типам участников...")
    processor.divide_save()


main()