from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum

T = TypeVar('T', default=Any)

class CompareMethod(Enum):

  equals: CompareMethod

  lessthan: CompareMethod

  lessthanorequals: CompareMethod

  morethan: CompareMethod

  morethanorequals: CompareMethod

  notequals: CompareMethod

  @staticmethod
  def valueOf(arg0: str) -> CompareMethod: ...

  @staticmethod
  def values() -> list[CompareMethod]: ...


class CompareResult(Enum):

  # False: CompareResult

  Invalid: CompareResult

  # True: CompareResult

  @staticmethod
  def valueOf(arg0: str) -> CompareResult: ...

  @staticmethod
  def values() -> list[CompareResult]: ...


class EditGlobal:

  def getGlobal(self) -> RadioGlobal: ...

  def getOperator(self) -> EditGlobalOps: ...

  def getValue(self) -> RadioGlobal: ...

  def __init__(self, g: RadioGlobal, op: EditGlobalOps, val: RadioGlobal): ...


class EditGlobalEvent(Enum):

  OnBroadcastRemove: EditGlobalEvent

  OnBroadcastSetActive: EditGlobalEvent

  OnExit: EditGlobalEvent

  OnPlayerListens: EditGlobalEvent

  OnPlayerListensOnce: EditGlobalEvent

  OnPostDelay: EditGlobalEvent

  OnSetActive: EditGlobalEvent

  @staticmethod
  def valueOf(arg0: str) -> EditGlobalEvent: ...

  @staticmethod
  def values() -> list[EditGlobalEvent]: ...


class EditGlobalOps(Enum):

  add: EditGlobalOps

  set: EditGlobalOps

  sub: EditGlobalOps

  @staticmethod
  def valueOf(arg0: str) -> EditGlobalOps: ...

  @staticmethod
  def values() -> list[EditGlobalOps]: ...


class RadioGlobal[T]:

  def compare(self, target: RadioGlobal, method: CompareMethod) -> CompareResult: ...

  def getName(self) -> str: ...

  def getString(self) -> str: ...

  def getType(self) -> RadioGlobalType: ...

  def setValue(self, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...


class RadioGlobalBool(RadioGlobal):

  def compare(self, target: RadioGlobal, method: CompareMethod) -> CompareResult: ...

  def getString(self) -> str: ...

  def getValue(self) -> bool: ...

  @overload
  def setValue(self, value: bool) -> None: ...

  @overload
  def setValue(self, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...

  @overload
  def __init__(self, value: bool): ...
  @overload
  def __init__(self, name: str, value: bool): ...


class RadioGlobalFloat(RadioGlobal):

  def compare(self, target: RadioGlobal, method: CompareMethod) -> CompareResult: ...

  def getString(self) -> str: ...

  def getValue(self) -> float: ...

  @overload
  def setValue(self, value: float) -> None: ...

  @overload
  def setValue(self, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...

  @overload
  def __init__(self, value: float): ...
  @overload
  def __init__(self, name: str, value: float): ...


class RadioGlobalInt(RadioGlobal):

  def compare(self, target: RadioGlobal, method: CompareMethod) -> CompareResult: ...

  def getString(self) -> str: ...

  def getValue(self) -> int: ...

  @overload
  def setValue(self, value: int) -> None: ...

  @overload
  def setValue(self, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...

  @overload
  def __init__(self, value: int): ...
  @overload
  def __init__(self, name: str, value: int): ...


class RadioGlobalString(RadioGlobal):

  def compare(self, target: RadioGlobal, method: CompareMethod) -> CompareResult: ...

  def getString(self) -> str: ...

  def getValue(self) -> str: ...

  @overload
  def setValue(self, value: str) -> None: ...

  @overload
  def setValue(self, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...

  @overload
  def __init__(self, value: str): ...
  @overload
  def __init__(self, name: str, value: str): ...


class RadioGlobalType(Enum):

  Boolean: RadioGlobalType

  Float: RadioGlobalType

  Integer: RadioGlobalType

  Invalid: RadioGlobalType

  String: RadioGlobalType

  @staticmethod
  def valueOf(arg0: str) -> RadioGlobalType: ...

  @staticmethod
  def values() -> list[RadioGlobalType]: ...


class RadioGlobalsManager:

  def addGlobal(self, name: str, arg1: RadioGlobal) -> bool: ...

  def addGlobalBool(self, name: str, value: bool) -> bool: ...

  def addGlobalFloat(self, name: str, value: float) -> bool: ...

  def addGlobalInt(self, name: str, value: int) -> bool: ...

  def addGlobalString(self, name: str, value: str) -> bool: ...

  @overload
  def compare(self, globalA: str, globalB: str, compareMethod: CompareMethod) -> CompareResult: ...

  @overload
  def compare(self, A: RadioGlobal, B: RadioGlobal, compareMethod: CompareMethod) -> CompareResult: ...

  def exists(self, name: str) -> bool: ...

  def getGlobal(self, name: str) -> RadioGlobal: ...

  def getGlobalBool(self, name: str) -> RadioGlobalBool: ...

  def getGlobalFloat(self, name: str) -> RadioGlobalFloat: ...

  def getGlobalInt(self, name: str) -> RadioGlobalInt: ...

  def getGlobalString(self, name: str) -> RadioGlobalString: ...

  def getString(self, name: str) -> str: ...

  def getType(self, name: str) -> RadioGlobalType: ...

  def reset(self) -> None: ...

  @overload
  def setGlobal(self, name: str, value: bool) -> bool: ...

  @overload
  def setGlobal(self, name: str, value: float) -> bool: ...

  @overload
  def setGlobal(self, name: str, value: int) -> bool: ...

  @overload
  def setGlobal(self, name: str, value: str) -> bool: ...

  @overload
  def setGlobal(self, name: str, value: RadioGlobal, operator: EditGlobalOps) -> bool: ...

  @staticmethod
  def getInstance() -> RadioGlobalsManager: ...

