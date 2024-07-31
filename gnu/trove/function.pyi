from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

T = TypeVar('T', default=Any)
R = TypeVar('R', default=Any)

class TByteFunction:

  def execute(self, arg0: int) -> int: ...


class TFloatFunction:

  def execute(self, arg0: float) -> float: ...


class TIntFunction:

  def execute(self, arg0: int) -> int: ...


class TLongFunction:

  def execute(self, arg0: int) -> int: ...


class TObjectFunction[T, R]:

  def execute(self, arg0: object) -> object: ...


class TShortFunction:

  def execute(self, arg0: int) -> int: ...

