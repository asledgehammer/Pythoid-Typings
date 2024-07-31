from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.awt import Image
from java.awt.image import BufferedImage, Raster
from java.io import InputStream, BufferedInputStream, File
from java.lang import Integer, Enum, RuntimeException
from java.net import URL
from java.nio import ByteBuffer, IntBuffer
from java.util import ArrayList, HashMap, HashSet, Stack
from java.util.function import Consumer
from zombie.asset import Asset, AssetType, AssetPath, AssetManager
from zombie.characterTextures import BloodBodyPartType
from zombie.core import Color, ImmutableColor, SpriteRenderer
from zombie.core.opengl import SmartShader, Shader
from zombie.core.skinnedmodel import ModelManager
from zombie.core.skinnedmodel.model import CharacterMask
from zombie.core.utils import BooleanGrid, WrappedBuffer
from zombie.interfaces import ITexture
from zombie.iso import Vector2
from zombie.iso.objects import ObjectRenderEffects
from zombie.popman import ObjectPool

class ColorInfo:

  def desaturate(self, s: float) -> None: ...

  def getA(self) -> float: ...

  def getB(self) -> float: ...

  def getG(self) -> float: ...

  def getR(self) -> float: ...

  def interp(self, to: ColorInfo, delta: float, dest: ColorInfo) -> None: ...

  @overload
  def set(self, other: ColorInfo) -> ColorInfo: ...

  @overload
  def set(self, R: float, G: float, B: float, A: float) -> ColorInfo: ...

  def toColor(self) -> Color: ...

  def toImmutableColor(self) -> ImmutableColor: ...

  def toString(self) -> str: ...

  @overload
  def __init__(self):
    self.a: float

    self.b: float

    self.g: float

    self.r: float

  @overload
  def __init__(self, R: float, G: float, B: float, A: float): ...


class GLFramebufferObject30:

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  def __init__(self): ...


class GLFramebufferObjectARB:

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  def __init__(self): ...


class GLFramebufferObjectEXT:

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH24_STENCIL8(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_DEPTH_STENCIL(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_RENDERBUFFER(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glCheckFramebufferStatus(self, target: int) -> int: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenFramebuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glGenRenderbuffers(self) -> int: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  @overload
  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...

  def __init__(self): ...


class IGLFramebufferObject:

  def GL_COLOR_ATTACHMENT0(self) -> int: ...

  def GL_DEPTH24_STENCIL8(self) -> int: ...

  def GL_DEPTH_ATTACHMENT(self) -> int: ...

  def GL_DEPTH_STENCIL(self) -> int: ...

  def GL_FRAMEBUFFER(self) -> int: ...

  def GL_FRAMEBUFFER_COMPLETE(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_FORMATS(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE(self) -> int: ...

  def GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER(self) -> int: ...

  def GL_FRAMEBUFFER_UNDEFINED(self) -> int: ...

  def GL_FRAMEBUFFER_UNSUPPORTED(self) -> int: ...

  def GL_RENDERBUFFER(self) -> int: ...

  def GL_STENCIL_ATTACHMENT(self) -> int: ...

  def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...

  def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...

  def glCheckFramebufferStatus(self, target: int) -> int: ...

  def glDeleteFramebuffers(self, renderbuffer: int) -> None: ...

  def glDeleteRenderbuffers(self, renderbuffer: int) -> None: ...

  def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...

  def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...

  def glGenFramebuffers(self) -> int: ...

  def glGenRenderbuffers(self) -> int: ...

  def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...


class ImageData:

  MIP_LEVEL_IDX_OFFSET: int

  def dispose(self) -> None: ...

  def getData(self) -> MipMapLevel: ...

  def getHeight(self) -> int: ...

  def getHeightHW(self) -> int: ...

  def getMipMapCount(self) -> int: ...

  def getMipMapData(self, idx: int) -> MipMapLevel: ...

  def getWidth(self) -> int: ...

  def getWidthHW(self) -> int: ...

  def initMipMaps(self) -> None: ...

  def isSolid(self) -> bool: ...

  @overload
  def makeTransp(self, red: int, green: int, blue: int) -> None: ...

  @overload
  def makeTransp(self, red: int, green: int, blue: int, alpha: int) -> None: ...

  @overload
  def setData(self, image: BufferedImage) -> None: ...

  @overload
  def setData(self, rasterData: Raster) -> None: ...

  @staticmethod
  def calculateNumMips(widthHW: int, heightHW: int) -> int: ...

  @staticmethod
  def createSteamAvatar(steamID: int) -> ImageData: ...

  @staticmethod
  def getNextMipDimension(dim: int) -> int: ...

  @staticmethod
  def getPixelClamped(dataBuff: ByteBuffer, width: int, height: int, x: int, y: int, result: list[int]) -> list[int]: ...

  @staticmethod
  def getPixelDiscard(dataBuff: ByteBuffer, width: int, height: int, x: int, y: int, result: list[int]) -> int: ...

  @staticmethod
  def setPixel(dataBuff: ByteBuffer, width: int, height: int, x: int, y: int, pixelRGBA: list[int]) -> None: ...

  @overload
  def __init__(self, path: str):
    self.alphapaddingdone: bool

    self.bpreservetransparentcolor: bool

    self.data: MipMapLevel

    self.id: int

    self.mask: BooleanGrid

  @overload
  def __init__(self, width: int, height: int): ...
  @overload
  def __init__(self, b: InputStream, bDoMask: bool): ...
  @overload
  def __init__(self, texture: TextureID, bb: WrappedBuffer): ...
  @overload
  def __init__(self, width: int, height: int, data: WrappedBuffer): ...
  @overload
  def __init__(self, b: BufferedInputStream, bDoMask: bool, format: Texture.PZFileformat): ...

  class L_generateMipMaps: ...

  class L_performAlphaPadding: ...


class Mask:

  def clone(self) -> object: ...

  def full(self) -> None: ...

  def get(self, x: int, y: int) -> bool: ...

  def save(self, name: str) -> None: ...

  def set(self, x: int, y: int, val: bool) -> None: ...

  @overload
  def __init__(self, obj: Mask): ...
  @overload
  def __init__(self, texture: ITexture): ...
  @overload
  def __init__(self, width: int, height: int): ...
  @overload
  def __init__(self, texture: ITexture, mask: list[bool]): ...
  @overload
  def __init__(self, texture: ITexture, mask: BooleanGrid): ...
  @overload
  def __init__(self, other: Mask, x: int, y: int, width: int, height: int): ...
  @overload
  def __init__(self, arg0: Texture, texture: Texture, x: int, y: int, width: int, height: int): ...
  @overload
  def __init__(self, mask1: list[bool], maskW: int, maskH: int, x: int, y: int, width: int, height: int): ...
  @overload
  def __init__(self, mask1: BooleanGrid, maskW: int, maskH: int, x: int, y: int, width: int, height: int): ...


class MipMapLevel:

  def dispose(self) -> None: ...

  def getBuffer(self) -> ByteBuffer: ...

  def getDataSize(self) -> int: ...

  def isDisposed(self) -> bool: ...

  def rewind(self) -> None: ...

  @overload
  def __init__(self, width: int, height: int):
    self.data: WrappedBuffer

    self.height: int

    self.width: int

  @overload
  def __init__(self, width: int, height: int, data: WrappedBuffer): ...


class MultiTextureFBO2:

  def create(self, xres: int, yres: int) -> None: ...

  def destroy(self) -> None: ...

  def doZoomScroll(self, playerIndex: int, arg1: int) -> None: ...

  def getCurrent(self, nPlayer: int) -> TextureFBO: ...

  def getDefaultZoomLevels(self) -> ArrayList[Integer]: ...

  def getHeight(self, playerIndex: int) -> int: ...

  def getMaxZoom(self) -> float: ...

  def getMinZoom(self) -> float: ...

  def getNextZoom(self, playerIndex: int, arg1: int) -> float: ...

  def getTexture(self, nPlayer: int) -> Texture: ...

  def getWidth(self, playerIndex: int) -> int: ...

  def render(self) -> None: ...

  def setTargetZoom(self, playerIndex: int, target: float) -> None: ...

  def setZoomLevelsFromOption(self, levels: str) -> None: ...

  def test(self) -> bool: ...

  def update(self) -> None: ...

  def __init__(self):
    self.bautozoom: list[bool]
    self.bzoomenabled: bool
    self.current: TextureFBO
    self.fborendered: TextureFBO
    self.startzoom: list[float]
    self.targetzoom: list[float]
    self.zoom: list[float]


class PNGDecoder:

  def decideTextureFormat(self, fmt: PNGDecoder.Format) -> PNGDecoder.Format: ...

  def decode(self, buffer: ByteBuffer, stride: int, fmt: PNGDecoder.Format) -> None: ...

  def decodeFlipped(self, buffer: ByteBuffer, stride: int, fmt: PNGDecoder.Format) -> None: ...

  def getHeight(self) -> int: ...

  def getWidth(self) -> int: ...

  def hasAlpha(self) -> bool: ...

  def hasAlphaChannel(self) -> bool: ...

  def isRGB(self) -> bool: ...

  def overwriteTRNS(self, r: int, g: int, b: int) -> None: ...

  def __init__(self, input: InputStream, bDoMask: bool):
    self.bdomask: bool
    self.mask: BooleanGrid
    self.maskid: int
    self.readtotal: int

  class Format(Enum):

    ABGR: PNGDecoder.Format

    ALPHA: PNGDecoder.Format

    BGRA: PNGDecoder.Format

    LUMINANCE: PNGDecoder.Format

    LUMINANCE_ALPHA: PNGDecoder.Format

    RGB: PNGDecoder.Format

    RGBA: PNGDecoder.Format

    def getNumComponents(self) -> int: ...

    def isHasAlpha(self) -> bool: ...

    @staticmethod
    def valueOf(arg0: str) -> PNGDecoder.Format: ...

    @staticmethod
    def values() -> list[PNGDecoder.Format]: ...


class PNGSize:

  @overload
  def readSize(self, input: InputStream) -> None: ...

  @overload
  def readSize(self, path: str) -> None: ...

  def __init__(self):
    self.height: int
    self.width: int


class Pcx:

  Cache: HashMap[str, Pcx]

  def getImage(self) -> Image: ...

  @overload
  def __init__(self, file: str):
    self.imagedata: list[int]

    self.imageheight: int

    self.imagewidth: int

    self.palette: list[int]

    self.pic: list[int]

  @overload
  def __init__(self, url: URL): ...
  @overload
  def __init__(self, url: str, urlPal: list[int]): ...
  @overload
  def __init__(self, url: str, urlPal: str): ...

  class pcx_t: ...


class SmartTexture(Texture):

  @overload
  def add(self, tex: str) -> None: ...

  @overload
  def add(self, tex: Texture) -> None: ...

  @overload
  def add(self, tex: str, srcBlend: int, destBlend: int) -> None: ...

  @overload
  def add(self, tex: str, shader: SmartShader, params: ArrayList[TextureCombinerShaderParam]) -> None: ...

  @overload
  def add(self, tex: Texture, srcBlend: int, destBlend: int) -> None: ...

  @overload
  def add(self, tex: Texture, shader: SmartShader, params: ArrayList[TextureCombinerShaderParam]) -> None: ...

  @overload
  def add(self, tex: str, shader: SmartShader, maskTex: str, srcBlend: int, destBlend: int) -> None: ...

  @overload
  def add(self, tex: Texture, shader: SmartShader, maskTex: Texture, srcBlend: int, destBlend: int) -> None: ...

  @overload
  def add(self, tex: str, shader: SmartShader, maskTex: str, params: ArrayList[TextureCombinerShaderParam], srcBlend: int, destBlend: int) -> None: ...

  @overload
  def add(self, tex: Texture, shader: SmartShader, maskTex: Texture, params: ArrayList[TextureCombinerShaderParam], srcBlend: int, destBlend: int) -> None: ...

  def addDirtOverlay(self, tex: str, mask: str, intensity: float, category: int) -> None: ...

  def addHole(self, part: BloodBodyPartType) -> Texture: ...

  @overload
  def addHue(self, tex: str, category: int, h: float) -> None: ...

  @overload
  def addHue(self, tex: Texture, category: int, h: float) -> None: ...

  @overload
  def addMaskedTexture(self, mask: CharacterMask, masksFolder: str, base: str, category: int, tint: ImmutableColor, hue: float) -> None: ...

  @overload
  def addMaskedTexture(self, mask: CharacterMask, masksFolder: str, base: Texture, category: int, tint: ImmutableColor, hue: float) -> None: ...

  @overload
  def addOverlay(self, tex: str) -> None: ...

  @overload
  def addOverlay(self, tex: str, mask: str, intensity: float, category: int) -> None: ...

  def addOverlayPatches(self, tex: str, mask: str, category: int) -> None: ...

  def addRect(self, tex: str, x: int, y: int, w: int, h: int) -> None: ...

  @overload
  def addSeparate(self, tex: str, srcBlend: int, destBlend: int, srcBlendA: int, destBlendA: int) -> None: ...

  @overload
  def addSeparate(self, tex: Texture, srcBlend: int, destBlend: int, srcBlendA: int, destBlendA: int) -> None: ...

  @overload
  def addSeparate(self, tex: str, shader: SmartShader, maskTex: str, params: ArrayList[TextureCombinerShaderParam], srcBlend: int, destBlend: int, srcBlendA: int, destBlendA: int) -> None: ...

  @overload
  def addSeparate(self, tex: Texture, shader: SmartShader, maskTex: Texture, params: ArrayList[TextureCombinerShaderParam], srcBlend: int, destBlend: int, srcBlendA: int, destBlendA: int) -> None: ...

  def addTexture(self, base: str, category: int, tint: ImmutableColor, hue: float) -> None: ...

  @overload
  def addTint(self, tex: str, category: int, r: float, g: float, b: float) -> None: ...

  @overload
  def addTint(self, tex: Texture, category: int, r: float, g: float, b: float) -> None: ...

  def bind(self) -> None: ...

  def calculate(self) -> None: ...

  def clear(self) -> None: ...

  def destroy(self) -> None: ...

  def getData(self) -> WrappedBuffer: ...

  def getFirstFromCategory(self, cat: int) -> TextureCombinerCommand: ...

  def getID(self) -> int: ...

  def isEmpty(self) -> bool: ...

  def isFailure(self) -> bool: ...

  def isReady(self) -> bool: ...

  @overload
  def mask(self, tex: str, maskTex: str, category: int) -> None: ...

  @overload
  def mask(self, tex: Texture, maskTex: Texture, category: int) -> None: ...

  @overload
  def maskHue(self, tex: str, maskTex: str, category: int, h: float) -> None: ...

  @overload
  def maskHue(self, tex: Texture, maskTex: Texture, category: int, h: float) -> None: ...

  @overload
  def maskTint(self, tex: str, maskTex: str, category: int, r: float, g: float, b: float) -> None: ...

  @overload
  def maskTint(self, tex: Texture, maskTex: Texture, category: int, r: float, g: float, b: float) -> None: ...

  @overload
  def removeHole(self, bodyTex: str, part: BloodBodyPartType) -> None: ...

  @overload
  def removeHole(self, bodyTex: Texture, part: BloodBodyPartType) -> None: ...

  @overload
  def removeHole(self, bodyTex: Texture, maskTex: Texture, part: BloodBodyPartType) -> None: ...

  def saveOnRenderThread(self, filename: str) -> None: ...

  def __init__(self):
    self.commands: ArrayList[TextureCombinerCommand]
    self.result: Texture


class Texture(Asset):

  ASSET_TYPE: AssetType

  bDoingQuad: bool

  BindCount: int

  la: float

  lastlastTextureID: int

  lastTextureID: int

  lb: float

  lg: float

  lr: float

  nullTextures: HashSet[str]

  totalTextureID: int

  WarnFailFindTexture: bool

  @overload
  def bind(self) -> None: ...

  @overload
  def bind(self) -> None: ...

  @overload
  def bind(self, unit: int) -> None: ...

  @overload
  def bind(self, unit: int) -> None: ...

  def copyMaskRegion(self, arg0: Texture, x: int, y: int, width: int, height: int) -> None: ...

  @overload
  def createMask(self) -> None: ...

  @overload
  def createMask(self, mask: list[bool]) -> None: ...

  @overload
  def createMask(self, mask: BooleanGrid) -> None: ...

  @overload
  def createMask(self, buf: WrappedBuffer) -> None: ...

  @overload
  def destroy(self) -> None: ...

  @overload
  def destroy(self) -> None: ...

  def equals(self, other: Texture) -> bool: ...

  @overload
  def getData(self) -> WrappedBuffer: ...

  @overload
  def getData(self) -> WrappedBuffer: ...

  @overload
  def getHeight(self) -> int: ...

  @overload
  def getHeight(self) -> int: ...

  @overload
  def getHeightHW(self) -> int: ...

  @overload
  def getHeightHW(self) -> int: ...

  def getHeightOrig(self) -> int: ...

  @overload
  def getID(self) -> int: ...

  @overload
  def getID(self) -> int: ...

  def getMask(self) -> Mask: ...

  def getName(self) -> str: ...

  def getOffsetX(self) -> float: ...

  def getOffsetY(self) -> float: ...

  def getRealHeight(self) -> int: ...

  def getRealWidth(self) -> int: ...

  def getTextureId(self) -> TextureID: ...

  def getType(self) -> AssetType: ...

  def getUVScale(self, uvScale: Vector2) -> Vector2: ...

  def getUseAlphaChannel(self) -> bool: ...

  @overload
  def getWidth(self) -> int: ...

  @overload
  def getWidth(self) -> int: ...

  @overload
  def getWidthHW(self) -> int: ...

  @overload
  def getWidthHW(self) -> int: ...

  def getWidthOrig(self) -> int: ...

  @overload
  def getXEnd(self) -> float: ...

  @overload
  def getXEnd(self) -> float: ...

  @overload
  def getXStart(self) -> float: ...

  @overload
  def getXStart(self) -> float: ...

  @overload
  def getYEnd(self) -> float: ...

  @overload
  def getYEnd(self) -> float: ...

  @overload
  def getYStart(self) -> float: ...

  @overload
  def getYStart(self) -> float: ...

  def isCollisionable(self) -> bool: ...

  @overload
  def isDestroyed(self) -> bool: ...

  @overload
  def isDestroyed(self) -> bool: ...

  @overload
  def isSolid(self) -> bool: ...

  @overload
  def isSolid(self) -> bool: ...

  def isValid(self) -> bool: ...

  def loadMaskRegion(self, cache: ByteBuffer) -> None: ...

  @overload
  def makeTransp(self, red: int, green: int, blue: int) -> None: ...

  @overload
  def makeTransp(self, red: int, green: int, blue: int) -> None: ...

  def onBeforeReady(self) -> None: ...

  def reloadFromFile(self, name: str) -> None: ...

  @overload
  def render(self, x: float, y: float) -> None: ...

  @overload
  def render(self, x: float, y: float, width: float, height: float) -> None: ...

  @overload
  def render(self, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def render(self, dr: ObjectRenderEffects, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  def renderdiamond(self, x: float, y: float, width: float, height: float, l: int, u: int, r: int, d: int) -> None: ...

  def rendershader2(self, x: float, y: float, width: float, height: float, texx: int, texy: int, texWidth: int, texHeight: int, r: float, g: float, b: float, a: float) -> None: ...

  def renderstrip(self, x: int, y: int, width: int, height: int, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  def renderwalln(self, x: float, y: float, width: float, height: float, u: int, d: int, u2: int, d2: int) -> None: ...

  def renderwallnw(self, x: float, y: float, width: float, height: float, u: int, d: int, u2: int, d2: int, r: int, r2: int) -> None: ...

  def renderwallw(self, x: float, y: float, width: float, height: float, u: int, d: int, u2: int, d2: int) -> None: ...

  def saveMask(self, name: str) -> None: ...

  def saveMaskRegion(self, cache: ByteBuffer) -> None: ...

  def saveOnRenderThread(self, filename: str) -> None: ...

  def saveToCurrentSavefileDirectory(self, filename: str) -> None: ...

  def saveToZomboidDirectory(self, filename: str) -> None: ...

  @overload
  def setAlphaForeach(self, red: int, green: int, blue: int, alpha: int) -> None: ...

  @overload
  def setAlphaForeach(self, red: int, green: int, blue: int, alpha: int) -> None: ...

  def setCustomizedTexture(self) -> None: ...

  @overload
  def setData(self, data: ByteBuffer) -> None: ...

  @overload
  def setData(self, data: ByteBuffer) -> None: ...

  def setHeight(self, height: int) -> None: ...

  @overload
  def setMask(self, mask: Mask) -> None: ...

  @overload
  def setMask(self, mask: Mask) -> None: ...

  def setName(self, name: str) -> None: ...

  def setNameOnly(self, name: str) -> None: ...

  def setOffsetX(self, offset: int) -> None: ...

  def setOffsetY(self, offset: int) -> None: ...

  def setRealHeight(self, realHeight: int) -> None: ...

  def setRealWidth(self, realWidth: int) -> None: ...

  @overload
  def setRegion(self, x: int, y: int, width: int, height: int) -> None: ...

  @overload
  def setRegion(self, x: int, y: int, width: int, height: int) -> None: ...

  def setUseAlphaChannel(self, value: bool) -> None: ...

  def setWidth(self, width: int) -> None: ...

  @overload
  def split(self, xOffset: int, yOffset: int, width: int, height: int) -> Texture: ...

  @overload
  def split(self, name: str, xOffset: int, yOffset: int, width: int, height: int) -> Texture: ...

  @overload
  def split(self, xOffset: int, yOffset: int, row: int, coloumn: int, width: int, height: int, spaceX: int, spaceY: int) -> list[Texture]: ...

  def split2D(self, xstep: list[int], ystep: list[int]) -> list[list[Texture]]: ...

  def splitIcon(self) -> Texture: ...

  def toString(self) -> str: ...

  @staticmethod
  def bindNone() -> None: ...

  @staticmethod
  def clearTextures() -> None: ...

  @staticmethod
  def collectAllIcons(map: HashMap[str, str], mapFull: HashMap[str, str]) -> None: ...

  @staticmethod
  def flipPixels(imgPixels: list[int], imgw: int, imgh: int) -> list[int]: ...

  @staticmethod
  def forgetTexture(name: str) -> None: ...

  @staticmethod
  def getEngineMipmapTexture() -> Texture: ...

  @staticmethod
  def getErrorTexture() -> Texture: ...

  @staticmethod
  @overload
  def getSharedTexture(name: str) -> Texture: ...

  @staticmethod
  @overload
  def getSharedTexture(name: str, flags: int) -> Texture: ...

  @staticmethod
  @overload
  def getSharedTexture(name: str, palette: str) -> Texture: ...

  @staticmethod
  @overload
  def getSharedTexture(name: str, palette: list[int], paletteName: str) -> Texture: ...

  @staticmethod
  def getSteamAvatar(steamID: int) -> Texture: ...

  @staticmethod
  def getTexture(name: str) -> Texture: ...

  @staticmethod
  def getWhite() -> Texture: ...

  @staticmethod
  def onTexturePacksChanged() -> None: ...

  @staticmethod
  def processFilePath(filePath: str) -> str: ...

  @staticmethod
  def reload(name: str) -> None: ...

  @staticmethod
  def steamAvatarChanged(steamID: int) -> None: ...

  @staticmethod
  def trygetTexture(name: str) -> Texture: ...

  @overload
  def __init__(self):
    self.assetparams: Texture.TextureAssetParams

    self.bindalways: bool

    self.flip: bool

    self.offsetx: float

    self.offsety: float

    self.xend: float

    self.xstart: float

    self.yend: float

    self.ystart: float

  @overload
  def __init__(self, file: str): ...
  @overload
  def __init__(self, t: Texture): ...
  @overload
  def __init__(self, name: str, palette: list[int]): ...
  @overload
  def __init__(self, file: str, useAlphaChannel: bool): ...
  @overload
  def __init__(self, name: str, palette: str): ...
  @overload
  def __init__(self, data: TextureID, name: str): ...
  @overload
  def __init__(self, width: int, height: int, flags: int): ...
  @overload
  def __init__(self, file: str, bDelete: bool, bUseAlpha: bool): ...
  @overload
  def __init__(self, name: str, b: BufferedInputStream, bDoMask: bool): ...
  @overload
  def __init__(self, path: AssetPath, manager: AssetManager, params: Texture.TextureAssetParams): ...
  @overload
  def __init__(self, width: int, height: int, name: str, flags: int): ...
  @overload
  def __init__(self, file: str, red: int, green: int, blue: int): ...
  @overload
  def __init__(self, name: str, b: BufferedInputStream, bDoMask: bool, format: Texture.PZFileformat): ...

  class TextureAssetParams(AssetManager.AssetParams):

    def __init__(self): ...

  class PZFileformat(Enum):

    DDS: Texture.PZFileformat

    PNG: Texture.PZFileformat

    @staticmethod
    def valueOf(arg0: str) -> Texture.PZFileformat: ...

    @staticmethod
    def values() -> list[Texture.PZFileformat]: ...


class TextureAssetManager(AssetManager):

  instance: TextureAssetManager

  def __init__(self): ...


class TextureBinder:

  instance: TextureBinder

  def bind(self, textureID: int) -> None: ...

  def __init__(self):
    self.activetextureindex: int
    self.maxtextureunits: int
    self.textureindex: int
    self.textureunitids: list[int]
    self.textureunitidstart: int


class TextureCombiner:

  count: int

  instance: TextureCombiner

  def clear(self) -> None: ...

  @overload
  def combine(self, cmdList: ArrayList[TextureCombinerCommand]) -> Texture: ...

  @overload
  def combine(self, tex1: Texture, tex2: Texture) -> Texture: ...

  def combineEnd(self) -> None: ...

  def combineStart(self) -> None: ...

  def init(self) -> None: ...

  def overlay(self, tex2: Texture) -> None: ...

  def releaseTexture(self, tex: Texture) -> None: ...

  @staticmethod
  def flipPixels(imgPixels: list[int], imgw: int, imgh: int) -> list[int]: ...

  @staticmethod
  def getResultingHeight(cmdList: ArrayList[TextureCombinerCommand]) -> int: ...

  @staticmethod
  def getResultingWidth(cmdList: ArrayList[TextureCombinerCommand]) -> int: ...

  def __init__(self): ...

  class CombinerFBO: ...


class TextureCombinerCommand:

  DEFAULT_DST_A: int

  DEFAULT_SRC_A: int

  pool: ObjectPool[TextureCombinerCommand]

  @overload
  def init(self, tex: Texture) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, shader: SmartShader) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, src: int, dest: int) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, shader: SmartShader, params: ArrayList[TextureCombinerShaderParam]) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, x: int, y: int, w: int, h: int) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, shader: SmartShader, mask: Texture, src: int, dest: int) -> TextureCombinerCommand: ...

  @overload
  def init(self, tex: Texture, shader: SmartShader, params: ArrayList[TextureCombinerShaderParam], mask: Texture, src: int, dest: int) -> TextureCombinerCommand: ...

  @overload
  def initSeparate(self, tex: Texture, src: int, dest: int, srcA: int, destA: int) -> TextureCombinerCommand: ...

  @overload
  def initSeparate(self, tex: Texture, shader: SmartShader, params: ArrayList[TextureCombinerShaderParam], mask: Texture, src: int, dest: int, srcA: int, destA: int) -> TextureCombinerCommand: ...

  def toString(self) -> str: ...

  @staticmethod
  def get() -> TextureCombinerCommand: ...

  def __init__(self):
    self.blenddest: int
    self.blenddesta: int
    self.blendsrc: int
    self.blendsrca: int
    self.h: int
    self.mask: Texture
    self.shader: SmartShader
    self.shaderparams: ArrayList[TextureCombinerShaderParam]
    self.tex: Texture
    self.w: int
    self.x: int
    self.y: int


class TextureCombinerShaderParam:

  @overload
  def __init__(self, name: str, val: float):
    self.max: float

    self.min: float

    self.name: str

  @overload
  def __init__(self, name: str, min: float, max: float): ...


class TextureDraw:

  def getColor(self, i: int) -> int: ...

  def postRender(self) -> None: ...

  def reset(self) -> None: ...

  def run(self) -> None: ...

  def toString(self) -> str: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> TextureDraw: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, wallSection: SpriteRenderer.WallShaderTexRender, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, texdModifier: Consumer[TextureDraw]) -> TextureDraw: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r1: float, g1: float, b1: float, a1: float) -> None: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, c1: int, c2: int, c3: int, c4: int) -> None: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, c1: int, c2: int, c3: int, c4: int, texdModifier: Consumer[TextureDraw]) -> TextureDraw: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, u4: float, v4: float, texdModifier: Consumer[TextureDraw]) -> TextureDraw: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x0: float, y0: float, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, c0: int, c1: int, c2: int, c3: int, u0: float, v0: float, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, texdModifier: Consumer[TextureDraw]) -> TextureDraw: ...

  @staticmethod
  @overload
  def Create(texd: TextureDraw, tex: Texture, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float, r1: float, g1: float, b1: float, a1: float, r2: float, g2: float, b2: float, a2: float, r3: float, g3: float, b3: float, a3: float, r4: float, g4: float, b4: float, a4: float, texdModifier: Consumer[TextureDraw]) -> None: ...

  @staticmethod
  def ShaderUpdate1f(texd: TextureDraw, shaderID: int, uniform: int, uniformValue: float) -> None: ...

  @staticmethod
  def ShaderUpdate1i(texd: TextureDraw, shaderID: int, uniform: int, uniformValue: int) -> None: ...

  @staticmethod
  def ShaderUpdate2f(texd: TextureDraw, shaderID: int, uniform: int, value1: float, value2: float) -> None: ...

  @staticmethod
  def ShaderUpdate3f(texd: TextureDraw, shaderID: int, uniform: int, value1: float, value2: float, value3: float) -> None: ...

  @staticmethod
  def ShaderUpdate4f(texd: TextureDraw, shaderID: int, uniform: int, value1: float, value2: float, value3: float, value4: float) -> None: ...

  @staticmethod
  def StartShader(texd: TextureDraw, iD: int) -> None: ...

  @staticmethod
  def doCoreIntParam(textureDraw: TextureDraw, id: int, val: float) -> None: ...

  @staticmethod
  def drawModel(texd: TextureDraw, model: ModelManager.ModelSlot) -> None: ...

  @staticmethod
  def drawParticles(texd: TextureDraw, userId: int, var1: int, var2: int) -> None: ...

  @staticmethod
  def drawPuddles(texd: TextureDraw, shader: Shader, userId: int, apiId: int, z: int) -> None: ...

  @staticmethod
  def drawSkyBox(texd: TextureDraw, shader: Shader, userId: int, apiId: int, bufferId: int) -> None: ...

  @staticmethod
  def drawWater(texd: TextureDraw, shader: Shader, userId: int, apiId: int, bShore: bool) -> None: ...

  @staticmethod
  def glAlphaFunc(texd: TextureDraw, a: int, b: float) -> None: ...

  @staticmethod
  def glBind(textureDraw: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glBlendEquation(texd: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glBlendFunc(texd: TextureDraw, a: int, b: int) -> None: ...

  @staticmethod
  def glBlendFuncSeparate(texd: TextureDraw, a: int, b: int, c: int, d: int) -> None: ...

  @staticmethod
  def glBuffer(texd: TextureDraw, a: int, b: int) -> None: ...

  @staticmethod
  def glClear(texd: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glClearColor(texd: TextureDraw, r: int, g: int, b: int, a: int) -> None: ...

  @staticmethod
  def glColorMask(texd: TextureDraw, a: int, b: int, c: int, d: int) -> None: ...

  @staticmethod
  def glDepthMask(textureDraw: TextureDraw, b: bool) -> None: ...

  @staticmethod
  def glDisable(texd: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glDoEndFrame(texd: TextureDraw) -> None: ...

  @staticmethod
  def glDoEndFrameFx(texd: TextureDraw, player: int) -> None: ...

  @staticmethod
  @overload
  def glDoStartFrame(texd: TextureDraw, w: int, h: int, zoom: float, player: int) -> None: ...

  @staticmethod
  @overload
  def glDoStartFrame(texd: TextureDraw, w: int, h: int, zoom: float, player: int, isTextFrame: bool) -> None: ...

  @staticmethod
  def glDoStartFrameFx(texd: TextureDraw, w: int, h: int, player: int) -> None: ...

  @staticmethod
  def glEnable(texd: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glGenerateMipMaps(textureDraw: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glIgnoreStyles(texd: TextureDraw, b: bool) -> None: ...

  @staticmethod
  def glLoadIdentity(textureDraw: TextureDraw) -> None: ...

  @staticmethod
  def glStencilFunc(texd: TextureDraw, a: int, b: int, c: int) -> None: ...

  @staticmethod
  def glStencilMask(texd: TextureDraw, a: int) -> None: ...

  @staticmethod
  def glStencilOp(texd: TextureDraw, a: int, b: int, c: int) -> None: ...

  @staticmethod
  def glTexParameteri(texd: TextureDraw, a: int, b: int, c: int) -> None: ...

  @staticmethod
  def glViewport(textureDraw: TextureDraw, x: int, y: int, width: int, height: int) -> None: ...

  def __init__(self):
    self.a: int
    self.b: int
    self.bsinglecol: bool
    self.c: int
    self.col0: int
    self.col1: int
    self.col2: int
    self.col3: int
    self.d: int
    self.drawer: TextureDraw.GenericDrawer
    self.f1: float
    self.flipped: bool
    self.tex: Texture
    self.tex1: Texture
    self.tex1_col0: int
    self.tex1_col1: int
    self.tex1_col2: int
    self.tex1_col3: int
    self.tex1_u0: float
    self.tex1_u1: float
    self.tex1_u2: float
    self.tex1_u3: float
    self.tex1_v0: float
    self.tex1_v1: float
    self.tex1_v2: float
    self.tex1_v3: float
    self.type: TextureDraw.Type
    self.u0: float
    self.u1: float
    self.u2: float
    self.u3: float
    self.useattribarray: int
    self.v0: float
    self.v1: float
    self.v2: float
    self.v3: float
    self.vars: list[float]
    self.x0: float
    self.x1: float
    self.x2: float
    self.x3: float
    self.y0: float
    self.y1: float
    self.y2: float
    self.y3: float

  class Type(Enum):

    BindActiveTexture: TextureDraw.Type

    doCoreIntParam: TextureDraw.Type

    DrawModel: TextureDraw.Type

    DrawParticles: TextureDraw.Type

    DrawPuddles: TextureDraw.Type

    DrawSkyBox: TextureDraw.Type

    drawTerrain: TextureDraw.Type

    DrawWater: TextureDraw.Type

    glAlphaFunc: TextureDraw.Type

    glBind: TextureDraw.Type

    glBlendEquation: TextureDraw.Type

    glBlendFunc: TextureDraw.Type

    glBlendFuncSeparate: TextureDraw.Type

    glBuffer: TextureDraw.Type

    glClear: TextureDraw.Type

    glClearColor: TextureDraw.Type

    glColorMask: TextureDraw.Type

    glDepthMask: TextureDraw.Type

    glDisable: TextureDraw.Type

    glDoEndFrame: TextureDraw.Type

    glDoEndFrameFx: TextureDraw.Type

    glDoStartFrame: TextureDraw.Type

    glDoStartFrameFx: TextureDraw.Type

    glDoStartFrameText: TextureDraw.Type

    glDraw: TextureDraw.Type

    glEnable: TextureDraw.Type

    glGenerateMipMaps: TextureDraw.Type

    glIgnoreStyles: TextureDraw.Type

    glLoadIdentity: TextureDraw.Type

    glStencilFunc: TextureDraw.Type

    glStencilMask: TextureDraw.Type

    glStencilOp: TextureDraw.Type

    glTexParameteri: TextureDraw.Type

    glViewport: TextureDraw.Type

    ShaderUpdate: TextureDraw.Type

    StartShader: TextureDraw.Type

    @staticmethod
    def valueOf(arg0: str) -> TextureDraw.Type: ...

    @staticmethod
    def values() -> list[TextureDraw.Type]: ...

  class GenericDrawer:

    def postRender(self) -> None: ...

    def render(self) -> None: ...

    def __init__(self): ...


class TextureFBO:

  def destroy(self) -> None: ...

  def destroyLeaveTexture(self) -> None: ...

  def endDrawing(self) -> None: ...

  def getBufferId(self) -> int: ...

  def getHeight(self) -> int: ...

  def getTexture(self) -> ITexture: ...

  def getWidth(self) -> int: ...

  def isDestroyed(self) -> bool: ...

  def releaseTexture(self) -> None: ...

  def setTexture(self, tex3: Texture) -> None: ...

  @overload
  def startDrawing(self) -> None: ...

  @overload
  def startDrawing(self, clear: bool, clearToAlphaZero: bool) -> None: ...

  def swapTexture(self, newTex: ITexture) -> None: ...

  @staticmethod
  def checkFBOSupport() -> bool: ...

  @staticmethod
  def getCurrentID() -> int: ...

  @staticmethod
  def getFuncs() -> IGLFramebufferObject: ...

  @staticmethod
  def reset() -> None: ...

  @overload
  def __init__(self, destination: ITexture): ...
  @overload
  def __init__(self, destination: ITexture, bUseStencil: bool): ...


class TextureFlags:

  CLAMP_TO_EDGE: int

  COMPRESS: int

  CREATE_MASK: int

  FBO: int

  FILTER_MAG_NEAREST: int

  FILTER_MIN_NEAREST: int

  LIMIT_TEXTURE_SIZE_1: int

  LIMIT_TEXTURE_SIZE_2: int

  MIPMAPS: int

  NONE: int

  def __init__(self): ...


class TextureID(Asset):

  ASSET_TYPE: AssetType

  bUseCompression: bool

  bUseCompressionOption: bool

  deleteTextureIDS: IntBuffer

  totalGraphicMemory: int

  totalMemUsed: float

  UseFiltering: bool

  def bind(self) -> bool: ...

  def bindalways(self) -> bool: ...

  @overload
  def destroy(self) -> None: ...

  @overload
  def destroy(self) -> None: ...

  def freeMemory(self) -> None: ...

  def getData(self) -> WrappedBuffer: ...

  def getID(self) -> int: ...

  def getImageData(self) -> ImageData: ...

  def getPathFileName(self) -> str: ...

  def getType(self) -> AssetType: ...

  def hasMipMaps(self) -> bool: ...

  @overload
  def isDestroyed(self) -> bool: ...

  @overload
  def isDestroyed(self) -> bool: ...

  def isSolid(self) -> bool: ...

  def setAssetParams(self, params: AssetManager.AssetParams) -> None: ...

  def setData(self, bdata: ByteBuffer) -> None: ...

  def setImageData(self, data: ImageData) -> None: ...

  def setMagFilter(self, filter: int) -> None: ...

  def setMinFilter(self, filter: int) -> None: ...

  @staticmethod
  def createSteamAvatar(steamID: int) -> TextureID: ...

  @overload
  def __init__(self, path: str):
    self.assetparams: TextureID.TextureIDAssetParams

  @overload
  def __init__(self, image: ImageData): ...
  @overload
  def __init__(self, pcx: str, palette: list[int]): ...
  @overload
  def __init__(self, pcx: str, palette: str): ...
  @overload
  def __init__(self, width: int, height: int, flags: int): ...
  @overload
  def __init__(self, b: BufferedInputStream, path: str, bDoMask: bool): ...
  @overload
  def __init__(self, path: AssetPath, manager: AssetManager, params: TextureID.TextureIDAssetParams): ...
  @overload
  def __init__(self, b: BufferedInputStream, path: str, bDoMask: bool, format: Texture.PZFileformat): ...
  @overload
  def __init__(self, path: str, red: int, green: int, blue: int): ...

  class TextureIDAssetParams(AssetManager.AssetParams):

    def __init__(self): ...


class TextureIDAssetManager(AssetManager):

  instance: TextureIDAssetManager

  def waitFileTask(self) -> None: ...

  def __init__(self): ...


class TextureNameAlreadyInUseException(RuntimeException):

  def __init__(self, name: str): ...


class TextureNotFoundException(RuntimeException):

  def __init__(self, name: str): ...


class TexturePackPage:

  bIgnoreWorldItemTextures: bool

  chl1: int

  chl2: int

  chl3: int

  chl4: int

  FoundTextures: HashMap[str, Stack[str]]

  subTextureMap: HashMap[str, Texture]

  subTextureMap2: HashMap[str, Texture]

  tempFilenameCheck: ArrayList[str]

  TempSubTextureInfo: ArrayList[TexturePackPage.SubTextureInfo]

  texturePackPageMap: HashMap[str, TexturePackPage]

  TexturePackPageNameMap: HashMap[str, str]

  def loadFromPackFile(self, input: BufferedInputStream) -> None: ...

  def loadFromPackFileDDS(self, input: BufferedInputStream) -> None: ...

  @staticmethod
  def LoadDir(path: str) -> None: ...

  @staticmethod
  def ReadString(input: InputStream) -> str: ...

  @staticmethod
  def getTexture(tex: str) -> Texture: ...

  @staticmethod
  @overload
  def readInt(__in__: InputStream) -> int: ...

  @staticmethod
  @overload
  def readInt(__in__: ByteBuffer) -> int: ...

  @staticmethod
  def readIntByte(__in__: InputStream) -> int: ...

  @staticmethod
  def searchFolders(fo: File) -> None: ...

  def __init__(self):
    self.subtextures: HashMap[str, Texture]
    self.tex: Texture

  class SubTextureInfo:

    def __init__(self, x: int, y: int, w: int, h: int, ox: int, oy: int, fx: int, fy: int, name: str):
      self.fx: int
      self.fy: int
      self.h: int
      self.name: str
      self.ox: int
      self.oy: int
      self.w: int
      self.x: int
      self.y: int

