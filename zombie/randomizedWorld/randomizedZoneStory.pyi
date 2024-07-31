from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import ArrayList
from zombie.iso import IsoMetaGrid, IsoGridSquare
from zombie.randomizedWorld import RandomizedWorldBase

class RZSBBQParty(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getBeachClutter() -> ArrayList[str]: ...

  def __init__(self): ...


class RZSBaseball(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSBeachParty(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getBeachClutter() -> ArrayList[str]: ...

  def __init__(self): ...


class RZSBuryingCamp(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSFishingTrip(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getFishes() -> ArrayList[str]: ...

  @staticmethod
  def getFishingTools() -> ArrayList[str]: ...

  def __init__(self): ...


class RZSForestCamp(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getCoolerClutter() -> ArrayList[str]: ...

  @staticmethod
  def getFireClutter() -> ArrayList[str]: ...

  @staticmethod
  def getForestClutter() -> ArrayList[str]: ...

  def __init__(self): ...


class RZSForestCampEaten(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSHunterCamp(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getForestClutter() -> ArrayList[str]: ...

  def __init__(self): ...


class RZSMusicFest(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSMusicFestStage(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSSexyTime(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  def __init__(self): ...


class RZSTrapperCamp(RandomizedZoneStoryBase):

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def getTrapList() -> ArrayList[str]: ...

  def __init__(self): ...


class RandomizedZoneStoryBase(RandomizedWorldBase):

  baseChance: int

  totalChance: int

  zoneStory: str

  def cleanAreaForStory(self, rzs: RandomizedZoneStoryBase, zone: IsoMetaGrid.Zone) -> None: ...

  def getMinimumHeight(self) -> int: ...

  def getMinimumWidth(self) -> int: ...

  def getRandomFreeSquare(self, rzs: RandomizedZoneStoryBase, zone: IsoMetaGrid.Zone) -> IsoGridSquare: ...

  def getRandomFreeSquareFullZone(self, rzs: RandomizedZoneStoryBase, zone: IsoMetaGrid.Zone) -> IsoGridSquare: ...

  @overload
  def isValid(self) -> bool: ...

  @overload
  def isValid(self, zone: IsoMetaGrid.Zone, force: bool) -> bool: ...

  def randomizeZoneStory(self, zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def initAllRZSMapChance(zone: IsoMetaGrid.Zone) -> None: ...

  @staticmethod
  def isValidForStory(zone: IsoMetaGrid.Zone, force: bool) -> bool: ...

  def __init__(self):
    self.alwaysdo: bool
    self.chance: int
    self.zonetype: ArrayList[str]

  class ZoneType(Enum):

    Baseball: RandomizedZoneStoryBase.ZoneType

    Beach: RandomizedZoneStoryBase.ZoneType

    Forest: RandomizedZoneStoryBase.ZoneType

    Lake: RandomizedZoneStoryBase.ZoneType

    MusicFest: RandomizedZoneStoryBase.ZoneType

    MusicFestStage: RandomizedZoneStoryBase.ZoneType

    NewsStory: RandomizedZoneStoryBase.ZoneType

    @staticmethod
    def valueOf(arg0: str) -> RandomizedZoneStoryBase.ZoneType: ...

    @staticmethod
    def values() -> list[RandomizedZoneStoryBase.ZoneType]: ...

