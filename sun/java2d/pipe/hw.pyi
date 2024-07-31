from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import BufferCapabilities, ImageCapabilities
from java.lang import Enum

class ExtendedBufferCapabilities(BufferCapabilities):

  def derive(self, arg0: ExtendedBufferCapabilities.VSyncType) -> ExtendedBufferCapabilities: ...

  def getVSync(self) -> ExtendedBufferCapabilities.VSyncType: ...

  def isPageFlipping(self) -> bool: ...

  @overload
  def __init__(self, arg0: BufferCapabilities): ...
  @overload
  def __init__(self, arg0: BufferCapabilities, arg1: ExtendedBufferCapabilities.VSyncType): ...
  @overload
  def __init__(self, arg0: ImageCapabilities, arg1: ImageCapabilities, arg2: BufferCapabilities.FlipContents): ...
  @overload
  def __init__(self, arg0: ImageCapabilities, arg1: ImageCapabilities, arg2: BufferCapabilities.FlipContents, arg3: ExtendedBufferCapabilities.VSyncType): ...

  class VSyncType(Enum):

    VSYNC_DEFAULT: ExtendedBufferCapabilities.VSyncType

    VSYNC_OFF: ExtendedBufferCapabilities.VSyncType

    VSYNC_ON: ExtendedBufferCapabilities.VSyncType

    def id(self) -> int: ...

    @staticmethod
    def valueOf(arg0: str) -> ExtendedBufferCapabilities.VSyncType: ...

    @staticmethod
    def values() -> list[ExtendedBufferCapabilities.VSyncType]: ...

