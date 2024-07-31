from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from gnu.trove.map.hash import TIntObjectHashMap
from java.io import DataInputStream, DataOutputStream
from java.util import HashMap, ArrayList
from java.util.function import Consumer
from org.joml import Vector3f
from zombie.core import Color
from zombie.core.opengl import Shader, ShaderProgram
from zombie.core.properties import PropertyContainer
from zombie.core.skinnedmodel import ModelManager
from zombie.core.textures import TextureDraw, Texture, ColorInfo, TextureFBO
from zombie.interfaces import ITexture
from zombie.iso import IsoDirections, IsoObject
from zombie.iso.SpriteDetails import IsoObjectType
from zombie.iso.weather import ClimateManager
from zombie.popman import ObjectPool

class CorpseFlies:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def render(squareX: int, squareY: int, squareZ: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...


class IsoAnim:

  GlobalAnimMap: HashMap[str, IsoAnim]

  def LoadFrames(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  @overload
  def LoadFramesBitRepeatFrame(self, ObjectName: str, AnimName: str, RepeatFrame: int) -> None: ...

  @overload
  def LoadFramesBitRepeatFrame(self, ObjectName: str, Variant: str, AnimName: str, RepeatFrame: int, pal: str) -> None: ...

  @overload
  def LoadFramesBits(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  @overload
  def LoadFramesBits(self, ObjectName: str, Variant: str, AnimName: str, nFrames: int) -> None: ...

  @overload
  def LoadFramesBits(self, ObjectName: str, Variant: str, AnimName: str, nFrames: int, pal: str) -> None: ...

  def LoadFramesPageSimple(self, NObjectName: str, SObjectName: str, EObjectName: str, WObjectName: str) -> None: ...

  def LoadFramesPcx(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  def LoadFramesReverseAltName(self, ObjectName: str, AnimName: str, AltName: str, nFrames: int) -> None: ...

  def LoadFramesUseOtherFrame(self, ObjectName: str, Variant: str, AnimName: str, OtherAnimName: str, nOtherFrameFrame: int, pal: str) -> None: ...

  @staticmethod
  def DisposeAll() -> None: ...

  def __init__(self):
    self.finishunloopedonframe: int
    self.framedelay: int
    self.frames: ArrayList[IsoDirectionFrame]
    self.framesarray: list[IsoDirectionFrame]
    self.id: int
    self.lastframe: int
    self.name: str


class IsoCursor:

  def render(self, playerIndex: int) -> None: ...

  @staticmethod
  def getInstance() -> IsoCursor: ...

  class IsoCursorShader(Shader):

    @overload
    def accept(self, arg0: object) -> None: ...

    @overload
    def accept(self, arg0: object) -> None: ...

    @overload
    def accept(self, arg0: TextureDraw) -> None: ...

    def andThen(self, arg0: Consumer[T]) -> Consumer[T]: ...

    def startMainThread(self, arg0: TextureDraw, arg1: int) -> None: ...

    def startRenderThread(self, arg0: TextureDraw) -> None: ...


class IsoDirectionFrame:

  def SetAllDirections(self, tex: Texture) -> None: ...

  def SetDirection(self, tex: Texture, dir: IsoDirections) -> None: ...

  def getTexture(self, dir: IsoDirections) -> Texture: ...

  def render(self, sx: float, sy: float, dir: IsoDirections, info: ColorInfo, Flip: bool, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def renderexplicit(self, sx: int, sy: int, dir: IsoDirections, scale: float) -> None: ...

  @overload
  def renderexplicit(self, sx: int, sy: int, dir: IsoDirections, scale: float, color: ColorInfo) -> None: ...

  @overload
  def __init__(self):
    self.directions: list[Texture]

  @overload
  def __init__(self, tex: Texture): ...
  @overload
  def __init__(self, n: Texture, s: Texture, e: Texture, w: Texture): ...
  @overload
  def __init__(self, nw: Texture, n: Texture, ne: Texture, e: Texture, se: Texture): ...
  @overload
  def __init__(self, n: Texture, nw: Texture, w: Texture, sw: Texture, s: Texture, se: Texture, e: Texture, ne: Texture): ...


class IsoSprite:

  alphaStep: float

  globalOffsetX: float

  globalOffsetY: float

  maxCount: int

  RL_DEFAULT: int

  RL_FLOOR: int

  def AddProperties(self, sprite: IsoSprite) -> None: ...

  def CacheAnims(self, key: str) -> None: ...

  def ChangeTintMod(self, NewTintMod: ColorInfo) -> None: ...

  def Dispose(self) -> None: ...

  def LoadCache(self, string: str) -> None: ...

  def LoadFrameExplicit(self, ObjectName: str) -> Texture: ...

  def LoadFrames(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  def LoadFramesNoDirPage(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  def LoadFramesNoDirPageDirect(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  def LoadFramesNoDirPageSimple(self, ObjectName: str) -> None: ...

  def LoadFramesPageSimple(self, NObjectName: str, SObjectName: str, EObjectName: str, WObjectName: str) -> None: ...

  def LoadFramesPcx(self, ObjectName: str, AnimName: str, nFrames: int) -> None: ...

  def LoadFramesReverseAltName(self, ObjectName: str, AnimName: str, AltName: str, nFrames: int) -> None: ...

  @overload
  def PlayAnim(self, name: str) -> None: ...

  @overload
  def PlayAnim(self, anim: IsoAnim) -> None: ...

  def PlayAnimUnlooped(self, name: str) -> None: ...

  def RenderGhostTile(self, x: int, y: int, z: int) -> None: ...

  @overload
  def RenderGhostTileColor(self, x: int, y: int, z: int, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def RenderGhostTileColor(self, x: int, y: int, z: int, offsetX: float, offsetY: float, r: float, g: float, b: float, a: float) -> None: ...

  def RenderGhostTileRed(self, x: int, y: int, z: int) -> None: ...

  def ReplaceCurrentAnimFrames(self, ObjectName: str) -> None: ...

  def getID(self) -> int: ...

  def getMaskClickedY(self, dir: IsoDirections, x: int, y: int, flip: bool) -> float: ...

  def getName(self) -> str: ...

  def getParentObjectName(self) -> str: ...

  def getProperties(self) -> PropertyContainer: ...

  def getSheetGridIdFromName(self) -> int: ...

  def getSpriteGrid(self) -> IsoSpriteGrid: ...

  def getTextureForCurrentFrame(self, dir: IsoDirections) -> Texture: ...

  def getTextureForFrame(self, frame: int, dir: IsoDirections) -> Texture: ...

  def getTintMod(self) -> ColorInfo: ...

  def getType(self) -> IsoObjectType: ...

  def hasActiveModel(self) -> bool: ...

  @overload
  def isMaskClicked(self, dir: IsoDirections, x: int, y: int) -> bool: ...

  @overload
  def isMaskClicked(self, dir: IsoDirections, x: int, y: int, flip: bool) -> bool: ...

  def isMoveWithWind(self) -> bool: ...

  def load(self, input: DataInputStream) -> None: ...

  def newInstance(self) -> IsoSpriteInstance: ...

  @overload
  def render(self, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, info2: ColorInfo, bDoRenderPrep: bool) -> None: ...

  @overload
  def render(self, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, info2: ColorInfo, bDoRenderPrep: bool, texdModifier: Consumer[TextureDraw]) -> None: ...

  @overload
  def render(self, inst: IsoSpriteInstance, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, info2: ColorInfo, bDoRenderPrep: bool) -> None: ...

  @overload
  def render(self, inst: IsoSpriteInstance, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, info2: ColorInfo, bDoRenderPrep: bool, texdModifier: Consumer[TextureDraw]) -> None: ...

  def renderActiveModel(self) -> None: ...

  def renderBloodSplat(self, x: float, y: float, z: float, info2: ColorInfo) -> None: ...

  def renderCurrentAnim(self, inst: IsoSpriteInstance, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, col: ColorInfo, bDoRenderPrep: bool, texdModifier: Consumer[TextureDraw]) -> None: ...

  def renderObjectPicker(self, arg0: IsoSpriteInstance, obj: IsoObject, dir: IsoDirections) -> None: ...

  def renderVehicle(self, inst: IsoSpriteInstance, obj: IsoObject, x: float, y: float, z: float, offsetX: float, offsetY: float, info2: ColorInfo, bDoRenderPrep: bool) -> None: ...

  def save(self, output: DataOutputStream) -> None: ...

  def setAnimate(self, animate: bool) -> None: ...

  def setFromCache(self, objectName: str, animName: str, numFrames: int) -> IsoSprite: ...

  def setHideForWaterRender(self) -> None: ...

  def setName(self, string: str) -> None: ...

  def setParentObjectName(self, val: str) -> None: ...

  def setSpriteGrid(self, sGrid: IsoSpriteGrid) -> None: ...

  def setTintMod(self, info: ColorInfo) -> None: ...

  def setType(self, ntype: IsoObjectType) -> None: ...

  @overload
  def update(self) -> None: ...

  @overload
  def update(self, arg0: IsoSpriteInstance) -> None: ...

  @staticmethod
  def CreateSprite(manager: IsoSpriteManager) -> IsoSprite: ...

  @staticmethod
  def CreateSpriteUsingCache(objectName: str, animName: str, numFrames: int) -> IsoSprite: ...

  @staticmethod
  def DisposeAll() -> None: ...

  @staticmethod
  def HasCache(string: str) -> bool: ...

  @staticmethod
  @overload
  def getSprite(manager: IsoSpriteManager, id: int) -> IsoSprite: ...

  @staticmethod
  @overload
  def getSprite(manager: IsoSpriteManager, name: str, offset: int) -> IsoSprite: ...

  @staticmethod
  @overload
  def getSprite(manager: IsoSpriteManager, spr: IsoSprite, offset: int) -> IsoSprite: ...

  @staticmethod
  def setSpriteID(manager: IsoSpriteManager, id: int, spr: IsoSprite) -> None: ...

  @overload
  def __init__(self):
    self.alwaysdraw: bool

    self.animate: bool

    self.animmap: HashMap[str, IsoAnim]

    self.animstack: ArrayList[IsoAnim]

    self.attachedfloor: bool

    self.burnttile: str

    self.canberemoved: bool

    self.currentanim: IsoAnim

    self.cutn: bool

    self.cutw: bool

    # self.def: IsoSpriteInstance

    self.deletewhenfinished: bool

    self.firerequirement: int

    self.forceambient: bool

    self.forcerender: bool

    self.id: int

    self.invisible: bool

    self.isbush: bool

    self.loop: bool

    self.modelslot: ModelManager.ModelSlot

    self.movewithwind: bool

    self.name: str

    self.properties: PropertyContainer

    self.renderlayer: int

    self.soffx: int

    self.soffy: int

    self.solid: bool

    self.solidfloor: bool

    self.solidtrans: bool

    self.tilesheetindex: int

    self.tintmod: ColorInfo

    self.treataswallorder: bool

    self.windtype: int

  @overload
  def __init__(self, manager: IsoSpriteManager): ...

  class l_renderCurrentAnim: ...


class IsoSpriteGrid:

  def getAnchorSprite(self) -> IsoSprite: ...

  def getHeight(self) -> int: ...

  def getSprite(self, x: int, y: int) -> IsoSprite: ...

  def getSpriteCount(self) -> int: ...

  def getSpriteFromIndex(self, index: int) -> IsoSprite: ...

  def getSpriteGridPosX(self, sprite: IsoSprite) -> int: ...

  def getSpriteGridPosY(self, sprite: IsoSprite) -> int: ...

  def getSpriteIndex(self, sprite: IsoSprite) -> int: ...

  def getSprites(self) -> list[IsoSprite]: ...

  def getWidth(self) -> int: ...

  def setSprite(self, x: int, y: int, sprite: IsoSprite) -> None: ...

  def validate(self) -> bool: ...

  def __init__(self, w: int, h: int): ...


class IsoSpriteInstance:

  pool: ObjectPool[IsoSpriteInstance]

  def Dispose(self) -> None: ...

  def RenderGhostTileColor(self, x: int, y: int, z: int, r: float, g: float, b: float, a: float) -> None: ...

  def SetAlpha(self, f: float) -> None: ...

  def SetTargetAlpha(self, targetAlpha: float) -> None: ...

  def getAlpha(self) -> float: ...

  def getFrame(self) -> float: ...

  def getID(self) -> int: ...

  def getName(self) -> str: ...

  def getParentSprite(self) -> IsoSprite: ...

  def getScaleX(self) -> float: ...

  def getScaleY(self) -> float: ...

  def getTargetAlpha(self) -> float: ...

  def getTintB(self) -> float: ...

  def getTintG(self) -> float: ...

  def getTintR(self) -> float: ...

  def isCopyTargetAlpha(self) -> bool: ...

  def isFinished(self) -> bool: ...

  def isMultiplyObjectAlpha(self) -> bool: ...

  def render(self, obj: IsoObject, x: float, y: float, z: float, dir: IsoDirections, offsetX: float, offsetY: float, info2: ColorInfo) -> None: ...

  def scaleAspect(self, texW: float, texH: float, width: float, height: float) -> None: ...

  def setFrameSpeedPerFrame(self, perSecond: float) -> None: ...

  def setScale(self, scaleX: float, scaleY: float) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def add(isoSpriteInstance: IsoSpriteInstance) -> None: ...

  @staticmethod
  def get(spr: IsoSprite) -> IsoSpriteInstance: ...

  @overload
  def __init__(self):
    self.alpha: float

    self.animframeincrease: float

    self.bcopytargetalpha: bool

    self.bmultiplyobjectalpha: bool

    self.finished: bool

    self.flip: bool

    self.frame: float

    self.looped: bool

    self.nextframe: bool

    self.offx: float

    self.offy: float

    self.offz: float

    self.parentsprite: IsoSprite

    self.scalex: float

    self.scaley: float

    self.targetalpha: float

    self.tintb: float

    self.tintg: float

    self.tintr: float

  @overload
  def __init__(self, spr: IsoSprite): ...


class IsoSpriteManager:

  instance: IsoSpriteManager

  @overload
  def AddSprite(self, tex: str) -> IsoSprite: ...

  @overload
  def AddSprite(self, tex: str, ID: int) -> IsoSprite: ...

  def Dispose(self) -> None: ...

  @overload
  def getOrAddSpriteCache(self, tex: str) -> IsoSprite: ...

  @overload
  def getOrAddSpriteCache(self, tex: str, col: Color) -> IsoSprite: ...

  @overload
  def getSprite(self, gid: int) -> IsoSprite: ...

  @overload
  def getSprite(self, gid: str) -> IsoSprite: ...

  def __init__(self):
    self.intmap: TIntObjectHashMap[IsoSprite]
    self.namedmap: HashMap[str, IsoSprite]


class SkyBox(IsoObject):

  def draw(self) -> None: ...

  def getShaderCloudCount(self) -> float: ...

  def getShaderCloudLight(self) -> float: ...

  def getShaderCloudSize(self) -> float: ...

  def getShaderFog(self) -> float: ...

  def getShaderSkyHColour(self) -> Color: ...

  def getShaderSkyLColour(self) -> Color: ...

  def getShaderStars(self) -> float: ...

  def getShaderSunColor(self) -> Color: ...

  def getShaderSunLight(self) -> Vector3f: ...

  def getShaderTime(self) -> int: ...

  def getShaderWind(self) -> Vector3f: ...

  def getTextureCurrent(self) -> ITexture: ...

  def getTextureFBOPrev(self) -> TextureFBO: ...

  def getTexturePrev(self) -> ITexture: ...

  def getTextureShift(self) -> float: ...

  def render(self) -> None: ...

  def swapTextureFBO(self) -> None: ...

  def update(self, cm: ClimateManager) -> None: ...

  @staticmethod
  def getInstance() -> SkyBox: ...

  def __init__(self):
    # self.def: IsoSpriteInstance
    self.effect: Shader


class SkyBoxShader(Shader):

  def onCompileSuccess(self, arg0: ShaderProgram) -> None: ...

  def startRenderThread(self, arg0: TextureDraw) -> None: ...

  def __init__(self, arg0: str): ...

