def log_action(a, b, operation, result):
    """Записує дані у файл log.txt"""
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Введені числа: {a}, {b}; Операція: {operation}; Результат: {result}\n")