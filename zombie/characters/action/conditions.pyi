from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import HashMap
from org.w3c.dom import Element
from zombie.characters.action import IActionCondition, ActionContext

class CharacterVariableCondition:

  s_factoryMap: HashMap[str, IActionCondition.IFactory]

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @staticmethod
  def createInstance(arg0: Element) -> IActionCondition: ...

  @staticmethod
  def registerFactory(arg0: str, arg1: IActionCondition.IFactory) -> None: ...

  def __init__(self): ...

  class CharacterVariableLookup:

    def toString(self) -> str: ...

    def __init__(self, arg0: str):
      self.variablename: str

  class Operator(Enum):

    Equal: CharacterVariableCondition.Operator

    Greater: CharacterVariableCondition.Operator

    GreaterEqual: CharacterVariableCondition.Operator

    Less: CharacterVariableCondition.Operator

    LessEqual: CharacterVariableCondition.Operator

    NotEqual: CharacterVariableCondition.Operator

    @staticmethod
    def valueOf(arg0: str) -> CharacterVariableCondition.Operator: ...

    @staticmethod
    def values() -> list[CharacterVariableCondition.Operator]: ...

  class Factory:

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    def __init__(self): ...


class EventNotOccurred:

  s_factoryMap: HashMap[str, IActionCondition.IFactory]

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @staticmethod
  def createInstance(arg0: Element) -> IActionCondition: ...

  @staticmethod
  def registerFactory(arg0: str, arg1: IActionCondition.IFactory) -> None: ...

  def __init__(self):
    self.eventname: str

  class Factory:

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    def __init__(self): ...


class EventOccurred:

  s_factoryMap: HashMap[str, IActionCondition.IFactory]

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @staticmethod
  def createInstance(arg0: Element) -> IActionCondition: ...

  @staticmethod
  def registerFactory(arg0: str, arg1: IActionCondition.IFactory) -> None: ...

  def __init__(self):
    self.eventname: str

  class Factory:

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    def __init__(self): ...


class LuaCall:

  s_factoryMap: HashMap[str, IActionCondition.IFactory]

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IActionCondition: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def getDescription(self) -> str: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @overload
  def passes(self, context: ActionContext, layerIdx: int) -> bool: ...

  @staticmethod
  def createInstance(arg0: Element) -> IActionCondition: ...

  @staticmethod
  def registerFactory(arg0: str, arg1: IActionCondition.IFactory) -> None: ...

  def __init__(self): ...

  class Factory:

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    @overload
    def create(self, conditionNode: Element) -> IActionCondition: ...

    def __init__(self): ...

