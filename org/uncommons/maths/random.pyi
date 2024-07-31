from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import Random

class CellularAutomatonRNG(Random):

  @overload
  def getSeed(self) -> list[int]: ...

  @overload
  def getSeed(self) -> list[int]: ...

  def next(self, arg0: int) -> int: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: SeedGenerator): ...


class SeedGenerator:

  def generateSeed(self, arg0: int) -> list[int]: ...

