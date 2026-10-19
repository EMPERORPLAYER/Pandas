import pandas as pd


print("--- Завдання 1 ---")


data = {
    "Ім'я": ["Олександр", "Марія", "Іван", "Софія", "Андрій"],
    "Вік": [25, 30, 22, 27, 35],
    "Місто": ["Київ", "Львів", "Одеса", "Харків", "Дніпро"],
}
df_users = pd.DataFrame(data)


print("Весь DataFrame:")
print(df_users)
print("\n")


rows, columns = df_users.shape
print(f"Кількість рядків: {rows}, кількість стовпців: {columns}")


print("Назви стовпців:", list(df_users.columns))


print("Перші три рядки:")
print(df_users.head(3))



print("\n--- Завдання 2 ---")



file_path = "movies.csv"

try:

  df_movies = pd.read_csv(file_path)


  print("Перші п'ять рядків файлу:")
  print(df_movies.head(5))
  print("\n")


  m_rows, m_cols = df_movies.shape
  print(f"Загальна кількість рядків: {m_rows}, стовпців: {m_cols}")


  print("Типи даних стовпців:")
  print(df_movies.dtypes)


  print("Кількість пропусків у кожному стовпці:")
  print(df_movies.isnull().sum())

except FileNotFoundError:
  print(
      f"Файл '{file_path}' не знайдено. Переконайтеся, що файл існує та шлях"
      " вказано правильно."
  )

print("--- Завдання 3 ---")


data_emp = {
    "Ім'я": ["Олег", "Ірина", "Максим", "Ольга", "Віктор"],
    "Вік": [28, 42, 35, 24, 50],
    "Відділ": ["IT", "HR", "IT", "Marketing", "Finance"],
    "Зарплата": [45000, 60000, 75000, 38000, 90000],
}
df_employees = pd.DataFrame(data_emp)

print("Початкова таблиця співробітників:")
print(df_employees)
print("\n")


high_salary = df_employees[df_employees["Зарплата"] > 50000]
print("Співробітники із зарплатою вищою за 50000:")
print(high_salary)
print("\n")


sorted_by_age = df_employees.sort_values(by="Вік", ascending=True)
print("Таблиця, відсортована за віком (зростання):")
print(sorted_by_age)
print("\n")


sorted_by_salary = df_employees.sort_values(by="Зарплата", ascending=False)
print("Таблиця, відсортована за зарплатою (спадання):")
print(sorted_by_salary)