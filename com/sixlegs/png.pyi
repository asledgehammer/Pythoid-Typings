from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Rectangle, Color
from java.awt.image import BufferedImage
from java.io import IOException, File, InputStream
from java.util import Map

class PngConfig:

  READ_ALL: int

  READ_EXCEPT_DATA: int

  READ_EXCEPT_METADATA: int

  READ_HEADER: int

  READ_UNTIL_DATA: int

  def getConvertIndexed(self) -> bool: ...

  def getDefaultGamma(self) -> float: ...

  def getDisplayExponent(self) -> float: ...

  def getGammaCorrect(self) -> bool: ...

  def getProgressive(self) -> bool: ...

  def getReadLimit(self) -> int: ...

  def getReduce16(self) -> bool: ...

  def getSourceRegion(self) -> Rectangle: ...

  def getSourceXSubsampling(self) -> int: ...

  def getSourceYSubsampling(self) -> int: ...

  def getSubsamplingXOffset(self) -> int: ...

  def getSubsamplingYOffset(self) -> int: ...

  def getWarningsFatal(self) -> bool: ...

  class Builder:

    def build(self) -> PngConfig: ...

    def convertIndexed(self, arg0: bool) -> PngConfig.Builder: ...

    def defaultGamma(self, arg0: float) -> PngConfig.Builder: ...

    def displayExponent(self, arg0: float) -> PngConfig.Builder: ...

    def gammaCorrect(self, arg0: bool) -> PngConfig.Builder: ...

    def progressive(self, arg0: bool) -> PngConfig.Builder: ...

    def readLimit(self, arg0: int) -> PngConfig.Builder: ...

    def reduce16(self, arg0: bool) -> PngConfig.Builder: ...

    def sourceRegion(self, arg0: Rectangle) -> PngConfig.Builder: ...

    def sourceSubsampling(self, arg0: int, arg1: int, arg2: int, arg3: int) -> PngConfig.Builder: ...

    def warningsFatal(self, arg0: bool) -> PngConfig.Builder: ...

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, arg0: PngConfig): ...


class PngConstants:

  BACKGROUND: str

  BIT_DEPTH: str

  bKGD: int

  cHRM: int

  CHROMATICITY: str

  COLOR_TYPE: str

  COLOR_TYPE_GRAY: int

  COLOR_TYPE_GRAY_ALPHA: int

  COLOR_TYPE_PALETTE: int

  COLOR_TYPE_RGB: int

  COLOR_TYPE_RGB_ALPHA: int

  COMPRESSION: str

  COMPRESSION_BASE: int

  FILTER: str

  FILTER_BASE: int

  gAMA: int

  GAMMA: str

  GIF_DELAY_TIME: str

  GIF_DISPOSAL_METHOD: str

  GIF_USER_INPUT_FLAG: str

  gIFg: int

  gIFx: int

  HEIGHT: str

  hIST: int

  HISTOGRAM: str

  ICC_PROFILE: str

  ICC_PROFILE_NAME: str

  iCCP: int

  IDAT: int

  IEND: int

  IHDR: int

  INTERLACE: str

  INTERLACE_ADAM7: int

  INTERLACE_NONE: int

  iTXt: int

  oFFs: int

  PALETTE: str

  PALETTE_ALPHA: str

  pCAL: int

  pHYs: int

  PIXEL_HEIGHT: str

  PIXEL_WIDTH: str

  PIXELS_PER_UNIT_X: str

  PIXELS_PER_UNIT_Y: str

  PLTE: int

  POSITION_UNIT: str

  POSITION_UNIT_MICROMETER: int

  POSITION_UNIT_PIXEL: int

  POSITION_X: str

  POSITION_Y: str

  RENDERING_INTENT: str

  sBIT: int

  sCAL: int

  SCALE_UNIT: str

  SCALE_UNIT_METER: int

  SCALE_UNIT_RADIAN: int

  SIGNATURE: int

  SIGNIFICANT_BITS: str

  sPLT: int

  sRGB: int

  SRGB_ABSOLUTE_COLORIMETRIC: int

  SRGB_PERCEPTUAL: int

  SRGB_RELATIVE_COLORIMETRIC: int

  SRGB_SATURATION_PRESERVING: int

  sTER: int

  STEREO_MODE: str

  STEREO_MODE_CROSS: int

  STEREO_MODE_DIVERGING: int

  SUGGESTED_PALETTES: str

  tEXt: int

  TEXT_CHUNKS: str

  tIME: int

  TRANSPARENCY: str

  tRNS: int

  UNIT: str

  UNIT_METER: int

  UNIT_UNKNOWN: int

  WIDTH: str

  zTXt: int

  @staticmethod
  def getChunkName(arg0: int) -> str: ...

  @staticmethod
  def getChunkType(arg0: str) -> int: ...

  @staticmethod
  def isAncillary(arg0: int) -> bool: ...

  @staticmethod
  def isPrivate(arg0: int) -> bool: ...

  @staticmethod
  def isReserved(arg0: int) -> bool: ...

  @staticmethod
  def isSafeToCopy(arg0: int) -> bool: ...

  def __init__(self): ...


class PngException(IOException):

  def isFatal(self) -> bool: ...


class PngImage:

  BITMASK: int

  OPAQUE: int

  TRANSLUCENT: int

  def getBackground(self) -> Color: ...

  def getBitDepth(self) -> int: ...

  def getColorType(self) -> int: ...

  def getConfig(self) -> PngConfig: ...

  def getGamma(self) -> float: ...

  def getGammaTable(self) -> list[int]: ...

  def getHeight(self) -> int: ...

  def getProperties(self) -> Map: ...

  def getProperty(self, arg0: str) -> object: ...

  def getSamples(self) -> int: ...

  def getTextChunk(self, arg0: str) -> TextChunk: ...

  @overload
  def getTransparency(self) -> int: ...

  @overload
  def getTransparency(self) -> int: ...

  def getWidth(self) -> int: ...

  def isInterlaced(self) -> bool: ...

  @overload
  def read(self, arg0: File) -> BufferedImage: ...

  @overload
  def read(self, arg0: InputStream, arg1: bool) -> BufferedImage: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: PngConfig): ...


class SuggestedPalette:

  def getFrequency(self, arg0: int) -> int: ...

  def getName(self) -> str: ...

  def getSample(self, arg0: int, arg1: list[int]) -> None: ...

  def getSampleCount(self) -> int: ...

  def getSampleDepth(self) -> int: ...


class TextChunk:

  def getKeyword(self) -> str: ...

  def getLanguage(self) -> str: ...

  def getText(self) -> str: ...

  def getTranslatedKeyword(self) -> str: ...

  def getType(self) -> int: ...

