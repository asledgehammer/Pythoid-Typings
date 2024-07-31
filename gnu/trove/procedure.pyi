from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

T = TypeVar('T', default=Any)
K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)

class TByteProcedure:

  def execute(self, arg0: int) -> bool: ...


class TFloatProcedure:

  def execute(self, arg0: float) -> bool: ...


class TIntIntProcedure:

  def execute(self, arg0: int, arg1: int) -> bool: ...


class TIntLongProcedure:

  def execute(self, arg0: int, arg1: int) -> bool: ...


class TIntObjectProcedure[T]:

  def execute(self, arg0: int, arg1: object) -> bool: ...


class TIntProcedure:

  def execute(self, arg0: int) -> bool: ...


class TLongObjectProcedure[T]:

  def execute(self, arg0: int, arg1: object) -> bool: ...


class TLongProcedure:

  def execute(self, arg0: int) -> bool: ...


class TObjectIntProcedure[K]:

  def execute(self, arg0: object, arg1: int) -> bool: ...


class TObjectObjectProcedure[K, V]:

  def execute(self, arg0: object, arg1: object) -> bool: ...


class TObjectProcedure[T]:

  def execute(self, arg0: object) -> bool: ...


class TShortObjectProcedure[T]:

  def execute(self, arg0: int, arg1: object) -> bool: ...


class TShortProcedure:

  def execute(self, arg0: int) -> bool: ...


class TShortShortProcedure:

  def execute(self, arg0: int, arg1: int) -> bool: ...

