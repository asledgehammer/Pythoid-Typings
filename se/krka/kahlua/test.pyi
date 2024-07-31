from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from se.krka.kahlua.vm import LuaCallFrame, Platform, KahluaTable

class UserdataArray:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @staticmethod
  def register(arg0: Platform, arg1: KahluaTable) -> None: ...

