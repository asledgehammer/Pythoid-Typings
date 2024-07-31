from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.nio import ByteBuffer
from zombie.Lua import LuaManager
from zombie.ui import UIFont
from zombie.util import PooledObject
from zombie.worldMap import UIWorldMap

class MapSymbolDefinitions:

  @overload
  def addTexture(self, id: str, path: str) -> None: ...

  @overload
  def addTexture(self, id: str, path: str, width: int, height: int) -> None: ...

  def getSymbolById(self, id: str) -> MapSymbolDefinitions.MapSymbolDefinition: ...

  def getSymbolByIndex(self, index: int) -> MapSymbolDefinitions.MapSymbolDefinition: ...

  def getSymbolCount(self) -> int: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getInstance() -> MapSymbolDefinitions: ...

  def __init__(self): ...

  class MapSymbolDefinition:

    def getHeight(self) -> int: ...

    def getId(self) -> str: ...

    def getTexturePath(self) -> str: ...

    def getWidth(self) -> int: ...

    def __init__(self): ...


class WorldMapBaseSymbol:

  DEFAULT_SCALE: float

  def getDisplayScale(self, ui: UIWorldMap) -> float: ...

  def getType(self) -> WorldMapSymbols.WorldMapSymbolType: ...

  def heightScaled(self, ui: UIWorldMap) -> float: ...

  def isVisible(self) -> bool: ...

  def layout(self, ui: UIWorldMap, collisions: WorldMapSymbolCollisions, rox: float, roy: float) -> None: ...

  def load(self, input: ByteBuffer, WorldVersion: int, SymbolsVersion: int) -> None: ...

  def release(self) -> None: ...

  def render(self, ui: UIWorldMap, rox: float, roy: float) -> None: ...

  def save(self, output: ByteBuffer) -> None: ...

  def setAnchor(self, x: float, y: float) -> None: ...

  def setCollide(self, collide: bool) -> None: ...

  def setPosition(self, x: float, y: float) -> None: ...

  def setRGBA(self, r: float, g: float, b: float, a: float) -> None: ...

  def setScale(self, scale: float) -> None: ...

  def setVisible(self, visible: bool) -> None: ...

  def widthScaled(self, ui: UIWorldMap) -> float: ...

  def __init__(self, owner: WorldMapSymbols): ...


class WorldMapSymbolCollisions:

  def __init__(self): ...


class WorldMapSymbols:

  COLLAPSED_RADIUS: float

  SAVEFILE_VERSION: int

  def addText(self, text: str, translated: bool, font: UIFont, x: float, y: float, anchorX: float, anchorY: float, scale: float, r: float, g: float, b: float, a: float) -> WorldMapTextSymbol: ...

  @overload
  def addTexture(self, symbolID: str, x: float, y: float, r: float, g: float, b: float, a: float) -> WorldMapTextureSymbol: ...

  @overload
  def addTexture(self, symbolID: str, x: float, y: float, anchorX: float, anchorY: float, scale: float, r: float, g: float, b: float, a: float) -> WorldMapTextureSymbol: ...

  def addTranslatedText(self, text: str, font: UIFont, x: float, y: float, r: float, g: float, b: float, a: float) -> WorldMapTextSymbol: ...

  def addUntranslatedText(self, text: str, font: UIFont, x: float, y: float, r: float, g: float, b: float, a: float) -> WorldMapTextSymbol: ...

  def clear(self) -> None: ...

  def getLayoutWorldScale(self) -> float: ...

  def getMiniMapSymbols(self) -> bool: ...

  def getSymbolByIndex(self, index: int) -> WorldMapBaseSymbol: ...

  def getSymbolCount(self) -> int: ...

  def invalidateLayout(self) -> None: ...

  def load(self, input: ByteBuffer, WorldVersion: int) -> None: ...

  def removeSymbolByIndex(self, index: int) -> None: ...

  def render(self, ui: UIWorldMap) -> None: ...

  def save(self, output: ByteBuffer) -> None: ...

  def __init__(self):
    self.min_visible_zoom: float

  class WorldMapSymbolType(Enum):

    NONE: WorldMapSymbols.WorldMapSymbolType

    Text: WorldMapSymbols.WorldMapSymbolType

    Texture: WorldMapSymbols.WorldMapSymbolType

    @staticmethod
    def valueOf(arg0: str) -> WorldMapSymbols.WorldMapSymbolType: ...

    @staticmethod
    def values() -> list[WorldMapSymbols.WorldMapSymbolType]: ...


class WorldMapSymbolsV1:

  def addTexture(self, symbolID: str, x: float, y: float) -> WorldMapSymbolsV1.WorldMapTextureSymbolV1: ...

  def addTranslatedText(self, text: str, font: UIFont, x: float, y: float) -> WorldMapSymbolsV1.WorldMapTextSymbolV1: ...

  def addUntranslatedText(self, text: str, font: UIFont, x: float, y: float) -> WorldMapSymbolsV1.WorldMapTextSymbolV1: ...

  def clear(self) -> None: ...

  def getSymbolByIndex(self, index: int) -> WorldMapSymbolsV1.WorldMapBaseSymbolV1: ...

  def getSymbolCount(self) -> int: ...

  def hitTest(self, uiX: float, uiY: float) -> int: ...

  def removeSymbolByIndex(self, index: int) -> None: ...

  @staticmethod
  def setExposed(exposer: LuaManager.Exposer) -> None: ...

  def __init__(self, ui: UIWorldMap, symbols: WorldMapSymbols): ...

  class WorldMapTextSymbolV1(WorldMapSymbolsV1.WorldMapBaseSymbolV1):

    def getAlpha(self) -> float: ...

    def getBlue(self) -> float: ...

    def getDisplayHeight(self) -> float: ...

    def getDisplayWidth(self) -> float: ...

    def getDisplayX(self) -> float: ...

    def getDisplayY(self) -> float: ...

    def getGreen(self) -> float: ...

    def getRed(self) -> float: ...

    def getTranslatedText(self) -> str: ...

    def getUntranslatedText(self) -> str: ...

    def getWorldX(self) -> float: ...

    def getWorldY(self) -> float: ...

    def isText(self) -> bool: ...

    def isTexture(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def setAnchor(self, arg0: float, arg1: float) -> None: ...

    def setCollide(self, arg0: bool) -> None: ...

    def setPosition(self, arg0: float, arg1: float) -> None: ...

    def setRGBA(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

    def setScale(self, arg0: float) -> None: ...

    def setTranslatedText(self, text: str) -> None: ...

    def setUntranslatedText(self, text: str) -> None: ...

    def setVisible(self, arg0: bool) -> None: ...

    def __init__(self): ...

  class WorldMapTextureSymbolV1(WorldMapSymbolsV1.WorldMapBaseSymbolV1):

    def getAlpha(self) -> float: ...

    def getBlue(self) -> float: ...

    def getDisplayHeight(self) -> float: ...

    def getDisplayWidth(self) -> float: ...

    def getDisplayX(self) -> float: ...

    def getDisplayY(self) -> float: ...

    def getGreen(self) -> float: ...

    def getRed(self) -> float: ...

    def getSymbolID(self) -> str: ...

    def getWorldX(self) -> float: ...

    def getWorldY(self) -> float: ...

    def isText(self) -> bool: ...

    def isTexture(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def setAnchor(self, arg0: float, arg1: float) -> None: ...

    def setCollide(self, arg0: bool) -> None: ...

    def setPosition(self, arg0: float, arg1: float) -> None: ...

    def setRGBA(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

    def setScale(self, arg0: float) -> None: ...

    def setVisible(self, arg0: bool) -> None: ...

    def __init__(self): ...

  class WorldMapBaseSymbolV1(PooledObject):

    def getAlpha(self) -> float: ...

    def getBlue(self) -> float: ...

    def getDisplayHeight(self) -> float: ...

    def getDisplayWidth(self) -> float: ...

    def getDisplayX(self) -> float: ...

    def getDisplayY(self) -> float: ...

    def getGreen(self) -> float: ...

    def getRed(self) -> float: ...

    def getWorldX(self) -> float: ...

    def getWorldY(self) -> float: ...

    def isText(self) -> bool: ...

    def isTexture(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def setAnchor(self, arg0: float, arg1: float) -> None: ...

    def setCollide(self, arg0: bool) -> None: ...

    def setPosition(self, arg0: float, arg1: float) -> None: ...

    def setRGBA(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...

    def setScale(self, arg0: float) -> None: ...

    def setVisible(self, arg0: bool) -> None: ...


class WorldMapTextSymbol(WorldMapBaseSymbol):

  def getTranslatedText(self) -> str: ...

  def getType(self) -> WorldMapSymbols.WorldMapSymbolType: ...

  def getUntranslatedText(self) -> str: ...

  def isVisible(self) -> bool: ...

  def load(self, input: ByteBuffer, WorldVersion: int, SymbolsVersion: int) -> None: ...

  def release(self) -> None: ...

  def render(self, ui: UIWorldMap, rox: float, roy: float) -> None: ...

  def save(self, output: ByteBuffer) -> None: ...

  def setTranslatedText(self, text: str) -> None: ...

  def setUntranslatedText(self, text: str) -> None: ...

  def __init__(self, owner: WorldMapSymbols): ...


class WorldMapTextureSymbol(WorldMapBaseSymbol):

  def checkTexture(self) -> None: ...

  def getSymbolID(self) -> str: ...

  def getType(self) -> WorldMapSymbols.WorldMapSymbolType: ...

  def layout(self, ui: UIWorldMap, collisions: WorldMapSymbolCollisions, rox: float, roy: float) -> None: ...

  def load(self, input: ByteBuffer, WorldVersion: int, SymbolsVersion: int) -> None: ...

  def release(self) -> None: ...

  def render(self, ui: UIWorldMap, rox: float, roy: float) -> None: ...

  def save(self, output: ByteBuffer) -> None: ...

  def setSymbolID(self, symbolID: str) -> None: ...

  def __init__(self, owner: WorldMapSymbols): ...

