from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt.image import BufferedImage, Raster, WritableRaster

class ColorTransform:

  Any: int

  Gamut: int

  Out: int

  Simulation: int

  @overload
  def colorConvert(self, arg0: list[int], arg1: list[int]) -> list[int]: ...

  @overload
  def colorConvert(self, arg0: list[int], arg1: list[int]) -> list[int]: ...

  @overload
  def colorConvert(self, arg0: BufferedImage, arg1: BufferedImage) -> None: ...

  @overload
  def colorConvert(self, arg0: Raster, arg1: WritableRaster) -> None: ...

  @overload
  def colorConvert(self, arg0: Raster, arg1: WritableRaster, arg2: list[float], arg3: list[float], arg4: list[float], arg5: list[float]) -> None: ...

  def getNumInComponents(self) -> int: ...

  def getNumOutComponents(self) -> int: ...


class Profile: ...


class ProfileDeferralInfo:

  def __init__(self, arg0: str, arg1: int, arg2: int, arg3: int):
    self.colorspacetype: int
    self.filename: str
    self.numcomponents: int
    self.profileclass: int

