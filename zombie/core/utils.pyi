from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum, StringBuilder, Thread, Class
from java.lang.ref import PhantomReference, ReferenceQueue
from java.nio import ByteBuffer, Buffer
from zombie.core.textures import Texture
from zombie.iso import IsoGridSquare

E = TypeVar('E', default=Any)
T = TypeVar('T', default=Any)
Entry_T = TypeVar('Entry_T', default=Any)

class Bits:

  BIT_0: int

  BIT_1: int

  BIT_10: int

  BIT_11: int

  BIT_12: int

  BIT_13: int

  BIT_14: int

  BIT_15: int

  BIT_16: int

  BIT_17: int

  BIT_18: int

  BIT_19: int

  BIT_2: int

  BIT_20: int

  BIT_21: int

  BIT_22: int

  BIT_23: int

  BIT_24: int

  BIT_25: int

  BIT_26: int

  BIT_27: int

  BIT_28: int

  BIT_29: int

  BIT_3: int

  BIT_30: int

  BIT_31: int

  BIT_32: int

  BIT_33: int

  BIT_34: int

  BIT_35: int

  BIT_36: int

  BIT_37: int

  BIT_38: int

  BIT_39: int

  BIT_4: int

  BIT_40: int

  BIT_41: int

  BIT_42: int

  BIT_43: int

  BIT_44: int

  BIT_45: int

  BIT_46: int

  BIT_47: int

  BIT_48: int

  BIT_49: int

  BIT_5: int

  BIT_50: int

  BIT_51: int

  BIT_52: int

  BIT_53: int

  BIT_54: int

  BIT_55: int

  BIT_56: int

  BIT_57: int

  BIT_58: int

  BIT_59: int

  BIT_6: int

  BIT_60: int

  BIT_61: int

  BIT_62: int

  BIT_63: int

  BIT_7: int

  BIT_8: int

  BIT_9: int

  BIT_BYTE_MAX: int

  BIT_INT_MAX: int

  BIT_LONG_MAX: int

  BIT_SHORT_MAX: int

  ENABLED: bool

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def addFlags(value: int, flags: int) -> int: ...

  @staticmethod
  @overload
  def checkFlags(value: int, flags: int, limit: int, option: Bits.CompareOption) -> bool: ...

  @staticmethod
  @overload
  def checkFlags(value: int, flags: int, limit: int, option: Bits.CompareOption) -> bool: ...

  @staticmethod
  @overload
  def getBitsString(bits: int) -> str: ...

  @staticmethod
  @overload
  def getBitsString(bits: int) -> str: ...

  @staticmethod
  @overload
  def getBitsString(bits: int) -> str: ...

  @staticmethod
  @overload
  def getBitsString(bits: int) -> str: ...

  @staticmethod
  @overload
  def getLen(b: int) -> int: ...

  @staticmethod
  @overload
  def getLen(i: int) -> int: ...

  @staticmethod
  @overload
  def getLen(l: int) -> int: ...

  @staticmethod
  @overload
  def getLen(s: int) -> int: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasEitherFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def hasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  @overload
  def notHasFlags(value: int, flags: int) -> bool: ...

  @staticmethod
  def packFloatUnitToByte(f: float) -> int: ...

  @staticmethod
  def unpackByteToFloatUnit(b: int) -> float: ...

  def __init__(self): ...

  class CompareOption(Enum):

    ContainsAll: Bits.CompareOption

    HasEither: Bits.CompareOption

    NotHas: Bits.CompareOption

    @staticmethod
    def valueOf(arg0: str) -> Bits.CompareOption: ...

    @staticmethod
    def values() -> list[Bits.CompareOption]: ...


class BooleanGrid:

  def LoadFromByteBuffer(self, cache: ByteBuffer) -> None: ...

  def PutToByteBuffer(self, cache: ByteBuffer) -> None: ...

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> BooleanGrid: ...

  def copy(self, src: BooleanGrid) -> None: ...

  def fill(self) -> None: ...

  def getHeight(self) -> int: ...

  def getValue(self, x: int, y: int) -> bool: ...

  def getWidth(self) -> int: ...

  def setValue(self, x: int, y: int, newValue: bool) -> None: ...

  def toString(self) -> str: ...

  def __init__(self, width: int, height: int): ...


class BoundedQueue[E]:

  def add(self, arg0: object) -> None: ...

  def capacity(self) -> int: ...

  def clear(self) -> None: ...

  def get(self, index: int) -> object: ...

  def isEmpty(self) -> bool: ...

  def isFull(self) -> bool: ...

  def remove(self, index: int) -> object: ...

  def removeFirst(self) -> object: ...

  def size(self) -> int: ...

  def __init__(self, numElements: int): ...


class BufferUtils:

  @staticmethod
  def createByteBuffer(size: int) -> ByteBuffer: ...

  @staticmethod
  def destroyDirectBuffer(toBeDestroyed: Buffer) -> None: ...

  @staticmethod
  def printCurrentDirectMemory(store: StringBuilder) -> None: ...

  @staticmethod
  def setTrackDirectMemoryEnabled(enabled: bool) -> None: ...

  def __init__(self): ...

  class ClearReferences(Thread):

    def run(self) -> None: ...

  class BufferInfo(PhantomReference):

    def __init__(self, arg0: Class, arg1: int, arg2: Buffer, arg3: ReferenceQueue[Buffer]): ...


class DirectBufferAllocator:

  @staticmethod
  def allocate(size: int) -> WrappedBuffer: ...

  @staticmethod
  def getBytesAllocated() -> int: ...

  def __init__(self): ...


class ExpandableBooleanList:

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> ExpandableBooleanList: ...

  def fill(self) -> None: ...

  def getValue(self, x: int) -> bool: ...

  def getWidth(self) -> int: ...

  def setValue(self, x: int, newValue: bool) -> None: ...

  def __init__(self, width: int): ...


class FibonacciHeap[T]:

  def decreaseKey(self, entry: FibonacciHeap.Entry, newPriority: float) -> None: ...

  @overload
  def delete(self, entry: FibonacciHeap.Entry) -> None: ...

  @overload
  def delete(self, threadID: int, node: IsoGridSquare) -> None: ...

  def dequeueMin(self) -> FibonacciHeap.Entry: ...

  def empty(self) -> None: ...

  def enqueue(self, arg0: object, arg1: float) -> FibonacciHeap.Entry: ...

  def isEmpty(self) -> bool: ...

  def min(self) -> FibonacciHeap.Entry: ...

  def size(self) -> int: ...

  @staticmethod
  def merge(one: FibonacciHeap[T], two: FibonacciHeap[T]) -> FibonacciHeap[T]: ...

  def __init__(self): ...

  class Entry[Entry_T]:

    def getPriority(self) -> float: ...

    def getValue(self) -> object: ...

    def setValue(self, arg0: object) -> None: ...


class HashMap:

  def clear(self) -> None: ...

  def get(self, key: object) -> object: ...

  def isEmpty(self) -> bool: ...

  def iterator(self) -> HashMap.Iterator: ...

  def put(self, key: object, value: object) -> object: ...

  def remove(self, key: object) -> object: ...

  def size(self) -> int: ...

  def toString(self) -> str: ...

  def __init__(self): ...

  class Bucket:

    def clear(self) -> None: ...

    def put(self, arg0: object, arg1: object) -> None: ...

    def remove(self, arg0: object) -> object: ...

    def size(self) -> int: ...

  class Iterator:

    def advance(self) -> bool: ...

    def getKey(self) -> object: ...

    def getValue(self) -> object: ...

    def hasNext(self) -> bool: ...

    def reset(self) -> HashMap.Iterator: ...

    def __init__(self, hashmap: HashMap): ...


class ImageUtils:

  USE_MIPMAP: bool

  @staticmethod
  def depureTexture(texture: Texture, limit: float) -> None: ...

  @staticmethod
  def getNextPowerOfTwo(fold: int) -> int: ...

  @staticmethod
  def getNextPowerOfTwoHW(fold: int) -> int: ...

  @staticmethod
  def getScreenShot() -> Texture: ...

  @staticmethod
  @overload
  def makeTransp(data: ByteBuffer, red: int, green: int, blue: int, widthHW: int, heightHW: int) -> ByteBuffer: ...

  @staticmethod
  @overload
  def makeTransp(data: ByteBuffer, red: int, green: int, blue: int, alpha: int, widthHW: int, heightHW: int) -> ByteBuffer: ...

  @staticmethod
  def saveBmpImage(texture: Texture, path: str) -> None: ...

  @staticmethod
  def saveImage(texture: Texture, path: str, format: str) -> None: ...

  @staticmethod
  def saveJpgImage(texture: Texture, path: str) -> None: ...

  @staticmethod
  def savePngImage(texture: Texture, path: str) -> None: ...


class IntGrid:

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IntGrid: ...

  def fill(self, newValue: int) -> None: ...

  def getHeight(self) -> int: ...

  def getValue(self, x: int, y: int) -> int: ...

  def getWidth(self) -> int: ...

  def setValue(self, x: int, y: int, newValue: int) -> None: ...

  def __init__(self, width: int, height: int): ...


class IntHyperCube2:

  def clear(self) -> None: ...

  def fill(self, newValue: int) -> None: ...

  def getDepth(self) -> int: ...

  def getHeight(self) -> int: ...

  def getQuanta(self) -> int: ...

  def getValue(self, x: int, y: int, z: int, w: int) -> int: ...

  def getWidth(self) -> int: ...

  def setValue(self, x: int, y: int, z: int, w: int, newValue: int) -> None: ...

  def __init__(self, width: int, height: int, depth: int, quanta: int): ...


class IntHypercube:

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> IntHypercube: ...

  def fill(self, newValue: int) -> None: ...

  def getDepth(self) -> int: ...

  def getHeight(self) -> int: ...

  def getQuanta(self) -> int: ...

  def getValue(self, x: int, y: int, z: int, w: int) -> int: ...

  def getWidth(self) -> int: ...

  def setValue(self, x: int, y: int, z: int, w: int, newValue: int) -> None: ...

  def __init__(self, width: int, height: int, depth: int, quanta: int): ...


class ObjectCube[T]:

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> ObjectCube[T]: ...

  def fill(self, arg0: object) -> None: ...

  def getDepth(self) -> int: ...

  def getHeight(self) -> int: ...

  def getValue(self, x: int, y: int, z: int) -> object: ...

  def getWidth(self) -> int: ...

  def setValue(self, arg0: int, arg1: int, arg2: int, arg3: object) -> None: ...

  def __init__(self, width: int, height: int, depth: int): ...


class ObjectGrid[T]:

  def clear(self) -> None: ...

  @overload
  def clone(self) -> object: ...

  @overload
  def clone(self) -> ObjectGrid[T]: ...

  def fill(self, arg0: object) -> None: ...

  def getHeight(self) -> int: ...

  def getValue(self, x: int, y: int) -> object: ...

  def getWidth(self) -> int: ...

  def setValue(self, arg0: int, arg1: int, arg2: object) -> None: ...

  def __init__(self, width: int, height: int): ...


class OnceEvery:

  def Check(self) -> bool: ...

  @staticmethod
  def getElapsedMillis() -> int: ...

  @staticmethod
  def update() -> None: ...

  @overload
  def __init__(self, seconds: float): ...
  @overload
  def __init__(self, seconds: float, randomStart: bool): ...


class UpdateLimit:

  def BlockCheck(self) -> None: ...

  def Check(self) -> bool: ...

  @overload
  def Reset(self) -> None: ...

  @overload
  def Reset(self, ms: int) -> None: ...

  def getDelay(self) -> int: ...

  def getLast(self) -> int: ...

  def getTimePeriod(self) -> float: ...

  def setSmoothUpdatePeriod(self, ms: int) -> None: ...

  def setUpdatePeriod(self, ms: int) -> None: ...

  def updateTimePeriod(self) -> None: ...

  @overload
  def __init__(self, ms: int): ...
  @overload
  def __init__(self, ms: int, shift: int): ...


class UpdateTimer:

  def check(self) -> bool: ...

  def getTime(self) -> int: ...

  def reset(self, time: int) -> None: ...

  def __init__(self): ...


class WrappedBuffer:

  def capacity(self) -> int: ...

  def dispose(self) -> None: ...

  def getBuffer(self) -> ByteBuffer: ...

  def isDisposed(self) -> bool: ...

  def __init__(self, size: int): ...

