from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import HashMap
from zombie.core.textures import Texture

class Texture2D:

  def Apply(self) -> None: ...

  def getHeight(self) -> int: ...

  def getTexture(self) -> int: ...

  def getWidth(self) -> int: ...

  def __init__(self, tex: Texture): ...


class TextureManager:

  Instance: TextureManager

  @overload
  def AddTexture(self, name: str) -> bool: ...

  @overload
  def AddTexture(self, name: str, texture: Texture) -> None: ...

  def __init__(self):
    self.textures: HashMap[str, Texture2D]

