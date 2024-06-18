from abc import ABC, abstractmethod


class FileWorker(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def write_vacancies(self, vacancies):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def del_vacancy_full(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy_one(self, vacancy):
        pass
