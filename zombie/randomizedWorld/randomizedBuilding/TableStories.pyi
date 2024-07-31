from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList, HashMap
from zombie.iso import BuildingDef, IsoObject, IsoGridSquare
from zombie.randomizedWorld.randomizedBuilding import RandomizedBuildingBase

class RBTSBreakfast(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSButcher(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSDinner(RBTableStoryBase):

  def generateFood(self) -> None: ...

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSDrink(RBTableStoryBase):

  def getDrink(self) -> str: ...

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSElectronics(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSFoodPreparation(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSSandwich(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSSewing(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTSSoup(RBTableStoryBase):

  def randomizeBuilding(self, arg0: BuildingDef) -> None: ...

  def __init__(self): ...


class RBTableStoryBase(RandomizedBuildingBase):

  allStories: ArrayList[RBTableStoryBase]

  totalChance: int

  def getSecondTable(self, table1: IsoObject) -> IsoObject: ...

  def isValid(self, sq: IsoGridSquare, table: IsoObject, force: bool) -> bool: ...

  @staticmethod
  def getRandomStory(sq: IsoGridSquare, table: IsoObject) -> RBTableStoryBase: ...

  @staticmethod
  def initStories(sq: IsoGridSquare, table: IsoObject) -> None: ...

  def __init__(self):
    self.fulltablemap: ArrayList[HashMap[str, Integer]]

