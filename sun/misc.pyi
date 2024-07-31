from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Class, Throwable
from java.lang.reflect import Field
from java.nio import ByteBuffer

class Unsafe:

  ADDRESS_SIZE: int

  ARRAY_BOOLEAN_BASE_OFFSET: int

  ARRAY_BOOLEAN_INDEX_SCALE: int

  ARRAY_BYTE_BASE_OFFSET: int

  ARRAY_BYTE_INDEX_SCALE: int

  ARRAY_CHAR_BASE_OFFSET: int

  ARRAY_CHAR_INDEX_SCALE: int

  ARRAY_DOUBLE_BASE_OFFSET: int

  ARRAY_DOUBLE_INDEX_SCALE: int

  ARRAY_FLOAT_BASE_OFFSET: int

  ARRAY_FLOAT_INDEX_SCALE: int

  ARRAY_INT_BASE_OFFSET: int

  ARRAY_INT_INDEX_SCALE: int

  ARRAY_LONG_BASE_OFFSET: int

  ARRAY_LONG_INDEX_SCALE: int

  ARRAY_OBJECT_BASE_OFFSET: int

  ARRAY_OBJECT_INDEX_SCALE: int

  ARRAY_SHORT_BASE_OFFSET: int

  ARRAY_SHORT_INDEX_SCALE: int

  INVALID_FIELD_OFFSET: int

  def addressSize(self) -> int: ...

  def allocateInstance(self, arg0: Class[Any]) -> object: ...

  def allocateMemory(self, arg0: int) -> int: ...

  def arrayBaseOffset(self, arg0: Class[Any]) -> int: ...

  def arrayIndexScale(self, arg0: Class[Any]) -> int: ...

  def compareAndSwapInt(self, arg0: object, arg1: int, arg2: int, arg3: int) -> bool: ...

  def compareAndSwapLong(self, arg0: object, arg1: int, arg2: int, arg3: int) -> bool: ...

  def compareAndSwapObject(self, arg0: object, arg1: int, arg2: object, arg3: object) -> bool: ...

  @overload
  def copyMemory(self, arg0: int, arg1: int, arg2: int) -> None: ...

  @overload
  def copyMemory(self, arg0: object, arg1: int, arg2: object, arg3: int, arg4: int) -> None: ...

  def ensureClassInitialized(self, arg0: Class[Any]) -> None: ...

  def freeMemory(self, arg0: int) -> None: ...

  def fullFence(self) -> None: ...

  def getAddress(self, arg0: int) -> int: ...

  def getAndAddInt(self, arg0: object, arg1: int, arg2: int) -> int: ...

  def getAndAddLong(self, arg0: object, arg1: int, arg2: int) -> int: ...

  def getAndSetInt(self, arg0: object, arg1: int, arg2: int) -> int: ...

  def getAndSetLong(self, arg0: object, arg1: int, arg2: int) -> int: ...

  def getAndSetObject(self, arg0: object, arg1: int, arg2: object) -> object: ...

  def getBoolean(self, arg0: object, arg1: int) -> bool: ...

  def getBooleanVolatile(self, arg0: object, arg1: int) -> bool: ...

  @overload
  def getByte(self, arg0: int) -> int: ...

  @overload
  def getByte(self, arg0: object, arg1: int) -> int: ...

  def getByteVolatile(self, arg0: object, arg1: int) -> int: ...

  @overload
  def getChar(self, arg0: int) -> str: ...

  @overload
  def getChar(self, arg0: object, arg1: int) -> str: ...

  def getCharVolatile(self, arg0: object, arg1: int) -> str: ...

  @overload
  def getDouble(self, arg0: int) -> float: ...

  @overload
  def getDouble(self, arg0: object, arg1: int) -> float: ...

  def getDoubleVolatile(self, arg0: object, arg1: int) -> float: ...

  @overload
  def getFloat(self, arg0: int) -> float: ...

  @overload
  def getFloat(self, arg0: object, arg1: int) -> float: ...

  def getFloatVolatile(self, arg0: object, arg1: int) -> float: ...

  @overload
  def getInt(self, arg0: int) -> int: ...

  @overload
  def getInt(self, arg0: object, arg1: int) -> int: ...

  def getIntVolatile(self, arg0: object, arg1: int) -> int: ...

  def getLoadAverage(self, arg0: list[float], arg1: int) -> int: ...

  @overload
  def getLong(self, arg0: int) -> int: ...

  @overload
  def getLong(self, arg0: object, arg1: int) -> int: ...

  def getLongVolatile(self, arg0: object, arg1: int) -> int: ...

  def getObject(self, arg0: object, arg1: int) -> object: ...

  def getObjectVolatile(self, arg0: object, arg1: int) -> object: ...

  @overload
  def getShort(self, arg0: int) -> int: ...

  @overload
  def getShort(self, arg0: object, arg1: int) -> int: ...

  def getShortVolatile(self, arg0: object, arg1: int) -> int: ...

  def invokeCleaner(self, arg0: ByteBuffer) -> None: ...

  def loadFence(self) -> None: ...

  def objectFieldOffset(self, arg0: Field) -> int: ...

  def pageSize(self) -> int: ...

  def park(self, arg0: bool, arg1: int) -> None: ...

  def putAddress(self, arg0: int, arg1: int) -> None: ...

  def putBoolean(self, arg0: object, arg1: int, arg2: bool) -> None: ...

  def putBooleanVolatile(self, arg0: object, arg1: int, arg2: bool) -> None: ...

  @overload
  def putByte(self, arg0: int, arg1: int) -> None: ...

  @overload
  def putByte(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putByteVolatile(self, arg0: object, arg1: int, arg2: int) -> None: ...

  @overload
  def putChar(self, arg0: int, arg1: str) -> None: ...

  @overload
  def putChar(self, arg0: object, arg1: int, arg2: str) -> None: ...

  def putCharVolatile(self, arg0: object, arg1: int, arg2: str) -> None: ...

  @overload
  def putDouble(self, arg0: int, arg1: float) -> None: ...

  @overload
  def putDouble(self, arg0: object, arg1: int, arg2: float) -> None: ...

  def putDoubleVolatile(self, arg0: object, arg1: int, arg2: float) -> None: ...

  @overload
  def putFloat(self, arg0: int, arg1: float) -> None: ...

  @overload
  def putFloat(self, arg0: object, arg1: int, arg2: float) -> None: ...

  def putFloatVolatile(self, arg0: object, arg1: int, arg2: float) -> None: ...

  @overload
  def putInt(self, arg0: int, arg1: int) -> None: ...

  @overload
  def putInt(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putIntVolatile(self, arg0: object, arg1: int, arg2: int) -> None: ...

  @overload
  def putLong(self, arg0: int, arg1: int) -> None: ...

  @overload
  def putLong(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putLongVolatile(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putObject(self, arg0: object, arg1: int, arg2: object) -> None: ...

  def putObjectVolatile(self, arg0: object, arg1: int, arg2: object) -> None: ...

  def putOrderedInt(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putOrderedLong(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putOrderedObject(self, arg0: object, arg1: int, arg2: object) -> None: ...

  @overload
  def putShort(self, arg0: int, arg1: int) -> None: ...

  @overload
  def putShort(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def putShortVolatile(self, arg0: object, arg1: int, arg2: int) -> None: ...

  def reallocateMemory(self, arg0: int, arg1: int) -> int: ...

  @overload
  def setMemory(self, arg0: int, arg1: int, arg2: int) -> None: ...

  @overload
  def setMemory(self, arg0: object, arg1: int, arg2: int, arg3: int) -> None: ...

  def shouldBeInitialized(self, arg0: Class[Any]) -> bool: ...

  def staticFieldBase(self, arg0: Field) -> object: ...

  def staticFieldOffset(self, arg0: Field) -> int: ...

  def storeFence(self) -> None: ...

  def throwException(self, arg0: Throwable) -> None: ...

  def unpark(self, arg0: object) -> None: ...

  @staticmethod
  def getUnsafe() -> Unsafe: ...

