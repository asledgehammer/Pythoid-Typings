from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Graphics2D, Font, Shape, Image, Color, Graphics, Rectangle, Composite, GraphicsConfiguration, FontMetrics, Paint, RenderingHints, Stroke
from java.awt.font import FontRenderContext, GlyphVector
from java.awt.geom import AffineTransform
from java.awt.image import ImageObserver, BufferedImage, BufferedImageOp, RenderedImage, ColorModel, Raster
from java.awt.image.renderable import RenderableImage
from java.lang import Enum
from java.lang.ref import WeakReference
from java.text import AttributedCharacterIterator
from java.util import Map
from sun.java2d.loops import FontInfo, MaskFill, CompositeType, RenderLoops, SurfaceType
from sun.java2d.pipe import Region, PixelDrawPipe, PixelFillPipe, DrawImagePipe, ShapeDrawPipe, TextPipe, PixelToShapeConverter, PixelToParallelogramConverter, ParallelogramPipe

K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)

class DestSurfaceProvider:

  def getDestSurface(self) -> Surface: ...


class DisposerRecord:

  def dispose(self) -> None: ...


class DisposerTarget:

  def getDisposerReferent(self) -> object: ...


class ReentrantContext:

  def __init__(self): ...


class ReentrantContextProvider[K]:

  REF_HARD: int

  REF_SOFT: int

  REF_WEAK: int

  def acquire(self) -> K: ...

  def release(self, arg0: K) -> None: ...

  class HardReference[V](WeakReference):

    def get(self) -> object: ...


class StateTrackable:

  def getState(self) -> StateTrackable.State: ...

  def getStateTracker(self) -> StateTracker: ...

  class State(Enum):

    DYNAMIC: StateTrackable.State

    IMMUTABLE: StateTrackable.State

    STABLE: StateTrackable.State

    UNTRACKABLE: StateTrackable.State

    @staticmethod
    def valueOf(arg0: str) -> StateTrackable.State: ...

    @staticmethod
    def values() -> list[StateTrackable.State]: ...


class StateTrackableDelegate:

  IMMUTABLE_DELEGATE: StateTrackableDelegate

  UNTRACKABLE_DELEGATE: StateTrackableDelegate

  def addDynamicAgent(self) -> None: ...

  @overload
  def getState(self) -> StateTrackable.State: ...

  @overload
  def getState(self) -> StateTrackable.State: ...

  @overload
  def getStateTracker(self) -> StateTracker: ...

  @overload
  def getStateTracker(self) -> StateTracker: ...

  def markDirty(self) -> None: ...

  def setImmutable(self) -> None: ...

  def setUntrackable(self) -> None: ...

  @staticmethod
  def createInstance(arg0: StateTrackable.State) -> StateTrackableDelegate: ...


class StateTracker:

  ALWAYS_CURRENT: StateTracker

  NEVER_CURRENT: StateTracker

  def isCurrent(self) -> bool: ...


class SunGraphics2D(Graphics2D):

  CLIP_DEVICE: int

  CLIP_RECTANGULAR: int

  CLIP_SHAPE: int

  COMP_ALPHA: int

  COMP_CUSTOM: int

  COMP_ISCOPY: int

  COMP_XOR: int

  MinPenSizeAA: float

  MinPenSizeAASquared: float

  MinPenSizeSquared: float

  PAINT_ALPHACOLOR: int

  PAINT_CUSTOM: int

  PAINT_GRADIENT: int

  PAINT_LIN_GRADIENT: int

  PAINT_OPAQUECOLOR: int

  PAINT_RAD_GRADIENT: int

  PAINT_TEXTURE: int

  STROKE_CUSTOM: int

  STROKE_THIN: int

  STROKE_THINDASHED: int

  STROKE_WIDE: int

  TRANSFORM_ANY_TRANSLATE: int

  TRANSFORM_GENERIC: int

  TRANSFORM_INT_TRANSLATE: int

  TRANSFORM_ISIDENT: int

  TRANSFORM_TRANSLATESCALE: int

  def addRenderingHints(self, arg0: Map[Any, Any]) -> None: ...

  def checkFontInfo(self, arg0: FontInfo, arg1: Font, arg2: FontRenderContext) -> FontInfo: ...

  def clearRect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def clip(self, arg0: Shape) -> None: ...

  def clipRect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def cloneTransform(self) -> AffineTransform: ...

  @overload
  def constrain(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  @overload
  def constrain(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  @overload
  def constrain(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: Region) -> None: ...

  def copyArea(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def copyImage(self, arg0: Image, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: Color, arg8: ImageObserver) -> bool: ...

  def create(self) -> Graphics: ...

  def dispose(self) -> None: ...

  def draw(self, arg0: Shape) -> None: ...

  def drawArc(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def drawBytes(self, arg0: list[int], arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  def drawChars(self, arg0: list[str], arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

  def drawGlyphVector(self, arg0: GlyphVector, arg1: float, arg2: float) -> None: ...

  @overload
  def drawImage(self, arg0: Image, arg1: AffineTransform, arg2: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: BufferedImage, arg1: BufferedImageOp, arg2: int, arg3: int) -> None: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: Color, arg4: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: int, arg4: int, arg5: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: int, arg4: int, arg5: Color, arg6: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: ImageObserver) -> bool: ...

  @overload
  def drawImage(self, arg0: Image, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: Color, arg10: ImageObserver) -> bool: ...

  def drawLine(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def drawOval(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def drawPolygon(self, arg0: list[int], arg1: list[int], arg2: int) -> None: ...

  def drawPolyline(self, arg0: list[int], arg1: list[int], arg2: int) -> None: ...

  def drawRect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def drawRenderableImage(self, arg0: RenderableImage, arg1: AffineTransform) -> None: ...

  def drawRenderedImage(self, arg0: RenderedImage, arg1: AffineTransform) -> None: ...

  def drawRoundRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  @overload
  def drawString(self, arg0: str, arg1: float, arg2: float) -> None: ...

  @overload
  def drawString(self, arg0: str, arg1: int, arg2: int) -> None: ...

  @overload
  def drawString(self, arg0: AttributedCharacterIterator, arg1: float, arg2: float) -> None: ...

  @overload
  def drawString(self, arg0: AttributedCharacterIterator, arg1: int, arg2: int) -> None: ...

  def fill(self, arg0: Shape) -> None: ...

  def fillArc(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def fillOval(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def fillPolygon(self, arg0: list[int], arg1: list[int], arg2: int) -> None: ...

  def fillRect(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def fillRoundRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...

  def finalize(self) -> None: ...

  def getBackground(self) -> Color: ...

  def getClip(self) -> Shape: ...

  @overload
  def getClipBounds(self) -> Rectangle: ...

  @overload
  def getClipBounds(self, arg0: Rectangle) -> Rectangle: ...

  def getColor(self) -> Color: ...

  def getCompClip(self) -> Region: ...

  def getComposite(self) -> Composite: ...

  @overload
  def getDestSurface(self) -> Surface: ...

  @overload
  def getDestSurface(self) -> Surface: ...

  def getDestination(self) -> object: ...

  def getDeviceColorModel(self) -> ColorModel: ...

  def getDeviceConfiguration(self) -> GraphicsConfiguration: ...

  def getFont(self) -> Font: ...

  def getFontInfo(self) -> FontInfo: ...

  @overload
  def getFontMetrics(self) -> FontMetrics: ...

  @overload
  def getFontMetrics(self, arg0: Font) -> FontMetrics: ...

  def getFontRenderContext(self) -> FontRenderContext: ...

  def getGVFontInfo(self, arg0: Font, arg1: FontRenderContext) -> FontInfo: ...

  def getPaint(self) -> Paint: ...

  def getRenderingHint(self, arg0: RenderingHints.Key) -> object: ...

  def getRenderingHints(self) -> RenderingHints: ...

  def getStroke(self) -> Stroke: ...

  def getSurfaceData(self) -> SurfaceData: ...

  def getTransform(self) -> AffineTransform: ...

  def hit(self, arg0: Rectangle, arg1: Shape, arg2: bool) -> bool: ...

  def hitClip(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool: ...

  @overload
  def rotate(self, arg0: float) -> None: ...

  @overload
  def rotate(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def scale(self, arg0: float, arg1: float) -> None: ...

  def setBackground(self, arg0: Color) -> None: ...

  @overload
  def setClip(self, arg0: Shape) -> None: ...

  @overload
  def setClip(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def setColor(self, arg0: Color) -> None: ...

  def setComposite(self, arg0: Composite) -> None: ...

  @overload
  def setDevClip(self, arg0: Rectangle) -> None: ...

  @overload
  def setDevClip(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...

  def setFont(self, arg0: Font) -> None: ...

  def setPaint(self, arg0: Paint) -> None: ...

  def setPaintMode(self) -> None: ...

  def setRenderingHint(self, arg0: RenderingHints.Key, arg1: object) -> None: ...

  def setRenderingHints(self, arg0: Map[Any, Any]) -> None: ...

  def setStroke(self, arg0: Stroke) -> None: ...

  def setTransform(self, arg0: AffineTransform) -> None: ...

  def setXORMode(self, arg0: Color) -> None: ...

  def shear(self, arg0: float, arg1: float) -> None: ...

  def transform(self, arg0: AffineTransform) -> None: ...

  @overload
  def translate(self, arg0: float, arg1: float) -> None: ...

  @overload
  def translate(self, arg0: int, arg1: int) -> None: ...

  def untransformShape(self, arg0: Shape) -> Shape: ...

  def validatePipe(self) -> None: ...

  @staticmethod
  def isRotated(arg0: list[float]) -> bool: ...

  def __init__(self, arg0: SurfaceData, arg1: Color, arg2: Color, arg3: Font):
    self.alphafill: MaskFill
    self.antialiashint: int
    self.backgroundcolor: Color
    self.clipregion: Region
    self.clipstate: int
    self.composite: Composite
    self.compositestate: int
    self.constrainclip: Region
    self.constrainx: int
    self.constrainy: int
    self.drawpipe: PixelDrawPipe
    self.eargb: int
    self.fillpipe: PixelFillPipe
    self.foregroundcolor: Color
    self.hints: RenderingHints
    self.imagecomp: CompositeType
    self.imagepipe: DrawImagePipe
    self.interpolationtype: int
    self.lcdtextcontrast: int
    self.loops: RenderLoops
    self.paint: Paint
    self.paintstate: int
    self.pixel: int
    self.renderhint: int
    self.shapepipe: ShapeDrawPipe
    self.stroke: Stroke
    self.strokehint: int
    self.strokestate: int
    self.surfacedata: SurfaceData
    self.textantialiashint: int
    self.textpipe: TextPipe
    self.transform: AffineTransform
    self.transformstate: int
    self.transx: int
    self.transy: int
    self.usrclip: Shape


class Surface: ...


class SurfaceData:

  aaTextRenderer: TextPipe

  BITMASK: int

  lcdTextRenderer: TextPipe

  OPAQUE: int

  outlineTextRenderer: TextPipe

  solidTextRenderer: TextPipe

  TRANSLUCENT: int

  def canRenderLCDText(self, arg0: SunGraphics2D) -> bool: ...

  def canRenderParallelograms(self, arg0: SunGraphics2D) -> bool: ...

  def copyArea(self, arg0: SunGraphics2D, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool: ...

  def flush(self) -> None: ...

  def getBounds(self) -> Rectangle: ...

  def getColorModel(self) -> ColorModel: ...

  def getDefaultScaleX(self) -> float: ...

  def getDefaultScaleY(self) -> float: ...

  def getDestination(self) -> object: ...

  def getDeviceConfiguration(self) -> GraphicsConfiguration: ...

  @overload
  def getDisposerReferent(self) -> object: ...

  @overload
  def getDisposerReferent(self) -> object: ...

  def getNativeOps(self) -> int: ...

  def getRaster(self, arg0: int, arg1: int, arg2: int, arg3: int) -> Raster: ...

  def getRenderLoops(self, arg0: SunGraphics2D) -> RenderLoops: ...

  def getReplacement(self) -> SurfaceData: ...

  def getSourceSurfaceData(self, arg0: Image, arg1: int, arg2: CompositeType, arg3: Color) -> SurfaceData: ...

  @overload
  def getState(self) -> StateTrackable.State: ...

  @overload
  def getState(self) -> StateTrackable.State: ...

  @overload
  def getStateTracker(self) -> StateTracker: ...

  @overload
  def getStateTracker(self) -> StateTracker: ...

  def getSurfaceType(self) -> SurfaceType: ...

  @overload
  def getTransparency(self) -> int: ...

  @overload
  def getTransparency(self) -> int: ...

  def invalidate(self) -> None: ...

  def isSurfaceLost(self) -> bool: ...

  def isValid(self) -> bool: ...

  def makeProxyFor(self, arg0: SurfaceData) -> SurfaceDataProxy: ...

  def markDirty(self) -> None: ...

  @overload
  def pixelFor(self, arg0: int) -> int: ...

  @overload
  def pixelFor(self, arg0: Color) -> int: ...

  def rgbFor(self, arg0: int) -> int: ...

  def setSurfaceLost(self, arg0: bool) -> None: ...

  def useTightBBoxes(self) -> bool: ...

  def validatePipe(self, arg0: SunGraphics2D) -> None: ...

  @staticmethod
  def getPrimarySurfaceData(arg0: Image) -> SurfaceData: ...

  @staticmethod
  def isNull(arg0: SurfaceData) -> bool: ...

  @staticmethod
  def makeRenderLoops(arg0: SurfaceType, arg1: CompositeType, arg2: SurfaceType) -> RenderLoops: ...

  @staticmethod
  def restoreContents(arg0: Image) -> SurfaceData: ...

  class PixelToShapeLoopConverter(PixelToShapeConverter):

    def __init__(self, arg0: ShapeDrawPipe): ...

  class PixelToPgramLoopConverter(PixelToParallelogramConverter):

    def __init__(self, arg0: ShapeDrawPipe, arg1: ParallelogramPipe, arg2: float, arg3: float, arg4: bool): ...


class SurfaceDataProxy:

  UNCACHED: SurfaceDataProxy

  @overload
  def displayChanged(self) -> None: ...

  @overload
  def displayChanged(self) -> None: ...

  @overload
  def flush(self) -> None: ...

  @overload
  def flush(self, arg0: bool) -> bool: ...

  @overload
  def flush(self, arg0: bool) -> bool: ...

  def getRetryTracker(self, arg0: SurfaceData) -> StateTracker: ...

  def invalidate(self) -> None: ...

  def isAccelerated(self) -> bool: ...

  def isSupportedOperation(self, arg0: SurfaceData, arg1: int, arg2: CompositeType, arg3: Color) -> bool: ...

  def isValid(self) -> bool: ...

  @overload
  def paletteChanged(self) -> None: ...

  @overload
  def paletteChanged(self) -> None: ...

  def replaceData(self, arg0: SurfaceData, arg1: int, arg2: CompositeType, arg3: Color) -> SurfaceData: ...

  def updateSurfaceData(self, arg0: SurfaceData, arg1: SurfaceData, arg2: int, arg3: int) -> None: ...

  def updateSurfaceDataBg(self, arg0: SurfaceData, arg1: SurfaceData, arg2: int, arg3: int, arg4: Color) -> None: ...

  def validateSurfaceData(self, arg0: SurfaceData, arg1: SurfaceData, arg2: int, arg3: int) -> SurfaceData: ...

  @staticmethod
  def isCachingAllowed() -> bool: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: int): ...

  class CountdownTracker:

    ALWAYS_CURRENT: StateTracker

    NEVER_CURRENT: StateTracker

    @overload
    def isCurrent(self) -> bool: ...

    @overload
    def isCurrent(self) -> bool: ...

    def __init__(self, arg0: int): ...

