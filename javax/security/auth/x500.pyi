from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream
from java.util import Map
from javax.security.auth import Subject

class X500Principal:

  CANONICAL: str

  RFC1779: str

  RFC2253: str

  @overload
  def equals(self, arg0: object) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  def getEncoded(self) -> list[int]: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self, arg0: str) -> str: ...

  @overload
  def getName(self, arg0: str, arg1: Map[str, str]) -> str: ...

  @overload
  def hashCode(self) -> int: ...

  @overload
  def hashCode(self) -> int: ...

  def implies(self, arg0: Subject) -> bool: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: InputStream): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: Map[str, str]): ...

