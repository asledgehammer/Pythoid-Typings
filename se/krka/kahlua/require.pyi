from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import Reader
from java.lang import Enum
from se.krka.kahlua.vm import LuaCallFrame, KahluaTable

class Loadfile:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def install(self, arg0: KahluaTable) -> None: ...

  def __init__(self, arg0: LuaSourceProvider): ...


class LuaSourceProvider:

  def getLuaSource(self, arg0: str) -> Reader: ...


class Require:

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  @overload
  def call(self, arg0: LuaCallFrame, arg1: int) -> int: ...

  def install(self, arg0: KahluaTable) -> None: ...

  def __init__(self, arg0: LuaSourceProvider): ...

  class Result:

    LOADED: Require.Result

    LOADING: Require.Result

    @staticmethod
    def error(arg0: str) -> Require.Result: ...

  class State(Enum):

    BROKEN: Require.State

    LOADED: Require.State

    LOADING: Require.State

    @staticmethod
    def valueOf(arg0: str) -> Require.State: ...

    @staticmethod
    def values() -> list[Require.State]: ...

