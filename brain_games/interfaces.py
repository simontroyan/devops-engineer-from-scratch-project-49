from abc import ABC, abstractmethod


class IGame(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        """Game description"""
        pass

    @abstractmethod
    def generate_question(self) -> str:
        """Generate question and return it as string"""
        pass

    @abstractmethod
    def get_correct_answer(self) -> str:
        """Get correct answer"""
        pass
