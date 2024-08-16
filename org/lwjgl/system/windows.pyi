from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteBuffer
from org.lwjgl.system import Struct, MemoryStack, StructBuffer

class RECT(Struct):

  ALIGNOF: int

  @overload
  def bottom(self) -> int: ...

  @overload
  def bottom(self, arg0: int) -> RECT: ...

  def close(self) -> None: ...

  def free(self) -> None: ...

  @overload
  def left(self) -> int: ...

  @overload
  def left(self, arg0: int) -> RECT: ...

  @overload
  def right(self) -> int: ...

  @overload
  def right(self, arg0: int) -> RECT: ...

  @overload
  def set(self, arg0: RECT) -> RECT: ...

  @overload
  def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> RECT: ...

  def sizeof(self) -> int: ...

  @overload
  def top(self) -> int: ...

  @overload
  def top(self, arg0: int) -> RECT: ...

  @staticmethod
  @overload
  def calloc() -> RECT: ...

  @staticmethod
  @overload
  def calloc(arg0: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def callocStack() -> RECT: ...

  @staticmethod
  @overload
  def callocStack(arg0: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def callocStack(arg0: MemoryStack) -> RECT: ...

  @staticmethod
  @overload
  def callocStack(arg0: int, arg1: MemoryStack) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def create() -> RECT: ...

  @staticmethod
  @overload
  def create(arg0: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def create(arg0: int) -> RECT: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def createSafe(arg0: int) -> RECT: ...

  @staticmethod
  @overload
  def createSafe(arg0: int, arg1: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def malloc() -> RECT: ...

  @staticmethod
  @overload
  def malloc(arg0: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def mallocStack() -> RECT: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def mallocStack(arg0: MemoryStack) -> RECT: ...

  @staticmethod
  @overload
  def mallocStack(arg0: int, arg1: MemoryStack) -> RECT.Buffer: ...

  @staticmethod
  @overload
  def nbottom(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nbottom(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nleft(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nleft(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def nright(arg0: int) -> int: ...

  @staticmethod
  @overload
  def nright(arg0: int, arg1: int) -> None: ...

  @staticmethod
  @overload
  def ntop(arg0: int) -> int: ...

  @staticmethod
  @overload
  def ntop(arg0: int, arg1: int) -> None: ...

  def __init__(self, arg0: ByteBuffer): ...

  class Buffer(StructBuffer):

    @overload
    def bottom(self) -> int: ...

    @overload
    def bottom(self, arg0: int) -> RECT.Buffer: ...

    def close(self) -> None: ...

    def free(self) -> None: ...

    @overload
    def left(self) -> int: ...

    @overload
    def left(self, arg0: int) -> RECT.Buffer: ...

    @overload
    def right(self) -> int: ...

    @overload
    def right(self, arg0: int) -> RECT.Buffer: ...

    @overload
    def top(self) -> int: ...

    @overload
    def top(self, arg0: int) -> RECT.Buffer: ...

    @overload
    def __init__(self, arg0: ByteBuffer): ...
    @overload
    def __init__(self, arg0: int, arg1: int): ...

