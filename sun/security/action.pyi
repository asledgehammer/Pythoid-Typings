from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Boolean
from java.util import Properties

class GetBooleanAction:

  @overload
  def run(self) -> object: ...

  @overload
  def run(self) -> Boolean: ...

  @overload
  def run(self) -> object: ...

  @staticmethod
  def privilegedGetProperty(arg0: str) -> bool: ...

  def __init__(self, arg0: str): ...


class GetPropertyAction:

  @overload
  def run(self) -> object: ...

  @overload
  def run(self) -> str: ...

  @overload
  def run(self) -> object: ...

  @staticmethod
  def privilegedGetProperties() -> Properties: ...

  @staticmethod
  @overload
  def privilegedGetProperty(arg0: str) -> str: ...

  @staticmethod
  @overload
  def privilegedGetProperty(arg0: str, arg1: str) -> str: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str): ...

