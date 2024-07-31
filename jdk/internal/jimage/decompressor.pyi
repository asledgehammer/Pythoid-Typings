from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import ByteOrder

class Decompressor:

  def decompressResource(self, arg0: ByteOrder, arg1: ResourceDecompressor.StringsProvider, arg2: list[int]) -> list[int]: ...

  def __init__(self): ...


class ResourceDecompressor:

  def decompress(self, arg0: ResourceDecompressor.StringsProvider, arg1: list[int], arg2: int, arg3: int) -> list[int]: ...

  def getName(self) -> str: ...

  class StringsProvider:

    def getString(self, arg0: int) -> str: ...

