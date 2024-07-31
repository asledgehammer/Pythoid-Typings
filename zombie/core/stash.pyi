from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from java.util import ArrayList
from se.krka.kahlua.j2se import KahluaTableImpl
from se.krka.kahlua.vm import KahluaTable
from zombie.inventory import InventoryItem
from zombie.iso import BuildingDef

class Stash:

  def getBuildingX(self) -> int: ...

  def getBuildingY(self) -> int: ...

  def getItem(self) -> str: ...

  def getName(self) -> str: ...

  def load(self, stashDesc: KahluaTableImpl) -> None: ...

  def __init__(self, name: str):
    self.annotations: ArrayList[StashAnnotation]
    self.barricades: int
    self.buildingx: int
    self.buildingy: int
    self.containers: ArrayList[StashContainer]
    self.customname: str
    self.item: str
    self.maxdaytospawn: int
    self.maxtraptospawn: int
    self.mindaytospawn: int
    self.mintraptospawn: int
    self.name: str
    self.spawnonlyonzed: bool
    self.spawntable: str
    self.type: str
    self.zombies: int


class StashAnnotation:

  def fromLua(self, lua: KahluaTable) -> None: ...

  def __init__(self):
    self.b: float
    self.g: float
    self.r: float
    self.symbol: str
    self.text: str
    self.x: float
    self.y: float


class StashBuilding:

  def getName(self) -> str: ...

  def __init__(self, stashName: str, buildingX: int, buildingY: int):
    self.buildingx: int
    self.buildingy: int
    self.stashname: str


class StashContainer:

  def __init__(self, room: str, containerSprite: str, containerType: str):
    self.containeritem: str
    self.containersprite: str
    self.containertype: str
    self.contx: int
    self.conty: int
    self.contz: int
    self.room: str


class StashSystem:

  allStashes: ArrayList[Stash]

  buildingsToDo: ArrayList[StashBuilding]

  possibleStashes: ArrayList[StashBuilding]

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def checkStashItem(item: InventoryItem) -> None: ...

  @staticmethod
  def doBuildingStash(arg0: BuildingDef) -> None: ...

  @staticmethod
  def doStashItem(stash: Stash, item: InventoryItem) -> None: ...

  @staticmethod
  def getPossibleStashes() -> ArrayList[StashBuilding]: ...

  @staticmethod
  def getStash(stashName: str) -> Stash: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def initAllStashes() -> None: ...

  @staticmethod
  def load(input: ByteBuffer, WorldVersion: int) -> None: ...

  @staticmethod
  def prepareBuildingStash(stashName: str) -> None: ...

  @staticmethod
  def reinit() -> None: ...

  @staticmethod
  def save(output: ByteBuffer) -> None: ...

  @staticmethod
  def visitedBuilding(arg0: BuildingDef) -> None: ...

  def __init__(self): ...

