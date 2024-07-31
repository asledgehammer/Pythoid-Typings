from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.asledgehammer.candle import CandleGraph, CandleClass
from java.lang import Class
from java.util import Map, List

class PythonTypingsRenderer:

  DISCOVERED_CLASSES: Map[str, Class[Any]]

  ILLEGAL: List[str]

  def render(self, arg0: CandleGraph) -> None: ...

  def renderClass(self, arg0: CandleGraph, arg1: CandleClass) -> None: ...

  def __init__(self): ...

