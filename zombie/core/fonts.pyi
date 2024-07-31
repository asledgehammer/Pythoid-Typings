from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.asset import Asset
from zombie.core import Color
from zombie.core.textures import Texture, TextureID

class AngelCodeFont:

  curA: float

  curB: float

  curCol: Color

  curG: float

  curR: float

  xoff: int

  yoff: int

  def destroy(self) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color, startIndex: int, endIndex: int) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color, startIndex: int, endIndex: int) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def drawString(self, x: float, y: float, scale: float, text: str, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, r: float, g: float, b: float, a: float, startIndex: int, endIndex: int) -> None: ...

  @overload
  def drawString(self, x: float, y: float, scale: float, text: str, r: float, g: float, b: float, a: float, startIndex: int, endIndex: int) -> None: ...

  @overload
  def getHeight(self, text: str) -> int: ...

  @overload
  def getHeight(self, text: str) -> int: ...

  @overload
  def getLineHeight(self) -> int: ...

  @overload
  def getLineHeight(self) -> int: ...

  @overload
  def getWidth(self, text: str) -> int: ...

  @overload
  def getWidth(self, text: str) -> int: ...

  @overload
  def getWidth(self, text: str, xAdvance: bool) -> int: ...

  @overload
  def getWidth(self, text: str, xAdvance: bool) -> int: ...

  @overload
  def getWidth(self, text: str, start: int, __end__: int) -> int: ...

  @overload
  def getWidth(self, text: str, start: int, __end__: int) -> int: ...

  @overload
  def getWidth(self, text: str, start: int, __end__: int, xadvance: bool) -> int: ...

  @overload
  def getWidth(self, text: str, start: int, __end__: int, xadvance: bool) -> int: ...

  def getYOffset(self, text: str) -> int: ...

  def isEmpty(self) -> bool: ...

  @overload
  def onStateChanged(self, oldState: Asset.State, newState: Asset.State, asset: Asset) -> None: ...

  @overload
  def onStateChanged(self, oldState: Asset.State, newState: Asset.State, asset: Asset) -> None: ...

  @overload
  def __init__(self, fntFile: str, imgFile: str):
    self.chars: list[AngelCodeFont.CharDef]

  @overload
  def __init__(self, fntFile: str, image: Texture): ...

  class DisplayList: ...

  class CharDef:

    def destroy(self) -> None: ...

    def draw(self, arg0: float, arg1: float) -> None: ...

    def getKerning(self, arg0: int) -> int: ...

    def init(self) -> None: ...

    def toString(self) -> str: ...

    def __init__(self, arg0: AngelCodeFont):
      self.dlindex: int
      self.height: int
      self.id: int
      self.image: Texture
      self.kerningamount: list[int]
      self.kerningsecond: list[int]
      self.page: int
      self.width: int
      self.x: int
      self.xadvance: int
      self.xoffset: int
      self.y: int
      self.yoffset: int

  class CharDefTexture(Texture):

    def releaseCharDef(self) -> None: ...

    def __init__(self, data: TextureID, name: str): ...


class Font:

  @overload
  def drawString(self, x: float, y: float, text: str) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color) -> None: ...

  @overload
  def drawString(self, x: float, y: float, text: str, col: Color, startIndex: int, endIndex: int) -> None: ...

  def getHeight(self, str: str) -> int: ...

  def getLineHeight(self) -> int: ...

  @overload
  def getWidth(self, str: str) -> int: ...

  @overload
  def getWidth(self, str: str, xAdvance: bool) -> int: ...

  @overload
  def getWidth(self, str: str, startIndex: int, endIndex: int) -> int: ...

  @overload
  def getWidth(self, str: str, startIndex: int, endIndex: int, xAdvance: bool) -> int: ...

