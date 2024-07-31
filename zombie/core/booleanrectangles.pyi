from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from org.lwjgl.util import Rectangle

class BooleanRectangleCollection(ArrayList):

  def Intersects(self, rect1: Rectangle, rect2: Rectangle) -> bool: ...

  def IntesectsLine(self, Line1: BooleanRectangleCollection.Line, Line2: BooleanRectangleCollection.Line) -> int: ...

  def IsPointInRect(self, x: int, y: int, rect: Rectangle) -> bool: ...

  def cutRectangle(self, rect: Rectangle) -> None: ...

  @overload
  def doIt(self, rectsToCut: ArrayList[Rectangle], rectToKeep: Rectangle) -> None: ...

  @overload
  def doIt(self, a: Rectangle, b: Rectangle) -> ArrayList[Rectangle]: ...

  def optimize(self) -> None: ...

  def __init__(self): ...

  class Line:

    def __init__(self, arg0: BooleanRectangleCollection, arg1: BooleanRectangleCollection.Point, arg2: BooleanRectangleCollection.Point):
      self.end: BooleanRectangleCollection.Point
      self.start: BooleanRectangleCollection.Point

  class Point:

    @overload
    def __init__(self):
      self.x: int

      self.y: int

    @overload
    def __init__(self, x: int, y: int): ...

