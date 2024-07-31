from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.security import GeneralSecurityException

class AlgorithmParameterSpec: ...


class EncodedKeySpec:

  def getAlgorithm(self) -> str: ...

  def getEncoded(self) -> list[int]: ...

  def getFormat(self) -> str: ...

  def __init__(self, arg0: list[int]): ...


class InvalidParameterSpecException(GeneralSecurityException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class KeySpec: ...

