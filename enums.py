from enum import Enum
from typing import Any

class Vesta(Enum):
    GPT4o_20Turn = ("gpt-4o", 20)
    GPT4o_1Turn = ("gpt-4o", 1)
    GPT35_20Turn = ("gpt-3.5-turbo", 20)
    GPT35_1Turn = ("gpt-3.5-turbo", 1)

    def get_model_type(self):
        return self.value[0]

    def get_turn_limit(self):
        return self.value[1]
    
    @staticmethod
    def get_model_list():
        return [model for model in Vesta]

class BaseEnum(Enum):
    @classmethod
    def list(cls):
        return [t for t in cls]

class ModelType(BaseEnum):
    GPT4o = "gpt-4o"
    GPT35 = "gpt-3.5-turbo"
    
class TurnLimit(BaseEnum):
    TWENTY = 20
    FIVE = 5
    ONE = 1

class GameType(BaseEnum):
    NORMAL = "normal"
    HEEJIN = "heejin"
    JEONGJUN = "jeongjun"