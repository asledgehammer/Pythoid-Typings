from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class

class JsonAdapter:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def nullSafe(self) -> bool: ...

  def toString(self) -> str: ...

  def value(self) -> Class[Any]: ...


class Since:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def value(self) -> float: ...


class Until:

  def annotationType(self) -> Class[Annotation]: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  def value(self) -> float: ...

