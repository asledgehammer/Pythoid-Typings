from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from se.krka.kahlua.vm import KahluaTable
from zombie.characters import IsoPlayer
from zombie.core.network import ByteBufferWriter
from zombie.iso import IsoObject

class SinglePlayerClient:

  connection: UdpConnection

  udpEngine: UdpEngine

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def addIncoming(id: int, bb: ByteBuffer) -> None: ...

  @staticmethod
  def sendClientCommand(player: IsoPlayer, module: str, command: str, args: KahluaTable) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...

  class UdpEngineClient(UdpEngine):

    def Receive(self, arg0: ByteBuffer) -> None: ...

    def Send(self, arg0: ByteBuffer) -> None: ...


class SinglePlayerServer:

  udpEngine: SinglePlayerServer.UdpEngineServer

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def addIncoming(id: int, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendObjectChange(arg0: IsoObject, arg1: str, arg2: list[object]) -> None: ...

  @staticmethod
  @overload
  def sendObjectChange(o: IsoObject, change: str, tbl: KahluaTable) -> None: ...

  @staticmethod
  @overload
  def sendServerCommand(module: str, command: str, args: KahluaTable) -> None: ...

  @staticmethod
  @overload
  def sendServerCommand(module: str, command: str, args: KahluaTable, c: UdpConnection) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...

  class UdpEngineServer(UdpEngine):

    def Receive(self, bb: ByteBuffer) -> None: ...

    def Send(self, bb: ByteBuffer) -> None: ...


class UdpConnection:

  def ReleventTo(self, x: float, y: float) -> bool: ...

  def cancelPacket(self) -> None: ...

  def endPacketImmediate(self) -> None: ...

  def startPacket(self) -> ByteBufferWriter: ...

  def __init__(self, engine: UdpEngine):
    self.players: list[IsoPlayer]


class UdpEngine:

  def Receive(self, bb: ByteBuffer) -> None: ...

  def Send(self, bb: ByteBuffer) -> None: ...

  def __init__(self): ...


class ZomboidNetData:

  @overload
  def isConnect(self) -> bool: ...

  @overload
  def isConnect(self) -> bool: ...

  @overload
  def isDisconnect(self) -> bool: ...

  @overload
  def isDisconnect(self) -> bool: ...

  def read(self, id: int, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  def reset(self) -> None: ...

  @overload
  def __init__(self):
    self.buffer: ByteBuffer

    self.connection: UdpConnection

    self.length: int

    self.type: int

  @overload
  def __init__(self, size: int): ...


class ZomboidNetDataPool:

  instance: ZomboidNetDataPool

  def discard(self, data: ZomboidNetData) -> None: ...

  def get(self) -> ZomboidNetData: ...

  def getLong(self, len: int) -> ZomboidNetData: ...

  def __init__(self): ...

