from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from fmod.fmod import Audio
from java.awt.image import BufferedImage
from java.io import File
from java.lang import Enum, Thread, Long
from java.nio import ByteBuffer
from java.util import ArrayList
from org.lwjgl.glfw import GLFWImage
from se.krka.kahlua.vm import KahluaTable
from zombie.config import ConfigOption, BooleanConfigOption
from zombie.core import GameVersion, Color
from zombie.core.textures import Texture
from zombie.iso import IsoCell, LosUtil
from zombie.worldMap import UIWorldMap

class AnimationViewerState(GameState):

  instance: AnimationViewerState

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def fromLua0(self, func: str) -> object: ...

  def fromLua1(self, func: str, arg0: object) -> object: ...

  def getBoolean(self, name: str) -> bool: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionByName(self, name: str) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def load(self) -> None: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def save(self) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setTable(self, table: KahluaTable) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def checkInstance() -> AnimationViewerState: ...

  def __init__(self): ...

  class BooleanDebugOption(BooleanConfigOption):

    def __init__(self, arg0: AnimationViewerState, arg1: str, arg2: bool): ...


class AttachmentEditorState(GameState):

  instance: AttachmentEditorState

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def fromLua0(self, func: str) -> object: ...

  def fromLua1(self, func: str, arg0: object) -> object: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def setTable(self, table: KahluaTable) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def checkInstance() -> AttachmentEditorState: ...

  def __init__(self): ...


class ChooseGameInfo:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getAvailableModDetails(modId: str) -> ChooseGameInfo.Mod: ...

  @staticmethod
  def getMapDetails(dir: str) -> ChooseGameInfo.Map: ...

  @staticmethod
  def getModDetails(modId: str) -> ChooseGameInfo.Mod: ...

  @staticmethod
  def readModInfo(modDir: str) -> ChooseGameInfo.Mod: ...

  class Map:

    def getDescription(self) -> str: ...

    def getDirectory(self) -> str: ...

    def getLotDirectories(self) -> ArrayList[str]: ...

    def getThumbnail(self) -> Texture: ...

    def getTitle(self) -> str: ...

    def isFixed2x(self) -> bool: ...

    def setDescription(self, desc: str) -> None: ...

    def setDirectory(self, dir: str) -> None: ...

    def setFixed2x(self, fixed: bool) -> None: ...

    def setThumbnail(self, thumb: Texture) -> None: ...

    def setTitle(self, title: str) -> None: ...

    def __init__(self): ...

  class Mod:

    def addPack(self, name: str, flags: int) -> None: ...

    def addTileDef(self, name: str, fileNumber: int) -> None: ...

    def getDescription(self) -> str: ...

    def getDir(self) -> str: ...

    def getId(self) -> str: ...

    def getName(self) -> str: ...

    def getPacks(self) -> ArrayList[ChooseGameInfo.PackFile]: ...

    def getPoster(self, index: int) -> str: ...

    def getPosterCount(self) -> int: ...

    def getRequire(self) -> ArrayList[str]: ...

    def getTexture(self) -> Texture: ...

    def getTileDefs(self) -> ArrayList[ChooseGameInfo.TileDef]: ...

    def getUrl(self) -> str: ...

    def getVersionMax(self) -> GameVersion: ...

    def getVersionMin(self) -> GameVersion: ...

    def getWorkshopID(self) -> str: ...

    def isAvailable(self) -> bool: ...

    def setAvailable(self, available: bool) -> None: ...

    def setId(self, id: str) -> None: ...

    def setName(self, name: str) -> None: ...

    def setRequire(self, require: ArrayList[str]) -> None: ...

    def setTexture(self, tex: Texture) -> None: ...

    def setUrl(self, url: str) -> None: ...

    def __init__(self, dir: str):
      self.actiongroupsfile: File
      self.animsetsfile: File
      self.animsxfile: File
      self.basefile: File
      self.dir: str
      self.mediafile: File
      self.tex: Texture

  class TileDef:

    def __init__(self, name: str, fileNumber: int):
      self.filenumber: int
      self.name: str

  class PackFile:

    def __init__(self, name: str, flags: int):
      self.flags: int
      self.name: str

  class SpawnOrigin:

    def __init__(self, x: int, y: int, w: int, h: int):
      self.h: int
      self.w: int
      self.x: int
      self.y: int


class ConnectToServerState(GameState):

  instance: ConnectToServerState

  def FromLua(self, button: str) -> None: ...

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def __init__(self, bb: ByteBuffer): ...

  class State(Enum):

    CheckMods: ConnectToServerState.State

    Exit: ConnectToServerState.State

    Finish: ConnectToServerState.State

    ServerWorkshopItemScreen: ConnectToServerState.State

    Start: ConnectToServerState.State

    TestTCP: ConnectToServerState.State

    WorkshopConfirm: ConnectToServerState.State

    WorkshopInit: ConnectToServerState.State

    WorkshopQuery: ConnectToServerState.State

    WorkshopUpdate: ConnectToServerState.State

    @staticmethod
    def valueOf(arg0: str) -> ConnectToServerState.State: ...

    @staticmethod
    def values() -> list[ConnectToServerState.State]: ...

  class WorkshopItem:

    @overload
    def onItemCreated(self, arg0: int, arg1: bool) -> None: ...

    @overload
    def onItemCreated(self, arg0: int, arg1: bool) -> None: ...

    @overload
    def onItemDownloaded(self, arg0: int) -> None: ...

    @overload
    def onItemDownloaded(self, arg0: int) -> None: ...

    @overload
    def onItemNotCreated(self, arg0: int) -> None: ...

    @overload
    def onItemNotCreated(self, arg0: int) -> None: ...

    @overload
    def onItemNotDownloaded(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotDownloaded(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotSubscribed(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotSubscribed(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotUpdated(self, arg0: int) -> None: ...

    @overload
    def onItemNotUpdated(self, arg0: int) -> None: ...

    @overload
    def onItemQueryCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryNotCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryNotCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemSubscribed(self, arg0: int) -> None: ...

    @overload
    def onItemSubscribed(self, arg0: int) -> None: ...

    @overload
    def onItemUpdated(self, arg0: bool) -> None: ...

    @overload
    def onItemUpdated(self, arg0: bool) -> None: ...

  class ItemQuery:

    def isCompleted(self) -> bool: ...

    def isNotCompleted(self) -> bool: ...

    @overload
    def onItemCreated(self, arg0: int, arg1: bool) -> None: ...

    @overload
    def onItemCreated(self, arg0: int, arg1: bool) -> None: ...

    @overload
    def onItemDownloaded(self, arg0: int) -> None: ...

    @overload
    def onItemDownloaded(self, arg0: int) -> None: ...

    @overload
    def onItemNotCreated(self, arg0: int) -> None: ...

    @overload
    def onItemNotCreated(self, arg0: int) -> None: ...

    @overload
    def onItemNotDownloaded(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotDownloaded(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotSubscribed(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotSubscribed(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemNotUpdated(self, arg0: int) -> None: ...

    @overload
    def onItemNotUpdated(self, arg0: int) -> None: ...

    @overload
    def onItemQueryCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryNotCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemQueryNotCompleted(self, arg0: int, arg1: int) -> None: ...

    @overload
    def onItemSubscribed(self, arg0: int) -> None: ...

    @overload
    def onItemSubscribed(self, arg0: int) -> None: ...

    @overload
    def onItemUpdated(self, arg0: bool) -> None: ...

    @overload
    def onItemUpdated(self, arg0: bool) -> None: ...

  class WorkshopItemState(Enum):

    CheckItemState: ConnectToServerState.WorkshopItemState

    DownloadPending: ConnectToServerState.WorkshopItemState

    Fail: ConnectToServerState.WorkshopItemState

    Ready: ConnectToServerState.WorkshopItemState

    SubscribePending: ConnectToServerState.WorkshopItemState

    @staticmethod
    def valueOf(arg0: str) -> ConnectToServerState.WorkshopItemState: ...

    @staticmethod
    def values() -> list[ConnectToServerState.WorkshopItemState]: ...


class DebugChunkState(GameState):

  instance: DebugChunkState

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def fromLua0(self, func: str) -> object: ...

  def fromLua1(self, func: str, arg0: object) -> object: ...

  def fromLua2(self, func: str, arg0: object, arg1: object) -> object: ...

  def getBoolean(self, name: str) -> bool: ...

  def getOptionByIndex(self, index: int) -> ConfigOption: ...

  def getOptionByName(self, name: str) -> ConfigOption: ...

  def getOptionCount(self) -> int: ...

  def lineClearCached(self, cell: IsoCell, x1: int, y1: int, z1: int, x0: int, y0: int, z0: int, bIgnoreDoors: bool) -> LosUtil.TestResults: ...

  def load(self) -> None: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def renderScene(self) -> None: ...

  def save(self) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setTable(self, table: KahluaTable) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def updateScene(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def checkInstance() -> DebugChunkState: ...

  def __init__(self): ...

  class BooleanDebugOption(BooleanConfigOption):

    def __init__(self, arg0: DebugChunkState, arg1: str, arg2: bool): ...

  class FloodFill: ...


class DebugGlobalObjectState(GameState):

  instance: DebugGlobalObjectState

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def fromLua0(self, func: str) -> object: ...

  def fromLua1(self, func: str, arg0: object) -> object: ...

  def fromLua2(self, func: str, arg0: object, arg1: object) -> object: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def renderScene(self) -> None: ...

  def setTable(self, table: KahluaTable) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def updateScene(self) -> GameStateMachine.StateAction: ...

  def __init__(self): ...


class GameLoadingState(GameState):

  bDone: bool

  build23Stop: bool

  convertingFileCount: int

  convertingFileMax: int

  convertingWorld: bool

  GameLoadingString: str

  loader: Thread

  mapDownloadFailed: bool

  newGame: bool

  playerCreated: bool

  playerWrongIP: bool

  unexpectedError: bool

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def redirectState(self) -> GameState: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def Done() -> None: ...

  @staticmethod
  def SendDone() -> None: ...

  def __init__(self):
    self.bforcedone: bool
    self.stage: int
    self.time: float


class GameState:

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def redirectState(self) -> GameState: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def __init__(self): ...


class GameStateMachine:

  def forceNextState(self, state: GameState) -> None: ...

  def render(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self):
    self.current: GameState
    self.firstrun: bool
    self.forcenext: GameState
    self.loop: bool
    self.looptostate: int
    self.stateindex: int
    self.states: ArrayList[GameState]

  class StateAction(Enum):

    Remain: GameStateMachine.StateAction

    @staticmethod
    def valueOf(arg0: str) -> GameStateMachine.StateAction: ...

    @staticmethod
    def values() -> list[GameStateMachine.StateAction]: ...


class IngameState(GameState):

  drawh: float

  draww: float

  GameID: Long

  instance: IngameState

  WaitMul: int

  def UpdateStuff(self) -> None: ...

  def debugFullyStreamedIn(self, squareX: int, squareY: int) -> None: ...

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def redirectState(self) -> GameState: ...

  def reenter(self) -> None: ...

  def render(self) -> None: ...

  def renderframe(self, nPlayer: int) -> None: ...

  def renderframetext(self, nPlayer: int) -> None: ...

  def renderframeui(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def copyDirectory(sourceLocation: File, targetLocation: File) -> None: ...

  @staticmethod
  def copyWorld(src: str, dest: str) -> None: ...

  @staticmethod
  def createWorld(worldName: str) -> None: ...

  @staticmethod
  def invTranslatePointX(x: float, camX: float, zoom: float, offx: float) -> float: ...

  @staticmethod
  def invTranslatePointY(y: float, camY: float, zoom: float, offy: float) -> float: ...

  @staticmethod
  def renderDebugOverhead(cell: IsoCell, drawFloor: int, tilew: int, offx: int, offy: int) -> None: ...

  @staticmethod
  def renderDebugOverhead2(cell: IsoCell, drawFloor: int, zoom: float, offx: int, offy: int, xPos: float, yPos: float, draww: int, drawh: int) -> None: ...

  @staticmethod
  def renderLine(x1: float, y1: float, x2: float, y2: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def renderRect(x: float, y: float, w: float, h: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def translatePointX(x: float, camX: float, zoom: float, offx: float) -> float: ...

  @staticmethod
  def translatePointY(y: float, camY: float, zoom: float, offy: float) -> float: ...

  def __init__(self):
    self.numberticks: int
    self.paused: bool
    self.savedelay: float
    self.showanimationviewer: bool
    self.showattachmenteditor: bool
    self.showchunkdebugger: bool
    self.showglobalobjectdebugger: bool
    self.showvehicleeditor: str
    self.showworldmapeditor: str

  class s_performance: ...


class LoadingQueueState(GameState):

  def enter(self) -> None: ...

  def redirectState(self) -> GameState: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  def onConnectionImmediate() -> None: ...

  @staticmethod
  def onPlaceInQueue(place: int) -> None: ...

  def __init__(self): ...


class MainScreenState(GameState):

  ambient: Audio

  instance: MainScreenState

  totalScale: float

  Version: str

  def ShouldShowLogo(self) -> bool: ...

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def redirectState(self) -> GameState: ...

  def render(self) -> None: ...

  def renderBackground(self) -> None: ...

  def setConnectToServerState(self, state: ConnectToServerState) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  @staticmethod
  @overload
  def DrawTexture(tex: Texture, x: int, y: int, width: int, height: int, alpha: float) -> None: ...

  @staticmethod
  @overload
  def DrawTexture(tex: Texture, x: int, y: int, width: int, height: int, col: Color) -> None: ...

  @staticmethod
  def convertToByteBuffer(image: BufferedImage) -> ByteBuffer: ...

  @staticmethod
  def getInstance() -> MainScreenState: ...

  @staticmethod
  def loadIcons() -> GLFWImage.Buffer: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self):
    self.alpha: float
    self.alphastep: float
    self.elements: ArrayList[MainScreenState.ScreenElement]
    self.lightningcount: float
    self.lightningdelta: float
    self.lightningfulltimer: float
    self.lightningtargetdelta: float
    self.lightningtimelinemarker: bool
    self.lightoffcount: float
    self.m_worldmap: UIWorldMap
    self.showlogo: bool
    self.targetalpha: float

  class ScreenElement:

    def render(self) -> None: ...

    def setY(self, y: float) -> None: ...

    def update(self) -> None: ...

    def __init__(self, tex: Texture, x: int, y: int, xVel: float, yVel: float, xCount: int):
      self.alpha: float
      self.alphastep: float
      self.jumpback: bool
      self.sx: float
      self.sy: float
      self.targetalpha: float
      self.tex: Texture
      self.tickstilltargetalpha: int
      self.x: float
      self.xcount: int
      self.xvel: float
      self.xvelo: float
      self.y: float
      self.yvel: float
      self.yvelo: float

  class Credit:

    def __init__(self, arg0: MainScreenState, arg1: Texture, arg2: Texture):
      self.disappeardelay: int
      self.name: Texture
      self.namealpha: float
      self.nameappeardelay: float
      self.nametargetalpha: float
      self.title: Texture
      self.titlealpha: float
      self.titletargetalpha: float


class ServerDisconnectState(GameState):

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def __init__(self): ...


class TISLogoState(GameState):

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def __init__(self):
    self.alpha: float
    self.alphastep: float
    self.logodisplaytime: float
    self.screennumber: int
    self.stage: int
    self.targetalpha: float

  class LogoElement: ...


class TermsOfServiceState(GameState):

  def enter(self) -> None: ...

  def exit(self) -> None: ...

  def fromLua0(self, arg0: str) -> object: ...

  def render(self) -> None: ...

  def update(self) -> GameStateMachine.StateAction: ...

  def __init__(self): ...

