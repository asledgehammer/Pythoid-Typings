from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Composite, AlphaComposite, Font
from java.awt.geom import Path2D
from java.awt.image import ColorModel
from java.io import PrintStream
from java.lang.reflect import Field
from sun.awt.image import PixelConverter
from sun.font import GlyphList, Font2D, FontStrike
from sun.java2d import SurfaceData, SunGraphics2D
from sun.java2d.pipe import Region, SpanIterator

class Blit(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def Blit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def getFromCache(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> Blit: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> Blit: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class GeneralXorBlit(Blit):

    def Blit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...

    def getCompositeType(self) -> CompositeType: ...

    def getDestType(self) -> SurfaceType: ...

    def getPrimTypeID(self) -> int: ...

    def getSignature(self) -> str: ...

    def getSourceType(self) -> SurfaceType: ...

    @overload
    def setPrimitives(self, arg0: Blit, arg1: Blit, arg2: GraphicsPrimitive, arg3: Blit) -> None: ...

    @overload
    def setPrimitives(self, arg0: Blit, arg1: Blit, arg2: GraphicsPrimitive, arg3: Blit) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class GeneralMaskBlit(Blit):

    def Blit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class AnyBlit(Blit):

    instance: Blit.AnyBlit

    def Blit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...

    def __init__(self): ...

  class TraceBlit(Blit):

    def Blit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: Blit): ...


class CompositeType:

  AlphaXor: CompositeType

  Any: CompositeType

  AnyAlpha: CompositeType

  Clear: CompositeType

  DESC_ALPHA_XOR: str

  DESC_ANY: str

  DESC_ANY_ALPHA: str

  DESC_CLEAR: str

  DESC_DST: str

  DESC_DST_ATOP: str

  DESC_DST_IN: str

  DESC_DST_OUT: str

  DESC_DST_OVER: str

  DESC_SRC: str

  DESC_SRC_ATOP: str

  DESC_SRC_IN: str

  DESC_SRC_NO_EA: str

  DESC_SRC_OUT: str

  DESC_SRC_OVER: str

  DESC_SRC_OVER_NO_EA: str

  DESC_XOR: str

  Dst: CompositeType

  DstAtop: CompositeType

  DstIn: CompositeType

  DstOut: CompositeType

  DstOver: CompositeType

  General: CompositeType

  OpaqueSrcOverNoEa: CompositeType

  Src: CompositeType

  SrcAtop: CompositeType

  SrcIn: CompositeType

  SrcNoEa: CompositeType

  SrcOut: CompositeType

  SrcOver: CompositeType

  SrcOverNoEa: CompositeType

  Xor: CompositeType

  def deriveSubType(self, arg0: str) -> CompositeType: ...

  def equals(self, arg0: object) -> bool: ...

  def getDescriptor(self) -> str: ...

  def getSuperType(self) -> CompositeType: ...

  def getUniqueID(self) -> int: ...

  def hashCode(self) -> int: ...

  def isDerivedFrom(self, arg0: CompositeType) -> bool: ...

  def toString(self) -> str: ...

  @staticmethod
  def forAlphaComposite(arg0: AlphaComposite) -> CompositeType: ...

  @staticmethod
  def makeUniqueID(arg0: str) -> int: ...


class DrawGlyphList(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawGlyphList(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawGlyphList: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class General(DrawGlyphList):

    def DrawGlyphList(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class TraceDrawGlyphList(DrawGlyphList):

    def DrawGlyphList(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawGlyphList): ...


class DrawGlyphListAA(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawGlyphListAA(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawGlyphListAA: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class General(DrawGlyphListAA):

    def DrawGlyphListAA(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class TraceDrawGlyphListAA(DrawGlyphListAA):

    def DrawGlyphListAA(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawGlyphListAA): ...


class DrawGlyphListColor(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawGlyphListColor(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

  def makePrimitive(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> GraphicsPrimitive: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawGlyphListColor: ...

  class General(DrawGlyphListColor):

    def DrawGlyphListColor(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class TraceDrawGlyphListColor(DrawGlyphListColor):

    def DrawGlyphListColor(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawGlyphListColor): ...


class DrawGlyphListLCD(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawGlyphListLCD(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawGlyphListLCD: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawGlyphListLCD(DrawGlyphListLCD):

    def DrawGlyphListLCD(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: GlyphList, arg3: int, arg4: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawGlyphListLCD): ...


class DrawLine(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawLine(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawLine: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawLine(DrawLine):

    def DrawLine(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawLine): ...


class DrawParallelogram(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawParallelogram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawParallelogram: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawParallelogram(DrawParallelogram):

    def DrawParallelogram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawParallelogram): ...


class DrawPath(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawPath(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: Path2D.Float) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawPath: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawPath(DrawPath):

    def DrawPath(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: Path2D.Float) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawPath): ...


class DrawPolygons(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawPolygons(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: list[int], arg3: list[int], arg4: list[int], arg5: int, arg6: int, arg7: int, arg8: bool) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawPolygons: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawPolygons(DrawPolygons):

    def DrawPolygons(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: list[int], arg3: list[int], arg4: list[int], arg5: int, arg6: int, arg7: int, arg8: bool) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawPolygons): ...


class DrawRect(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def DrawRect(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> DrawRect: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceDrawRect(DrawRect):

    def DrawRect(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: DrawRect): ...


class FillParallelogram(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def FillParallelogram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> FillParallelogram: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceFillParallelogram(FillParallelogram):

    def FillParallelogram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: FillParallelogram): ...


class FillPath(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def FillPath(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: Path2D.Float) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> FillPath: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceFillPath(FillPath):

    def FillPath(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: Path2D.Float) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: FillPath): ...


class FillRect(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def FillRect(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> FillRect: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class General(FillRect):

    def FillRect(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType):
      self.fillop: MaskFill

  class TraceFillRect(FillRect):

    def FillRect(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: FillRect): ...


class FillSpans(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def FillSpans(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: SpanIterator) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> FillSpans: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class TraceFillSpans(FillSpans):

    def FillSpans(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: SpanIterator) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: FillSpans): ...


class FontInfo:

  def clone(self) -> object: ...

  def mtx(self, arg0: list[float]) -> str: ...

  def toString(self) -> str: ...

  def __init__(self):
    self.aahint: int
    self.devtx: list[float]
    self.font: Font
    self.font2d: Font2D
    self.fontstrike: FontStrike
    self.glyphtx: list[float]
    self.lcdrgborder: bool
    self.lcdsubpixpos: bool
    self.noninvertibletx: bool
    self.originx: float
    self.originy: float
    self.pixelheight: int


class GraphicsPrimitive:

  TRACECOUNTS: int

  tracefile: str

  traceflags: int

  TRACELOG: int

  traceout: PrintStream

  TRACETIMESTAMP: int

  def getCompositeType(self) -> CompositeType: ...

  def getDestType(self) -> SurfaceType: ...

  def getNativePrim(self) -> int: ...

  def getPrimTypeID(self) -> int: ...

  def getSignature(self) -> str: ...

  def getSourceType(self) -> SurfaceType: ...

  def getUniqueID(self) -> int: ...

  def satisfies(self, arg0: str, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType) -> bool: ...

  def toString(self) -> str: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def makePrimTypeID() -> int: ...

  @staticmethod
  def makeUniqueID(arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType) -> int: ...

  @staticmethod
  @overload
  def simplename(arg0: CompositeType) -> str: ...

  @staticmethod
  @overload
  def simplename(arg0: SurfaceType) -> str: ...

  @staticmethod
  @overload
  def simplename(arg0: list[Field], arg1: object) -> str: ...

  @staticmethod
  def tracePrimitive(arg0: object) -> None: ...

  @staticmethod
  def tracingEnabled() -> bool: ...

  class TraceReporter:

    @overload
    def run(self) -> None: ...

    @overload
    def run(self) -> None: ...

    @staticmethod
    def setShutdownHook() -> None: ...

    def __init__(self): ...

  class GeneralBinaryOp:

    def getCompositeType(self) -> CompositeType: ...

    def getDestType(self) -> SurfaceType: ...

    def getPrimTypeID(self) -> int: ...

    def getSignature(self) -> str: ...

    def getSourceType(self) -> SurfaceType: ...

    def setPrimitives(self, arg0: Blit, arg1: Blit, arg2: GraphicsPrimitive, arg3: Blit) -> None: ...

  class GeneralUnaryOp:

    def getCompositeType(self) -> CompositeType: ...

    def getDestType(self) -> SurfaceType: ...

    def getPrimTypeID(self) -> int: ...

    def getSignature(self) -> str: ...

    def setPrimitives(self, arg0: Blit, arg1: GraphicsPrimitive, arg2: Blit) -> None: ...


class MaskBlit(GraphicsPrimitive):

  methodSignature: str

  primTypeID: int

  def MaskBlit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: list[int], arg11: int, arg12: int) -> None: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def getFromCache(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> MaskBlit: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> MaskBlit: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class General(MaskBlit):

    def MaskBlit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: list[int], arg11: int, arg12: int) -> None: ...

    def getCompositeType(self) -> CompositeType: ...

    def getDestType(self) -> SurfaceType: ...

    def getPrimTypeID(self) -> int: ...

    def getSignature(self) -> str: ...

    def getSourceType(self) -> SurfaceType: ...

    @overload
    def setPrimitives(self, arg0: Blit, arg1: Blit, arg2: GraphicsPrimitive, arg3: Blit) -> None: ...

    @overload
    def setPrimitives(self, arg0: Blit, arg1: Blit, arg2: GraphicsPrimitive, arg3: Blit) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class TraceMaskBlit(MaskBlit):

    def MaskBlit(self, arg0: SurfaceData, arg1: SurfaceData, arg2: Composite, arg3: Region, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: list[int], arg11: int, arg12: int) -> None: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: MaskBlit): ...


class MaskFill(GraphicsPrimitive):

  drawPgramSignature: str

  fillPgramSignature: str

  methodSignature: str

  primTypeID: int

  def DrawAAPgram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float) -> None: ...

  def FillAAPgram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None: ...

  def MaskFill(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: int, arg4: int, arg5: int, arg6: int, arg7: list[int], arg8: int, arg9: int) -> None: ...

  def canDoParallelograms(self) -> bool: ...

  def traceWrap(self) -> GraphicsPrimitive: ...

  @staticmethod
  def getFromCache(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> MaskFill: ...

  @staticmethod
  def locate(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> MaskFill: ...

  @staticmethod
  def locatePrim(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> MaskFill: ...

  def __init__(self, arg0: int, arg1: SurfaceType, arg2: CompositeType, arg3: SurfaceType): ...

  class General(MaskFill):

    def MaskFill(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: int, arg4: int, arg5: int, arg6: int, arg7: list[int], arg8: int, arg9: int) -> None: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType): ...

  class TraceMaskFill(MaskFill):

    def DrawAAPgram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float) -> None: ...

    def FillAAPgram(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None: ...

    def MaskFill(self, arg0: SunGraphics2D, arg1: SurfaceData, arg2: Composite, arg3: int, arg4: int, arg5: int, arg6: int, arg7: list[int], arg8: int, arg9: int) -> None: ...

    def canDoParallelograms(self) -> bool: ...

    def traceWrap(self) -> GraphicsPrimitive: ...

    def __init__(self, arg0: MaskFill): ...


class RenderCache:

  def get(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> object: ...

  def put(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType, arg3: object) -> None: ...

  def __init__(self, arg0: int): ...

  class Entry:

    def getValue(self) -> object: ...

    def matches(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> bool: ...

    def __init__(self, arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType, arg3: object): ...


class RenderLoops:

  primTypeID: int

  def __init__(self):
    self.drawglyphlistaaloop: DrawGlyphListAA
    self.drawglyphlistcolorloop: DrawGlyphListColor
    self.drawglyphlistlcdloop: DrawGlyphListLCD
    self.drawglyphlistloop: DrawGlyphList
    self.drawlineloop: DrawLine
    self.drawparallelogramloop: DrawParallelogram
    self.drawpathloop: DrawPath
    self.drawpolygonsloop: DrawPolygons
    self.drawrectloop: DrawRect
    self.fillparallelogramloop: FillParallelogram
    self.fillpathloop: FillPath
    self.fillrectloop: FillRect
    self.fillspansloop: FillSpans


class SurfaceType:

  Any: SurfaceType

  Any3Byte: SurfaceType

  Any4Byte: SurfaceType

  AnyByte: SurfaceType

  AnyByteBinary: SurfaceType

  AnyColor: SurfaceType

  AnyDcm: SurfaceType

  AnyInt: SurfaceType

  AnyPaint: SurfaceType

  AnyShort: SurfaceType

  ByteBinary1Bit: SurfaceType

  ByteBinary2Bit: SurfaceType

  ByteBinary4Bit: SurfaceType

  ByteGray: SurfaceType

  ByteIndexed: SurfaceType

  ByteIndexedBm: SurfaceType

  ByteIndexedOpaque: SurfaceType

  Custom: SurfaceType

  DESC_3BYTE_BGR: str

  DESC_3BYTE_RGB: str

  DESC_4BYTE_ABGR: str

  DESC_4BYTE_ABGR_PRE: str

  DESC_ANY: str

  DESC_ANY_3BYTE: str

  DESC_ANY_4BYTE: str

  DESC_ANY_BYTE: str

  DESC_ANY_COLOR: str

  DESC_ANY_INT: str

  DESC_ANY_INT_DCM: str

  DESC_ANY_PAINT: str

  DESC_ANY_SHORT: str

  DESC_BYTE_BINARY: str

  DESC_BYTE_BINARY_1BIT: str

  DESC_BYTE_BINARY_2BIT: str

  DESC_BYTE_BINARY_4BIT: str

  DESC_BYTE_GRAY: str

  DESC_BYTE_INDEXED: str

  DESC_BYTE_INDEXED_BM: str

  DESC_BYTE_INDEXED_OPAQUE: str

  DESC_GRADIENT_PAINT: str

  DESC_INDEX12_GRAY: str

  DESC_INDEX8_GRAY: str

  DESC_INT_ARGB: str

  DESC_INT_ARGB_BM: str

  DESC_INT_ARGB_PRE: str

  DESC_INT_BGR: str

  DESC_INT_BGRx: str

  DESC_INT_RGB: str

  DESC_INT_RGBx: str

  DESC_LINEAR_GRADIENT_PAINT: str

  DESC_OPAQUE_COLOR: str

  DESC_OPAQUE_GRADIENT_PAINT: str

  DESC_OPAQUE_LINEAR_GRADIENT_PAINT: str

  DESC_OPAQUE_RADIAL_GRADIENT_PAINT: str

  DESC_OPAQUE_TEXTURE_PAINT: str

  DESC_RADIAL_GRADIENT_PAINT: str

  DESC_TEXTURE_PAINT: str

  DESC_USHORT_4444_ARGB: str

  DESC_USHORT_555_RGB: str

  DESC_USHORT_555_RGBx: str

  DESC_USHORT_565_RGB: str

  DESC_USHORT_GRAY: str

  DESC_USHORT_INDEXED: str

  FourByteAbgr: SurfaceType

  FourByteAbgrPre: SurfaceType

  GradientPaint: SurfaceType

  Index12Gray: SurfaceType

  Index8Gray: SurfaceType

  IntArgb: SurfaceType

  IntArgbBm: SurfaceType

  IntArgbPre: SurfaceType

  IntBgr: SurfaceType

  IntBgrx: SurfaceType

  IntRgb: SurfaceType

  IntRgbx: SurfaceType

  LinearGradientPaint: SurfaceType

  OpaqueColor: SurfaceType

  OpaqueGradientPaint: SurfaceType

  OpaqueLinearGradientPaint: SurfaceType

  OpaqueRadialGradientPaint: SurfaceType

  OpaqueTexturePaint: SurfaceType

  RadialGradientPaint: SurfaceType

  TexturePaint: SurfaceType

  ThreeByteBgr: SurfaceType

  ThreeByteRgb: SurfaceType

  Ushort4444Argb: SurfaceType

  Ushort555Rgb: SurfaceType

  Ushort555Rgbx: SurfaceType

  Ushort565Rgb: SurfaceType

  UshortGray: SurfaceType

  UshortIndexed: SurfaceType

  @overload
  def deriveSubType(self, arg0: str) -> SurfaceType: ...

  @overload
  def deriveSubType(self, arg0: str, arg1: PixelConverter) -> SurfaceType: ...

  def equals(self, arg0: object) -> bool: ...

  def getAlphaMask(self) -> int: ...

  def getDescriptor(self) -> str: ...

  def getPixelConverter(self) -> PixelConverter: ...

  def getSuperType(self) -> SurfaceType: ...

  def getUniqueID(self) -> int: ...

  def hashCode(self) -> int: ...

  def pixelFor(self, arg0: int, arg1: ColorModel) -> int: ...

  def rgbFor(self, arg0: int, arg1: ColorModel) -> int: ...

  def toString(self) -> str: ...

  @staticmethod
  def makeUniqueID(arg0: str) -> int: ...

