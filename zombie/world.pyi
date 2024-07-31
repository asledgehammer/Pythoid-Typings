from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Exception, Throwable
from java.nio import ByteBuffer
from java.util import List
from zombie.inventory import InventoryItem
from zombie.scripting.objects import Item

class DictionaryData:

  def __init__(self): ...


class DictionaryDataClient(DictionaryData):

  def __init__(self): ...


class ItemInfo:

  def DebugPrint(self) -> None: ...

  def GetDebugString(self) -> str: ...

  def ToString(self) -> str: ...

  def copy(self) -> ItemInfo: ...

  def getFullType(self) -> str: ...

  def getModID(self) -> str: ...

  def getModOverrides(self) -> List[str]: ...

  def getRegistryID(self) -> int: ...

  def getScriptItem(self) -> Item: ...

  def isExistsAsVanilla(self) -> bool: ...

  def isLoaded(self) -> bool: ...

  def isModded(self) -> bool: ...

  def isObsolete(self) -> bool: ...

  def isRemoved(self) -> bool: ...

  def isValid(self) -> bool: ...

  def __init__(self): ...


class WorldDictionary:

  logMissingObjectID: bool

  logUnset: bool

  SAVE_EXT: str

  SAVE_FILE: str

  SAVE_FILE_LOG: str

  SAVE_FILE_READABLE: str

  @staticmethod
  @overload
  def DebugPrintItem(fullitem: str) -> None: ...

  @staticmethod
  @overload
  def DebugPrintItem(id: int) -> None: ...

  @staticmethod
  @overload
  def DebugPrintItem(item: InventoryItem) -> None: ...

  @staticmethod
  @overload
  def DebugPrintItem(item: Item) -> None: ...

  @staticmethod
  def ScriptsLoaded() -> None: ...

  @staticmethod
  def StartScriptLoading() -> None: ...

  @staticmethod
  def getIdForObjectName(name: str) -> int: ...

  @staticmethod
  def getIdForSpriteName(name: str) -> int: ...

  @staticmethod
  def getItemInfoFromID(registeryID: int) -> ItemInfo: ...

  @staticmethod
  def getItemInfoFromType(fulltype: str) -> ItemInfo: ...

  @staticmethod
  @overload
  def getItemModID(fulltype: str) -> str: ...

  @staticmethod
  @overload
  def getItemModID(registeryID: int) -> str: ...

  @staticmethod
  def getItemRegistryID(fullType: str) -> int: ...

  @staticmethod
  def getItemTypeDebugString(id: int) -> str: ...

  @staticmethod
  def getItemTypeFromID(id: int) -> str: ...

  @staticmethod
  def getModNameFromID(modid: str) -> str: ...

  @staticmethod
  def getObjectNameFromID(id: int) -> str: ...

  @staticmethod
  def getSpriteNameFromID(id: int) -> str: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isIsNewGame() -> bool: ...

  @staticmethod
  def loadDataFromServer(bb: ByteBuffer) -> None: ...

  @staticmethod
  def onLoadItem(item: Item) -> None: ...

  @staticmethod
  def onWorldLoaded() -> None: ...

  @staticmethod
  def saveDataForClient(bb: ByteBuffer) -> None: ...

  @staticmethod
  def setIsNewGame(isNewGame: bool) -> None: ...

  def __init__(self): ...


class WorldDictionaryException(Exception):

  @overload
  def __init__(self, errorMessage: str): ...
  @overload
  def __init__(self, errorMessage: str, err: Throwable): ...

