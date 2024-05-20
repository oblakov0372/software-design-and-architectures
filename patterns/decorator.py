class Text:
    def __init__(self, content: str):
        self._content = content

    def render(self):
        return self._content


class TextDecorator(Text):
    def __init__(self, wrapped: Text):
        self._wrapped = wrapped

    def render(self):
        return self._wrapped.render()


class StarDecorator(TextDecorator):
    def render(self):
        return f"*** {self._wrapped.render()} ***"


class ExclamationDecorator(TextDecorator):
    def render(self):
        return f"{self._wrapped.render()}!!!"


# Пример использования
simple_text = Text("Hello, world")
print(simple_text.render())  # Output: Hello, world

# Добавляем декоратор звездочек
star_decorated_text = StarDecorator(simple_text)
print(star_decorated_text.render())  # Output: *** Hello, world ***

# Добавляем декоратор восклицательных знаков поверх декоратора звездочек
exclamation_decorated_text = ExclamationDecorator(star_decorated_text)
print(exclamation_decorated_text.render())  # Output: *** Hello, world ***!!!
