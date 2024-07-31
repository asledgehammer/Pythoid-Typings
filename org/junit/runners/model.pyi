from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

class Statement:

  def evaluate(self) -> None: ...

  def __init__(self): ...

