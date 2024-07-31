from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.junit import Assert

class PZCryptTest(Assert):

  def hash(self) -> None: ...

  def hashSalt(self) -> None: ...

  def __init__(self): ...


class PZcrypt:

  @staticmethod
  def checkHashSalt(generatedSecuredPasswordHash: str, originalPassword: str) -> bool: ...

  @staticmethod
  @overload
  def hash(originalPassword: str) -> str: ...

  @staticmethod
  @overload
  def hash(originalPassword: str, checkNull: bool) -> str: ...

  @staticmethod
  def hashSalt(originalPassword: str) -> str: ...

  def __init__(self): ...

