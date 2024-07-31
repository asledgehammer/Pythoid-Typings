from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from java.util import ArrayList
from zombie.erosion.categories import ErosionCategory
from zombie.erosion.season import ErosionSeason
from zombie.iso import IsoChunk, IsoGridSquare
from zombie.iso.sprite import IsoSpriteManager

class ErosionClient:

  instance: ErosionClient

  @staticmethod
  def Reset() -> None: ...

  def __init__(self, _sprMngr: IsoSpriteManager, _debug: bool): ...


class ErosionConfig:

  def consolePrint(self) -> None: ...

  def getDebug(self) -> ErosionConfig.Debug: ...

  def load(self, bb: ByteBuffer) -> None: ...

  def readFile(self, _file: str) -> bool: ...

  def save(self, bb: ByteBuffer) -> None: ...

  def writeFile(self, _file: str) -> None: ...

  def __init__(self):
    self.debug: ErosionConfig.Debug
    self.season: ErosionConfig.Season
    self.seeds: ErosionConfig.Seeds
    self.time: ErosionConfig.Time

  class Seeds:

    def __init__(self): ...

  class Time:

    def __init__(self): ...

  class Debug:

    def getEnabled(self) -> bool: ...

    def getStartDay(self) -> int: ...

    def getStartMonth(self) -> int: ...

    def __init__(self): ...

  class Season:

    def __init__(self): ...


class ErosionData:

  staticRand: bool

  def __init__(self): ...

  class Chunk:

    def load(self, input: ByteBuffer, WorldVersion: int) -> None: ...

    def save(self, output: ByteBuffer) -> None: ...

    def set(self, chunk: IsoChunk) -> None: ...

    def __init__(self):
      self.epoch: int
      self.etickstamp: int
      self.init: bool
      self.minerals: float
      self.moisture: float
      self.soil: int
      self.x: int
      self.y: int

  class Square:

    def load(self, input: ByteBuffer, WorldVersion: int) -> None: ...

    def rand(self, x: int, y: int, max: int) -> int: ...

    def reset(self) -> None: ...

    def save(self, output: ByteBuffer) -> None: ...

    def __init__(self):
      self.donothing: bool
      self.init: bool
      self.magicnum: float
      self.magicnumbyte: int
      self.noisekudzu: float
      self.noisemain: float
      self.noisemainbyte: int
      self.noisemainint: int
      self.regions: ArrayList[ErosionCategory.Data]
      self.soil: int


class ErosionGlobals:

  EROSION_DEBUG: bool

  @staticmethod
  def Boot(_sprMngr: IsoSpriteManager) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  def __init__(self): ...


class ErosionMain:

  def DebugUpdateMapNow(self) -> None: ...

  def getConfig(self) -> ErosionConfig: ...

  def getEtick(self) -> int: ...

  def getSeasons(self) -> ErosionSeason: ...

  def getSnowFraction(self) -> int: ...

  def getSnowFractionYesterday(self) -> int: ...

  def getSpriteManager(self) -> IsoSpriteManager: ...

  def isSnow(self) -> bool: ...

  def mainTimer(self) -> None: ...

  def receiveState(self, bb: ByteBuffer) -> None: ...

  def sendState(self, bb: ByteBuffer) -> None: ...

  def snowCheck(self) -> None: ...

  def start(self) -> None: ...

  @staticmethod
  def ChunkLoaded(_chunk: IsoChunk) -> None: ...

  @staticmethod
  def EveryTenMinutes() -> None: ...

  @staticmethod
  def LoadGridsquare(_sq: IsoGridSquare) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getInstance() -> ErosionMain: ...

  def __init__(self, _sprMngr: IsoSpriteManager, _debug: bool): ...


class ErosionRegions:

  CATEGORY_BUSH: int

  CATEGORY_FLOWERBED: int

  CATEGORY_GENERIC: int

  CATEGORY_PLANTS: int

  CATEGORY_STREET_CRACKS: int

  CATEGORY_TREES: int

  CATEGORY_WALL_CRACKS: int

  CATEGORY_WALL_VINES: int

  REGION_FLOWERBED: int

  REGION_NATURE: int

  REGION_STREET: int

  REGION_WALL: int

  regions: ArrayList[ErosionRegions.Region]

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getCategory(regionID: int, categoryID: int) -> ErosionCategory: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...

  class Region:

    def Reset(self) -> None: ...

    def addCategory(self, ID: int, _cat: ErosionCategory) -> ErosionRegions.Region: ...

    def init(self) -> None: ...

    def __init__(self, _ID: int, _tileMatch: str, _checkExt: bool, _isExt: bool, _hasWall: bool):
      self.categories: ArrayList[ErosionCategory]
      self.checkexterior: bool
      self.haswall: bool
      self.id: int
      self.isexterior: bool
      self.tilenamematch: str


class ErosionWorld:

  def init(self) -> bool: ...

  def update(self, _sq: IsoGridSquare, _sqErosionData: ErosionData.Square, _chunkData: ErosionData.Chunk, _eTick: int) -> None: ...

  def validateSpawn(self, _sq: IsoGridSquare, _sqErosionData: ErosionData.Square, _chunkData: ErosionData.Chunk) -> None: ...

  def __init__(self): ...

