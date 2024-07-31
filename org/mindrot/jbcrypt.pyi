from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.security import SecureRandom

class BCrypt:

  def crypt_raw(self, arg0: list[int], arg1: list[int], arg2: int, arg3: list[int]) -> list[int]: ...

  @staticmethod
  def checkpw(arg0: str, arg1: str) -> bool: ...

  @staticmethod
  @overload
  def gensalt() -> str: ...

  @staticmethod
  @overload
  def gensalt(arg0: int) -> str: ...

  @staticmethod
  @overload
  def gensalt(arg0: int, arg1: SecureRandom) -> str: ...

  @staticmethod
  def hashpw(arg0: str, arg1: str) -> str: ...

  def __init__(self): ...

