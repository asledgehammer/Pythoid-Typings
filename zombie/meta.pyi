from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.iso import IsoGridSquare

class Meta:

  instance: Meta

  def dealWithSquareSeen(self, square: IsoGridSquare) -> None: ...

  def dealWithSquareSeenActual(self, square: IsoGridSquare) -> None: ...

  def update(self) -> None: ...

  def __init__(self): ...

