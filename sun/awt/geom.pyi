from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt.geom import PathIterator
from java.util import Vector

class Crossings:

  debug: bool

  def accumulateCubic(self, arg0: float, arg1: float, arg2: list[float]) -> bool: ...

  @overload
  def accumulateLine(self, arg0: float, arg1: float, arg2: float, arg3: float) -> bool: ...

  @overload
  def accumulateLine(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: int) -> bool: ...

  def accumulateQuad(self, arg0: float, arg1: float, arg2: list[float]) -> bool: ...

  def covers(self, arg0: float, arg1: float) -> bool: ...

  def getXHi(self) -> float: ...

  def getXLo(self) -> float: ...

  def getYHi(self) -> float: ...

  def getYLo(self) -> float: ...

  def isEmpty(self) -> bool: ...

  def print(self) -> None: ...

  def record(self, arg0: float, arg1: float, arg2: int) -> None: ...

  @staticmethod
  @overload
  def findCrossings(arg0: PathIterator, arg1: float, arg2: float, arg3: float, arg4: float) -> Crossings: ...

  @staticmethod
  @overload
  def findCrossings(arg0: Vector[Curve], arg1: float, arg2: float, arg3: float, arg4: float) -> Crossings: ...

  def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float): ...

  class EvenOdd(Crossings):

    def covers(self, arg0: float, arg1: float) -> bool: ...

    def record(self, arg0: float, arg1: float, arg2: int) -> None: ...

    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float): ...

  class NonZero(Crossings):

    def covers(self, arg0: float, arg1: float) -> bool: ...

    def insert(self, arg0: int, arg1: float, arg2: float, arg3: int) -> None: ...

    def record(self, arg0: float, arg1: float, arg2: int) -> None: ...

    def remove(self, arg0: int) -> None: ...

    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float): ...


class PathConsumer2D:

  def closePath(self) -> None: ...

  def curveTo(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...

  def getNativeConsumer(self) -> int: ...

  def lineTo(self, arg0: float, arg1: float) -> None: ...

  def moveTo(self, arg0: float, arg1: float) -> None: ...

  def pathDone(self) -> None: ...

  def quadTo(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

