from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio.file import Path
from zombie.core.textures import Texture

class Bucket:

  @overload
  def AddTexture(self, filename: str, texture: Texture) -> None: ...

  @overload
  def AddTexture(self, filename: Path, texture: Texture) -> None: ...

  def Dispose(self) -> None: ...

  @overload
  def HasTexture(self, filename: str) -> bool: ...

  @overload
  def HasTexture(self, filename: Path) -> bool: ...

  def forgetTexture(self, name: str) -> None: ...

  @overload
  def getTexture(self, filename: str) -> Texture: ...

  @overload
  def getTexture(self, filename: Path) -> Texture: ...

  def __init__(self): ...


class BucketManager:

  @staticmethod
  def Active() -> Bucket: ...

  @staticmethod
  def Shared() -> Bucket: ...

  def __init__(self): ...

