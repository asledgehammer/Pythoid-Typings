from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum

class When(Enum):

  ALWAYS: When

  MAYBE: When

  NEVER: When

  UNKNOWN: When

  @staticmethod
  def valueOf(arg0: str) -> When: ...

  @staticmethod
  def values() -> list[When]: ...

