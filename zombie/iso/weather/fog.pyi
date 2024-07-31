from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.joml import Vector2i
from zombie.core.textures import Texture
from zombie.iso import IsoGridSquare

class FogShader:

  instance: FogShader

  def StartShader(self) -> bool: ...

  def initShader(self) -> None: ...

  def setCameraInfo(self, x: float, y: float, z: float, w: float) -> None: ...

  def setColorInfo(self, r: float, g: float, b: float, a: float) -> None: ...

  def setParamInfo(self, x: float, y: float, z: float, w: float) -> None: ...

  def setRectangleInfo(self, x: float, y: float, w: float, h: float) -> None: ...

  def setScalingInfo(self, a: float, b: float, c: float, d: float) -> None: ...

  def setScreenInfo(self, width: float, height: float, zoom: float, secondLayerAlpha: float) -> None: ...

  def setTextureInfo(self, u1: float, u2: float, alpha: float, u3: float) -> None: ...

  def setWorldOffset(self, x: float, y: float, z: float, u: float) -> None: ...

  def __init__(self): ...


class ImprovedFog:

  @staticmethod
  def DrawSubTextureRGBA(tex: Texture, subX: float, subY: float, subW: float, subH: float, x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def endRender() -> None: ...

  @staticmethod
  def getAlphaCircleAlpha() -> float: ...

  @staticmethod
  def getAlphaCircleRad() -> float: ...

  @staticmethod
  def getBaseAlpha() -> float: ...

  @staticmethod
  def getBottomAlphaHeight() -> float: ...

  @staticmethod
  def getColorB() -> float: ...

  @staticmethod
  def getColorG() -> float: ...

  @staticmethod
  def getColorR() -> float: ...

  @staticmethod
  def getMaxXOffset() -> int: ...

  @staticmethod
  def getMaxYOffset() -> int: ...

  @staticmethod
  def getMinXOffset() -> int: ...

  @staticmethod
  def getOctaves() -> float: ...

  @staticmethod
  def getRenderEveryXRow() -> int: ...

  @staticmethod
  def getRenderXRowsFromCenter() -> int: ...

  @staticmethod
  def getScalingX() -> float: ...

  @staticmethod
  def getScalingY() -> float: ...

  @staticmethod
  def getSecondLayerAlpha() -> float: ...

  @staticmethod
  def getTopAlphaHeight() -> float: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isDrawDebugColors() -> bool: ...

  @staticmethod
  def isEnableEditing() -> bool: ...

  @staticmethod
  def isHighQuality() -> bool: ...

  @staticmethod
  def isRenderCurrentLayerOnly() -> bool: ...

  @staticmethod
  def isRenderEndOnly() -> bool: ...

  @staticmethod
  def isRenderOnlyOneRow() -> bool: ...

  @staticmethod
  def renderRowsBehind(squareMax: IsoGridSquare) -> None: ...

  @staticmethod
  def setAlphaCircleAlpha(alphaCircleAlpha: float) -> None: ...

  @staticmethod
  def setAlphaCircleRad(alphaCircleRad: float) -> None: ...

  @staticmethod
  def setBaseAlpha(baseAlpha: float) -> None: ...

  @staticmethod
  def setBottomAlphaHeight(bottomAlphaHeight: float) -> None: ...

  @staticmethod
  def setColorB(colorB: float) -> None: ...

  @staticmethod
  def setColorG(colorG: float) -> None: ...

  @staticmethod
  def setColorR(colorR: float) -> None: ...

  @staticmethod
  def setDrawDebugColors(drawDebugColors: bool) -> None: ...

  @staticmethod
  def setEnableEditing(enableEditing: bool) -> None: ...

  @staticmethod
  def setHighQuality(highQuality: bool) -> None: ...

  @staticmethod
  def setMaxXOffset(maxXOffset: int) -> None: ...

  @staticmethod
  def setMaxYOffset(maxYOffset: int) -> None: ...

  @staticmethod
  def setMinXOffset(minXOffset: int) -> None: ...

  @staticmethod
  def setOctaves(octaves: float) -> None: ...

  @staticmethod
  def setRenderCurrentLayerOnly(renderCurrentLayerOnly: bool) -> None: ...

  @staticmethod
  def setRenderEndOnly(renderEndOnly: bool) -> None: ...

  @staticmethod
  def setRenderEveryXRow(renderEveryXRow: int) -> None: ...

  @staticmethod
  def setRenderOnlyOneRow(renderOnlyOneRow: bool) -> None: ...

  @staticmethod
  def setRenderXRowsFromCenter(renderXRowsFromCenter: int) -> None: ...

  @staticmethod
  def setScalingX(scalingX: float) -> None: ...

  @staticmethod
  def setScalingY(scalingY: float) -> None: ...

  @staticmethod
  def setSecondLayerAlpha(secondLayerAlpha: float) -> None: ...

  @staticmethod
  def setTopAlphaHeight(topAlphaHeight: float) -> None: ...

  @staticmethod
  def startRender(nPlayer: int, z: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  @staticmethod
  def updateKeys() -> None: ...

  def __init__(self): ...

  class RectangleIterator:

    def next(self, arg0: Vector2i) -> bool: ...

    def reset(self, arg0: int, arg1: int) -> None: ...

  class FogRectangle: ...
