from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import PrintStream
from java.lang import RuntimeException, Throwable, Runnable, Thread, Integer, Enum
from java.nio import ShortBuffer, FloatBuffer
from java.util import HashMap
from java.util.function import BooleanSupplier
from org.joml import Matrix4f
from org.lwjgl.util.vector import Matrix4f
from org.lwjglx.opengl import OpenGLException
from zombie.core import Color
from zombie.core.skinnedmodel import ModelCamera
from zombie.core.textures import TextureDraw, Texture
from zombie.iso import Vector2, Vector3
from zombie.iso.weather import ClimateColorInfo
from zombie.util.lambda import Invokers

T = TypeVar('T', default=Any)
T1 = TypeVar('T1', default=Any)
T2 = TypeVar('T2', default=Any)
T3 = TypeVar('T3', default=Any)
T4 = TypeVar('T4', default=Any)

class CharacterModelCamera(ModelCamera):

  instance: CharacterModelCamera

  def Begin(self) -> None: ...

  def End(self) -> None: ...

  def __init__(self): ...


class GLState:

  AlphaFunc: GLState.CAlphaFunc

  AlphaTest: GLState.CAlphaTest

  BlendFunc: GLState.CBlendFunc

  BlendFuncSeparate: GLState.CBlendFuncSeparate

  ColorMask: GLState.CColorMask

  StencilFunc: GLState.CStencilFunc

  StencilMask: GLState.CStencilMask

  StencilOp: GLState.CStencilOp

  StencilTest: GLState.CStencilTest

  @staticmethod
  def startFrame() -> None: ...

  def __init__(self): ...

  class CAlphaFunc(GLState.BaseIntFloat):

    def __init__(self): ...

  class CAlphaTest(GLState.BaseBoolean):

    def __init__(self): ...

  class CBlendFunc(GLState.Base2Ints):

    def __init__(self): ...

  class CBlendFuncSeparate(GLState.Base4Ints):

    def __init__(self): ...

  class CColorMask(GLState.Base4Booleans):

    def __init__(self): ...

  class CStencilFunc(GLState.Base3Ints):

    def __init__(self): ...

  class CStencilMask(GLState.BaseInt):

    def __init__(self): ...

  class CStencilOp(GLState.Base3Ints):

    def __init__(self): ...

  class CStencilTest(GLState.BaseBoolean):

    def __init__(self): ...

  class Base4Ints(IOpenGLState):

    def __init__(self): ...

  class Base3Ints(IOpenGLState):

    def __init__(self): ...

  class Base2Ints(IOpenGLState):

    def __init__(self): ...

  class BaseInt(IOpenGLState):

    def __init__(self): ...

  class BaseIntFloat(IOpenGLState):

    def __init__(self): ...

  class Base4Booleans(IOpenGLState):

    def __init__(self): ...

  class BaseBoolean(IOpenGLState):

    def __init__(self): ...

  class CIntFloatValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, a: int, b: float) -> GLState.CIntFloatValue: ...

    def __init__(self): ...

  class C4IntsValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, a: int, b: int, c: int, d: int) -> GLState.C4IntsValue: ...

    def __init__(self): ...

  class C3IntsValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, a: int, b: int, c: int) -> GLState.C3IntsValue: ...

    def __init__(self): ...

  class C2IntsValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, a: int, b: int) -> GLState.C2IntsValue: ...

    def __init__(self): ...

  class CIntValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, a: int) -> GLState.CIntValue: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    def __init__(self): ...

  class C4BooleansValue:

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, a: bool, b: bool, c: bool, d: bool) -> GLState.C4BooleansValue: ...

    def __init__(self): ...

  class CBooleanValue:

    FALSE: GLState.CBooleanValue

    TRUE: GLState.CBooleanValue

    def equals(self, other: object) -> bool: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...

    @overload
    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...


class IModelCamera:

  def Begin(self) -> None: ...

  def End(self) -> None: ...


class IOpenGLState[T]:

  def set(self, arg0: IOpenGLState.Value) -> None: ...

  def setDirty(self) -> None: ...

  def __init__(self): ...

  class Value:

    def set(self, other: IOpenGLState.Value) -> IOpenGLState.Value: ...


class IShaderProgramListener:

  def callback(self, sender: ShaderProgram) -> None: ...


class PZGLUtil:

  @staticmethod
  def checkGLError(stackTrace: bool) -> bool: ...

  @staticmethod
  def checkGLErrorThrow(arg0: str, arg1: list[object]) -> None: ...

  @staticmethod
  @overload
  def loadMatrix(matrix: Matrix4f) -> None: ...

  @staticmethod
  @overload
  def loadMatrix(mode: int, matrix: Matrix4f) -> None: ...

  @staticmethod
  @overload
  def multMatrix(matrix: Matrix4f) -> None: ...

  @staticmethod
  @overload
  def multMatrix(mode: int, matrix: Matrix4f) -> None: ...

  @staticmethod
  def popMatrix(mode: int) -> None: ...

  @staticmethod
  def printGLState(out: PrintStream) -> None: ...

  @staticmethod
  def pushAndLoadMatrix(mode: int, matrix: Matrix4f) -> None: ...

  @staticmethod
  def pushAndMultMatrix(mode: int, matrix: Matrix4f) -> None: ...

  def __init__(self): ...


class ParticleModelCamera(ModelCamera):

  def Begin(self) -> None: ...

  def End(self) -> None: ...

  def __init__(self): ...


class RenderContextQueueException(RuntimeException):

  def __init__(self, cause: Throwable): ...


class RenderContextQueueItem:

  def getThrown(self) -> Throwable: ...

  def invoke(self) -> None: ...

  def isFinished(self) -> bool: ...

  def isWaiting(self) -> bool: ...

  def notifyWaitingListeners(self) -> None: ...

  def setWaiting(self) -> None: ...

  def waitUntilFinished(self, waitCallback: BooleanSupplier) -> None: ...

  @staticmethod
  def alloc(runnable: Runnable) -> RenderContextQueueItem: ...


class RenderSettings:

  def applyRenderSettings(self, playerIndex: int) -> None: ...

  def getAmbientForPlayer(self, plrIndex: int) -> float: ...

  def getMaskClearColorForPlayer(self, plrIndex: int) -> Color: ...

  def getPlayerSettings(self, playerIndex: int) -> RenderSettings.PlayerRenderSettings: ...

  def legacyPostRender(self, playerIndex: int) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def getInstance() -> RenderSettings: ...

  def __init__(self): ...

  class PlayerRenderSettings:

    def getAmbient(self) -> float: ...

    def getBlendColor(self) -> Color: ...

    def getBlendIntensity(self) -> float: ...

    def getBmod(self) -> float: ...

    def getDarkness(self) -> float: ...

    def getDesaturation(self) -> float: ...

    def getFogMod(self) -> float: ...

    def getGmod(self) -> float: ...

    def getMaskClearColor(self) -> Color: ...

    def getNight(self) -> float: ...

    def getRmod(self) -> float: ...

    def getSM_Alpha(self) -> float: ...

    def getSM_Radius(self) -> float: ...

    def getViewDistance(self) -> float: ...

    def isApplyNightVisionGoggles(self) -> bool: ...

    def isExterior(self) -> bool: ...

    def __init__(self):
      self.cm_ambient: float
      self.cm_daylightstrength: float
      self.cm_desaturation: float
      self.cm_fogintensity: float
      self.cm_globallight: ClimateColorInfo
      self.cm_globallightintensity: float
      self.cm_nightstrength: float
      self.cm_viewdistance: float


class RenderThread:

  m_contextLock: object

  RenderThread: Thread

  @staticmethod
  def Ready() -> None: ...

  @staticmethod
  def getDisplayHeight() -> int: ...

  @staticmethod
  def getDisplayWidth() -> int: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def initServerGUI() -> None: ...

  @staticmethod
  @overload
  def invokeOnRenderContext(toInvoke: Runnable) -> None: ...

  @staticmethod
  @overload
  def invokeOnRenderContext(arg0: object, arg1: Invokers.Params1.ICallback) -> None: ...

  @staticmethod
  @overload
  def invokeOnRenderContext(arg0: object, arg1: object, arg2: Invokers.Params2.ICallback) -> None: ...

  @staticmethod
  @overload
  def invokeOnRenderContext(arg0: object, arg1: object, arg2: object, arg3: Invokers.Params3.ICallback) -> None: ...

  @staticmethod
  @overload
  def invokeOnRenderContext(arg0: object, arg1: object, arg2: object, arg3: object, arg4: Invokers.Params4.ICallback) -> None: ...

  @staticmethod
  def isCloseRequested() -> bool: ...

  @staticmethod
  def isCursorVisible() -> bool: ...

  @staticmethod
  def isRunning() -> bool: ...

  @staticmethod
  def isWaitForRenderState() -> bool: ...

  @staticmethod
  @overload
  def logGLException(glEx: OpenGLException) -> None: ...

  @staticmethod
  @overload
  def logGLException(glEx: OpenGLException, stackTrace: bool) -> None: ...

  @staticmethod
  def onGameThreadExited() -> None: ...

  @staticmethod
  @overload
  def queueInvokeOnRenderContext(runnable: Runnable) -> None: ...

  @staticmethod
  @overload
  def queueInvokeOnRenderContext(queueItem: RenderContextQueueItem) -> None: ...

  @staticmethod
  def renderLoop() -> None: ...

  @staticmethod
  def setWaitForRenderState(wait: bool) -> None: ...

  @staticmethod
  def shutdown() -> None: ...

  @staticmethod
  def startRendering() -> None: ...

  def __init__(self): ...

  class s_performance: ...


class Shader:

  ShaderMap: HashMap[Integer, Shader]

  def End(self) -> None: ...

  def Start(self) -> None: ...

  @overload
  def callback(self, sender: ShaderProgram) -> None: ...

  @overload
  def callback(self, sender: ShaderProgram) -> None: ...

  def destroy(self) -> None: ...

  def getID(self) -> int: ...

  def getProgram(self) -> ShaderProgram: ...

  def isCompiled(self) -> bool: ...

  def postRender(self, texd: TextureDraw) -> None: ...

  def setTexture(self, tex: Texture) -> None: ...

  def startMainThread(self, texd: TextureDraw, playerIndex: int) -> None: ...

  def startRenderThread(self, tex: TextureDraw) -> None: ...

  def __init__(self, name: str):
    self.height: int
    self.name: str
    self.tex: Texture
    self.width: int


class ShaderProgram:

  def End(self) -> None: ...

  def Start(self) -> None: ...

  def addCompileListener(self, listener: IShaderProgramListener) -> None: ...

  def addShader(self, fileName: str, unitType: ShaderUnit.Type) -> ShaderUnit: ...

  def compile(self) -> None: ...

  def destroy(self) -> None: ...

  def getName(self) -> str: ...

  def getShaderID(self) -> int: ...

  @overload
  def getUniform(self, loc: str, type: int) -> ShaderProgram.Uniform: ...

  @overload
  def getUniform(self, loc: str, type: int, bWarn: bool) -> ShaderProgram.Uniform: ...

  def isCompiled(self) -> bool: ...

  def removeCompileListener(self, listener: IShaderProgramListener) -> None: ...

  def setSamplerUnit(self, loc: str, textureUnit: int) -> None: ...

  @overload
  def setValue(self, loc: str, val: float) -> None: ...

  @overload
  def setValue(self, loc: str, val: int) -> None: ...

  @overload
  def setValue(self, loc: str, matrix4f: Matrix4f) -> None: ...

  @overload
  def setValue(self, loc: str, val: Vector2) -> None: ...

  @overload
  def setValue(self, loc: str, val: Vector3) -> None: ...

  @overload
  def setValue(self, loc: str, tex: Texture, samplerUnit: int) -> None: ...

  def setValueColor(self, loc: str, rgba: int) -> None: ...

  def setValueColorRGB(self, loc: str, rgb: int) -> None: ...

  @overload
  def setVector2(self, id: int, x: float, y: float) -> None: ...

  @overload
  def setVector2(self, loc: str, val_x: float, val_y: float) -> None: ...

  @overload
  def setVector3(self, id: int, x: float, y: float, z: float) -> None: ...

  @overload
  def setVector3(self, loc: str, val_x: float, val_y: float, val_z: float) -> None: ...

  @overload
  def setVector4(self, id: int, x: float, y: float, z: float, w: float) -> None: ...

  @overload
  def setVector4(self, loc: str, val_x: float, val_y: float, val_z: float, val_w: float) -> None: ...

  @staticmethod
  def createFragShader(fileName: str) -> int: ...

  @staticmethod
  def createShaderProgram(name: str, isStatic: bool, compile: bool) -> ShaderProgram: ...

  @staticmethod
  def createVertShader(fileName: str) -> int: ...

  @staticmethod
  def getLogInfo(obj: int) -> str: ...

  @staticmethod
  def printLogInfo(obj: int) -> None: ...

  class Uniform:

    def __init__(self):
      self.loc: int
      self.name: str
      self.sampler: int
      self.size: int
      self.type: int

  class L_setValue: ...


class ShaderUnit:

  def attach(self) -> bool: ...

  def compile(self) -> bool: ...

  def destroy(self) -> None: ...

  def getFileName(self) -> str: ...

  def getGLID(self) -> int: ...

  def getParentShaderProgramGLID(self) -> int: ...

  def isCompiled(self) -> bool: ...

  def __init__(self, parent: ShaderProgram, fileName: str, unitType: ShaderUnit.Type): ...

  class Type(Enum):

    Frag: ShaderUnit.Type

    Vert: ShaderUnit.Type

    @staticmethod
    def valueOf(arg0: str) -> ShaderUnit.Type: ...

    @staticmethod
    def values() -> list[ShaderUnit.Type]: ...


class SharedVertexBufferObjects:

  def next(self) -> None: ...

  def startFrame(self) -> None: ...

  def unmap(self) -> None: ...

  def __init__(self, BYTES_PER_VERTEX: int):
    self.buffersizevertices: int
    self.indices: ShortBuffer
    self.vertices: FloatBuffer


class SmartShader:

  def End(self) -> None: ...

  def Start(self) -> None: ...

  @overload
  def setValue(self, loc: str, val: float) -> None: ...

  @overload
  def setValue(self, loc: str, val: int) -> None: ...

  @overload
  def setValue(self, loc: str, matrix4f: Matrix4f) -> None: ...

  @overload
  def setValue(self, loc: str, val: Vector2) -> None: ...

  @overload
  def setValue(self, loc: str, val: Vector3) -> None: ...

  @overload
  def setValue(self, loc: str, tex: Texture, samplerUnit: int) -> None: ...

  def setVector2f(self, loc: str, f1: float, f2: float) -> None: ...

  def setVector3f(self, loc: str, f1: float, f2: float, f3: float) -> None: ...

  def setVector4f(self, loc: str, f1: float, f2: float, f3: float, f4: float) -> None: ...

  @overload
  def __init__(self, name: str): ...
  @overload
  def __init__(self, name: str, bStatic: bool): ...


class VBOLines:

  def addElement(self, x: float, y: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addLine(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, r: float, g: float, b: float, a: float) -> None: ...

  @overload
  def addLine(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, r0: float, g0: float, b0: float, a0: float, r1: float, g1: float, b1: float, a1: float) -> None: ...

  def addQuad(self, x0: float, y0: float, x1: float, y1: float, z: float, r: float, g: float, b: float, a: float) -> None: ...

  def addTriangle(self, x0: float, y0: float, z0: float, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, a: float) -> None: ...

  def flush(self) -> None: ...

  def reserve(self, numElements: int) -> None: ...

  def setDepthTest(self, enabled: bool) -> None: ...

  def setLineWidth(self, width: float) -> None: ...

  def setMode(self, mode: int) -> None: ...

  def setOffset(self, dx: float, dy: float, dz: float) -> None: ...

  def __init__(self): ...

