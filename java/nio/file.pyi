from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import IOException, OutputStream, InputStream, BufferedReader, BufferedWriter, File
from java.lang import Enum, Class, Iterable, ClassLoader, CharSequence
from java.net import URI
from java.nio.channels import SeekableByteChannel
from java.nio.charset import Charset
from java.nio.file.attribute import UserPrincipalLookupService, BasicFileAttributes, FileAttribute, FileTime, UserPrincipal, PosixFilePermission
from java.nio.file.spi import FileSystemProvider
from java.util import Iterator, Spliterator, Comparator, Set, Map, List
from java.util.concurrent import TimeUnit
from java.util.function import Consumer, BiPredicate
from java.util.stream import Stream

T = TypeVar('T', default=Any)
Filter_T = TypeVar('Filter_T', default=Any)
V = TypeVar('V', default=Any)
A = TypeVar('A', default=Any)
Kind_T = TypeVar('Kind_T', default=Any)

class AccessMode(Enum):

  EXECUTE: AccessMode

  READ: AccessMode

  WRITE: AccessMode

  @staticmethod
  def valueOf(arg0: str) -> AccessMode: ...

  @staticmethod
  def values() -> list[AccessMode]: ...


class CopyOption: ...


class DirectoryStream[T]:

  def close(self) -> None: ...

  def forEach(self, arg0: Consumer[T]) -> None: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  def spliterator(self) -> Spliterator[T]: ...

  class Filter[Filter_T]:

    def accept(self, arg0: object) -> bool: ...


class FileChannelLinesSpliterator:

  CONCURRENT: int

  DISTINCT: int

  IMMUTABLE: int

  NONNULL: int

  ORDERED: int

  SIZED: int

  SORTED: int

  SUBSIZED: int

  @overload
  def characteristics(self) -> int: ...

  @overload
  def characteristics(self) -> int: ...

  @overload
  def estimateSize(self) -> int: ...

  @overload
  def estimateSize(self) -> int: ...

  @overload
  def forEachRemaining(self, arg0: Consumer[str]) -> None: ...

  @overload
  def forEachRemaining(self, arg0: Consumer[T]) -> None: ...

  def getComparator(self) -> Comparator[T]: ...

  @overload
  def getExactSizeIfKnown(self) -> int: ...

  @overload
  def getExactSizeIfKnown(self) -> int: ...

  def hasCharacteristics(self, arg0: int) -> bool: ...

  @overload
  def tryAdvance(self, arg0: Consumer[str]) -> bool: ...

  @overload
  def tryAdvance(self, arg0: Consumer[T]) -> bool: ...

  @overload
  def trySplit(self) -> Spliterator[str]: ...

  @overload
  def trySplit(self) -> Spliterator[T]: ...


class FileStore:

  def getAttribute(self, arg0: str) -> object: ...

  def getBlockSize(self) -> int: ...

  def getFileStoreAttributeView(self, arg0: Class[V]) -> V: ...

  def getTotalSpace(self) -> int: ...

  def getUnallocatedSpace(self) -> int: ...

  def getUsableSpace(self) -> int: ...

  def isReadOnly(self) -> bool: ...

  def name(self) -> str: ...

  @overload
  def supportsFileAttributeView(self, arg0: Class[FileAttributeView]) -> bool: ...

  @overload
  def supportsFileAttributeView(self, arg0: str) -> bool: ...

  def type(self) -> str: ...


class FileSystem:

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  def getFileStores(self) -> Iterable[FileStore]: ...

  def getPath(self, arg0: str, arg1: list[str]) -> Path: ...

  def getPathMatcher(self, arg0: str) -> PathMatcher: ...

  def getRootDirectories(self) -> Iterable[Path]: ...

  def getSeparator(self) -> str: ...

  def getUserPrincipalLookupService(self) -> UserPrincipalLookupService: ...

  def isOpen(self) -> bool: ...

  def isReadOnly(self) -> bool: ...

  def newWatchService(self) -> WatchService: ...

  def provider(self) -> FileSystemProvider: ...

  def supportedFileAttributeViews(self) -> Set[str]: ...


class FileSystemException(IOException):

  def getFile(self) -> str: ...

  def getMessage(self) -> str: ...

  def getOtherFile(self) -> str: ...

  def getReason(self) -> str: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str): ...


class FileSystems:

  @staticmethod
  def getDefault() -> FileSystem: ...

  @staticmethod
  def getFileSystem(arg0: URI) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: Path) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: URI, arg1: Map[str, Any]) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: Path, arg1: ClassLoader) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: Path, arg1: Map[str, Any]) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: URI, arg1: Map[str, Any], arg2: ClassLoader) -> FileSystem: ...

  @staticmethod
  @overload
  def newFileSystem(arg0: Path, arg1: Map[str, Any], arg2: ClassLoader) -> FileSystem: ...

  class DefaultFileSystemHolder: ...


class FileVisitOption(Enum):

  FOLLOW_LINKS: FileVisitOption

  @staticmethod
  def valueOf(arg0: str) -> FileVisitOption: ...

  @staticmethod
  def values() -> list[FileVisitOption]: ...


class FileVisitResult(Enum):

  SKIP_SIBLINGS: FileVisitResult

  SKIP_SUBTREE: FileVisitResult

  TERMINATE: FileVisitResult

  @staticmethod
  def valueOf(arg0: str) -> FileVisitResult: ...

  @staticmethod
  def values() -> list[FileVisitResult]: ...


class FileVisitor[T]:

  def postVisitDirectory(self, arg0: object, arg1: IOException) -> FileVisitResult: ...

  def preVisitDirectory(self, arg0: object, arg1: BasicFileAttributes) -> FileVisitResult: ...

  def visitFile(self, arg0: object, arg1: BasicFileAttributes) -> FileVisitResult: ...

  def visitFileFailed(self, arg0: object, arg1: IOException) -> FileVisitResult: ...


class Files:

  @staticmethod
  @overload
  def copy(arg0: Path, arg1: OutputStream) -> int: ...

  @staticmethod
  @overload
  def copy(arg0: InputStream, arg1: Path, arg2: list[CopyOption]) -> int: ...

  @staticmethod
  @overload
  def copy(arg0: Path, arg1: Path, arg2: list[CopyOption]) -> Path: ...

  @staticmethod
  def createDirectories(arg0: Path, arg1: list[FileAttribute]) -> Path: ...

  @staticmethod
  def createDirectory(arg0: Path, arg1: list[FileAttribute]) -> Path: ...

  @staticmethod
  def createFile(arg0: Path, arg1: list[FileAttribute]) -> Path: ...

  @staticmethod
  def createLink(arg0: Path, arg1: Path) -> Path: ...

  @staticmethod
  def createSymbolicLink(arg0: Path, arg1: Path, arg2: list[FileAttribute]) -> Path: ...

  @staticmethod
  @overload
  def createTempDirectory(arg0: str, arg1: list[FileAttribute]) -> Path: ...

  @staticmethod
  @overload
  def createTempDirectory(arg0: Path, arg1: str, arg2: list[FileAttribute]) -> Path: ...

  @staticmethod
  @overload
  def createTempFile(arg0: str, arg1: str, arg2: list[FileAttribute]) -> Path: ...

  @staticmethod
  @overload
  def createTempFile(arg0: Path, arg1: str, arg2: str, arg3: list[FileAttribute]) -> Path: ...

  @staticmethod
  def delete(arg0: Path) -> None: ...

  @staticmethod
  def deleteIfExists(arg0: Path) -> bool: ...

  @staticmethod
  def exists(arg0: Path, arg1: list[LinkOption]) -> bool: ...

  @staticmethod
  def find(arg0: Path, arg1: int, arg2: BiPredicate[Path, BasicFileAttributes], arg3: list[FileVisitOption]) -> Stream[Path]: ...

  @staticmethod
  def getAttribute(arg0: Path, arg1: str, arg2: list[LinkOption]) -> object: ...

  @staticmethod
  def getFileAttributeView(arg0: Path, arg1: Class[V], arg2: list[LinkOption]) -> V: ...

  @staticmethod
  def getFileStore(arg0: Path) -> FileStore: ...

  @staticmethod
  def getLastModifiedTime(arg0: Path, arg1: list[LinkOption]) -> FileTime: ...

  @staticmethod
  def getOwner(arg0: Path, arg1: list[LinkOption]) -> UserPrincipal: ...

  @staticmethod
  def getPosixFilePermissions(arg0: Path, arg1: list[LinkOption]) -> Set[PosixFilePermission]: ...

  @staticmethod
  def isDirectory(arg0: Path, arg1: list[LinkOption]) -> bool: ...

  @staticmethod
  def isExecutable(arg0: Path) -> bool: ...

  @staticmethod
  def isHidden(arg0: Path) -> bool: ...

  @staticmethod
  def isReadable(arg0: Path) -> bool: ...

  @staticmethod
  def isRegularFile(arg0: Path, arg1: list[LinkOption]) -> bool: ...

  @staticmethod
  def isSameFile(arg0: Path, arg1: Path) -> bool: ...

  @staticmethod
  def isSymbolicLink(arg0: Path) -> bool: ...

  @staticmethod
  def isWritable(arg0: Path) -> bool: ...

  @staticmethod
  @overload
  def lines(arg0: Path) -> Stream[str]: ...

  @staticmethod
  @overload
  def lines(arg0: Path, arg1: Charset) -> Stream[str]: ...

  @staticmethod
  def list(arg0: Path) -> Stream[Path]: ...

  @staticmethod
  def mismatch(arg0: Path, arg1: Path) -> int: ...

  @staticmethod
  def move(arg0: Path, arg1: Path, arg2: list[CopyOption]) -> Path: ...

  @staticmethod
  @overload
  def newBufferedReader(arg0: Path) -> BufferedReader: ...

  @staticmethod
  @overload
  def newBufferedReader(arg0: Path, arg1: Charset) -> BufferedReader: ...

  @staticmethod
  @overload
  def newBufferedWriter(arg0: Path, arg1: list[OpenOption]) -> BufferedWriter: ...

  @staticmethod
  @overload
  def newBufferedWriter(arg0: Path, arg1: Charset, arg2: list[OpenOption]) -> BufferedWriter: ...

  @staticmethod
  @overload
  def newByteChannel(arg0: Path, arg1: list[OpenOption]) -> SeekableByteChannel: ...

  @staticmethod
  @overload
  def newByteChannel(arg0: Path, arg1: Set[OpenOption], arg2: list[FileAttribute]) -> SeekableByteChannel: ...

  @staticmethod
  @overload
  def newDirectoryStream(arg0: Path) -> DirectoryStream[Path]: ...

  @staticmethod
  @overload
  def newDirectoryStream(arg0: Path, arg1: str) -> DirectoryStream[Path]: ...

  @staticmethod
  @overload
  def newDirectoryStream(arg0: Path, arg1: DirectoryStream.Filter) -> DirectoryStream[Path]: ...

  @staticmethod
  def newInputStream(arg0: Path, arg1: list[OpenOption]) -> InputStream: ...

  @staticmethod
  def newOutputStream(arg0: Path, arg1: list[OpenOption]) -> OutputStream: ...

  @staticmethod
  def notExists(arg0: Path, arg1: list[LinkOption]) -> bool: ...

  @staticmethod
  def probeContentType(arg0: Path) -> str: ...

  @staticmethod
  def readAllBytes(arg0: Path) -> list[int]: ...

  @staticmethod
  @overload
  def readAllLines(arg0: Path) -> List[str]: ...

  @staticmethod
  @overload
  def readAllLines(arg0: Path, arg1: Charset) -> List[str]: ...

  @staticmethod
  @overload
  def readAttributes(arg0: Path, arg1: Class[A], arg2: list[LinkOption]) -> A: ...

  @staticmethod
  @overload
  def readAttributes(arg0: Path, arg1: str, arg2: list[LinkOption]) -> Map[str, object]: ...

  @staticmethod
  @overload
  def readString(arg0: Path) -> str: ...

  @staticmethod
  @overload
  def readString(arg0: Path, arg1: Charset) -> str: ...

  @staticmethod
  def readSymbolicLink(arg0: Path) -> Path: ...

  @staticmethod
  def setAttribute(arg0: Path, arg1: str, arg2: object, arg3: list[LinkOption]) -> Path: ...

  @staticmethod
  def setLastModifiedTime(arg0: Path, arg1: FileTime) -> Path: ...

  @staticmethod
  def setOwner(arg0: Path, arg1: UserPrincipal) -> Path: ...

  @staticmethod
  def setPosixFilePermissions(arg0: Path, arg1: Set[PosixFilePermission]) -> Path: ...

  @staticmethod
  def size(arg0: Path) -> int: ...

  @staticmethod
  @overload
  def walk(arg0: Path, arg1: list[FileVisitOption]) -> Stream[Path]: ...

  @staticmethod
  @overload
  def walk(arg0: Path, arg1: int, arg2: list[FileVisitOption]) -> Stream[Path]: ...

  @staticmethod
  @overload
  def walkFileTree(arg0: Path, arg1: FileVisitor[Path]) -> Path: ...

  @staticmethod
  @overload
  def walkFileTree(arg0: Path, arg1: Set[FileVisitOption], arg2: int, arg3: FileVisitor[Path]) -> Path: ...

  @staticmethod
  @overload
  def write(arg0: Path, arg1: list[int], arg2: list[OpenOption]) -> Path: ...

  @staticmethod
  @overload
  def write(arg0: Path, arg1: Iterable[CharSequence], arg2: list[OpenOption]) -> Path: ...

  @staticmethod
  @overload
  def write(arg0: Path, arg1: Iterable[CharSequence], arg2: Charset, arg3: list[OpenOption]) -> Path: ...

  @staticmethod
  @overload
  def writeString(arg0: Path, arg1: CharSequence, arg2: list[OpenOption]) -> Path: ...

  @staticmethod
  @overload
  def writeString(arg0: Path, arg1: CharSequence, arg2: Charset, arg3: list[OpenOption]) -> Path: ...

  class AcceptAllFilter:

    @overload
    def accept(self, arg0: object) -> bool: ...

    @overload
    def accept(self, arg0: object) -> bool: ...

    @overload
    def accept(self, arg0: Path) -> bool: ...

  class FileTypeDetectors: ...


class LinkOption(Enum):

  NOFOLLOW_LINKS: LinkOption

  @staticmethod
  def valueOf(arg0: str) -> LinkOption: ...

  @staticmethod
  def values() -> list[LinkOption]: ...


class NoSuchFileException(FileSystemException):

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: str, arg1: str, arg2: str): ...


class OpenOption: ...


class Path:

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: Path) -> int: ...

  @overload
  def endsWith(self, arg0: str) -> bool: ...

  @overload
  def endsWith(self, arg0: Path) -> bool: ...

  def equals(self, arg0: object) -> bool: ...

  def forEach(self, arg0: Consumer[T]) -> None: ...

  def getFileName(self) -> Path: ...

  def getFileSystem(self) -> FileSystem: ...

  def getName(self, arg0: int) -> Path: ...

  def getNameCount(self) -> int: ...

  def getParent(self) -> Path: ...

  def getRoot(self) -> Path: ...

  def hashCode(self) -> int: ...

  def isAbsolute(self) -> bool: ...

  @overload
  def iterator(self) -> Iterator[Path]: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  def normalize(self) -> Path: ...

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind]) -> WatchKey: ...

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind]) -> WatchKey: ...

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind], arg2: list[WatchEvent.Modifier]) -> WatchKey: ...

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind], arg2: list[WatchEvent.Modifier]) -> WatchKey: ...

  def relativize(self, arg0: Path) -> Path: ...

  @overload
  def resolve(self, arg0: str) -> Path: ...

  @overload
  def resolve(self, arg0: Path) -> Path: ...

  @overload
  def resolveSibling(self, arg0: str) -> Path: ...

  @overload
  def resolveSibling(self, arg0: Path) -> Path: ...

  def spliterator(self) -> Spliterator[T]: ...

  @overload
  def startsWith(self, arg0: str) -> bool: ...

  @overload
  def startsWith(self, arg0: Path) -> bool: ...

  def subpath(self, arg0: int, arg1: int) -> Path: ...

  def toAbsolutePath(self) -> Path: ...

  def toFile(self) -> File: ...

  def toRealPath(self, arg0: list[LinkOption]) -> Path: ...

  def toString(self) -> str: ...

  def toUri(self) -> URI: ...

  @staticmethod
  @overload
  def of(arg0: URI) -> Path: ...

  @staticmethod
  @overload
  def of(arg0: str, arg1: list[str]) -> Path: ...


class PathMatcher:

  def matches(self, arg0: Path) -> bool: ...


class Paths:

  @staticmethod
  @overload
  def get(arg0: URI) -> Path: ...

  @staticmethod
  @overload
  def get(arg0: str, arg1: list[str]) -> Path: ...


class StandardOpenOption(Enum):

  APPEND: StandardOpenOption

  CREATE: StandardOpenOption

  CREATE_NEW: StandardOpenOption

  DELETE_ON_CLOSE: StandardOpenOption

  DSYNC: StandardOpenOption

  READ: StandardOpenOption

  SPARSE: StandardOpenOption

  SYNC: StandardOpenOption

  TRUNCATE_EXISTING: StandardOpenOption

  WRITE: StandardOpenOption

  @staticmethod
  def valueOf(arg0: str) -> StandardOpenOption: ...

  @staticmethod
  def values() -> list[StandardOpenOption]: ...


class WatchEvent[T]:

  def context(self) -> object: ...

  def count(self) -> int: ...

  def kind(self) -> WatchEvent.Kind: ...

  class Modifier:

    def name(self) -> str: ...

  class Kind[Kind_T]:

    def name(self) -> str: ...

    def type(self) -> Class[T]: ...


class WatchKey:

  def cancel(self) -> None: ...

  def isValid(self) -> bool: ...

  def pollEvents(self) -> List[WatchEvent[Any]]: ...

  def reset(self) -> bool: ...

  def watchable(self) -> Watchable: ...


class WatchService:

  @overload
  def close(self) -> None: ...

  @overload
  def close(self) -> None: ...

  @overload
  def poll(self) -> WatchKey: ...

  @overload
  def poll(self, arg0: int, arg1: TimeUnit) -> WatchKey: ...

  def take(self) -> WatchKey: ...


class Watchable:

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind]) -> WatchKey: ...

  @overload
  def register(self, arg0: WatchService, arg1: list[WatchEvent.Kind], arg2: list[WatchEvent.Modifier]) -> WatchKey: ...

