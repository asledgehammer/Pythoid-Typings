from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util.function import Consumer
from zombie.core.textures import TextureDraw

ZoomBasedSetting = TypeVar('ZoomBasedSetting', default=Any)

class DiamondShaper:

  instance: DiamondShaper

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

  def __init__(self): ...


class FloorShaper:

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

  def setAlpha4(self, alpha: float) -> None: ...

  def setShore(self, isShore: bool) -> None: ...

  def setTintColor(self, tintABGR: int) -> None: ...

  def setVertColors(self, col0: int, col1: int, col2: int, col3: int) -> None: ...

  def setWaterDepth(self, val0: float, val1: float, val2: float, val3: float) -> None: ...

  def __init__(self): ...


class FloorShaperAttachedSprites(FloorShaper):

  instance: FloorShaperAttachedSprites

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def __init__(self): ...

  class Settings(SpritePaddingSettings.GenericZoomBasedSettingGroup):

    @overload
    def getCurrentZoomSetting(self) -> FloorShaperAttachedSprites.Settings.ASBorderSetting: ...

    @overload
    def getCurrentZoomSetting(self) -> object: ...

    def __init__(self):
      self.notzoomed: FloorShaperAttachedSprites.Settings.ASBorderSetting
      self.zoomedin: FloorShaperAttachedSprites.Settings.ASBorderSetting
      self.zoomedout: FloorShaperAttachedSprites.Settings.ASBorderSetting

    class ASBorderSetting:

      @overload
      def __init__(self):
        self.borderthicknessdown: float

        self.borderthicknesslr: float

        self.borderthicknessup: float

        self.uvfraction: float

      @overload
      def __init__(self, borderThicknessUp: float, borderThicknessDown: float, borderThicknessLR: float, uvFraction: float): ...


class FloorShaperDeDiamond(FloorShaper):

  instance: FloorShaperDeDiamond

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def __init__(self): ...

  class Settings(SpritePaddingSettings.GenericZoomBasedSettingGroup):

    @overload
    def getCurrentZoomSetting(self) -> FloorShaperDeDiamond.Settings.BorderSetting: ...

    @overload
    def getCurrentZoomSetting(self) -> object: ...

    def __init__(self):
      self.notzoomed: FloorShaperDeDiamond.Settings.BorderSetting
      self.zoomedin: FloorShaperDeDiamond.Settings.BorderSetting
      self.zoomedout: FloorShaperDeDiamond.Settings.BorderSetting

    class BorderSetting:

      @overload
      def __init__(self):
        self.borderthicknessdown: float

        self.borderthicknesslr: float

        self.borderthicknessup: float

        self.uvfraction: float

      @overload
      def __init__(self, borderThicknessUp: float, borderThicknessDown: float, borderThicknessLR: float, uvFraction: float): ...


class FloorShaperDiamond(FloorShaper):

  instance: FloorShaperDiamond

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def __init__(self): ...


class SpritePadding:

  @staticmethod
  def applyIsoPadding(ddraw: TextureDraw, settings: SpritePadding.IsoPaddingSettings) -> None: ...

  @staticmethod
  def applyPadding(ddraw: TextureDraw, xPadLeft: float, yPadUp: float, xPadRight: float, yPadDown: float, uPadLeft: float, vPadUp: float, uPadRight: float, vPadDown: float) -> None: ...

  @staticmethod
  def applyPaddingBorder(ddraw: TextureDraw, borderThickness: float, uvFraction: float) -> None: ...

  def __init__(self): ...

  class IsoPaddingSettings(SpritePaddingSettings.GenericZoomBasedSettingGroup):

    @overload
    def getCurrentZoomSetting(self) -> SpritePadding.IsoPaddingSettings.IsoBorderSetting: ...

    @overload
    def getCurrentZoomSetting(self) -> object: ...

    def __init__(self):
      self.notzoomed: SpritePadding.IsoPaddingSettings.IsoBorderSetting
      self.zoomedin: SpritePadding.IsoPaddingSettings.IsoBorderSetting
      self.zoomedout: SpritePadding.IsoPaddingSettings.IsoBorderSetting

    class IsoBorderSetting:

      @overload
      def __init__(self):
        self.borderthickness: float

        self.uvfraction: float

      @overload
      def __init__(self, borderThickness: float, uvFraction: float): ...


class SpritePaddingSettings:

  @staticmethod
  def getSettings() -> SpritePaddingSettings.Settings: ...

  @staticmethod
  def settingsFileChanged(settings: SpritePaddingSettings.Settings) -> None: ...

  def __init__(self): ...

  class Settings:

    def __init__(self):
      self.attachedsprites: FloorShaperAttachedSprites.Settings
      self.floordediamond: FloorShaperDeDiamond.Settings
      self.isopadding: SpritePadding.IsoPaddingSettings

  class GenericZoomBasedSettingGroup:

    def getCurrentZoomSetting(self) -> object: ...

    def __init__(self): ...


class WallPaddingShaper:

  instance: WallPaddingShaper

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, ddraw: TextureDraw) -> None: ...

  def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

  def __init__(self): ...


class WallShaper:

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, texd: TextureDraw) -> None: ...

  def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

  def setTintColor(self, tintABGR: int) -> None: ...

  def __init__(self):
    self.col: list[int]


class WallShaperN(WallShaper):

  instance: WallShaperN

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, texd: TextureDraw) -> None: ...

  def __init__(self): ...


class WallShaperW(WallShaper):

  instance: WallShaperW

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, texd: TextureDraw) -> None: ...

  def __init__(self): ...


class WallShaperWhole(WallShaper):

  instance: WallShaperWhole

  @overload
  def accept(self, arg0: object) -> None: ...

  @overload
  def accept(self, texd: TextureDraw) -> None: ...

  def __init__(self): ...

