from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Enum
from java.lang.module import ModuleReference
from java.util import Comparator
from java.util.function import Function, ToDoubleFunction, ToIntFunction, ToLongFunction

U = TypeVar('U', default=Any)
T = TypeVar('T', default=Any)

class LauncherHelper:

  @staticmethod
  def checkAndLoadMain(arg0: bool, arg1: int, arg2: str) -> Class[Any]: ...

  @staticmethod
  def getApplicationClass() -> Class[Any]: ...

  @staticmethod
  def printSystemMetrics() -> None: ...

  class SizePrefix(Enum):

    GIGA: LauncherHelper.SizePrefix

    KILO: LauncherHelper.SizePrefix

    MEGA: LauncherHelper.SizePrefix

    TERA: LauncherHelper.SizePrefix

    @staticmethod
    def valueOf(arg0: str) -> LauncherHelper.SizePrefix: ...

    @staticmethod
    def values() -> list[LauncherHelper.SizePrefix]: ...

  class ResourceBundleHolder: ...

  class FXHelper:

    @staticmethod
    def main(arg0: list[str]) -> None: ...

  class StdArg:

    def toString(self) -> str: ...

  class JrtFirstComparator:

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: ModuleReference, arg1: ModuleReference) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def reversed(self) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

    def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    @staticmethod
    def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def naturalOrder() -> Comparator[T]: ...

    @staticmethod
    def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def reverseOrder() -> Comparator[T]: ...

