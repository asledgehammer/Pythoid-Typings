from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Number, ArrayIndexOutOfBoundsException, IndexOutOfBoundsException, StringIndexOutOfBoundsException
from java.nio.charset import Charset
from java.util import List, Map
from java.util.function import BiFunction, Function

X = TypeVar('X', default=Any)

class ArraysSupport:

  LOG2_ARRAY_BOOLEAN_INDEX_SCALE: int

  LOG2_ARRAY_BYTE_INDEX_SCALE: int

  LOG2_ARRAY_CHAR_INDEX_SCALE: int

  LOG2_ARRAY_DOUBLE_INDEX_SCALE: int

  LOG2_ARRAY_FLOAT_INDEX_SCALE: int

  LOG2_ARRAY_INT_INDEX_SCALE: int

  LOG2_ARRAY_LONG_INDEX_SCALE: int

  LOG2_ARRAY_SHORT_INDEX_SCALE: int

  SOFT_MAX_ARRAY_LENGTH: int

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: list[int], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[str], arg1: list[str], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[float], arg1: list[float], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[float], arg1: list[float], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: list[int], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: list[int], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: list[int], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[bool], arg1: list[bool], arg2: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[str], arg1: int, arg2: list[str], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[float], arg1: int, arg2: list[float], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[float], arg1: int, arg2: list[float], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[int], arg1: int, arg2: list[int], arg3: int, arg4: int) -> int: ...

  @staticmethod
  @overload
  def mismatch(arg0: list[bool], arg1: int, arg2: list[bool], arg3: int, arg4: int) -> int: ...

  @staticmethod
  def newLength(arg0: int, arg1: int, arg2: int) -> int: ...

  @staticmethod
  def vectorizedMismatch(arg0: object, arg1: int, arg2: object, arg3: int, arg4: int, arg5: int) -> int: ...


class Preconditions:

  AIOOBE_FORMATTER: BiFunction[str, List[Number], ArrayIndexOutOfBoundsException]

  IOOBE_FORMATTER: BiFunction[str, List[Number], IndexOutOfBoundsException]

  SIOOBE_FORMATTER: BiFunction[str, List[Number], StringIndexOutOfBoundsException]

  @staticmethod
  @overload
  def checkFromIndexSize(arg0: int, arg1: int, arg2: int, arg3: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  @overload
  def checkFromIndexSize(arg0: int, arg1: int, arg2: int, arg3: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  @overload
  def checkFromToIndex(arg0: int, arg1: int, arg2: int, arg3: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  @overload
  def checkFromToIndex(arg0: int, arg1: int, arg2: int, arg3: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  @overload
  def checkIndex(arg0: int, arg1: int, arg2: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  @overload
  def checkIndex(arg0: int, arg1: int, arg2: BiFunction[str, List[Number], X]) -> int: ...

  @staticmethod
  def outOfBoundsExceptionFormatter(arg0: Function[str, X]) -> BiFunction[str, List[Number], X]: ...

  def __init__(self): ...


class StaticProperty:

  @staticmethod
  def fileEncoding() -> str: ...

  @staticmethod
  def javaHome() -> str: ...

  @staticmethod
  def javaIoTmpDir() -> str: ...

  @staticmethod
  def javaLibraryPath() -> str: ...

  @staticmethod
  def javaPropertiesDate() -> str: ...

  @staticmethod
  def jdkSerialFilter() -> str: ...

  @staticmethod
  def jdkSerialFilterFactory() -> str: ...

  @staticmethod
  def jnuCharset() -> Charset: ...

  @staticmethod
  def jnuEncoding() -> str: ...

  @staticmethod
  def nativeEncoding() -> str: ...

  @staticmethod
  def sunBootLibraryPath() -> str: ...

  @staticmethod
  def userDir() -> str: ...

  @staticmethod
  def userHome() -> str: ...

  @staticmethod
  def userName() -> str: ...


class SystemProps:

  @staticmethod
  def initProperties() -> Map[str, str]: ...

  class Raw: ...

