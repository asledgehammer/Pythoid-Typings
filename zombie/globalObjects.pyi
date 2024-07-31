from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from java.util import ArrayList
from se.krka.kahlua.vm import KahluaTable
from zombie.characters import IsoPlayer
from zombie.iso import IsoMetaGrid, IsoObject

class CGlobalObject(GlobalObject): ...


class CGlobalObjectNetwork:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def receive(bb: ByteBuffer) -> None: ...

  @staticmethod
  def sendClientCommand(player: IsoPlayer, systemName: str, command: str, args: KahluaTable) -> None: ...

  def __init__(self): ...


class CGlobalObjectSystem(GlobalObjectSystem):

  def Reset(self) -> None: ...

  def receiveNewLuaObjectAt(self, x: int, y: int, z: int, args: KahluaTable) -> None: ...

  def receiveRemoveLuaObjectAt(self, x: int, y: int, z: int) -> None: ...

  def receiveServerCommand(self, command: str, args: KahluaTable) -> None: ...

  def receiveUpdateLuaObjectAt(self, x: int, y: int, z: int, args: KahluaTable) -> None: ...

  def sendCommand(self, command: str, player: IsoPlayer, args: KahluaTable) -> None: ...

  def __init__(self, name: str): ...


class CGlobalObjects:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getSystemByIndex(index: int) -> CGlobalObjectSystem: ...

  @staticmethod
  def getSystemByName(name: str) -> CGlobalObjectSystem: ...

  @staticmethod
  def getSystemCount() -> int: ...

  @staticmethod
  def initSystems() -> None: ...

  @staticmethod
  def loadInitialState(bb: ByteBuffer) -> None: ...

  @staticmethod
  def newSystem(name: str) -> CGlobalObjectSystem: ...

  @staticmethod
  def noise(message: str) -> None: ...

  @staticmethod
  def receiveServerCommand(systemName: str, command: str, args: KahluaTable) -> bool: ...

  @staticmethod
  def registerSystem(name: str) -> CGlobalObjectSystem: ...

  def __init__(self): ...


class GlobalObject:

  def Reset(self) -> None: ...

  def getModData(self) -> KahluaTable: ...

  def getSystem(self) -> GlobalObjectSystem: ...

  def getX(self) -> int: ...

  def getY(self) -> int: ...

  def getZ(self) -> int: ...

  def setLocation(self, x: int, y: int, z: int) -> None: ...


class GlobalObjectLookup:

  def addObject(self, object: GlobalObject) -> None: ...

  def getObjectAt(self, x: int, y: int, z: int) -> GlobalObject: ...

  def getObjectsAdjacentTo(self, x: int, y: int, z: int, objects: ArrayList[GlobalObject]) -> ArrayList[GlobalObject]: ...

  def getObjectsInChunk(self, wx: int, wy: int, objects: ArrayList[GlobalObject]) -> ArrayList[GlobalObject]: ...

  def hasObjectsInChunk(self, wx: int, wy: int) -> bool: ...

  def removeObject(self, object: GlobalObject) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def init(metaGrid: IsoMetaGrid) -> None: ...

  def __init__(self, system: GlobalObjectSystem): ...

  class Shared: ...

  class Cell: ...

  class Chunk: ...


class GlobalObjectSystem:

  def Reset(self) -> None: ...

  def allocList(self) -> ArrayList[GlobalObject]: ...

  def finishedWithList(self, list: ArrayList[GlobalObject]) -> None: ...

  def getModData(self) -> KahluaTable: ...

  def getName(self) -> str: ...

  def getObjectAt(self, x: int, y: int, z: int) -> GlobalObject: ...

  def getObjectByIndex(self, index: int) -> GlobalObject: ...

  def getObjectCount(self) -> int: ...

  def getObjectsAdjacentTo(self, x: int, y: int, z: int) -> ArrayList[GlobalObject]: ...

  def getObjectsInChunk(self, wx: int, wy: int) -> ArrayList[GlobalObject]: ...

  def hasObjectsInChunk(self, wx: int, wy: int) -> bool: ...

  def newObject(self, x: int, y: int, z: int) -> GlobalObject: ...

  def removeObject(self, object: GlobalObject) -> None: ...


class SGlobalObject(GlobalObject):

  def load(self, bb: ByteBuffer, WorldVersion: int) -> None: ...

  def save(self, bb: ByteBuffer) -> None: ...


class SGlobalObjectNetwork:

  PACKET_ClientCommand: int

  PACKET_NewLuaObjectAt: int

  PACKET_RemoveLuaObjectAt: int

  PACKET_ServerCommand: int

  PACKET_UpdateLuaObjectAt: int

  @staticmethod
  def addGlobalObjectOnClient(globalObject: SGlobalObject) -> None: ...

  @staticmethod
  def receive(bb: ByteBuffer, player: IsoPlayer) -> None: ...

  @staticmethod
  def removeGlobalObjectOnClient(globalObject: GlobalObject) -> None: ...

  @staticmethod
  def sendServerCommand(systemName: str, command: str, args: KahluaTable) -> None: ...

  @staticmethod
  def updateGlobalObjectOnClient(globalObject: SGlobalObject) -> None: ...

  def __init__(self): ...


class SGlobalObjectSystem(GlobalObjectSystem):

  def OnIsoObjectChangedItself(self, isoObject: IsoObject) -> None: ...

  def Reset(self) -> None: ...

  def addGlobalObjectOnClient(self, globalObject: SGlobalObject) -> None: ...

  def chunkLoaded(self, wx: int, wy: int) -> None: ...

  def getInitialStateForClient(self) -> KahluaTable: ...

  @overload
  def load(self) -> None: ...

  @overload
  def load(self, bb: ByteBuffer, WorldVersion: int) -> None: ...

  def loadedWorldVersion(self) -> int: ...

  def receiveClientCommand(self, command: str, playerObj: IsoPlayer, args: KahluaTable) -> None: ...

  def removeGlobalObjectOnClient(self, globalObject: SGlobalObject) -> None: ...

  @overload
  def save(self) -> None: ...

  @overload
  def save(self, bb: ByteBuffer) -> None: ...

  def sendCommand(self, command: str, args: KahluaTable) -> None: ...

  def setModDataKeys(self, keys: KahluaTable) -> None: ...

  def setObjectModDataKeys(self, keys: KahluaTable) -> None: ...

  def setObjectSyncKeys(self, keys: KahluaTable) -> None: ...

  def update(self) -> None: ...

  def updateGlobalObjectOnClient(self, globalObject: SGlobalObject) -> None: ...

  def __init__(self, name: str): ...


class SGlobalObjects:

  @staticmethod
  def OnIsoObjectChangedItself(systemName: str, isoObject: IsoObject) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def chunkLoaded(wx: int, wy: int) -> None: ...

  @staticmethod
  def getSystemByIndex(index: int) -> SGlobalObjectSystem: ...

  @staticmethod
  def getSystemByName(name: str) -> SGlobalObjectSystem: ...

  @staticmethod
  def getSystemCount() -> int: ...

  @staticmethod
  def initSystems() -> None: ...

  @staticmethod
  def load() -> None: ...

  @staticmethod
  def newSystem(name: str) -> SGlobalObjectSystem: ...

  @staticmethod
  def noise(message: str) -> None: ...

  @staticmethod
  def receiveClientCommand(systemName: str, command: str, playerObj: IsoPlayer, args: KahluaTable) -> bool: ...

  @staticmethod
  def registerSystem(name: str) -> SGlobalObjectSystem: ...

  @staticmethod
  def save() -> None: ...

  @staticmethod
  def saveInitialStateForClient(bb: ByteBuffer) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...

