from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from zombie.iso import Vector2

class Polygon:

  def BuildEdges(self) -> None: ...

  def Center(self) -> Vector2: ...

  @overload
  def Offset(self, v: Vector2) -> None: ...

  @overload
  def Offset(self, x: float, y: float) -> None: ...

  def Set(self, x: float, y: float, x2: float, y2: float) -> None: ...

  def __init__(self):
    self.edges: ArrayList[Vector2]
    self.points: ArrayList[Vector2]

