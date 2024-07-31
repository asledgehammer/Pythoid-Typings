from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer, Enum
from java.nio import ByteBuffer
from java.util import List
from zombie.core.raknet import UdpConnection
from zombie.iso import IsoChunk
from zombie.iso.areas.isoregion.data import DataChunk, DataRoot

class JobApplyChanges(RegionJob):

  def isSaveToDisk(self) -> bool: ...


class JobChunkUpdate(RegionJob):

  def addChunkFromDataChunk(self, chunk: DataChunk) -> bool: ...

  def addChunkFromFile(self, bb: ByteBuffer) -> bool: ...

  def addChunkFromIsoChunk(self, isoChunk: IsoChunk) -> bool: ...

  def canAddChunk(self) -> bool: ...

  def getBuffer(self) -> ByteBuffer: ...

  def getChunkCount(self) -> int: ...

  def getNetTimeStamp(self) -> int: ...

  def getTargetConn(self) -> UdpConnection: ...

  def readChunksFromNetBuffer(self, bb: ByteBuffer, serverTimeStamp: int) -> bool: ...

  def readChunksPacket(self, root: DataRoot, knownChunks: List[Integer]) -> bool: ...

  def saveChunksToDisk(self) -> bool: ...

  def saveChunksToNetBuffer(self, bb: ByteBuffer) -> bool: ...

  def setNetTimeStamp(self, netTimeStamp: int) -> None: ...

  def setTargetConn(self, conn: UdpConnection) -> None: ...


class JobDebugResetAllData(RegionJob): ...


class JobServerSendFullData(RegionJob):

  def getTargetConn(self) -> UdpConnection: ...


class JobSquareUpdate(RegionJob):

  def getNewSquareFlags(self) -> int: ...

  def getWorldSquareX(self) -> int: ...

  def getWorldSquareY(self) -> int: ...

  def getWorldSquareZ(self) -> int: ...


class RegionJob:

  def getJobType(self) -> RegionJobType: ...


class RegionJobManager:

  @staticmethod
  def allocApplyChanges(saveToDisk: bool) -> JobApplyChanges: ...

  @staticmethod
  def allocChunkUpdate() -> JobChunkUpdate: ...

  @staticmethod
  def allocDebugResetAllData() -> JobDebugResetAllData: ...

  @staticmethod
  def allocServerSendFullData(conn: UdpConnection) -> JobServerSendFullData: ...

  @staticmethod
  def allocSquareUpdate(x: int, y: int, z: int, flags: int) -> JobSquareUpdate: ...

  @staticmethod
  def release(job: RegionJob) -> None: ...

  def __init__(self): ...


class RegionJobType(Enum):

  ApplyChanges: RegionJobType

  ChunkUpdate: RegionJobType

  DebugResetAllData: RegionJobType

  ServerSendFullData: RegionJobType

  SquareUpdate: RegionJobType

  @staticmethod
  def valueOf(arg0: str) -> RegionJobType: ...

  @staticmethod
  def values() -> list[RegionJobType]: ...

