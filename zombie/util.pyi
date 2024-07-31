from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import RandomAccessFile, File, InputStream, OutputStream
from java.lang import Enum, Runnable, Exception, Throwable, Class, Boolean
from java.nio import ByteBuffer
from java.sql import Connection
from java.util import Comparator, List, Date, Calendar
from java.util.function import Predicate, Consumer, BiPredicate, Function, BiConsumer, Supplier, BiFunction
from javax.xml.bind import Unmarshaller, Marshaller
from org.w3c.dom import Document, Element
from zombie.characters import IsoPlayer
from zombie.iso import Vector3
from zombie.util.lambda import Stacks, Comparators, Consumers, Predicates, IntSupplierFunction, Invokers

E = TypeVar('E', default=Any)
T = TypeVar('T', default=Any)
T1 = TypeVar('T1', default=Any)
T2 = TypeVar('T2', default=Any)
T3 = TypeVar('T3', default=Any)
T4 = TypeVar('T4', default=Any)
T5 = TypeVar('T5', default=Any)
T6 = TypeVar('T6', default=Any)
F = TypeVar('F', default=Any)
R = TypeVar('R', default=Any)
PO = TypeVar('PO', default=Any)
I = TypeVar('I', default=Any)

class AbstractIntCollection:

  @overload
  def add(self, v: int) -> bool: ...

  @overload
  def add(self, v: int) -> bool: ...

  @overload
  def addAll(self, c: IntCollection) -> bool: ...

  @overload
  def addAll(self, c: IntCollection) -> bool: ...

  @overload
  def clear(self) -> None: ...

  @overload
  def clear(self) -> None: ...

  @overload
  def contains(self, v: int) -> bool: ...

  @overload
  def contains(self, v: int) -> bool: ...

  @overload
  def containsAll(self, c: IntCollection) -> bool: ...

  @overload
  def containsAll(self, c: IntCollection) -> bool: ...

  def equals(self, arg0: object) -> bool: ...

  def hashCode(self) -> int: ...

  @overload
  def isEmpty(self) -> bool: ...

  @overload
  def isEmpty(self) -> bool: ...

  def iterator(self) -> IntIterator: ...

  @overload
  def remove(self, v: int) -> bool: ...

  @overload
  def remove(self, v: int) -> bool: ...

  @overload
  def removeAll(self, c: IntCollection) -> bool: ...

  @overload
  def removeAll(self, c: IntCollection) -> bool: ...

  @overload
  def retainAll(self, c: IntCollection) -> bool: ...

  @overload
  def retainAll(self, c: IntCollection) -> bool: ...

  @overload
  def size(self) -> int: ...

  @overload
  def size(self) -> int: ...

  @overload
  def toArray(self) -> list[int]: ...

  @overload
  def toArray(self) -> list[int]: ...

  @overload
  def toArray(self, a: list[int]) -> list[int]: ...

  @overload
  def toArray(self, a: list[int]) -> list[int]: ...

  def toString(self) -> str: ...

  @overload
  def trimToSize(self) -> None: ...

  @overload
  def trimToSize(self) -> None: ...


class AddCoopPlayer:

  def accessDenied(self, playerIndex: int, reason: str) -> None: ...

  def accessGranted(self, playerIndex: int) -> None: ...

  def isFinished(self) -> bool: ...

  def isLoadingThisSquare(self, x: int, y: int) -> bool: ...

  def receivePlayerConnect(self, playerIndex: int) -> None: ...

  def update(self) -> None: ...

  def __init__(self, player: IsoPlayer): ...

  class Stage(Enum):

    AddToWorld: AddCoopPlayer.Stage

    CheckMapLoading: AddCoopPlayer.Stage

    Finished: AddCoopPlayer.Stage

    Init: AddCoopPlayer.Stage

    ReceiveClientConnect: AddCoopPlayer.Stage

    ReceivePlayerConnect: AddCoopPlayer.Stage

    SendPlayerConnect: AddCoopPlayer.Stage

    StartMapLoading: AddCoopPlayer.Stage

    @staticmethod
    def valueOf(arg0: str) -> AddCoopPlayer.Stage: ...

    @staticmethod
    def values() -> list[AddCoopPlayer.Stage]: ...


class BufferedRandomAccessFile(RandomAccessFile):

  def getFilePointer(self) -> int: ...

  def getNextLine(self) -> str: ...

  @overload
  def read(self) -> int: ...

  @overload
  def read(self, b: list[int], __off__: int, len: int) -> int: ...

  def seek(self, pos: int) -> None: ...

  @overload
  def __init__(self, file: File, mode: str, bufsize: int): ...
  @overload
  def __init__(self, filename: str, mode: str, bufsize: int): ...


class ByteBufferBackedInputStream(InputStream):

  @overload
  def read(self) -> int: ...

  @overload
  def read(self, bytes: list[int], __off__: int, len: int) -> int: ...

  def __init__(self, buf: ByteBuffer): ...


class ByteBufferOutputStream(OutputStream):

  def clear(self) -> None: ...

  def flip(self) -> None: ...

  def getWrappedBuffer(self) -> ByteBuffer: ...

  def toByteBuffer(self) -> ByteBuffer: ...

  @overload
  def write(self, bytes: list[int]) -> None: ...

  @overload
  def write(self, bty: int) -> None: ...

  @overload
  def write(self, bytes: list[int], __off__: int, len: int) -> None: ...

  def __init__(self, wrappedBuffer: ByteBuffer, autoEnlarge: bool): ...


class ExecuteTimeAnalyse:

  def add(self, comment: str) -> None: ...

  def getMsTime(self) -> int: ...

  def getNanoTime(self) -> int: ...

  def print(self) -> None: ...

  def reset(self) -> None: ...

  def __init__(self, caption: str, size: int): ...

  class TimeStamp:

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, arg0: str): ...


class ICloner[E]:

  def clone(self, arg0: object) -> object: ...


class IPooledObject:

  def getPool(self) -> Pool[IPooledObject]: ...

  def isFree(self) -> bool: ...

  def onReleased(self) -> None: ...

  def release(self) -> None: ...

  def setFree(self, isFree: bool) -> None: ...

  def setPool(self, pool: Pool[IPooledObject]) -> None: ...

  @staticmethod
  def releaseAndBlank(list: list[IPooledObject]) -> None: ...

  @staticmethod
  def tryReleaseAndBlank(list: list[IPooledObject]) -> None: ...


class IPredicate[E]:

  def negate(self) -> Predicate[T]: ...

  def test(self, arg0: object) -> bool: ...

  @staticmethod
  def isEqual(arg0: object) -> Predicate[T]: ...


class IntCollection:

  def add(self, v: int) -> bool: ...

  def addAll(self, c: IntCollection) -> bool: ...

  def clear(self) -> None: ...

  def contains(self, v: int) -> bool: ...

  def containsAll(self, c: IntCollection) -> bool: ...

  def equals(self, obj: object) -> bool: ...

  def hashCode(self) -> int: ...

  def isEmpty(self) -> bool: ...

  def iterator(self) -> IntIterator: ...

  def remove(self, v: int) -> bool: ...

  def removeAll(self, c: IntCollection) -> bool: ...

  def retainAll(self, c: IntCollection) -> bool: ...

  def size(self) -> int: ...

  @overload
  def toArray(self) -> list[int]: ...

  @overload
  def toArray(self, a: list[int]) -> list[int]: ...

  def trimToSize(self) -> None: ...


class IntComparator:

  def compare(self, v1: int, v2: int) -> int: ...


class IntIterator:

  def hasNext(self) -> bool: ...

  def next(self) -> int: ...

  def remove(self) -> None: ...


class Lambda:

  @staticmethod
  @overload
  def capture(arg0: object, arg1: Stacks.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def capture(arg0: object, arg1: object, arg2: Stacks.Params2.ICallback) -> None: ...

  @staticmethod
  @overload
  def capture(arg0: object, arg1: object, arg2: object, arg3: Stacks.Params3.ICallback) -> None: ...

  @staticmethod
  @overload
  def capture(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Stacks.Params4.ICallback) -> None: ...

  @staticmethod
  @overload
  def capture(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: Stacks.Params5.ICallback) -> None: ...

  @staticmethod
  @overload
  def capture(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: Stacks.Params6.ICallback) -> None: ...

  @staticmethod
  @overload
  def comparator(arg0: object, arg1: Comparators.Params1.ICallback) -> Comparator[E]: ...

  @staticmethod
  @overload
  def comparator(arg0: object, arg1: object, arg2: Comparators.Params2.ICallback) -> Comparator[E]: ...

  @staticmethod
  @overload
  def consumer(arg0: object, arg1: Consumers.Params1.ICallback) -> Consumer[E]: ...

  @staticmethod
  @overload
  def consumer(arg0: object, arg1: object, arg2: Consumers.Params2.ICallback) -> Consumer[E]: ...

  @staticmethod
  @overload
  def consumer(arg0: object, arg1: object, arg2: object, arg3: Consumers.Params3.ICallback) -> Consumer[E]: ...

  @staticmethod
  @overload
  def consumer(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Consumers.Params4.ICallback) -> Consumer[E]: ...

  @staticmethod
  @overload
  def consumer(arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: Consumers.Params5.ICallback) -> Consumer[E]: ...

  @staticmethod
  def contains(arg0: Predicate[Predicate[E]], arg1: object, arg2: Predicates.Params1.ICallback) -> bool: ...

  @staticmethod
  def containsFrom(arg0: BiPredicate[F, Predicate[E]], arg1: F, arg2: object, arg3: Predicates.Params1.ICallback) -> bool: ...

  @staticmethod
  def find(arg0: Function[Predicate[E], R], arg1: object, arg2: Predicates.Params1.ICallback) -> object: ...

  @staticmethod
  @overload
  def forEach(arg0: Consumer[Consumer[E]], arg1: object, arg2: Consumers.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def forEach(arg0: Consumer[Consumer[E]], arg1: object, arg2: object, arg3: Consumers.Params2.ICallback) -> None: ...

  @staticmethod
  @overload
  def forEachFrom(arg0: BiConsumer[F, Consumer[E]], arg1: object, arg2: object, arg3: Consumers.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def forEachFrom(arg0: BiConsumer[List[E], Consumer[E]], arg1: List[E], arg2: object, arg3: Consumers.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def forEachFrom(arg0: BiConsumer[F, Consumer[E]], arg1: object, arg2: object, arg3: object, arg4: Consumers.Params2.ICallback) -> None: ...

  @staticmethod
  @overload
  def forEachFrom(arg0: BiConsumer[List[E], Consumer[E]], arg1: List[E], arg2: object, arg3: object, arg4: Consumers.Params2.ICallback) -> None: ...

  @staticmethod
  def indexOf(arg0: IntSupplierFunction[Predicate[E]], arg1: object, arg2: Predicates.Params1.ICallback) -> int: ...

  @staticmethod
  @overload
  def invoke(arg0: Consumer[Runnable], arg1: object, arg2: Invokers.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def invoke(arg0: Consumer[Runnable], arg1: object, arg2: object, arg3: Invokers.Params2.ICallback) -> None: ...

  @staticmethod
  @overload
  def invoker(arg0: object, arg1: Invokers.Params1.ICallback) -> Runnable: ...

  @staticmethod
  @overload
  def invoker(arg0: object, arg1: object, arg2: Invokers.Params2.ICallback) -> Runnable: ...

  @staticmethod
  @overload
  def invoker(arg0: object, arg1: object, arg2: object, arg3: Invokers.Params3.ICallback) -> Runnable: ...

  @staticmethod
  @overload
  def invoker(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Invokers.Params4.ICallback) -> Runnable: ...

  @staticmethod
  @overload
  def predicate(arg0: object, arg1: Predicates.Params1.ICallback) -> Predicate[E]: ...

  @staticmethod
  @overload
  def predicate(arg0: object, arg1: object, arg2: Predicates.Params2.ICallback) -> Predicate[E]: ...

  @staticmethod
  @overload
  def predicate(arg0: object, arg1: object, arg2: object, arg3: Predicates.Params3.ICallback) -> Predicate[E]: ...

  def __init__(self): ...


class LocationRNG:

  instance: LocationRNG

  def getSeed(self) -> int: ...

  def nextFloat(self) -> float: ...

  @overload
  def nextInt(self, n: int) -> int: ...

  @overload
  def nextInt(self, n: int, x: int, y: int, z: int) -> int: ...

  def setSeed(self, seed: int) -> None: ...

  def __init__(self): ...


class PZCalendar:

  def get(self, field: int) -> int: ...

  def getTime(self) -> Date: ...

  def getTimeInMillis(self) -> int: ...

  def isLeapYear(self, year: int) -> bool: ...

  def set(self, year: int, month: int, dayOfMonth: int, hourOfDay: int, minute: int) -> None: ...

  def setTimeInMillis(self, millis: int) -> None: ...

  @staticmethod
  def getInstance() -> PZCalendar: ...

  def __init__(self, calendar: Calendar): ...


class PZSQLUtils:

  @staticmethod
  def getConnection(absolutePath: str) -> Connection: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class PZXmlParserException(Exception):

  def toString(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, message: str): ...
  @overload
  def __init__(self, cause: Throwable): ...
  @overload
  def __init__(self, message: str, cause: Throwable): ...


class PZXmlUtil:

  @staticmethod
  def createNewDocument() -> Document: ...

  @staticmethod
  def forEachElement(root: Element, consumer: Consumer[Element]) -> None: ...

  @staticmethod
  def parse(type: Class[T], source: str) -> object: ...

  @staticmethod
  def parseXml(source: str) -> Element: ...

  @staticmethod
  @overload
  def tryWrite(arg0: object, arg1: File) -> bool: ...

  @staticmethod
  @overload
  def tryWrite(doc: Document, outFile: File) -> bool: ...

  @staticmethod
  @overload
  def write(arg0: object, arg1: File) -> None: ...

  @staticmethod
  @overload
  def write(doc: Document, outFile: File) -> None: ...

  def __init__(self): ...

  class UnmarshallerAllocator:

    @staticmethod
    def get(arg0: Class[T]) -> Unmarshaller: ...

  class MarshallerAllocator:

    @staticmethod
    @overload
    def get(arg0: Class[T]) -> Marshaller: ...

    @staticmethod
    @overload
    def get(arg0: object) -> Marshaller: ...


class Pool[PO]:

  def alloc(self) -> PO: ...

  def release(self, item: IPooledObject) -> None: ...

  @staticmethod
  @overload
  def tryRelease(arg0: list[IPooledObject]) -> list[IPooledObject]: ...

  @staticmethod
  @overload
  def tryRelease(arg0: object) -> object: ...

  @staticmethod
  @overload
  def tryRelease(arg0: E) -> E: ...

  def __init__(self, allocator: Supplier[PO]): ...

  class PoolStacks: ...


class PooledArrayObject[T](PooledObject):

  def array(self) -> list[object]: ...

  def get(self, idx: int) -> object: ...

  def isEmpty(self) -> bool: ...

  def length(self) -> int: ...

  def set(self, arg0: int, arg1: object) -> None: ...

  def __init__(self): ...


class PooledFloatArrayObject(PooledObject):

  def array(self) -> list[float]: ...

  def get(self, idx: int) -> float: ...

  def length(self) -> int: ...

  def set(self, idx: int, val: float) -> None: ...

  @staticmethod
  def alloc(count: int) -> PooledFloatArrayObject: ...

  @staticmethod
  def toArray(source: PooledFloatArrayObject) -> PooledFloatArrayObject: ...

  def __init__(self): ...


class PooledObject:

  @overload
  def getPool(self) -> Pool[IPooledObject]: ...

  @overload
  def getPool(self) -> Pool[IPooledObject]: ...

  @overload
  def isFree(self) -> bool: ...

  @overload
  def isFree(self) -> bool: ...

  def onReleased(self) -> None: ...

  @overload
  def release(self) -> None: ...

  @overload
  def release(self) -> None: ...

  @overload
  def setFree(self, isFree: bool) -> None: ...

  @overload
  def setFree(self, isFree: bool) -> None: ...

  @overload
  def setPool(self, pool: Pool[IPooledObject]) -> None: ...

  @overload
  def setPool(self, pool: Pool[IPooledObject]) -> None: ...

  @staticmethod
  def releaseAndBlank(arg0: list[IPooledObject]) -> None: ...

  @staticmethod
  def tryReleaseAndBlank(arg0: list[IPooledObject]) -> None: ...

  def __init__(self): ...


class PooledObjectArrayObject[T](PooledArrayObject):

  def onReleased(self) -> None: ...

  def __init__(self): ...


class PublicServerUtil:

  webSite: str

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def insertOrUpdate() -> None: ...

  @staticmethod
  def isEnabled() -> bool: ...

  @staticmethod
  def update() -> None: ...

  @staticmethod
  def updatePlayerCountIfChanged() -> None: ...

  @staticmethod
  def updatePlayers() -> None: ...

  def __init__(self): ...


class RaySphereIntersectCheck:

  @staticmethod
  def intersects(origin: Vector3, dirAndLength: Vector3, sphereCentre: Vector3, sphereRadius: float) -> bool: ...

  def __init__(self): ...


class SharedStrings:

  def clear(self) -> None: ...

  def get(self, s: str) -> str: ...

  def __init__(self): ...


class StringUtils:

  s_emptyString: str

  UTF8_BOM: str

  @staticmethod
  def contains(array: list[str], val: str, equalizer: BiFunction[str, str, Boolean]) -> bool: ...

  @staticmethod
  def containsDoubleDot(arg0: str) -> bool: ...

  @staticmethod
  def containsIgnoreCase(haystack: str, needle: str) -> bool: ...

  @staticmethod
  def discardNullOrWhitespace(str: str) -> str: ...

  @staticmethod
  def endsWithIgnoreCase(str: str, suffix: str) -> bool: ...

  @staticmethod
  def equals(a: str, b: str) -> bool: ...

  @staticmethod
  def equalsIgnoreCase(a: str, b: str) -> bool: ...

  @staticmethod
  def indent(text: str) -> str: ...

  @staticmethod
  def indexOf(array: list[str], val: str, equalizer: BiFunction[str, str, Boolean]) -> int: ...

  @staticmethod
  def isBoolean(varStr: str) -> bool: ...

  @staticmethod
  def isNullOrEmpty(s: str) -> bool: ...

  @staticmethod
  def isNullOrWhitespace(s: str) -> bool: ...

  @staticmethod
  def leftJustify(text: str, length: int) -> str: ...

  @staticmethod
  def moduleDotType(module: str, type: str) -> str: ...

  @staticmethod
  def startsWithIgnoreCase(str: str, prefix: str) -> bool: ...

  @staticmethod
  def stripBOM(line: str) -> str: ...

  @staticmethod
  def trimPrefix(str: str, prefix: str) -> str: ...

  @staticmethod
  def trimSuffix(str: str, suffix: str) -> str: ...

  @staticmethod
  def tryParseBoolean(varStr: str) -> bool: ...

  def __init__(self): ...


class Type:

  @staticmethod
  @overload
  def asBoolean(val: object) -> bool: ...

  @staticmethod
  @overload
  def asBoolean(val: object, defaultVal: bool) -> bool: ...

  @staticmethod
  def tryCastTo(arg0: object, arg1: Class[R]) -> object: ...

  def __init__(self): ...

