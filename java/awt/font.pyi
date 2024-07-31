from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Font, Shape, Rectangle, Graphics2D
from java.awt.geom import AffineTransform, Rectangle2D, Point2D
from java.lang import Enum, Float, Integer, Boolean
from java.text import AttributedCharacterIterator
from java.util import Set

class FontRenderContext:

  @overload
  def equals(self, arg0: FontRenderContext) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  def getAntiAliasingHint(self) -> object: ...

  def getFractionalMetricsHint(self) -> object: ...

  def getTransform(self) -> AffineTransform: ...

  def getTransformType(self) -> int: ...

  def hashCode(self) -> int: ...

  def isAntiAliased(self) -> bool: ...

  def isTransformed(self) -> bool: ...

  def usesFractionalMetrics(self) -> bool: ...

  @overload
  def __init__(self, arg0: AffineTransform, arg1: bool, arg2: bool): ...
  @overload
  def __init__(self, arg0: AffineTransform, arg1: object, arg2: object): ...


class GlyphJustificationInfo:

  PRIORITY_INTERCHAR: int

  PRIORITY_KASHIDA: int

  PRIORITY_NONE: int

  PRIORITY_WHITESPACE: int

  def __init__(self, arg0: float, arg1: bool, arg2: int, arg3: float, arg4: float, arg5: bool, arg6: int, arg7: float, arg8: float):
    self.growabsorb: bool
    self.growleftlimit: float
    self.growpriority: int
    self.growrightlimit: float
    self.shrinkabsorb: bool
    self.shrinkleftlimit: float
    self.shrinkpriority: int
    self.shrinkrightlimit: float
    self.weight: float


class GlyphMetrics:

  COMBINING: int

  COMPONENT: int

  LIGATURE: int

  STANDARD: int

  WHITESPACE: int

  def getAdvance(self) -> float: ...

  def getAdvanceX(self) -> float: ...

  def getAdvanceY(self) -> float: ...

  def getBounds2D(self) -> Rectangle2D: ...

  def getLSB(self) -> float: ...

  def getRSB(self) -> float: ...

  def getType(self) -> int: ...

  def isCombining(self) -> bool: ...

  def isComponent(self) -> bool: ...

  def isLigature(self) -> bool: ...

  def isStandard(self) -> bool: ...

  def isWhitespace(self) -> bool: ...

  @overload
  def __init__(self, arg0: float, arg1: Rectangle2D, arg2: int): ...
  @overload
  def __init__(self, arg0: bool, arg1: float, arg2: float, arg3: Rectangle2D, arg4: int): ...


class GlyphVector:

  FLAG_COMPLEX_GLYPHS: int

  FLAG_HAS_POSITION_ADJUSTMENTS: int

  FLAG_HAS_TRANSFORMS: int

  FLAG_MASK: int

  FLAG_RUN_RTL: int

  def equals(self, arg0: GlyphVector) -> bool: ...

  def getFont(self) -> Font: ...

  def getFontRenderContext(self) -> FontRenderContext: ...

  def getGlyphCharIndex(self, arg0: int) -> int: ...

  def getGlyphCharIndices(self, arg0: int, arg1: int, arg2: list[int]) -> list[int]: ...

  def getGlyphCode(self, arg0: int) -> int: ...

  def getGlyphCodes(self, arg0: int, arg1: int, arg2: list[int]) -> list[int]: ...

  def getGlyphJustificationInfo(self, arg0: int) -> GlyphJustificationInfo: ...

  def getGlyphLogicalBounds(self, arg0: int) -> Shape: ...

  def getGlyphMetrics(self, arg0: int) -> GlyphMetrics: ...

  @overload
  def getGlyphOutline(self, arg0: int) -> Shape: ...

  @overload
  def getGlyphOutline(self, arg0: int, arg1: float, arg2: float) -> Shape: ...

  def getGlyphPixelBounds(self, arg0: int, arg1: FontRenderContext, arg2: float, arg3: float) -> Rectangle: ...

  def getGlyphPosition(self, arg0: int) -> Point2D: ...

  def getGlyphPositions(self, arg0: int, arg1: int, arg2: list[float]) -> list[float]: ...

  def getGlyphTransform(self, arg0: int) -> AffineTransform: ...

  def getGlyphVisualBounds(self, arg0: int) -> Shape: ...

  def getLayoutFlags(self) -> int: ...

  def getLogicalBounds(self) -> Rectangle2D: ...

  def getNumGlyphs(self) -> int: ...

  @overload
  def getOutline(self) -> Shape: ...

  @overload
  def getOutline(self, arg0: float, arg1: float) -> Shape: ...

  def getPixelBounds(self, arg0: FontRenderContext, arg1: float, arg2: float) -> Rectangle: ...

  def getVisualBounds(self) -> Rectangle2D: ...

  def performDefaultLayout(self) -> None: ...

  def setGlyphPosition(self, arg0: int, arg1: Point2D) -> None: ...

  def setGlyphTransform(self, arg0: int, arg1: AffineTransform) -> None: ...


class GraphicAttribute:

  BOTTOM_ALIGNMENT: int

  CENTER_BASELINE: int

  HANGING_BASELINE: int

  ROMAN_BASELINE: int

  TOP_ALIGNMENT: int

  def draw(self, arg0: Graphics2D, arg1: float, arg2: float) -> None: ...

  def getAdvance(self) -> float: ...

  def getAlignment(self) -> int: ...

  def getAscent(self) -> float: ...

  def getBounds(self) -> Rectangle2D: ...

  def getDescent(self) -> float: ...

  def getJustificationInfo(self) -> GlyphJustificationInfo: ...

  def getOutline(self, arg0: AffineTransform) -> Shape: ...


class LineMetrics:

  def getAscent(self) -> float: ...

  def getBaselineIndex(self) -> int: ...

  def getBaselineOffsets(self) -> list[float]: ...

  def getDescent(self) -> float: ...

  def getHeight(self) -> float: ...

  def getLeading(self) -> float: ...

  def getNumChars(self) -> int: ...

  def getStrikethroughOffset(self) -> float: ...

  def getStrikethroughThickness(self) -> float: ...

  def getUnderlineOffset(self) -> float: ...

  def getUnderlineThickness(self) -> float: ...


class NumericShaper:

  ALL_RANGES: int

  ARABIC: int

  BENGALI: int

  DEVANAGARI: int

  EASTERN_ARABIC: int

  ETHIOPIC: int

  EUROPEAN: int

  GUJARATI: int

  GURMUKHI: int

  KANNADA: int

  KHMER: int

  LAO: int

  MALAYALAM: int

  MONGOLIAN: int

  MYANMAR: int

  ORIYA: int

  TAMIL: int

  TELUGU: int

  THAI: int

  TIBETAN: int

  def equals(self, arg0: object) -> bool: ...

  def getRangeSet(self) -> Set[NumericShaper.Range]: ...

  def getRanges(self) -> int: ...

  def hashCode(self) -> int: ...

  def isContextual(self) -> bool: ...

  @overload
  def shape(self, arg0: list[str], arg1: int, arg2: int) -> None: ...

  @overload
  def shape(self, arg0: list[str], arg1: int, arg2: int, arg3: int) -> None: ...

  @overload
  def shape(self, arg0: list[str], arg1: int, arg2: int, arg3: NumericShaper.Range) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def getContextualShaper(arg0: int) -> NumericShaper: ...

  @staticmethod
  @overload
  def getContextualShaper(arg0: Set[NumericShaper.Range]) -> NumericShaper: ...

  @staticmethod
  @overload
  def getContextualShaper(arg0: int, arg1: int) -> NumericShaper: ...

  @staticmethod
  @overload
  def getContextualShaper(arg0: Set[NumericShaper.Range], arg1: NumericShaper.Range) -> NumericShaper: ...

  @staticmethod
  @overload
  def getShaper(arg0: int) -> NumericShaper: ...

  @staticmethod
  @overload
  def getShaper(arg0: NumericShaper.Range) -> NumericShaper: ...

  class Range(Enum):

    ARABIC: NumericShaper.Range

    BALINESE: NumericShaper.Range

    BENGALI: NumericShaper.Range

    CHAM: NumericShaper.Range

    DEVANAGARI: NumericShaper.Range

    EASTERN_ARABIC: NumericShaper.Range

    ETHIOPIC: NumericShaper.Range

    EUROPEAN: NumericShaper.Range

    GUJARATI: NumericShaper.Range

    GURMUKHI: NumericShaper.Range

    JAVANESE: NumericShaper.Range

    KANNADA: NumericShaper.Range

    KAYAH_LI: NumericShaper.Range

    KHMER: NumericShaper.Range

    LAO: NumericShaper.Range

    LEPCHA: NumericShaper.Range

    LIMBU: NumericShaper.Range

    MALAYALAM: NumericShaper.Range

    MEETEI_MAYEK: NumericShaper.Range

    MONGOLIAN: NumericShaper.Range

    MYANMAR: NumericShaper.Range

    MYANMAR_SHAN: NumericShaper.Range

    MYANMAR_TAI_LAING: NumericShaper.Range

    NEW_TAI_LUE: NumericShaper.Range

    NKO: NumericShaper.Range

    OL_CHIKI: NumericShaper.Range

    ORIYA: NumericShaper.Range

    SAURASHTRA: NumericShaper.Range

    SINHALA: NumericShaper.Range

    SUNDANESE: NumericShaper.Range

    TAI_THAM_HORA: NumericShaper.Range

    TAI_THAM_THAM: NumericShaper.Range

    TAMIL: NumericShaper.Range

    TELUGU: NumericShaper.Range

    THAI: NumericShaper.Range

    TIBETAN: NumericShaper.Range

    VAI: NumericShaper.Range

    @staticmethod
    def valueOf(arg0: str) -> NumericShaper.Range: ...

    @staticmethod
    def values() -> list[NumericShaper.Range]: ...


class TextAttribute(AttributedCharacterIterator.Attribute):

  BACKGROUND: TextAttribute

  BIDI_EMBEDDING: TextAttribute

  CHAR_REPLACEMENT: TextAttribute

  FAMILY: TextAttribute

  FONT: TextAttribute

  FOREGROUND: TextAttribute

  INPUT_METHOD_HIGHLIGHT: TextAttribute

  INPUT_METHOD_UNDERLINE: TextAttribute

  JUSTIFICATION: TextAttribute

  JUSTIFICATION_FULL: Float

  JUSTIFICATION_NONE: Float

  KERNING: TextAttribute

  KERNING_ON: Integer

  LIGATURES: TextAttribute

  LIGATURES_ON: Integer

  NUMERIC_SHAPING: TextAttribute

  POSTURE: TextAttribute

  POSTURE_OBLIQUE: Float

  POSTURE_REGULAR: Float

  RUN_DIRECTION: TextAttribute

  RUN_DIRECTION_LTR: Boolean

  RUN_DIRECTION_RTL: Boolean

  SIZE: TextAttribute

  STRIKETHROUGH: TextAttribute

  STRIKETHROUGH_ON: Boolean

  SUPERSCRIPT: TextAttribute

  SUPERSCRIPT_SUB: Integer

  SUPERSCRIPT_SUPER: Integer

  SWAP_COLORS: TextAttribute

  SWAP_COLORS_ON: Boolean

  TRACKING: TextAttribute

  TRACKING_LOOSE: Float

  TRACKING_TIGHT: Float

  TRANSFORM: TextAttribute

  UNDERLINE: TextAttribute

  UNDERLINE_LOW_DASHED: Integer

  UNDERLINE_LOW_DOTTED: Integer

  UNDERLINE_LOW_GRAY: Integer

  UNDERLINE_LOW_ONE_PIXEL: Integer

  UNDERLINE_LOW_TWO_PIXEL: Integer

  UNDERLINE_ON: Integer

  WEIGHT: TextAttribute

  WEIGHT_BOLD: Float

  WEIGHT_DEMIBOLD: Float

  WEIGHT_DEMILIGHT: Float

  WEIGHT_EXTRA_LIGHT: Float

  WEIGHT_EXTRABOLD: Float

  WEIGHT_HEAVY: Float

  WEIGHT_LIGHT: Float

  WEIGHT_MEDIUM: Float

  WEIGHT_REGULAR: Float

  WEIGHT_SEMIBOLD: Float

  WEIGHT_ULTRABOLD: Float

  WIDTH: TextAttribute

  WIDTH_CONDENSED: Float

  WIDTH_EXTENDED: Float

  WIDTH_REGULAR: Float

  WIDTH_SEMI_CONDENSED: Float

  WIDTH_SEMI_EXTENDED: Float


class TextHitInfo:

  @overload
  def equals(self, arg0: TextHitInfo) -> bool: ...

  @overload
  def equals(self, arg0: object) -> bool: ...

  def getCharIndex(self) -> int: ...

  def getInsertionIndex(self) -> int: ...

  def getOffsetHit(self, arg0: int) -> TextHitInfo: ...

  def getOtherHit(self) -> TextHitInfo: ...

  def hashCode(self) -> int: ...

  def isLeadingEdge(self) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  def afterOffset(arg0: int) -> TextHitInfo: ...

  @staticmethod
  def beforeOffset(arg0: int) -> TextHitInfo: ...

  @staticmethod
  def leading(arg0: int) -> TextHitInfo: ...

  @staticmethod
  def trailing(arg0: int) -> TextHitInfo: ...


class TransformAttribute:

  IDENTITY: TransformAttribute

  def equals(self, arg0: object) -> bool: ...

  def getTransform(self) -> AffineTransform: ...

  def hashCode(self) -> int: ...

  def isIdentity(self) -> bool: ...

  def __init__(self, arg0: AffineTransform): ...

