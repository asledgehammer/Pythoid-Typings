from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.nio import ByteBuffer, CharBuffer, DoubleBuffer, FloatBuffer, IntBuffer, LongBuffer, ShortBuffer
from org.lwjgl.system import CustomBuffer, Pointer

T = TypeVar('T', default=Any)

class BufferUtils:

  @staticmethod
  def createByteBuffer(arg0: int) -> ByteBuffer: ...

  @staticmethod
  def createCLongBuffer(arg0: int) -> CLongBuffer: ...

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
  def createPointerBuffer(arg0: int) -> PointerBuffer: ...

  @staticmethod
  def createShortBuffer(arg0: int) -> ShortBuffer: ...

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

  @staticmethod
  @overload
  def zeroBuffer(arg0: T) -> None: ...


class CLongBuffer(CustomBuffer):

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: CLongBuffer) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def get(self) -> int: ...

  @overload
  def get(self, arg0: list[int]) -> CLongBuffer: ...

  @overload
  def get(self, arg0: int) -> int: ...

  @overload
  def get(self, arg0: list[int], arg1: int, arg2: int) -> CLongBuffer: ...

  def hashCode(self) -> int: ...

  @overload
  def put(self, arg0: list[int]) -> CLongBuffer: ...

  @overload
  def put(self, arg0: int) -> CLongBuffer: ...

  @overload
  def put(self, arg0: int, arg1: int) -> CLongBuffer: ...

  @overload
  def put(self, arg0: list[int], arg1: int, arg2: int) -> CLongBuffer: ...

  def sizeof(self) -> int: ...

  @staticmethod
  def allocateDirect(arg0: int) -> CLongBuffer: ...

  @staticmethod
  @overload
  def create(arg0: ByteBuffer) -> CLongBuffer: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> CLongBuffer: ...


class PointerBuffer(CustomBuffer):

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: object) -> int: ...

  @overload
  def compareTo(self, arg0: PointerBuffer) -> int: ...

  def equals(self, arg0: object) -> bool: ...

  @overload
  def get(self) -> int: ...

  @overload
  def get(self, arg0: list[int]) -> PointerBuffer: ...

  @overload
  def get(self, arg0: int) -> int: ...

  @overload
  def get(self, arg0: list[int], arg1: int, arg2: int) -> PointerBuffer: ...

  @overload
  def getByteBuffer(self, arg0: int) -> ByteBuffer: ...

  @overload
  def getByteBuffer(self, arg0: int, arg1: int) -> ByteBuffer: ...

  @overload
  def getDoubleBuffer(self, arg0: int) -> DoubleBuffer: ...

  @overload
  def getDoubleBuffer(self, arg0: int, arg1: int) -> DoubleBuffer: ...

  @overload
  def getFloatBuffer(self, arg0: int) -> FloatBuffer: ...

  @overload
  def getFloatBuffer(self, arg0: int, arg1: int) -> FloatBuffer: ...

  @overload
  def getIntBuffer(self, arg0: int) -> IntBuffer: ...

  @overload
  def getIntBuffer(self, arg0: int, arg1: int) -> IntBuffer: ...

  @overload
  def getLongBuffer(self, arg0: int) -> LongBuffer: ...

  @overload
  def getLongBuffer(self, arg0: int, arg1: int) -> LongBuffer: ...

  @overload
  def getPointerBuffer(self, arg0: int) -> PointerBuffer: ...

  @overload
  def getPointerBuffer(self, arg0: int, arg1: int) -> PointerBuffer: ...

  @overload
  def getShortBuffer(self, arg0: int) -> ShortBuffer: ...

  @overload
  def getShortBuffer(self, arg0: int, arg1: int) -> ShortBuffer: ...

  @overload
  def getStringASCII(self) -> str: ...

  @overload
  def getStringASCII(self, arg0: int) -> str: ...

  @overload
  def getStringUTF16(self) -> str: ...

  @overload
  def getStringUTF16(self, arg0: int) -> str: ...

  @overload
  def getStringUTF8(self) -> str: ...

  @overload
  def getStringUTF8(self, arg0: int) -> str: ...

  def hashCode(self) -> int: ...

  @overload
  def put(self, arg0: list[int]) -> PointerBuffer: ...

  @overload
  def put(self, arg0: ByteBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: DoubleBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: FloatBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: IntBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: LongBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: ShortBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int) -> PointerBuffer: ...

  @overload
  def put(self, arg0: Pointer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: ByteBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: DoubleBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: FloatBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: IntBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: LongBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: ShortBuffer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: int) -> PointerBuffer: ...

  @overload
  def put(self, arg0: int, arg1: Pointer) -> PointerBuffer: ...

  @overload
  def put(self, arg0: list[int], arg1: int, arg2: int) -> PointerBuffer: ...

  @overload
  def putAddressOf(self, arg0: CustomBuffer[Any]) -> PointerBuffer: ...

  @overload
  def putAddressOf(self, arg0: int, arg1: CustomBuffer[Any]) -> PointerBuffer: ...

  def sizeof(self) -> int: ...

  @staticmethod
  def allocateDirect(arg0: int) -> PointerBuffer: ...

  @staticmethod
  @overload
  def create(arg0: ByteBuffer) -> PointerBuffer: ...

  @staticmethod
  @overload
  def create(arg0: int, arg1: int) -> PointerBuffer: ...


class Version:

  BUILD_TYPE: Version.BuildType

  VERSION_MAJOR: int

  VERSION_MINOR: int

  VERSION_REVISION: int

  @staticmethod
  def getVersion() -> str: ...

  @staticmethod
  def main(arg0: list[str]) -> None: ...

  class BuildType(Enum):

    ALPHA: Version.BuildType

    BETA: Version.BuildType

    STABLE: Version.BuildType

    @staticmethod
    def valueOf(arg0: str) -> Version.BuildType: ...

    @staticmethod
    def values() -> list[Version.BuildType]: ...

