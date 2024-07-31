from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import Calendar, Date
from java.util.function import Consumer
from se.krka.kahlua.vm import LuaCallFrame, KahluaTable, KahluaThread, Platform

class BaseLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def collectgarbage(arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def luaEquals(arg0: object, arg1: object) -> bool: ...

  @staticmethod
  def pcall(arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def register(arg0: KahluaTable) -> None: ...

  @staticmethod
  def setPrintCallback(arg0: Consumer[str]) -> None: ...

  @staticmethod
  def setmetatable(arg0: KahluaThread, arg1: object, arg2: KahluaTable, arg3: bool) -> None: ...

  def __init__(self, arg0: int): ...


class CoroutineLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

  def __init__(self, arg0: int): ...


class OsLib:

  TIME_DIVIDEND: int

  TIME_DIVIDEND_INVERTED: float

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def formatTime(arg0: str, arg1: Calendar) -> str: ...

  @staticmethod
  def getDateFromTable(arg0: KahluaTable) -> Date: ...

  @staticmethod
  def getDayOfYear(arg0: Calendar) -> int: ...

  @staticmethod
  def getTableFromDate(arg0: Calendar, arg1: Platform) -> KahluaTable: ...

  @staticmethod
  def getWeekOfYear(arg0: Calendar, arg1: bool, arg2: bool) -> int: ...

  @staticmethod
  @overload
  def getdate(arg0: str, arg1: Platform) -> object: ...

  @staticmethod
  @overload
  def getdate(arg0: str, arg1: int, arg2: Platform) -> object: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...


class RandomLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

  def __init__(self, arg0: int): ...


class StringLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

  @staticmethod
  def roundToPrecision(arg0: float, arg1: int) -> float: ...

  @staticmethod
  def roundToSignificantNumbers(arg0: float, arg1: int) -> float: ...

  def __init__(self, arg0: int): ...

  class MatchState:

    def getCapture(self, arg0: int) -> object: ...

    def __init__(self, arg0: LuaCallFrame, arg1: StringLib.StringPointer, arg2: int):
      self.callframe: LuaCallFrame
      self.capture: list[StringLib.MatchState.Capture]
      self.endindex: int
      self.level: int
      self.src_init: StringLib.StringPointer

    class Capture:

      def __init__(self):
        self.init: StringLib.StringPointer
        self.len: int

  class StringPointer:

    def compareTo(self, arg0: StringLib.StringPointer, arg1: int) -> int: ...

    @overload
    def getChar(self) -> str: ...

    @overload
    def getChar(self, arg0: int) -> str: ...

    def getClone(self) -> StringLib.StringPointer: ...

    def getIndex(self) -> int: ...

    def getString(self) -> str: ...

    @overload
    def getStringLength(self) -> int: ...

    @overload
    def getStringLength(self, arg0: int) -> int: ...

    def getStringSubString(self, arg0: int) -> str: ...

    def length(self) -> int: ...

    def postIncrString(self, arg0: int) -> str: ...

    def postIncrStringI(self, arg0: int) -> int: ...

    def preIncrStringI(self, arg0: int) -> int: ...

    def setIndex(self, arg0: int) -> None: ...

    @overload
    def __init__(self, arg0: str): ...
    @overload
    def __init__(self, arg0: str, arg1: int): ...


class TableLib:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def append(arg0: KahluaThread, arg1: KahluaTable, arg2: object) -> None: ...

  @staticmethod
  @overload
  def insert(arg0: KahluaThread, arg1: KahluaTable, arg2: object) -> None: ...

  @staticmethod
  @overload
  def insert(arg0: KahluaThread, arg1: KahluaTable, arg2: int, arg3: object) -> None: ...

  @staticmethod
  def rawappend(arg0: KahluaTable, arg1: object) -> None: ...

  @staticmethod
  def rawinsert(arg0: KahluaTable, arg1: int, arg2: object) -> None: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

  @staticmethod
  @overload
  def remove(arg0: KahluaThread, arg1: KahluaTable) -> object: ...

  @staticmethod
  @overload
  def remove(arg0: KahluaThread, arg1: KahluaTable, arg2: int) -> object: ...

  def __init__(self, arg0: int): ...

