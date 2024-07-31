from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Exception, Throwable, Integer
from java.nio import ByteBuffer, CharBuffer, DoubleBuffer, FloatBuffer, IntBuffer, LongBuffer, ShortBuffer, Buffer

class BufferUtils:

  @staticmethod
  def createByteBuffer(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def createCharBuffer(arg0: int) -> CharBuffer: ...

  @staticmethod
  def createDoubleBuffer(arg0: int) -> DoubleBuffer: ...

  @staticmethod
  def createFloatBuffer(arg0: int) -> FloatBuffer: ...

  @staticmethod
  def createIntBuffer(arg0: int) -> IntBuffer: ...

  @staticmethod
  def createLongBuffer(arg0: int) -> LongBuffer: ...

  @staticmethod
  def createShortBuffer(arg0: int) -> ShortBuffer: ...

  @staticmethod
  def getElementSizeExponent(arg0: Buffer) -> int: ...

  @staticmethod
  def getOffset(arg0: Buffer) -> int: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: ByteBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: CharBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: DoubleBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: FloatBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: IntBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: LongBuffer) -> None: ...

  @staticmethod
  @overload
  def zeroBuffer(arg0: ShortBuffer) -> None: ...

  def __init__(self): ...


class LWJGLException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: Throwable): ...
  @overload
  def __init__(self, arg0: str, arg1: Throwable): ...


class LWJGLUtil:

  CHECKS: bool

  DEBUG: bool

  PLATFORM_LINUX: int

  PLATFORM_LINUX_NAME: str

  PLATFORM_MACOSX: int

  PLATFORM_MACOSX_NAME: str

  PLATFORM_WINDOWS: int

  PLATFORM_WINDOWS_NAME: str

  @staticmethod
  def getPlatform() -> int: ...

  @staticmethod
  def getPlatformName() -> str: ...

  @staticmethod
  def getPrivilegedBoolean(arg0: str) -> bool: ...

  @staticmethod
  @overload
  def getPrivilegedInteger(arg0: str) -> Integer: ...

  @staticmethod
  @overload
  def getPrivilegedInteger(arg0: str, arg1: int) -> Integer: ...

  def __init__(self): ...


class Sys:

  @staticmethod
  def getNanoTime() -> int: ...

  @staticmethod
  def getTime() -> int: ...

  @staticmethod
  def getTimerResolution() -> int: ...

  def __init__(self): ...

