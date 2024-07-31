from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from fmod import SoundBuffer, FMODSoundBuffer
from gnu.trove.list.array import TShortArrayList
from java.awt import Dimension
from java.lang import Long, Enum, Integer
from java.net import InetSocketAddress
from java.nio import ByteBuffer
from java.util import Deque, List, ArrayList
from javax.swing import JPanel
from se.krka.kahlua.vm import Platform, KahluaTable
from zombie.characters import IsoPlayer
from zombie.core.network import ByteBufferWriter
from zombie.core.utils import UpdateTimer
from zombie.core.znet import ZNetStatistics
from zombie.iso import Vector3
from zombie.network import ClientServerMap, PlayerDownloadServer, PacketValidator, PacketTypes
from zombie.radio.devices import DeviceData

class FMODTest:

  def __init__(self): ...


class RakNetPeerInterface:

  ConnectionType_Disconnected: int

  ConnectionType_Steam: int

  ConnectionType_UDPRakNet: int

  ID_ALREADY_CONNECTED: int

  ID_CONNECTED_PING: int

  ID_CONNECTION_ATTEMPT_FAILED: int

  ID_CONNECTION_BANNED: int

  ID_CONNECTION_LOST: int

  ID_CONNECTION_REQUEST_ACCEPTED: int

  ID_DISCONNECTION_NOTIFICATION: int

  ID_INCOMPATIBLE_PROTOCOL_VERSION: int

  ID_INVALID_PASSWORD: int

  ID_NEW_INCOMING_CONNECTION: int

  ID_NO_FREE_INCOMING_CONNECTIONS: int

  ID_PING: int

  ID_RAKVOICE_CLOSE_CHANNEL: int

  ID_RAKVOICE_OPEN_CHANNEL_REPLY: int

  ID_RAKVOICE_OPEN_CHANNEL_REQUEST: int

  ID_REMOTE_CONNECTION_LOST: int

  ID_REMOTE_DISCONNECTION_NOTIFICATION: int

  ID_REMOTE_NEW_INCOMING_CONNECTION: int

  ID_UNCONNECTED_PING: int

  ID_USER_PACKET_ENUM: int

  PacketPriority_HIGH: int

  PacketPriority_IMMEDIATE: int

  PacketPriority_LOW: int

  PacketPriority_MEDIUM: int

  PacketReliability_RELIABLE: int

  PacketReliability_RELIABLE_ORDERED: int

  PacketReliability_RELIABLE_ORDERED_WITH_ACK_RECEIPT: int

  PacketReliability_RELIABLE_SEQUENCED: int

  PacketReliability_RELIABLE_WITH_ACK_RECEIPT: int

  PacketReliability_UNRELIABLE: int

  PacketReliability_UNRELIABLE_SEQUENCED: int

  PacketReliability_UNRELIABLE_WITH_ACK_RECEIPT: int

  def Connect(self, arg0: str, arg1: int, arg2: str, arg3: bool) -> int: ...

  def ConnectToSteamServer(self, arg0: int, arg1: str, arg2: bool) -> int: ...

  def GetAveragePing(self, guid: int) -> int: ...

  def GetClientOwnerSteamID(self, guid: int) -> int: ...

  def GetClientSteamID(self, guid: int) -> int: ...

  def GetConnectionType(self, guid: int) -> int: ...

  def GetConnectionsNumber(self) -> int: ...

  def GetLastPing(self, guid: int) -> int: ...

  def GetLowestPing(self, guid: int) -> int: ...

  def GetMTUSize(self, guid: int) -> int: ...

  def GetNetStatistics(self, guid: int) -> ZNetStatistics: ...

  def GetServerIP(self) -> str: ...

  def Init(self, steamMode: bool) -> None: ...

  def Receive(self, buffer: ByteBuffer) -> bool: ...

  def Send(self, data: ByteBuffer, PacketPriority: int, PacketReliability: int, orderingChannel: int, guid: int, broadcast: bool) -> int: ...

  def SendRaw(self, data: ByteBuffer, PacketPriority: int, PacketReliability: int, orderingChannel: int, guid: int, broadcast: bool) -> int: ...

  def SetClientPort(self, port: int) -> None: ...

  def SetIncomingPassword(self, password: str) -> None: ...

  def SetMaximumIncomingConnections(self, num: int) -> None: ...

  def SetOccasionalPing(self, bPing: bool) -> None: ...

  def SetServerIP(self, ip: str) -> None: ...

  def SetServerPort(self, port: int, UDPPort: int) -> None: ...

  def SetTimeoutTime(self, time: int) -> None: ...

  def SetUnreliableTimeout(self, timeout: int) -> None: ...

  def Shutdown(self) -> None: ...

  def Startup(self, maxConnections: int) -> int: ...

  def disconnect(self, connectedGUID: int, message: str) -> None: ...

  def getGuidFromIndex(self, id: int) -> int: ...

  def getGuidOfPacket(self) -> int: ...

  def getIPFromGUID(self, guid: int) -> str: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class RakVoice:

  @staticmethod
  def CloseAllChannels() -> None: ...

  @staticmethod
  def CloseVoiceChannel(uuid: int) -> None: ...

  @staticmethod
  def GetBufferSizeBytes() -> int: ...

  @staticmethod
  def GetBuffering() -> int: ...

  @staticmethod
  def GetChannelStatistics(uuid: int, buf: list[int]) -> bool: ...

  @staticmethod
  def GetComplexity() -> int: ...

  @staticmethod
  def GetIs3D() -> bool: ...

  @staticmethod
  def GetMaxDistance() -> float: ...

  @staticmethod
  def GetMinDistance() -> float: ...

  @staticmethod
  def GetSampleRate() -> int: ...

  @staticmethod
  def GetSendFramePeriod() -> int: ...

  @staticmethod
  def GetServerVOIPEnable() -> bool: ...

  @staticmethod
  def RVDeinit() -> None: ...

  @staticmethod
  def RVInit(frames_per_buffer: int) -> None: ...

  @staticmethod
  def RVInitServer(enable: bool, sample_rate: int, framePeriod: int, complexity: int, buffering: int, minDistance: float, maxDistance: float, is3D: bool) -> None: ...

  @staticmethod
  def ReceiveFrame(playerid: int, buf: list[int]) -> bool: ...

  @staticmethod
  def RequestVoiceChannel(uuid: int) -> None: ...

  @staticmethod
  def SendFrame(uuid: int, playerid: int, buf: list[int], bufSize: int) -> None: ...

  @staticmethod
  def SetChannelsRouting(uuid: int, isCanHearAll: bool, radioData: list[int], radioDataCount: int) -> None: ...

  @staticmethod
  def SetComplexity(value: int) -> None: ...

  @staticmethod
  def SetLoopbackMode(mode: bool) -> None: ...

  @staticmethod
  def SetVoiceBan(uuid: int, is_ban: bool) -> None: ...

  def __init__(self): ...


class TestClient:

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self): ...


class TestServer:

  @staticmethod
  def Receive() -> ByteBuffer: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self): ...


class UdpConnection:

  CONNECTION_GRACE_INTERVAL: int

  @overload
  def RelevantTo(self, x: float, y: float) -> bool: ...

  @overload
  def RelevantTo(self, x: float, y: float, radius: float) -> bool: ...

  def RelevantToPlayerIndex(self, n: int, x: float, y: float) -> bool: ...

  def calcCountPlayersInRelevantPosition(self) -> None: ...

  def cancelPacket(self) -> None: ...

  @overload
  def endPacket(self) -> None: ...

  @overload
  def endPacket(self, priority: int, reliability: int, ordering: int) -> None: ...

  def endPacketImmediate(self) -> None: ...

  def endPacketSuperHighUnreliable(self) -> None: ...

  def endPacketUnordered(self) -> None: ...

  def endPacketUnreliable(self) -> None: ...

  def endPingPacket(self) -> None: ...

  def forceDisconnect(self, description: str) -> None: ...

  def getAveragePing(self) -> int: ...

  def getBufferPosition(self) -> int: ...

  def getConnectedGUID(self) -> int: ...

  def getConnectionType(self) -> UdpConnection.ConnectionType: ...

  def getInetSocketAddress(self) -> InetSocketAddress: ...

  def getLastPing(self) -> int: ...

  def getLowestPing(self) -> int: ...

  def getMTUSize(self) -> int: ...

  def getPeer(self) -> RakNetPeerInterface: ...

  def getRelevantAndDistance(self, x: float, y: float, z: float) -> float: ...

  def getServerIP(self) -> str: ...

  def getStatistics(self) -> ZNetStatistics: ...

  def havePlayer(self, p: IsoPlayer) -> bool: ...

  def isConnectionAttemptTimeout(self) -> bool: ...

  def isConnectionGraceIntervalTimeout(self) -> bool: ...

  def isFullyConnected(self) -> bool: ...

  def setConnectionTimestamp(self) -> None: ...

  def setFullyConnected(self) -> None: ...

  def startPacket(self) -> ByteBufferWriter: ...

  def startPingPacket(self) -> ByteBufferWriter: ...

  def toString(self) -> str: ...

  def __init__(self, engine: UdpEngine, connectedGUID: int, index: int):
    self.accesslevel: int
    self.allchatmuted: bool
    self.awaitingcoopapprove: bool
    self.checksumstate: UdpConnection.ChecksumState
    self.checksumtime: int
    self.chunkgridwidth: int
    self.chunkobjectstate: TShortArrayList
    self.connectarea: list[Vector3]
    self.connectiontimestamp: int
    self.idstr: str
    self.index: int
    self.ip: str
    self.iscoophost: bool
    self.isneighborplayer: bool
    self.lastunauthorizedpacket: int
    self.loadedcells: list[ClientServerMap]
    self.maxplayers: int
    self.netstatistics: ZNetStatistics
    self.ownerid: int
    self.password: str
    self.ping: bool
    self.pinghistory: Deque[Long]
    self.playerdownloadserver: PlayerDownloadServer
    self.playerids: list[int]
    self.players: list[IsoPlayer]
    self.preferredinqueue: bool
    self.releventpos: list[Vector3]
    self.releventrange: int
    self.statistic: UdpConnection.MPClientStatistic
    self.steamid: int
    self.timersendzombie: UpdateTimer
    self.username: str
    self.usernames: list[str]
    self.validator: PacketValidator
    self.wasinloadingqueue: bool

  class ChecksumState(Enum):

    Different: UdpConnection.ChecksumState

    Done: UdpConnection.ChecksumState

    Init: UdpConnection.ChecksumState

    @staticmethod
    def valueOf(arg0: str) -> UdpConnection.ChecksumState: ...

    @staticmethod
    def values() -> list[UdpConnection.ChecksumState]: ...

  class MPClientStatistic:

    def parse(self, arg0: ByteBuffer) -> None: ...

    def __init__(self, arg0: UdpConnection):
      self.diff: int
      self.enable: int
      self.fps: float
      self.fpsavg: float
      self.fpshistogramm: list[int]
      self.fpsmax: float
      self.fpsmin: float
      self.pingavg: float
      self.remoteplayerscount: int
      self.remoteplayersdesyncavg: float
      self.remoteplayersdesyncmax: float
      self.remoteplayersteleports: int
      self.zombiescount: int
      self.zombiesdesyncavg: float
      self.zombiesdesyncmax: float
      self.zombieslocalownership: int
      self.zombiesteleports: int

  class ConnectionType(Enum):

    Disconnected: UdpConnection.ConnectionType

    Steam: UdpConnection.ConnectionType

    UDPRakNet: UdpConnection.ConnectionType

    @staticmethod
    def valueOf(arg0: str) -> UdpConnection.ConnectionType: ...

    @staticmethod
    def values() -> list[UdpConnection.ConnectionType]: ...


class UdpEngine:

  def Connect(self, arg0: str, arg1: int, arg2: str, arg3: bool) -> None: ...

  def Receive(self) -> ByteBuffer: ...

  def SetServerPassword(self, password: str) -> None: ...

  def Shutdown(self) -> None: ...

  def connected(self) -> None: ...

  def endPacketBroadcast(self, packetType: PacketTypes.PacketType) -> None: ...

  def endPacketBroadcastExcept(self, priority: int, reliability: int, connection: UdpConnection) -> None: ...

  def forceDisconnect(self, connectedGUID: int, message: str) -> None: ...

  def getActiveConnection(self, connection: int) -> UdpConnection: ...

  def getClientOwnerSteamID(self, guid: int) -> int: ...

  def getClientSteamID(self, guid: int) -> int: ...

  def getDescription(self) -> str: ...

  def getMaxConnections(self) -> int: ...

  def getPeer(self) -> RakNetPeerInterface: ...

  def getServerIP(self) -> str: ...

  def hashServerPassword(self, password: str) -> str: ...

  def startPacket(self) -> ByteBufferWriter: ...

  def __init__(self, port: int, UDPPort: int, maxConnections: int, serverPassword: str, bListen: bool):
    self.connections: List[UdpConnection]
    self.port: int


class VoiceDebug(JPanel):

  def getPreferredSize(self) -> Dimension: ...

  @staticmethod
  def createAndShowGui() -> None: ...

  @staticmethod
  def updateGui(playBuf: SoundBuffer, recBuf: FMODSoundBuffer) -> None: ...

  def __init__(self, scores: List[Integer], title: str):
    self.current: int
    self.last: int
    self.psize: int
    self.scores: List[Integer]
    self.scores_max: int
    self.title: str


class VoiceManager:

  AGCModeAdaptiveAnalog: int

  AGCModeAdaptiveDigital: int

  AGCModeFixedDigital: int

  instance: VoiceManager

  modeMute: int

  modePPT: int

  modeVAD: int

  VADModeAggressive: int

  VADModeLowBitrate: int

  VADModeQuality: int

  VADModeVeryAggressive: int

  VoipDisabled: bool

  def DeinitRecSound(self) -> None: ...

  def DeinitVMClient(self) -> None: ...

  def InitVMClient(self) -> None: ...

  def LuaRegister(self, platform: Platform, environment: KahluaTable) -> None: ...

  def ResetRecSound(self) -> None: ...

  def UpdateChannelsRoaming(self, connection: UdpConnection) -> None: ...

  def UpdateRecordDevice(self) -> None: ...

  def VMServerBan(self, player_id: int, is_ban: bool) -> None: ...

  def VoiceConnectClose(self, uuid: int) -> None: ...

  def VoiceConnectReq(self, uuid: int) -> None: ...

  def VoiceRestartClient(self, isEnable: bool) -> None: ...

  def getMicVolumeError(self) -> bool: ...

  def getMicVolumeIndicator(self) -> int: ...

  def getServerVOIPEnable(self) -> bool: ...

  def loadConfig(self) -> None: ...

  def notifyThread(self) -> None: ...

  def setAGCMode(self, mode: int) -> None: ...

  def setMode(self, mode: int) -> None: ...

  def setTestingMicrophone(self, testing: bool) -> None: ...

  def setVADMode(self, mode: int) -> None: ...

  def setVolumeMic(self, volume: int) -> None: ...

  def setVolumePlayers(self, volume: int) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def getInstance() -> VoiceManager: ...

  @staticmethod
  def playerGetMute(username: str) -> bool: ...

  @staticmethod
  def playerSetMute(username: str) -> None: ...

  def __init__(self): ...


class VoiceManagerData:

  data: ArrayList[VoiceManagerData]

  @staticmethod
  def get(onlineId: int) -> VoiceManagerData: ...

  def __init__(self, index: int):
    self.iscanhearall: bool
    self.radiodata: ArrayList[VoiceManagerData.RadioData]
    self.userplaychannel: int
    self.userplaymute: bool
    self.userplaysound: int
    self.voicetimeout: int

  class RadioData:

    def getDeviceData(self) -> DeviceData: ...

    def isReceivingAvailable(self, channel: int) -> bool: ...

    def isTransmissionAvailable(self) -> bool: ...

    @overload
    def __init__(self, distance: float, x: float, y: float):
      self.distance: float

      self.freq: int

      self.x: int

      self.y: int

    @overload
    def __init__(self, data: DeviceData, x: float, y: float): ...
    @overload
    def __init__(self, freq: int, distance: float, x: float, y: float): ...

  class VoiceDataSource(Enum):

    Cheat: VoiceManagerData.VoiceDataSource

    Radio: VoiceManagerData.VoiceDataSource

    Unknown: VoiceManagerData.VoiceDataSource

    Voice: VoiceManagerData.VoiceDataSource

    @staticmethod
    def valueOf(arg0: str) -> VoiceManagerData.VoiceDataSource: ...

    @staticmethod
    def values() -> list[VoiceManagerData.VoiceDataSource]: ...


class VoiceTest:

  @staticmethod
  def main(args: list[str]) -> None: ...

  @staticmethod
  def rakNetClientReceive() -> ByteBuffer: ...

  @staticmethod
  def rakNetServerReceive() -> ByteBuffer: ...

  def __init__(self): ...

