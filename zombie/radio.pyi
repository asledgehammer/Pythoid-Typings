from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum, Integer
from java.util import ArrayList, Map
from se.krka.kahlua.vm import KahluaTable
from zombie.chat import ChatMessage
from zombie.core import Language
from zombie.core.network import ByteBufferWriter
from zombie.radio.devices import WaveSignalDevice, DeviceData
from zombie.radio.media import RecordedMedia
from zombie.radio.scripting import RadioChannel, RadioScriptManager

class ChannelCategory(Enum):

  Amateur: ChannelCategory

  Bandit: ChannelCategory

  Emergency: ChannelCategory

  Military: ChannelCategory

  Other: ChannelCategory

  Radio: ChannelCategory

  Television: ChannelCategory

  Undefined: ChannelCategory

  @staticmethod
  def valueOf(arg0: str) -> ChannelCategory: ...

  @staticmethod
  def values() -> list[ChannelCategory]: ...


class GameMode(Enum):

  Client: GameMode

  Server: GameMode

  SinglePlayer: GameMode

  @staticmethod
  def valueOf(arg0: str) -> GameMode: ...

  @staticmethod
  def values() -> list[GameMode]: ...


class RadioAPI:

  def getChannels(self, category: str) -> KahluaTable: ...

  @staticmethod
  def getInstance() -> RadioAPI: ...

  @staticmethod
  def hasInstance() -> bool: ...

  @staticmethod
  def timeStampToDays(stamp: int) -> int: ...

  @staticmethod
  def timeStampToHours(stamp: int) -> int: ...

  @staticmethod
  def timeStampToMinutes(stamp: int) -> int: ...

  @staticmethod
  def timeToTimeStamp(days: int, hours: int, minutes: int) -> int: ...


class RadioData:

  def getRadioChannels(self) -> ArrayList[RadioChannel]: ...

  def isVanilla(self) -> bool: ...

  @staticmethod
  def fetchAllRadioData() -> ArrayList[RadioData]: ...

  @staticmethod
  def getTranslatorNames(language: Language) -> ArrayList[str]: ...

  def __init__(self, xmlFile: str): ...


class RadioDebugConsole:

  def render(self) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def timeStampToString(stamp: int) -> str: ...

  def __init__(self): ...


class RadioTranslationData:

  def getFilePath(self) -> str: ...

  def getGuid(self) -> str: ...

  def getLanguage(self) -> str: ...

  def getLanguageEnum(self) -> Language: ...

  def getTranslation(self, guid: str) -> str: ...

  def getTranslationCount(self) -> int: ...

  def getTranslators(self) -> ArrayList[str]: ...

  def getVersion(self) -> int: ...

  def loadTranslations(self) -> bool: ...

  def validate(self) -> bool: ...

  @staticmethod
  def ReadFile(file: str) -> RadioTranslationData: ...

  def __init__(self, file: str): ...


class RadioXmlReader:

  @staticmethod
  def LoadFile(file: str) -> bool: ...

  @staticmethod
  def LoadTranslatorNames(file: str) -> ArrayList[str]: ...

  @staticmethod
  def ReadFileHeader(file: str) -> RadioData: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, printDebug: bool): ...


class ZomboidRadio:

  DEBUG_MODE: bool

  DEBUG_SOUND: bool

  DEBUG_XML: bool

  DISABLE_BROADCASTING: bool

  LOUISVILLE_OBFUSCATION: bool

  POST_RADIO_SILENCE: bool

  SAVE_FILE: str

  def GetChannelList(self, category: str) -> Map[Integer, str]: ...

  def Init(self, savedWorldVersion: int) -> None: ...

  def Load(self) -> bool: ...

  def PlayerListensChannel(self, channel: int, listenmode: bool, isTV: bool) -> None: ...

  def ReceiveTransmission(self, sourceX: int, sourceY: int, channel: int, msg: str, guid: str, codes: str, r: float, g: float, b: float, signalStrength: int, isTV: bool) -> None: ...

  def RegisterDevice(self, device: WaveSignalDevice) -> None: ...

  def Reset(self) -> None: ...

  def Save(self) -> None: ...

  @overload
  def SendTransmission(self, sourceX: int, sourceY: int, msg: ChatMessage, signalStrength: int) -> None: ...

  @overload
  def SendTransmission(self, sourceX: int, sourceY: int, channel: int, msg: str, guid: str, codes: str, r: float, g: float, b: float, signalStrength: int, isTV: bool) -> None: ...

  @overload
  def SendTransmission(self, source: int, sourceX: int, sourceY: int, channel: int, msg: str, guid: str, codes: str, r: float, g: float, b: float, signalStrength: int, isTV: bool) -> None: ...

  def UnRegisterDevice(self, device: WaveSignalDevice) -> None: ...

  def UpdateScripts(self, hour: int, mins: int) -> None: ...

  def WriteRadioServerDataPacket(self, bb: ByteBufferWriter) -> None: ...

  @overload
  def addChannelName(self, name: str, frequency: int, category: str) -> None: ...

  @overload
  def addChannelName(self, name: str, frequency: int, category: str, overwrite: bool) -> None: ...

  def clone(self) -> object: ...

  def computerize(self, str: str) -> str: ...

  def getBroadcastDevices(self) -> ArrayList[WaveSignalDevice]: ...

  def getChannelName(self, frequency: int) -> str: ...

  def getDaysSinceStart(self) -> int: ...

  def getDevices(self) -> ArrayList[WaveSignalDevice]: ...

  def getDisableBroadcasting(self) -> bool: ...

  def getDisableMediaLineLearning(self) -> bool: ...

  def getFullChannelList(self) -> Map[str, Map[Integer, str]]: ...

  def getGameMode(self) -> GameMode: ...

  def getRandomBzztFzzt(self) -> str: ...

  @overload
  def getRandomFrequency(self) -> int: ...

  @overload
  def getRandomFrequency(self, rangemin: int, rangemax: int) -> int: ...

  def getRecordedMedia(self) -> RecordedMedia: ...

  def getScriptManager(self) -> RadioScriptManager: ...

  def removeChannelName(self, frequency: int) -> None: ...

  def render(self) -> None: ...

  def scrambleString(self, msg: str, intensity: int, ignoreBBcode: bool, customScramble: str) -> str: ...

  def setDisableBroadcasting(self, b: bool) -> None: ...

  def setDisableMediaLineLearning(self, b: bool) -> None: ...

  def setHasRecievedServerData(self, state: bool) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def ObfuscateChannelCheck(channel: RadioChannel) -> None: ...

  @staticmethod
  def getInstance() -> ZomboidRadio: ...

  @staticmethod
  def hasInstance() -> bool: ...

  @staticmethod
  def isStaticSound(str: str) -> bool: ...

  class FreqListEntry:

    def __init__(self, arg0: bool, arg1: DeviceData, arg2: int, arg3: int):
      self.devicedata: DeviceData
      self.isinvitem: bool
      self.sourcex: int
      self.sourcey: int

