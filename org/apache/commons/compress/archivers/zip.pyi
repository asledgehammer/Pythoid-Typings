from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import InputStream, DataOutput, OutputStream, File
from java.lang import Enum
from java.nio import ByteBuffer
from java.nio.channels import SeekableByteChannel
from java.util import Date
from java.util.concurrent import Callable, ExecutorService
from java.util.zip import Deflater, ZipEntry
from org.apache.commons.compress.archivers import ArchiveOutputStream, ArchiveEntry
from org.apache.commons.compress.parallel import InputStreamSupplier, ScatterGatherBackingStoreSupplier, ScatterGatherBackingStore

class GeneralPurposeBit:

  UFT8_NAMES_FLAG: int

  def clone(self) -> object: ...

  @overload
  def encode(self) -> list[int]: ...

  @overload
  def encode(self, arg0: list[int], arg1: int) -> None: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  def useDataDescriptor(self, arg0: bool) -> None: ...

  def useEncryption(self, arg0: bool) -> None: ...

  def useStrongEncryption(self, arg0: bool) -> None: ...

  def useUTF8ForNames(self, arg0: bool) -> None: ...

  def usesDataDescriptor(self) -> bool: ...

  def usesEncryption(self) -> bool: ...

  def usesStrongEncryption(self) -> bool: ...

  def usesUTF8ForNames(self) -> bool: ...

  @staticmethod
  def parse(arg0: list[int], arg1: int) -> GeneralPurposeBit: ...

  def __init__(self): ...


class ParallelScatterZipCreator:

  @overload
  def addArchiveEntry(self, arg0: ZipArchiveEntryRequestSupplier) -> None: ...

  @overload
  def addArchiveEntry(self, arg0: ZipArchiveEntry, arg1: InputStreamSupplier) -> None: ...

  @overload
  def createCallable(self, arg0: ZipArchiveEntryRequestSupplier) -> Callable[object]: ...

  @overload
  def createCallable(self, arg0: ZipArchiveEntry, arg1: InputStreamSupplier) -> Callable[object]: ...

  def getStatisticsMessage(self) -> ScatterStatistics: ...

  def submit(self, arg0: Callable[object]) -> None: ...

  def writeTo(self, arg0: ZipArchiveOutputStream) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: ExecutorService): ...
  @overload
  def __init__(self, arg0: ExecutorService, arg1: ScatterGatherBackingStoreSupplier): ...

  class DefaultBackingStoreSupplier:

    @overload
    def get(self) -> ScatterGatherBackingStore: ...

    @overload
    def get(self) -> ScatterGatherBackingStore: ...


class ScatterStatistics:

  def getCompressionElapsed(self) -> int: ...

  def getMergingElapsed(self) -> int: ...

  def toString(self) -> str: ...


class StreamCompressor:

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  def deflate(self, arg0: InputStream, arg1: int) -> None: ...

  def getBytesRead(self) -> int: ...

  def getBytesWrittenForLastEntry(self) -> int: ...

  def getCrc32(self) -> int: ...

  def getTotalBytesWritten(self) -> int: ...

  @overload
  def writeCounted(self, arg0: list[int]) -> None: ...

  @overload
  def writeCounted(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @staticmethod
  @overload
  def create(arg0: ScatterGatherBackingStore) -> StreamCompressor: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: ScatterGatherBackingStore) -> StreamCompressor: ...

  class SeekableByteChannelCompressor(StreamCompressor):

    def __init__(self, arg0: Deflater, arg1: SeekableByteChannel): ...

  class DataOutputCompressor(StreamCompressor):

    def __init__(self, arg0: Deflater, arg1: DataOutput): ...

  class OutputStreamCompressor(StreamCompressor):

    def __init__(self, arg0: Deflater, arg1: OutputStream): ...

  class ScatterGatherBackingStoreCompressor(StreamCompressor):

    def __init__(self, arg0: Deflater, arg1: ScatterGatherBackingStore): ...


class UnparseableExtraFieldData:

  EXTRAFIELD_HEADER_SIZE: int

  @overload
  def getCentralDirectoryData(self) -> list[int]: ...

  @overload
  def getCentralDirectoryData(self) -> list[int]: ...

  @overload
  def getCentralDirectoryLength(self) -> ZipShort: ...

  @overload
  def getCentralDirectoryLength(self) -> ZipShort: ...

  @overload
  def getHeaderId(self) -> ZipShort: ...

  @overload
  def getHeaderId(self) -> ZipShort: ...

  @overload
  def getLocalFileDataData(self) -> list[int]: ...

  @overload
  def getLocalFileDataData(self) -> list[int]: ...

  @overload
  def getLocalFileDataLength(self) -> ZipShort: ...

  @overload
  def getLocalFileDataLength(self) -> ZipShort: ...

  @overload
  def parseFromCentralDirectoryData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def parseFromCentralDirectoryData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def parseFromLocalFileData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def parseFromLocalFileData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def __init__(self): ...


class Zip64Mode(Enum):

  Always: Zip64Mode

  AsNeeded: Zip64Mode

  Never: Zip64Mode

  @staticmethod
  def valueOf(arg0: str) -> Zip64Mode: ...

  @staticmethod
  def values() -> list[Zip64Mode]: ...


class ZipArchiveEntry(ZipEntry):

  CRC_UNKNOWN: int

  OFFSET_UNKNOWN: int

  PLATFORM_FAT: int

  PLATFORM_UNIX: int

  SIZE_UNKNOWN: int

  def addAsFirstExtraField(self, arg0: ZipExtraField) -> None: ...

  def addExtraField(self, arg0: ZipExtraField) -> None: ...

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getCentralDirectoryExtra(self) -> list[int]: ...

  def getCommentSource(self) -> ZipArchiveEntry.CommentSource: ...

  @overload
  def getDataOffset(self) -> int: ...

  @overload
  def getDataOffset(self) -> int: ...

  def getExternalAttributes(self) -> int: ...

  def getExtraField(self, arg0: ZipShort) -> ZipExtraField: ...

  @overload
  def getExtraFields(self) -> list[ZipExtraField]: ...

  @overload
  def getExtraFields(self, arg0: bool) -> list[ZipExtraField]: ...

  def getGeneralPurposeBit(self) -> GeneralPurposeBit: ...

  def getInternalAttributes(self) -> int: ...

  @overload
  def getLastModifiedDate(self) -> Date: ...

  @overload
  def getLastModifiedDate(self) -> Date: ...

  def getLocalFileDataExtra(self) -> list[int]: ...

  def getMethod(self) -> int: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  def getNameSource(self) -> ZipArchiveEntry.NameSource: ...

  def getPlatform(self) -> int: ...

  def getRawFlag(self) -> int: ...

  def getRawName(self) -> list[int]: ...

  @overload
  def getSize(self) -> int: ...

  @overload
  def getSize(self) -> int: ...

  def getUnixMode(self) -> int: ...

  def getUnparseableExtraFieldData(self) -> UnparseableExtraFieldData: ...

  def getVersionMadeBy(self) -> int: ...

  def getVersionRequired(self) -> int: ...

  def hashCode(self) -> int: ...

  @overload
  def isDirectory(self) -> bool: ...

  @overload
  def isDirectory(self) -> bool: ...

  @overload
  def isStreamContiguous(self) -> bool: ...

  @overload
  def isStreamContiguous(self) -> bool: ...

  def isUnixSymlink(self) -> bool: ...

  def removeExtraField(self, arg0: ZipShort) -> None: ...

  def removeUnparseableExtraFieldData(self) -> None: ...

  def setAlignment(self, arg0: int) -> None: ...

  def setCentralDirectoryExtra(self, arg0: list[int]) -> None: ...

  def setCommentSource(self, arg0: ZipArchiveEntry.CommentSource) -> None: ...

  def setExternalAttributes(self, arg0: int) -> None: ...

  def setExtra(self, arg0: list[int]) -> None: ...

  def setExtraFields(self, arg0: list[ZipExtraField]) -> None: ...

  def setGeneralPurposeBit(self, arg0: GeneralPurposeBit) -> None: ...

  def setInternalAttributes(self, arg0: int) -> None: ...

  def setMethod(self, arg0: int) -> None: ...

  def setNameSource(self, arg0: ZipArchiveEntry.NameSource) -> None: ...

  def setRawFlag(self, arg0: int) -> None: ...

  def setSize(self, arg0: int) -> None: ...

  def setUnixMode(self, arg0: int) -> None: ...

  def setVersionMadeBy(self, arg0: int) -> None: ...

  def setVersionRequired(self, arg0: int) -> None: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: ZipEntry): ...
  @overload
  def __init__(self, arg0: ZipArchiveEntry): ...
  @overload
  def __init__(self, arg0: File, arg1: str): ...

  class CommentSource(Enum):

    COMMENT: ZipArchiveEntry.CommentSource

    UNICODE_EXTRA_FIELD: ZipArchiveEntry.CommentSource

    @staticmethod
    def valueOf(arg0: str) -> ZipArchiveEntry.CommentSource: ...

    @staticmethod
    def values() -> list[ZipArchiveEntry.CommentSource]: ...

  class NameSource(Enum):

    NAME: ZipArchiveEntry.NameSource

    NAME_WITH_EFS_FLAG: ZipArchiveEntry.NameSource

    UNICODE_EXTRA_FIELD: ZipArchiveEntry.NameSource

    @staticmethod
    def valueOf(arg0: str) -> ZipArchiveEntry.NameSource: ...

    @staticmethod
    def values() -> list[ZipArchiveEntry.NameSource]: ...


class ZipArchiveEntryRequest:

  def getMethod(self) -> int: ...

  def getPayloadStream(self) -> InputStream: ...

  @staticmethod
  def createZipArchiveEntryRequest(arg0: ZipArchiveEntry, arg1: InputStreamSupplier) -> ZipArchiveEntryRequest: ...


class ZipArchiveEntryRequestSupplier:

  def get(self) -> ZipArchiveEntryRequest: ...


class ZipArchiveOutputStream(ArchiveOutputStream):

  DEFAULT_COMPRESSION: int

  DEFLATED: int

  EFS_FLAG: int

  STORED: int

  def addRawArchiveEntry(self, arg0: ZipArchiveEntry, arg1: InputStream) -> None: ...

  def canWriteEntryData(self, arg0: ArchiveEntry) -> bool: ...

  def close(self) -> None: ...

  def closeArchiveEntry(self) -> None: ...

  def createArchiveEntry(self, arg0: File, arg1: str) -> ArchiveEntry: ...

  def finish(self) -> None: ...

  def flush(self) -> None: ...

  def getEncoding(self) -> str: ...

  def isSeekable(self) -> bool: ...

  def putArchiveEntry(self, arg0: ArchiveEntry) -> None: ...

  def setComment(self, arg0: str) -> None: ...

  def setCreateUnicodeExtraFields(self, arg0: ZipArchiveOutputStream.UnicodeExtraFieldPolicy) -> None: ...

  def setEncoding(self, arg0: str) -> None: ...

  def setFallbackToUTF8(self, arg0: bool) -> None: ...

  def setLevel(self, arg0: int) -> None: ...

  def setMethod(self, arg0: int) -> None: ...

  def setUseLanguageEncodingFlag(self, arg0: bool) -> None: ...

  def setUseZip64(self, arg0: Zip64Mode) -> None: ...

  def write(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def __init__(self, arg0: File): ...
  @overload
  def __init__(self, arg0: OutputStream): ...
  @overload
  def __init__(self, arg0: SeekableByteChannel): ...

  class EntryMetaData: ...

  class CurrentEntry: ...

  class UnicodeExtraFieldPolicy:

    ALWAYS: ZipArchiveOutputStream.UnicodeExtraFieldPolicy

    NEVER: ZipArchiveOutputStream.UnicodeExtraFieldPolicy

    NOT_ENCODEABLE: ZipArchiveOutputStream.UnicodeExtraFieldPolicy

    def toString(self) -> str: ...


class ZipEncoding:

  def canEncode(self, arg0: str) -> bool: ...

  def decode(self, arg0: list[int]) -> str: ...

  def encode(self, arg0: str) -> ByteBuffer: ...


class ZipExtraField:

  EXTRAFIELD_HEADER_SIZE: int

  def getCentralDirectoryData(self) -> list[int]: ...

  def getCentralDirectoryLength(self) -> ZipShort: ...

  def getHeaderId(self) -> ZipShort: ...

  def getLocalFileDataData(self) -> list[int]: ...

  def getLocalFileDataLength(self) -> ZipShort: ...

  def parseFromCentralDirectoryData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def parseFromLocalFileData(self, arg0: list[int], arg1: int, arg2: int) -> None: ...


class ZipShort:

  ZERO: ZipShort

  def clone(self) -> object: ...

  def equals(self, arg0: object) -> bool: ...

  def getBytes(self) -> list[int]: ...

  def getValue(self) -> int: ...

  def hashCode(self) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def putShort(arg0: int, arg1: list[int], arg2: int) -> None: ...

  @overload
  def __init__(self, arg0: list[int]): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: list[int], arg1: int): ...
