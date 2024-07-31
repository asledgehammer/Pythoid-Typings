from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from se.krka.kahlua.j2se import KahluaTableImpl
from zombie.characters import IsoGameCharacter

class IReplace:

  def getString(self) -> str: ...


class IReplaceProvider:

  def getReplacer(self, key: str) -> IReplace: ...

  def hasReplacer(self, key: str) -> bool: ...


class ITemplateBuilder:

  @overload
  def Build(self, input: str) -> str: ...

  @overload
  def Build(self, input: str, table: KahluaTableImpl) -> str: ...

  @overload
  def Build(self, input: str, replaceProvider: IReplaceProvider) -> str: ...

  @overload
  def RegisterKey(self, key: str, table: KahluaTableImpl) -> None: ...

  @overload
  def RegisterKey(self, key: str, replace: IReplace) -> None: ...

  def Reset(self) -> None: ...


class ReplaceList:

  @overload
  def getString(self) -> str: ...

  @overload
  def getString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, replacements: ArrayList[str]): ...


class ReplaceProvider:

  @overload
  def addKey(self, key: str, value: str) -> None: ...

  @overload
  def addKey(self, key: str, table: KahluaTableImpl) -> None: ...

  def addReplacer(self, key: str, replace: IReplace) -> None: ...

  @overload
  def getReplacer(self, key: str) -> IReplace: ...

  @overload
  def getReplacer(self, key: str) -> IReplace: ...

  @overload
  def hasReplacer(self, key: str) -> bool: ...

  @overload
  def hasReplacer(self, key: str) -> bool: ...

  def __init__(self): ...


class ReplaceProviderCharacter(ReplaceProvider):

  def __init__(self, character: IsoGameCharacter): ...


class ReplaceProviderLua(ReplaceProvider):

  def addKey(self, key: str, value: str) -> None: ...

  def fromLuaTable(self, table: KahluaTableImpl) -> None: ...

  def release(self) -> None: ...

  def __init__(self): ...


class ReplaceSingle:

  @overload
  def getString(self) -> str: ...

  @overload
  def getString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, value: str): ...


class TemplateText:

  @staticmethod
  @overload
  def Build(input: str) -> str: ...

  @staticmethod
  @overload
  def Build(input: str, table: KahluaTableImpl) -> str: ...

  @staticmethod
  @overload
  def Build(input: str, replaceProvider: IReplaceProvider) -> str: ...

  @staticmethod
  def Initialize() -> None: ...

  @staticmethod
  @overload
  def RandNext(bound: float) -> float: ...

  @staticmethod
  @overload
  def RandNext(bound: int) -> int: ...

  @staticmethod
  @overload
  def RandNext(min: float, max: float) -> float: ...

  @staticmethod
  @overload
  def RandNext(min: int, max: int) -> int: ...

  @staticmethod
  @overload
  def RegisterKey(key: str, table: KahluaTableImpl) -> None: ...

  @staticmethod
  @overload
  def RegisterKey(key: str, replace: IReplace) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self): ...


class TemplateTextBuilder:

  @overload
  def Build(self, input: str) -> str: ...

  @overload
  def Build(self, input: str) -> str: ...

  @overload
  def Build(self, input: str, table: KahluaTableImpl) -> str: ...

  @overload
  def Build(self, input: str, table: KahluaTableImpl) -> str: ...

  @overload
  def Build(self, input: str, replaceProvider: IReplaceProvider) -> str: ...

  @overload
  def Build(self, input: str, replaceProvider: IReplaceProvider) -> str: ...

  @overload
  def RegisterKey(self, key: str, table: KahluaTableImpl) -> None: ...

  @overload
  def RegisterKey(self, key: str, table: KahluaTableImpl) -> None: ...

  @overload
  def RegisterKey(self, key: str, replace: IReplace) -> None: ...

  @overload
  def RegisterKey(self, key: str, replace: IReplace) -> None: ...

  @overload
  def Reset(self) -> None: ...

  @overload
  def Reset(self) -> None: ...

