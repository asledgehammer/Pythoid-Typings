from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import FilterOutputStream, OutputStream, FilterInputStream, InputStream, IOException, File
from java.lang import Exception
from java.nio import ByteBuffer
from java.nio.charset import Charset
from java.nio.file.attribute import FileTime, BasicFileAttributes
from java.time import LocalDateTime
from java.util import Enumeration, Iterator, Spliterators
from java.util.function import Consumer
from java.util.stream import Stream

T = TypeVar('T', default=Any)

class CRC32:

  @overload
  def getValue(self) -> int: ...

  @overload
  def getValue(self) -> int: ...

  @overload
  def reset(self) -> None: ...

  @overload
  def reset(self) -> None: ...

  @overload
  def update(self, arg0: list[int]) -> None: ...

  @overload
  def update(self, arg0: int) -> None: ...

  @overload
  def update(self, arg0: int) -> None: ...

  @overload
  def update(self, arg0: ByteBuffer) -> None: ...

  @overload
  def update(self, arg0: ByteBuffer) -> None: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def __init__(self): ...


class Checksum:

  def getValue(self) -> int: ...

  def reset(self) -> None: ...

  @overload
  def update(self, arg0: list[int]) -> None: ...

  @overload
  def update(self, arg0: int) -> None: ...

  @overload
  def update(self, arg0: ByteBuffer) -> None: ...

  @overload
  def update(self, arg0: list[int], arg1: int, arg2: int) -> None: ...


class DataFormatException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Deflater:

  BEST_COMPRESSION: int

  BEST_SPEED: int

  DEFAULT_COMPRESSION: int

  DEFAULT_STRATEGY: int

  DEFLATED: int

  FILTERED: int

  FULL_FLUSH: int

  HUFFMAN_ONLY: int

  NO_COMPRESSION: int

  NO_FLUSH: int

  SYNC_FLUSH: int

  @overload
  def deflate(self, arg0: list[int]) -> int: ...

  @overload
  def deflate(self, arg0: ByteBuffer) -> int: ...

  @overload
  def deflate(self, arg0: ByteBuffer, arg1: int) -> int: ...

  @overload
  def deflate(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

  @overload
  def deflate(self, arg0: list[int], arg1: int, arg2: int, arg3: int) -> int: ...

  def end(self) -> None: ...

  def finish(self) -> None: ...

  def finished(self) -> bool: ...

  def getAdler(self) -> int: ...

  def getBytesRead(self) -> int: ...

  def getBytesWritten(self) -> int: ...

  def getTotalIn(self) -> int: ...

  def getTotalOut(self) -> int: ...

  def needsInput(self) -> bool: ...

  def reset(self) -> None: ...

  @overload
  def setDictionary(self, arg0: list[int]) -> None: ...

  @overload
  def setDictionary(self, arg0: ByteBuffer) -> None: ...

  @overload
  def setDictionary(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def setInput(self, arg0: list[int]) -> None: ...

  @overload
  def setInput(self, arg0: ByteBuffer) -> None: ...

  @overload
  def setInput(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  def setLevel(self, arg0: int) -> None: ...

  def setStrategy(self, arg0: int) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...
  @overload
  def __init__(self, arg0: int, arg1: bool): ...

  class DeflaterZStreamRef:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...


class DeflaterOutputStream(FilterOutputStream):

  def close(self) -> None: ...

  def finish(self) -> None: ...

  def flush(self) -> None: ...

  @overload
  def write(self, arg0: int) -> None: ...

  @overload
  def write(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def __init__(self, arg0: OutputStream): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: bool): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: Deflater): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: Deflater, arg2: bool): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: Deflater, arg2: int): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: Deflater, arg2: int, arg3: bool): ...


class Inflater:

  def end(self) -> None: ...

  def finished(self) -> bool: ...

  def getAdler(self) -> int: ...

  def getBytesRead(self) -> int: ...

  def getBytesWritten(self) -> int: ...

  def getRemaining(self) -> int: ...

  def getTotalIn(self) -> int: ...

  def getTotalOut(self) -> int: ...

  @overload
  def inflate(self, arg0: list[int]) -> int: ...

  @overload
  def inflate(self, arg0: ByteBuffer) -> int: ...

  @overload
  def inflate(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

  def needsDictionary(self) -> bool: ...

  def needsInput(self) -> bool: ...

  def reset(self) -> None: ...

  @overload
  def setDictionary(self, arg0: list[int]) -> None: ...

  @overload
  def setDictionary(self, arg0: ByteBuffer) -> None: ...

  @overload
  def setDictionary(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def setInput(self, arg0: list[int]) -> None: ...

  @overload
  def setInput(self, arg0: ByteBuffer) -> None: ...

  @overload
  def setInput(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: bool): ...

  class InflaterZStreamRef:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...


class InflaterInputStream(FilterInputStream):

  def available(self) -> int: ...

  def close(self) -> None: ...

  def mark(self, arg0: int) -> None: ...

  def markSupported(self) -> bool: ...

  @overload
  def read(self) -> int: ...

  @overload
  def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

  def reset(self) -> None: ...

  def skip(self, arg0: int) -> int: ...

  @overload
  def __init__(self, arg0: InputStream): ...
  @overload
  def __init__(self, arg0: InputStream, arg1: Inflater): ...
  @overload
  def __init__(self, arg0: InputStream, arg1: Inflater, arg2: int): ...


class ZipCoder:

  @staticmethod
  def get(arg0: Charset) -> ZipCoder: ...

  class UTF8ZipCoder(ZipCoder): ...


class ZipConstants:

  CENATT: int

  CENATX: int

  CENCOM: int

  CENCRC: int

  CENDSK: int

  CENEXT: int

  CENFLG: int

  CENHDR: int

  CENHOW: int

  CENLEN: int

  CENNAM: int

  CENOFF: int

  CENSIG: int

  CENSIZ: int

  CENTIM: int

  CENVEM: int

  CENVER: int

  ENDCOM: int

  ENDHDR: int

  ENDOFF: int

  ENDSIG: int

  ENDSIZ: int

  ENDSUB: int

  ENDTOT: int

  EXTCRC: int

  EXTHDR: int

  EXTLEN: int

  EXTSIG: int

  EXTSIZ: int

  LOCCRC: int

  LOCEXT: int

  LOCFLG: int

  LOCHDR: int

  LOCHOW: int

  LOCLEN: int

  LOCNAM: int

  LOCSIG: int

  LOCSIZ: int

  LOCTIM: int

  LOCVER: int


class ZipEntry:

  CENATT: int

  CENATX: int

  CENCOM: int

  CENCRC: int

  CENDSK: int

  CENEXT: int

  CENFLG: int

  CENHDR: int

  CENHOW: int

  CENLEN: int

  CENNAM: int

  CENOFF: int

  CENSIG: int

  CENSIZ: int

  CENTIM: int

  CENVEM: int

  CENVER: int

  DEFLATED: int

  ENDCOM: int

  ENDHDR: int

  ENDOFF: int

  ENDSIG: int

  ENDSIZ: int

  ENDSUB: int

  ENDTOT: int

  EXTCRC: int

  EXTHDR: int

  EXTLEN: int

  EXTSIG: int

  EXTSIZ: int

  LOCCRC: int

  LOCEXT: int

  LOCFLG: int

  LOCHDR: int

  LOCHOW: int

  LOCLEN: int

  LOCNAM: int

  LOCSIG: int

  LOCSIZ: int

  LOCTIM: int

  LOCVER: int

  STORED: int

  def clone(self) -> object: ...

  def getComment(self) -> str: ...

  def getCompressedSize(self) -> int: ...

  def getCrc(self) -> int: ...

  def getCreationTime(self) -> FileTime: ...

  def getExtra(self) -> list[int]: ...

  def getLastAccessTime(self) -> FileTime: ...

  def getLastModifiedTime(self) -> FileTime: ...

  def getMethod(self) -> int: ...

  def getName(self) -> str: ...

  def getSize(self) -> int: ...

  def getTime(self) -> int: ...

  def getTimeLocal(self) -> LocalDateTime: ...

  def hashCode(self) -> int: ...

  def isDirectory(self) -> bool: ...

  def setComment(self, arg0: str) -> None: ...

  def setCompressedSize(self, arg0: int) -> None: ...

  def setCrc(self, arg0: int) -> None: ...

  def setCreationTime(self, arg0: FileTime) -> ZipEntry: ...

  def setExtra(self, arg0: list[int]) -> None: ...

  def setLastAccessTime(self, arg0: FileTime) -> ZipEntry: ...

  def setLastModifiedTime(self, arg0: FileTime) -> ZipEntry: ...

  def setMethod(self, arg0: int) -> None: ...

  def setSize(self, arg0: int) -> None: ...

  def setTime(self, arg0: int) -> None: ...

  def setTimeLocal(self, arg0: LocalDateTime) -> None: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: ZipEntry): ...


class ZipException(IOException):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class ZipFile:

  CENATT: int

  CENATX: int

  CENCOM: int

  CENCRC: int

  CENDSK: int

  CENEXT: int

  CENFLG: int

  CENHDR: int

  CENHOW: int

  CENLEN: int

  CENNAM: int

  CENOFF: int

  CENSIG: int

  CENSIZ: int

  CENTIM: int

  CENVEM: int

  CENVER: int

  ENDCOM: int

  ENDHDR: int

  ENDOFF: int

  ENDSIG: int

  ENDSIZ: int

  ENDSUB: int

  ENDTOT: int

  EXTCRC: int

  EXTHDR: int

  EXTLEN: int

  EXTSIG: int

  EXTSIZ: int

  LOCCRC: int

  LOCEXT: int

  LOCFLG: int

  LOCHDR: int

  LOCHOW: int

  LOCLEN: int

  LOCNAM: int

  LOCSIG: int

  LOCSIZ: int

  LOCTIM: int

  LOCVER: int

  OPEN_DELETE: int

  OPEN_READ: int

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  def entries(self) -> Enumeration[ZipEntry]: ...

  def getComment(self) -> str: ...

  def getEntry(self, arg0: str) -> ZipEntry: ...

  def getInputStream(self, arg0: ZipEntry) -> InputStream: ...

  def getName(self) -> str: ...

  def size(self) -> int: ...

  def stream(self) -> Stream[ZipEntry]: ...

  @overload
  def __init__(self, arg0: File): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: File, arg1: int): ...
  @overload
  def __init__(self, arg0: File, arg1: Charset): ...
  @overload
  def __init__(self, arg0: str, arg1: Charset): ...
  @overload
  def __init__(self, arg0: File, arg1: int, arg2: Charset): ...

  class CleanableResource:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...

  class Source:

    class Key:

      def equals(self, arg0: object) -> bool: ...

      def hashCode(self) -> int: ...

      def __init__(self, arg0: File, arg1: BasicFileAttributes, arg2: ZipCoder): ...

    class End: ...

  class ZipFileInputStream(InputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

    def size(self) -> int: ...

    def skip(self, arg0: int) -> int: ...

  class ZipFileInflaterInputStream(InflaterInputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

  class ZipEntryIterator[T]:

    @overload
    def asIterator(self) -> Iterator[T]: ...

    @overload
    def asIterator(self) -> Iterator[E]: ...

    def forEachRemaining(self, arg0: Consumer[E]) -> None: ...

    @overload
    def hasMoreElements(self) -> bool: ...

    @overload
    def hasMoreElements(self) -> bool: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def hasNext(self) -> bool: ...

    @overload
    def next(self) -> object: ...

    @overload
    def next(self) -> T: ...

    @overload
    def next(self) -> object: ...

    @overload
    def nextElement(self) -> T: ...

    @overload
    def nextElement(self) -> object: ...

    @overload
    def nextElement(self) -> object: ...

    def remove(self) -> None: ...

    def __init__(self, arg0: ZipFile, arg1: int): ...

  class EntrySpliterator[T](Spliterators.AbstractSpliterator):

    def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

  class InflaterCleanupAction:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...


class ZipOutputStream(DeflaterOutputStream):

  CENATT: int

  CENATX: int

  CENCOM: int

  CENCRC: int

  CENDSK: int

  CENEXT: int

  CENFLG: int

  CENHDR: int

  CENHOW: int

  CENLEN: int

  CENNAM: int

  CENOFF: int

  CENSIG: int

  CENSIZ: int

  CENTIM: int

  CENVEM: int

  CENVER: int

  DEFLATED: int

  ENDCOM: int

  ENDHDR: int

  ENDOFF: int

  ENDSIG: int

  ENDSIZ: int

  ENDSUB: int

  ENDTOT: int

  EXTCRC: int

  EXTHDR: int

  EXTLEN: int

  EXTSIG: int

  EXTSIZ: int

  LOCCRC: int

  LOCEXT: int

  LOCFLG: int

  LOCHDR: int

  LOCHOW: int

  LOCLEN: int

  LOCNAM: int

  LOCSIG: int

  LOCSIZ: int

  LOCTIM: int

  LOCVER: int

  STORED: int

  def close(self) -> None: ...

  def closeEntry(self) -> None: ...

  def finish(self) -> None: ...

  def putNextEntry(self, arg0: ZipEntry) -> None: ...

  def setComment(self, arg0: str) -> None: ...

  def setLevel(self, arg0: int) -> None: ...

  def setMethod(self, arg0: int) -> None: ...

  def write(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

  @overload
  def __init__(self, arg0: OutputStream): ...
  @overload
  def __init__(self, arg0: OutputStream, arg1: Charset): ...

  class XEntry:

    def __init__(self, arg0: ZipEntry, arg1: int): ...


class ZipUtils:

  UPPER_UNIXTIME_BOUND: int

  WINDOWS_TIME_NOT_AVAILABLE: int

  @staticmethod
  def dosToJavaTime(arg0: int) -> int: ...

  @staticmethod
  def extendedDosToJavaTime(arg0: int) -> int: ...

  @staticmethod
  def fileTimeToUnixTime(arg0: FileTime) -> int: ...

  @staticmethod
  def fileTimeToWinTime(arg0: FileTime) -> int: ...

  @staticmethod
  def get16(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def get32(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def get32S(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def get64(arg0: list[int], arg1: int) -> int: ...

  @staticmethod
  def unixTimeToFileTime(arg0: int) -> FileTime: ...

  @staticmethod
  def winTimeToFileTime(arg0: int) -> FileTime: ...

