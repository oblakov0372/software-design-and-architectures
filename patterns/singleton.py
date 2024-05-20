class Singleton:
    _instance = None  # Класс-атрибут для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Проверка, существует ли уже экземпляр
            # Вызов __new__ родительского класса (object), чтобы создать новый экземпляр
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value):
        # Проверка, был ли экземпляр уже инициализирован
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = (
                True  # Устанавливаем флаг, чтобы не инициализировать повторно
            )


# Пример использования
singleton1 = Singleton("First Instance")
print(singleton1.value)  # Output: First Instance

singleton2 = Singleton("Second Instance")
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True
