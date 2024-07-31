from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream, Reader
from se.krka.kahlua.vm import LuaCallFrame, KahluaTable, LuaClosure

class LuaCompiler:

  rewriteEvents: bool

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  @overload
  def loadis(arg0: InputStream, arg1: str, arg2: KahluaTable) -> LuaClosure: ...

  @staticmethod
  @overload
  def loadis(arg0: Reader, arg1: str, arg2: KahluaTable) -> LuaClosure: ...

  @staticmethod
  def loadstream(arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def loadstring(arg0: str, arg1: str, arg2: KahluaTable) -> LuaClosure: ...

  @staticmethod
  def register(arg0: KahluaTable) -> None: ...

