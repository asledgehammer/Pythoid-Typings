from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import Stack

class AStarPathFinder:

  def __init__(self): ...

  class PathFindProgress(Enum):

    failed: AStarPathFinder.PathFindProgress

    found: AStarPathFinder.PathFindProgress

    notrunning: AStarPathFinder.PathFindProgress

    notyetfound: AStarPathFinder.PathFindProgress

    @staticmethod
    def valueOf(arg0: str) -> AStarPathFinder.PathFindProgress: ...

    @staticmethod
    def values() -> list[AStarPathFinder.PathFindProgress]: ...


class AStarPathFinderResult:

  def __init__(self):
    self.maxsearchdistance: int
    self.progress: AStarPathFinder.PathFindProgress


class IPathfinder:

  def Failed(self, mover: Mover) -> None: ...

  def Succeeded(self, path: Path, mover: Mover) -> None: ...

  def getName(self) -> str: ...


class Mover:

  def getID(self) -> int: ...

  def getPathFindIndex(self) -> int: ...


class Path:

  stepstore: Stack[Path.Step]

  def appendStep(self, x: int, y: int, z: int) -> None: ...

  def contains(self, x: int, y: int, z: int) -> bool: ...

  def costPerStep(self) -> float: ...

  def getLength(self) -> int: ...

  def getStep(self, index: int) -> Path.Step: ...

  def getX(self, index: int) -> int: ...

  def getY(self, index: int) -> int: ...

  def getZ(self, index: int) -> int: ...

  def prependStep(self, x: int, y: int, z: int) -> None: ...

  @staticmethod
  def createStep() -> Path.Step: ...

  def __init__(self):
    self.cost: float

  class Step:

    def equals(self, other: object) -> bool: ...

    def getX(self) -> int: ...

    def getY(self) -> int: ...

    def getZ(self) -> int: ...

    def hashCode(self) -> int: ...

    @overload
    def __init__(self):
      self.x: int

      self.y: int

      self.z: int

    @overload
    def __init__(self, x: int, y: int, z: int): ...

