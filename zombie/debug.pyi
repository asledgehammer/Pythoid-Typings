from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import OutputStream, FilterOutputStream, PrintStream
from java.lang import Throwable, StackTraceElement, Iterable, Enum
from java.util import ArrayList
from zombie.config import BooleanConfigOption
from zombie.debug.options import IDebugOptionGroup, IDebugOption, Animation, Character, IsoSprite, Network, OffscreenBuffer, Terrain, Weather, OptionGroup

class BooleanDebugOption(BooleanConfigOption):

  def getName(self) -> str: ...

  @overload
  def getParent(self) -> IDebugOptionGroup: ...

  @overload
  def getParent(self) -> IDebugOptionGroup: ...

  def getValue(self) -> bool: ...

  def isDebugOnly(self) -> bool: ...

  @overload
  def setParent(self, parent: IDebugOptionGroup) -> None: ...

  @overload
  def setParent(self, parent: IDebugOptionGroup) -> None: ...

  def __init__(self, name: str, debugOnly: bool, defaultValue: bool): ...


class DebugLog:

  ActionSystem: DebugLogStream

  Animation: DebugLogStream

  Asset: DebugLogStream

  Clothing: DebugLogStream

  Combat: DebugLogStream

  Damage: DebugLogStream

  Death: DebugLogStream

  FileIO: DebugLogStream

  Fireplace: DebugLogStream

  General: DebugLogStream

  Input: DebugLogStream

  IsoRegion: DebugLogStream

  Lua: DebugLogStream

  MapLoading: DebugLogStream

  Mod: DebugLogStream

  Multiplayer: DebugLogStream

  Network: DebugLogStream

  NetworkFileDebug: DebugLogStream

  Objects: DebugLogStream

  Packet: DebugLogStream

  printServerTime: bool

  Radio: DebugLogStream

  Recipe: DebugLogStream

  Script: DebugLogStream

  Shader: DebugLogStream

  Sound: DebugLogStream

  Statistic: DebugLogStream

  UnitTests: DebugLogStream

  Vehicle: DebugLogStream

  VERSION: int

  Voice: DebugLogStream

  Zombie: DebugLogStream

  @staticmethod
  def enableLog(type: DebugType, severity: LogSeverity) -> None: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, formatNoParams: str) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object) -> str: ...

  @staticmethod
  @overload
  def formatString(type: DebugType, logSeverity: LogSeverity, prefix: str, affix: object, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object, param8: object) -> str: ...

  @staticmethod
  def formatStringVarArgs(arg0: DebugType, arg1: LogSeverity, arg2: str, arg3: object, arg4: str, arg5: list[object]) -> str: ...

  @staticmethod
  def getDebugTypes() -> ArrayList[DebugType]: ...

  @staticmethod
  def getLogLevel(type: DebugType) -> LogSeverity: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isEnabled(type: DebugType) -> bool: ...

  @staticmethod
  @overload
  def isLogEnabled(type: DebugType, logSeverity: LogSeverity) -> bool: ...

  @staticmethod
  @overload
  def isLogEnabled(logSeverity: LogSeverity, type: DebugType) -> bool: ...

  @staticmethod
  def load() -> None: ...

  @staticmethod
  @overload
  def log(o: object) -> None: ...

  @staticmethod
  @overload
  def log(str: str) -> None: ...

  @staticmethod
  @overload
  def log(type: DebugType, str: str) -> None: ...

  @staticmethod
  def save() -> None: ...

  @staticmethod
  def setLogEnabled(type: DebugType, bEnabled: bool) -> None: ...

  @staticmethod
  def setStdErr(out: OutputStream) -> None: ...

  @staticmethod
  def setStdOut(out: OutputStream) -> None: ...

  def __init__(self): ...

  class OutputStreamWrapper(FilterOutputStream):

    def setStream(self, arg0: OutputStream) -> None: ...

    def write(self, arg0: list[int], arg1: int, arg2: int) -> None: ...

    def __init__(self, arg0: OutputStream): ...


class DebugLogStream(PrintStream):

  s_prefixDebug: str

  s_prefixErr: str

  s_prefixOut: str

  s_prefixTrace: str

  s_prefixWarn: str

  @overload
  def debugln(self, str: str) -> None: ...

  @overload
  def debugln(self, format: str, param0: object) -> None: ...

  @overload
  def debugln(self, format: str, param0: object, param1: object) -> None: ...

  @overload
  def debugln(self, format: str, param0: object, param1: object, param2: object) -> None: ...

  @overload
  def debugln(self, format: str, param0: object, param1: object, param2: object, param3: object) -> None: ...

  @overload
  def debugln(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> None: ...

  @overload
  def debugln(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> None: ...

  @overload
  def error(self, obj: object) -> None: ...

  @overload
  def error(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def noise(self, str: str) -> None: ...

  @overload
  def noise(self, format: str, param0: object) -> None: ...

  @overload
  def noise(self, format: str, param0: object, param1: object) -> None: ...

  @overload
  def noise(self, format: str, param0: object, param1: object, param2: object) -> None: ...

  @overload
  def noise(self, format: str, param0: object, param1: object, param2: object, param3: object) -> None: ...

  @overload
  def noise(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> None: ...

  @overload
  def noise(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> None: ...

  @overload
  def print(self, b: bool) -> None: ...

  @overload
  def print(self, c: str) -> None: ...

  @overload
  def print(self, d: float) -> None: ...

  @overload
  def print(self, f: float) -> None: ...

  @overload
  def print(self, i: int) -> None: ...

  @overload
  def print(self, obj: object) -> None: ...

  @overload
  def print(self, s: str) -> None: ...

  @overload
  def print(self, l: int) -> None: ...

  @overload
  def printException(self, ex: Throwable, errorMessage: str, severity: LogSeverity) -> None: ...

  @overload
  def printException(self, ex: Throwable, errorMessage: str, callerPrefix: str, severity: LogSeverity) -> None: ...

  @overload
  def printStackTrace(self) -> None: ...

  @overload
  def printStackTrace(self, message: str) -> None: ...

  @overload
  def printStackTrace(self, depth: int, message: str) -> None: ...

  def printUnitTest(self, arg0: str, arg1: bool, arg2: list[object]) -> None: ...

  def printf(self, arg0: str, arg1: list[object]) -> PrintStream: ...

  @overload
  def println(self) -> None: ...

  @overload
  def println(self, x: list[str]) -> None: ...

  @overload
  def println(self, x: bool) -> None: ...

  @overload
  def println(self, x: str) -> None: ...

  @overload
  def println(self, x: float) -> None: ...

  @overload
  def println(self, x: float) -> None: ...

  @overload
  def println(self, x: int) -> None: ...

  @overload
  def println(self, x: object) -> None: ...

  @overload
  def println(self, x: str) -> None: ...

  @overload
  def println(self, x: int) -> None: ...

  @overload
  def println(self, format: str, param0: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object) -> None: ...

  @overload
  def println(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object, param8: object) -> None: ...

  @overload
  def trace(self, str: str) -> None: ...

  @overload
  def trace(self, format: str, param0: object) -> None: ...

  @overload
  def trace(self, format: str, param0: object, param1: object) -> None: ...

  @overload
  def trace(self, format: str, param0: object, param1: object, param2: object) -> None: ...

  @overload
  def trace(self, format: str, param0: object, param1: object, param2: object, param3: object) -> None: ...

  @overload
  def trace(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> None: ...

  @overload
  def trace(self, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> None: ...

  @overload
  def warn(self, obj: object) -> None: ...

  @overload
  def warn(self, arg0: str, arg1: list[object]) -> None: ...

  @staticmethod
  def generateCallerPrefix() -> str: ...

  @staticmethod
  def getStackTraceElementString(stackTraceElement: StackTraceElement, includeLineNo: bool) -> str: ...

  @staticmethod
  def getTopStackTraceString(ex: Throwable) -> str: ...

  @staticmethod
  def tryGetCallerTraceElement(depthIdx: int) -> StackTraceElement: ...

  def __init__(self, out: PrintStream, warn: PrintStream, err: PrintStream, formatter: IDebugLogFormatter): ...


class DebugOptions:

  instance: DebugOptions

  VERSION: int

  @overload
  def addChild(self, newChild: IDebugOption) -> None: ...

  @overload
  def addChild(self, newChild: IDebugOption) -> None: ...

  def getBoolean(self, name: str) -> bool: ...

  @overload
  def getChildren(self) -> Iterable[IDebugOption]: ...

  @overload
  def getChildren(self) -> Iterable[IDebugOption]: ...

  def getName(self) -> str: ...

  def getOptionByIndex(self, index: int) -> BooleanDebugOption: ...

  def getOptionByName(self, name: str) -> BooleanDebugOption: ...

  def getOptionCount(self) -> int: ...

  def getParent(self) -> IDebugOptionGroup: ...

  def init(self) -> None: ...

  def load(self) -> None: ...

  @overload
  def onChildAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onChildAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onDescendantAdded(self, newOption: IDebugOption) -> None: ...

  @overload
  def onDescendantAdded(self, newOption: IDebugOption) -> None: ...

  def save(self) -> None: ...

  def setBoolean(self, name: str, value: bool) -> None: ...

  def setParent(self, parent: IDebugOptionGroup) -> None: ...

  @staticmethod
  def testThreadCrash(idx: int) -> None: ...

  def __init__(self):
    self.animation: Animation
    self.assetslowload: BooleanDebugOption
    self.character: str
    self.cheatclockvisible: BooleanDebugOption
    self.cheatdoorunlock: BooleanDebugOption
    self.cheatplayerinvisiblesprint: BooleanDebugOption
    self.cheatplayerseeeveryone: BooleanDebugOption
    self.cheatplayerstartinvisible: BooleanDebugOption
    self.cheatrecipeknowall: BooleanDebugOption
    self.cheattimedactioninstant: BooleanDebugOption
    self.cheatunlimitedammo: BooleanDebugOption
    self.cheatvehiclemechanicsanywhere: BooleanDebugOption
    self.cheatvehiclestartwithoutkey: BooleanDebugOption
    self.cheatwindowunlock: BooleanDebugOption
    self.checks: DebugOptions.Checks
    self.collidewithobstaclesrendernormals: BooleanDebugOption
    self.collidewithobstaclesrenderobstacles: BooleanDebugOption
    self.collidewithobstaclesrenderradius: BooleanDebugOption
    self.deadbodyatlasrender: BooleanDebugOption
    self.debugdraw_skipdrawnonskinnedmodel: BooleanDebugOption
    self.debugdraw_skipvbodraw: BooleanDebugOption
    self.debugdraw_skipworldshading: BooleanDebugOption
    self.debugscenarioforcelaunch: BooleanDebugOption
    self.gameprofilerenabled: BooleanDebugOption
    self.gametimespeedhalf: BooleanDebugOption
    self.gametimespeedquarter: BooleanDebugOption
    self.isosprite: IsoSprite
    self.joypadrenderui: BooleanDebugOption
    self.lightingrender: BooleanDebugOption
    self.mechanicsrenderhitbox: BooleanDebugOption
    self.modelrenderattachments: BooleanDebugOption
    self.modelrenderaxis: BooleanDebugOption
    self.modelrenderbones: BooleanDebugOption
    self.modelrenderbounds: BooleanDebugOption
    self.modelrenderlights: BooleanDebugOption
    self.modelrendermuzzleflash: BooleanDebugOption
    self.modelrenderskipvehicles: BooleanDebugOption
    self.modelrenderweaponhitpoint: BooleanDebugOption
    self.modelrenderwireframe: BooleanDebugOption
    self.modelskeleton: BooleanDebugOption
    self.modrenderloaded: BooleanDebugOption
    self.multiplayerattackplayer: BooleanDebugOption
    self.multiplayerautoequip: BooleanDebugOption
    self.multiplayercriticalhit: BooleanDebugOption
    self.multiplayerfailchecksum: BooleanDebugOption
    self.multiplayerfollowplayer: BooleanDebugOption
    self.multiplayerhotkey: BooleanDebugOption
    self.multiplayerlogprediction: BooleanDebugOption
    self.multiplayerplayerzombie: BooleanDebugOption
    self.multiplayerseenonpvpzones: BooleanDebugOption
    self.multiplayershowhit: BooleanDebugOption
    self.multiplayershowplayerprediction: BooleanDebugOption
    self.multiplayershowplayerstatus: BooleanDebugOption
    self.multiplayershowposition: BooleanDebugOption
    self.multiplayershowteleport: BooleanDebugOption
    self.multiplayershowzombiedesync: BooleanDebugOption
    self.multiplayershowzombiemultiplier: BooleanDebugOption
    self.multiplayershowzombieowner: BooleanDebugOption
    self.multiplayershowzombieprediction: BooleanDebugOption
    self.multiplayershowzombiestatus: BooleanDebugOption
    self.multiplayertorsohit: BooleanDebugOption
    self.multiplayerzombiecrawler: BooleanDebugOption
    self.network: Network
    self.objectambientemitterrender: BooleanDebugOption
    self.offscreenbuffer: OffscreenBuffer
    self.pathfindpathtomouseallowcrawl: BooleanDebugOption
    self.pathfindpathtomouseallowthump: BooleanDebugOption
    self.pathfindpathtomouseenable: BooleanDebugOption
    self.pathfindpathtomouseignorecrawlcost: BooleanDebugOption
    self.pathfindrenderpath: BooleanDebugOption
    self.pathfindrenderwaiting: BooleanDebugOption
    self.physicsrender: BooleanDebugOption
    self.polymaprenderclusters: BooleanDebugOption
    self.polymaprenderconnections: BooleanDebugOption
    self.polymaprendercrawling: BooleanDebugOption
    self.polymaprenderlineclearcollide: BooleanDebugOption
    self.polymaprendernodes: BooleanDebugOption
    self.skyboxshow: BooleanDebugOption
    self.terrain: Terrain
    self.threadcrash_enabled: BooleanDebugOption
    self.threadcrash_gameloadingthread: list[BooleanDebugOption]
    self.threadcrash_gamethread: list[BooleanDebugOption]
    self.threadcrash_renderthread: list[BooleanDebugOption]
    self.tooltipinfo: BooleanDebugOption
    self.tooltipmodname: BooleanDebugOption
    self.translationprefix: BooleanDebugOption
    self.uidebugconsoledebuglog: BooleanDebugOption
    self.uidebugconsoleechocommand: BooleanDebugOption
    self.uidebugconsolestartvisible: BooleanDebugOption
    self.uidisablewelcomemessage: BooleanDebugOption
    self.uirenderoutline: BooleanDebugOption
    self.vehiclecyclecolor: BooleanDebugOption
    self.vehiclerenderarea: BooleanDebugOption
    self.vehiclerenderattackpositions: BooleanDebugOption
    self.vehiclerenderauthorizations: BooleanDebugOption
    self.vehiclerenderblood0: BooleanDebugOption
    self.vehiclerenderblood100: BooleanDebugOption
    self.vehiclerenderblood50: BooleanDebugOption
    self.vehiclerenderdamage0: BooleanDebugOption
    self.vehiclerenderdamage1: BooleanDebugOption
    self.vehiclerenderdamage2: BooleanDebugOption
    self.vehiclerenderexit: BooleanDebugOption
    self.vehiclerenderinterpolatebuffer: BooleanDebugOption
    self.vehiclerenderintersectedsquares: BooleanDebugOption
    self.vehiclerenderoutline: BooleanDebugOption
    self.vehiclerenderrust0: BooleanDebugOption
    self.vehiclerenderrust100: BooleanDebugOption
    self.vehiclerenderrust50: BooleanDebugOption
    self.vehiclerendertrailerpositions: BooleanDebugOption
    self.vehiclespawneverywhere: BooleanDebugOption
    self.weather: Weather
    self.worldchunkmap5x5: BooleanDebugOption
    self.worlditematlasrender: BooleanDebugOption
    self.worldsoundrender: BooleanDebugOption
    self.worldstreamerslowload: BooleanDebugOption
    self.zombieoutfitrandom: BooleanDebugOption
    self.zombierendercancrawlundervehicle: BooleanDebugOption
    self.zombierenderfakedead: BooleanDebugOption
    self.zombierendermemory: BooleanDebugOption

  class Checks(OptionGroup):

    def __init__(self):
      self.boundtextures: BooleanDebugOption
      self.slowluaevents: BooleanDebugOption


class DebugType(Enum):

  ActionSystem: DebugType

  Animation: DebugType

  Asset: DebugType

  Checksum: DebugType

  Clothing: DebugType

  Combat: DebugType

  Damage: DebugType

  Death: DebugType

  FileIO: DebugType

  Fireplace: DebugType

  General: DebugType

  Input: DebugType

  IsoRegion: DebugType

  Lua: DebugType

  MapLoading: DebugType

  Mod: DebugType

  Multiplayer: DebugType

  Network: DebugType

  NetworkFileDebug: DebugType

  Objects: DebugType

  Ownership: DebugType

  Packet: DebugType

  Radio: DebugType

  Recipe: DebugType

  Script: DebugType

  Shader: DebugType

  Sound: DebugType

  Statistic: DebugType

  UnitTests: DebugType

  Vehicle: DebugType

  Voice: DebugType

  Zombie: DebugType

  @staticmethod
  def Do(arg0: DebugType) -> bool: ...

  @staticmethod
  def valueOf(arg0: str) -> DebugType: ...

  @staticmethod
  def values() -> list[DebugType]: ...


class IDebugLogFormatter:

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, formatNoParams: str) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object, param4: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object) -> str: ...

  @overload
  def format(self, logSeverity: LogSeverity, prefix: str, affix: str, format: str, param0: object, param1: object, param2: object, param3: object, param4: object, param5: object, param6: object, param7: object, param8: object) -> str: ...

  def isLogEnabled(self, logSeverity: LogSeverity) -> bool: ...

  def isLogSeverityEnabled(self, logSeverity: LogSeverity) -> bool: ...


class LineDrawer:

  alpha: int

  blue: int

  green: int

  red: int

  def removeLine(self, name: str) -> None: ...

  @staticmethod
  @overload
  def DrawIsoCircle(x: float, y: float, z: float, radius: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  @overload
  def DrawIsoCircle(x: float, y: float, z: float, radius: float, segments: int, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def DrawIsoLine(x: float, y: float, z: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  @staticmethod
  @overload
  def DrawIsoRect(x: float, y: float, width: float, height: float, z: int, r: float, g: float, bl: float) -> None: ...

  @staticmethod
  @overload
  def DrawIsoRect(x: float, y: float, width: float, height: float, z: int, yPixelOffset: int, r: float, g: float, bl: float) -> None: ...

  @staticmethod
  def DrawIsoRectRotated(x: float, y: float, z: float, w: float, h: float, angleRadians: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def DrawIsoTransform(px: float, py: float, z: float, rx: float, ry: float, radius: float, segments: int, r: float, g: float, b: float, a: float, t: int) -> None: ...

  @staticmethod
  @overload
  def addLine(x: float, y: float, z: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  @overload
  def addLine(x: float, y: float, z: float, x2: float, y2: float, z2: float, r: int, g: int, b: int, name: str) -> None: ...

  @staticmethod
  @overload
  def addLine(x: float, y: float, z: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, name: str, bLine: bool) -> None: ...

  @staticmethod
  def addRect(x: float, y: float, z: float, width: float, height: float, r: float, g: float, b: float) -> None: ...

  @staticmethod
  def addRectYOffset(x: float, y: float, z: float, width: float, height: float, yOffset: int, r: float, g: float, b: float) -> None: ...

  @staticmethod
  def clear() -> None: ...

  @staticmethod
  def drawArc(cx: float, cy: float, cz: float, radius: float, direction: float, angle: float, segments: int, r: float, g: float, b: float, a: float) -> None: ...

  @staticmethod
  def drawCircle(x: float, y: float, radius: float, segments: int, r: float, g: float, b: float) -> None: ...

  @staticmethod
  def drawDirectionLine(cx: float, cy: float, cz: float, radius: float, radians: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  @staticmethod
  def drawDotLines(cx: float, cy: float, cz: float, radius: float, direction: float, dot: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  @staticmethod
  def drawLine(x: float, y: float, x2: float, y2: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  @staticmethod
  def drawLines() -> None: ...

  @staticmethod
  def drawRect(x: float, y: float, width: float, height: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

  @staticmethod
  def render() -> None: ...

  def __init__(self): ...

  class DrawableLine:

    def equals(self, arg0: object) -> bool: ...

    @overload
    def init(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> LineDrawer.DrawableLine: ...

    @overload
    def init(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: str) -> LineDrawer.DrawableLine: ...

    @overload
    def init(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: str, arg10: bool) -> LineDrawer.DrawableLine: ...


class LogSeverity(Enum):

  Debug: LogSeverity

  Error: LogSeverity

  General: LogSeverity

  Trace: LogSeverity

  Warning: LogSeverity

  @staticmethod
  def valueOf(arg0: str) -> LogSeverity: ...

  @staticmethod
  def values() -> list[LogSeverity]: ...


class ObjectsSyncRequestJUnit:

  def __init__(self): ...

