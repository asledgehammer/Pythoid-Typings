from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation

class Result:

  PI_DISABLE_OUTPUT_ESCAPING: str

  PI_ENABLE_OUTPUT_ESCAPING: str

  def getSystemId(self) -> str: ...

  def setSystemId(self, arg0: str) -> None: ...


class Source:

  def getSystemId(self) -> str: ...

  def isEmpty(self) -> bool: ...

  def setSystemId(self, arg0: str) -> None: ...

