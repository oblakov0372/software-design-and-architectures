class Observer:
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class TemperatureObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} получил уведомление: {message}")


# Создаем субъект
temperature_subject = Subject()

# Создаем наблюдателей
observer1 = TemperatureObserver("Observer 1")
observer2 = TemperatureObserver("Observer 2")

# Присоединяем наблюдателей к субъекту
temperature_subject.attach(observer1)
temperature_subject.attach(observer2)

# Уведомляем наблюдателей об изменении состояния
temperature_subject.notify("Температура изменилась до 25°C")

# Отсоединяем одного наблюдателя и снова уведомляем
temperature_subject.detach(observer1)
temperature_subject.notify("Температура изменилась до 30°C")
