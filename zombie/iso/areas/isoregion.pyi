from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import File
from java.lang import Exception, Throwable, Enum
from java.nio import ByteBuffer
from java.util import ArrayList
from zombie.config import ConfigOption, BooleanConfigOption
from zombie.core import Color
from zombie.core.raknet import UdpConnection
from zombie.iso import IsoChunk, IsoGridSquare
from zombie.iso.areas.isoregion.data import DataChunk
from zombie.iso.areas.isoregion.regions import IChunkRegion, IWorldRegion, IsoChunkRegion
from zombie.ui import UIElement

class ChunkUpdate:

  @staticmethod
  def writeIsoChunkIntoBuffer(c: IsoChunk, bb: ByteBuffer) -> None: ...

  def __init__(self): ...


class IsoRegionException(Exception):

  @overload
  def __init__(self, errorMessage: str): ...
  @overload
  def __init__(self, errorMessage: str, err: Throwable): ...


class IsoRegionLogType(Enum):

  Normal: IsoRegionLogType

  Warn: IsoRegionLogType

  @staticmethod
  def valueOf(arg0: str) -> IsoRegionLogType: ...

  @staticmethod
  def values() -> list[IsoRegionLogType]: ...


class IsoRegionWorker: ...


class IsoRegions:

  BIT_EMPTY: int

  BIT_HAS_FLOOR: int

  BIT_HAS_ROOF: int

  BIT_PATH_WALL_N: int

  BIT_PATH_WALL_W: int

  BIT_STAIRCASE: int

  BIT_WALL_N: int

  BIT_WALL_W: int

  CELL_CHUNK_DIM: int

  CELL_DIM: int

  CHUNK_DIM: int

  CHUNK_MAX_Z: int

  CHUNKS_DATA_PACKET_SIZE: int

  DIR_2D_MAX: int

  DIR_2D_NW: int

  DIR_BOT: int

  DIR_E: int

  DIR_MAX: int

  DIR_N: int

  DIR_NONE: int

  DIR_S: int

  DIR_TOP: int

  DIR_W: int

  FILE_DIR: str

  FILE_EXT: str

  FILE_PRE: str

  FILE_SEP: str

  PRINT_D: bool

  SINGLE_CHUNK_PACKET_SIZE: int

  @staticmethod
  def GetOppositeDir(dir: int) -> int: ...

  @staticmethod
  def ResetAllDataDebug() -> None: ...

  @staticmethod
  def getChunkFile(chunkX: int, chunkY: int) -> File: ...

  @staticmethod
  def getChunkRegion(x: int, y: int, z: int) -> IChunkRegion: ...

  @staticmethod
  def getDataChunk(chunkx: int, chunky: int) -> DataChunk: ...

  @staticmethod
  def getDirectory() -> File: ...

  @staticmethod
  def getHeaderFile() -> File: ...

  @staticmethod
  def getIsoWorldRegion(x: int, y: int, z: int) -> IWorldRegion: ...

  @staticmethod
  def getLogger() -> IsoRegionsLogger: ...

  @staticmethod
  def getSquareFlags(x: int, y: int, z: int) -> int: ...

  @staticmethod
  def hash(x: int, y: int) -> int: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isDebugLoadAllChunks() -> bool: ...

  @staticmethod
  @overload
  def log(str: str) -> None: ...

  @staticmethod
  @overload
  def log(str: str, col: Color) -> None: ...

  @staticmethod
  def receiveClientRequestFullDataChunks(input: ByteBuffer, conn: UdpConnection) -> None: ...

  @staticmethod
  def receiveServerUpdatePacket(input: ByteBuffer) -> None: ...

  @staticmethod
  def reset() -> None: ...

  @staticmethod
  def setDebugLoadAllChunks(b: bool) -> None: ...

  @staticmethod
  def setPreviousFlags(gs: IsoGridSquare) -> None: ...

  @staticmethod
  @overload
  def squareChanged(gs: IsoGridSquare) -> None: ...

  @staticmethod
  @overload
  def squareChanged(gs: IsoGridSquare, isRemoval: bool) -> None: ...

  @staticmethod
  def update() -> None: ...

  @staticmethod
  def warn(str: str) -> None: ...

  def __init__(self): ...


class IsoRegionsLogger:

  def getLogs(self) -> ArrayList[IsoRegionsLogger.IsoRegionLog]: ...

  def isDirtyUI(self) -> bool: ...

  def unsetDirtyUI(self) -> None: ...

  def __init__(self, doConsolePrint: bool): ...

  class IsoRegionLog:

    def getColor(self) -> Color: ...

    def getStr(self) -> str: ...

    def getType(self) -> IsoRegionLogType: ...

    def __init__(self): ...


class IsoRegionsRenderer:

  def editRotate(self) -> None: ...

  def editSquare(self, x: int, y: int) -> None: ...

  def getBoolean(self, name: str) -> bool: ...

  def getChunkRegion(self, x: int, y: int) -> IsoChunkRegion: ...

  def getEditOptionByIndex(self, index: int) -> ConfigOption: ...

  def getEditOptionByName(self, name: str) -> ConfigOption: ...

  def getEditOptionCount(self) -> int: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionByName(self, name: str) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def getZLevel(self) -> int: ...

  def getZLevelOptionByIndex(self, index: int) -> ConfigOption: ...

  def getZLevelOptionByName(self, name: str) -> ConfigOption: ...

  def getZLevelOptionCount(self) -> int: ...

  def hasChunkRegion(self, x: int, y: int) -> bool: ...

  def isEditingEnabled(self) -> bool: ...

  def isHasSelected(self) -> bool: ...

  def load(self) -> None: ...

  def outlineRect(self, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  def recalcSurroundings(self) -> None: ...

  def render(self, ui: UIElement, zoom: float, xPos: float, yPos: float) -> None: ...

  def renderCellInfo(self, cellX: int, cellY: int, effectivePopulation: int, targetPopulation: int, lastRepopTime: float) -> None: ...

  def renderEntity(self, size: float, x: float, y: float, r: float, g: float, b: float, a: float) -> None: ...

  def renderLine(self, x1: float, y1: float, x2: float, y2: float, r: float, g: float, b: float, a: float) -> None: ...

  def renderRect(self, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  def renderSquare(self, x: float, y: float, r: float, g: float, b: float, alpha: float) -> None: ...

  def renderString(self, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def renderStringUI(self, x: float, y: float, str: str, c: Color) -> None: ...

  @overload
  def renderStringUI(self, x: float, y: float, str: str, r: float, g: float, b: float, a: float) -> None: ...

  def renderZombie(self, x: float, y: float, r: float, g: float, b: float) -> None: ...

  def save(self) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setEditOption(self, index: int, b: bool) -> None: ...

  def setEditSquareCoord(self, x: int, y: int) -> None: ...

  def setSelected(self, x: int, y: int) -> None: ...

  def setSelectedWorld(self, x: int, y: int) -> None: ...

  def setZLevelOption(self, index: int, b: bool) -> None: ...

  def uiToWorldX(self, x: float) -> float: ...

  def uiToWorldY(self, y: float) -> float: ...

  def unsetSelected(self) -> None: ...

  def worldToScreenX(self, x: float) -> float: ...

  def worldToScreenY(self, y: float) -> float: ...

  def __init__(self): ...

  class BooleanDebugOption(BooleanConfigOption):

    def getIndex(self) -> int: ...

    @overload
    def __init__(self, optionList: ArrayList[ConfigOption], name: str, defaultValue: bool): ...
    @overload
    def __init__(self, optionList: ArrayList[ConfigOption], name: str, defaultValue: bool, zLevel: int): ...

