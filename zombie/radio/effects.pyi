from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.characters import IsoPlayer

class LineEffectMemory:

  def addLine(self, plr: IsoPlayer, lineguid: str) -> None: ...

  def contains(self, plr: IsoPlayer, lineguid: str) -> bool: ...

  def __init__(self): ...

