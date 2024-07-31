from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Exception

class ParserConfigurationException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...

