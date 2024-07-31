from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class
from org.hamcrest import Matcher
from org.junit.function import ThrowingRunnable

T = TypeVar('T', default=Any)

class Assert:

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[int], arg1: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[str], arg1: list[str]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[int], arg1: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[int], arg1: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[object], arg1: list[object]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[int], arg1: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[bool], arg1: list[bool]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[float], arg1: list[float], arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: list[float], arg1: list[float], arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[str], arg2: list[str]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[object], arg2: list[object]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[int], arg2: list[int]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[bool], arg2: list[bool]) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[float], arg2: list[float], arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertArrayEquals(arg0: str, arg1: list[float], arg2: list[float], arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: list[object], arg1: list[object]) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: float, arg1: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: object, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: float, arg1: float, arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: float, arg1: float, arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: list[object], arg2: list[object]) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: float, arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: object, arg2: object) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: int, arg2: int) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertEquals(arg0: str, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertFalse(arg0: bool) -> None: ...

  @staticmethod
  @overload
  def assertFalse(arg0: str, arg1: bool) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: object, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: float, arg1: float, arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: float, arg1: float, arg2: float) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: str, arg1: object, arg2: object) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: str, arg1: int, arg2: int) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: str, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertNotEquals(arg0: str, arg1: float, arg2: float, arg3: float) -> None: ...

  @staticmethod
  @overload
  def assertNotNull(arg0: object) -> None: ...

  @staticmethod
  @overload
  def assertNotNull(arg0: str, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertNotSame(arg0: object, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertNotSame(arg0: str, arg1: object, arg2: object) -> None: ...

  @staticmethod
  @overload
  def assertNull(arg0: object) -> None: ...

  @staticmethod
  @overload
  def assertNull(arg0: str, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertSame(arg0: object, arg1: object) -> None: ...

  @staticmethod
  @overload
  def assertSame(arg0: str, arg1: object, arg2: object) -> None: ...

  @staticmethod
  @overload
  def assertThat(arg0: object, arg1: Matcher[T]) -> None: ...

  @staticmethod
  @overload
  def assertThat(arg0: str, arg1: object, arg2: Matcher[T]) -> None: ...

  @staticmethod
  @overload
  def assertThrows(arg0: Class[T], arg1: ThrowingRunnable) -> T: ...

  @staticmethod
  @overload
  def assertThrows(arg0: str, arg1: Class[T], arg2: ThrowingRunnable) -> T: ...

  @staticmethod
  @overload
  def assertTrue(arg0: bool) -> None: ...

  @staticmethod
  @overload
  def assertTrue(arg0: str, arg1: bool) -> None: ...

  @staticmethod
  @overload
  def fail() -> None: ...

  @staticmethod
  @overload
  def fail(arg0: str) -> None: ...

