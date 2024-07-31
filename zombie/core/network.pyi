from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer

class ByteBufferReader:

  def getBoolean(self) -> bool: ...

  def getByte(self) -> int: ...

  def getChar(self) -> str: ...

  def getDouble(self) -> float: ...

  def getFloat(self) -> float: ...

  def getInt(self) -> int: ...

  def getLong(self) -> int: ...

  def getShort(self) -> int: ...

  def getUTF(self) -> str: ...

  def __init__(self, bb: ByteBuffer):
    self.bb: ByteBuffer


class ByteBufferWriter:

  def putBoolean(self, v: bool) -> None: ...

  def putByte(self, v: int) -> None: ...

  def putChar(self, v: str) -> None: ...

  def putDouble(self, v: float) -> None: ...

  def putFloat(self, v: float) -> None: ...

  def putInt(self, v: int) -> None: ...

  def putLong(self, v: int) -> None: ...

  def putShort(self, v: int) -> None: ...

  def putUTF(self, string: str) -> None: ...

  def __init__(self, bb: ByteBuffer):
    self.bb: ByteBuffer

