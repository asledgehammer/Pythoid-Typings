from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from de.btobastian.javacord import DiscordAPI
from de.btobastian.javacord.entities.message import Message
from gnu.trove.map.hash import TShortObjectHashMap
from java.lang import Enum, Throwable, Integer, Short, Long, Thread, Boolean, Class, Byte, Double, Float
from java.net import Socket
from java.nio import ByteBuffer
from java.sql import Connection
from java.util import ArrayList, HashMap, List, Map, Calendar, HashSet, Collection, Iterator, Spliterator, Comparator
from java.util.concurrent import ConcurrentLinkedQueue
from java.util.function import Consumer, Function, ToDoubleFunction, ToIntFunction, ToLongFunction
from se.krka.kahlua.vm import Platform, KahluaTable
from zombie import SandboxOptions, WorldSoundManager, GameTime
from zombie.characters import IsoPlayer, IsoZombie, IsoGameCharacter, Faction, Safety
from zombie.characters.BodyDamage import BodyPart
from zombie.characters.CharacterTimedActions import BaseAction
from zombie.characters.skills import PerkFactory
from zombie.config import BooleanConfigOption, ConfigOption, StringConfigOption, IntegerConfigOption, DoubleConfigOption
from zombie.core.network import ByteBufferWriter
from zombie.core.raknet import UdpConnection, UdpEngine, VoiceManagerData
from zombie.core.textures import ColorInfo
from zombie.core.utils import UpdateLimit, OnceEvery
from zombie.erosion import ErosionConfig
from zombie.inventory import ItemContainer, InventoryItem
from zombie.inventory.types import Food, HandWeapon
from zombie.iso import IsoDirections, Vector2, IsoMovingObject, IsoObject, IsoMetaGrid, IsoGridSquare, IsoObjectSyncRequests, ObjectsSyncRequests, IsoChunk, BuildingDef, Vector3
from zombie.iso.areas import SafeHouse, NonPvpZone
from zombie.iso.objects import IsoWindow, IsoCompost, BSFurnace, IsoDeadBody
from zombie.iso.objects.interfaces import Thumpable
from zombie.network.packets import PlayerPacket, ZombiePacket, ValidatePacket, DeadPlayerPacket, SyncSafehousePacket, RequestDataPacket
from zombie.network.packets.hit import Hit, IPositional, Zombie, Character, IMovable, Player
from zombie.scripting.objects import Recipe
from zombie.vehicles import BaseVehicle

K = TypeVar('K', default=Any)
V = TypeVar('V', default=Any)
T = TypeVar('T', default=Any)
U = TypeVar('U', default=Any)

class BodyDamageSync:

  BD_additionalPain: int

  BD_alcoholicBandage: int

  BD_alcoholLevel: int

  BD_bandaged: int

  BD_bandageLife: int

  BD_bandageType: int

  BD_biteTime: int

  BD_bitten: int

  BD_bleeding: int

  BD_bleedingTime: int

  BD_BodyDamage: int

  BD_burnTime: int

  BD_comfreyFactor: int

  BD_cut: int

  BD_cutTime: int

  BD_deepWounded: int

  BD_deepWoundTime: int

  BD_fractureTime: int

  BD_garlicFactor: int

  BD_getBandageXp: int

  BD_getSplintXp: int

  BD_getStitchXp: int

  BD_haveBullet: int

  BD_haveGlass: int

  BD_Health: int

  BD_infectedWound: int

  BD_IsBleedingStemmed: int

  BD_IsCortorised: int

  BD_IsFakeInfected: int

  BD_IsInfected: int

  BD_lastTimeBurnWash: int

  BD_needBurnWash: int

  BD_plantainFactor: int

  BD_scratched: int

  BD_scratchTime: int

  BD_splint: int

  BD_splintFactor: int

  BD_splintItem: int

  BD_stiffness: int

  BD_stitched: int

  BD_stitchTime: int

  BD_woundInfectionLevel: int

  instance: BodyDamageSync

  def clientPacket(self, bb: ByteBuffer) -> None: ...

  def serverPacket(self, bb: ByteBuffer) -> None: ...

  def startReceivingUpdates(self, remoteID: int) -> None: ...

  def startSendingUpdates(self, localIndex: int, remoteID: int) -> None: ...

  def stopReceivingUpdates(self, remoteID: int) -> None: ...

  def stopSendingUpdates(self, localIndex: int, remoteID: int) -> None: ...

  def update(self) -> None: ...

  def __init__(self): ...

  class Updater:

    @overload
    def updateField(self, id: int, value: bool) -> None: ...

    @overload
    def updateField(self, id: int, value: str) -> None: ...

    @overload
    def updateField(self, id: int, value1: float, value2: float) -> bool: ...

    def __init__(self): ...


class ChunkChecksum:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def createChecksum(filename: str) -> int: ...

  @staticmethod
  def getChecksum(wx: int, wy: int) -> int: ...

  @staticmethod
  def getChecksumIfExists(wx: int, wy: int) -> int: ...

  @staticmethod
  def setChecksum(wx: int, wy: int, crc: int) -> None: ...

  def __init__(self): ...


class ClientChunkRequest:

  freeBuffers: ConcurrentLinkedQueue[ByteBuffer]

  def getByteBuffer(self, chunk: ClientChunkRequest.Chunk) -> None: ...

  def getChunk(self) -> ClientChunkRequest.Chunk: ...

  def releaseBuffer(self, chunk: ClientChunkRequest.Chunk) -> None: ...

  def releaseBuffers(self) -> None: ...

  def releaseChunk(self, chunk: ClientChunkRequest.Chunk) -> None: ...

  def unpack(self, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  def unpackLargeArea(self, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  def __init__(self):
    self.chunks: ArrayList[ClientChunkRequest.Chunk]
    self.largearea: bool

  class Chunk:

    def __init__(self):
      self.bb: ByteBuffer
      self.crc: int
      self.requestnumber: int
      self.wx: int
      self.wy: int


class ClientServerMap:

  def getMaxX(self) -> int: ...

  def getMaxY(self) -> int: ...

  def getMinX(self) -> int: ...

  def getMinY(self) -> int: ...

  def isValidCell(self, x: int, y: int) -> bool: ...

  def sendPacket(self, connection: UdpConnection) -> None: ...

  def setLoaded(self) -> bool: ...

  def setPlayerPosition(self, squareX: int, squareY: int) -> bool: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def characterIn(connection: UdpConnection, playerIndex: int) -> None: ...

  @staticmethod
  def isChunkLoaded(wx: int, wy: int) -> bool: ...

  @staticmethod
  def receivePacket(bb: ByteBuffer) -> None: ...

  @staticmethod
  def render(playerIndex: int) -> None: ...

  def __init__(self, playerIndex: int, squareX: int, squareY: int, chunkGridWidth: int): ...


class ConnectionDetails:

  @staticmethod
  def parse(b: ByteBuffer) -> None: ...

  @staticmethod
  def write(connection: UdpConnection, logonResult: ServerWorldDatabase.LogonResult, bb: ByteBuffer) -> None: ...

  def __init__(self): ...


class ConnectionManager:

  @staticmethod
  def log(event: str, message: str, connection: UdpConnection) -> None: ...

  def __init__(self): ...


class CoopMaster:

  instance: CoopMaster

  def abortServer(self) -> None: ...

  @overload
  def addListener(self, listener: ICoopServerMessageListener) -> None: ...

  @overload
  def addListener(self, listener: ICoopServerMessageListener, options: CoopMaster.ListenerOptions) -> None: ...

  def getMessage(self) -> str: ...

  def getPlayerSaveFolder(self, serverName: str) -> str: ...

  def getServerName(self) -> str: ...

  def getServerPort(self) -> int: ...

  def getServerSaveFolder(self, serverName: str) -> str: ...

  def invokeServer(self, tag: str, payload: str, responseHandler: ICoopServerMessageListener) -> None: ...

  def isRunning(self) -> bool: ...

  def launchServer(self, serverName: str, username: str, memory: int) -> None: ...

  def register(self, platform: Platform, environment: KahluaTable) -> None: ...

  def removeListener(self, listener: ICoopServerMessageListener) -> None: ...

  @overload
  def sendMessage(self, tag: str, payload: str) -> None: ...

  @overload
  def sendMessage(self, tag: str, cookie: str, payload: str) -> None: ...

  def softreset(self, serverName: str, username: str, memory: int) -> None: ...

  def terminationReason(self) -> CoopMaster.TerminationReason: ...

  def update(self) -> None: ...

  class TerminationReason(Enum):

    NormalTermination: CoopMaster.TerminationReason

    Timeout: CoopMaster.TerminationReason

    @staticmethod
    def valueOf(arg0: str) -> CoopMaster.TerminationReason: ...

    @staticmethod
    def values() -> list[CoopMaster.TerminationReason]: ...

  class ListenerOptions:

    @overload
    def __init__(self, arg0: CoopMaster, arg1: str):
      self.autoremove: bool

      self.cookie: str

      self.tag: str

    @overload
    def __init__(self, arg0: CoopMaster, arg1: str, arg2: str): ...
    @overload
    def __init__(self, arg0: CoopMaster, arg1: str, arg2: str, arg3: bool): ...

  class Pair[K, V]:

    def getFirst(self) -> object: ...

    def getSecond(self) -> object: ...

    def __init__(self, arg0: CoopMaster, arg1: object, arg2: object): ...


class CoopSlave:

  instance: CoopSlave

  def getHostUser(self) -> str: ...

  def handleCommand(self, command: str) -> bool: ...

  def isHost(self, steamID: int) -> bool: ...

  def isInvited(self, friendSteamID: int) -> bool: ...

  def masterLost(self) -> bool: ...

  def notify(self, notification: str) -> None: ...

  def sendExternalIPAddress(self, cookie: str) -> None: ...

  @overload
  def sendMessage(self, message: str) -> None: ...

  @overload
  def sendMessage(self, tag: str, cookie: str, payload: str) -> None: ...

  def sendStatus(self, status: str) -> None: ...

  def sendSteamID(self, cookie: str) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def initStreams() -> None: ...

  @staticmethod
  def status(status: str) -> None: ...


class DBResult:

  def getColumns(self) -> ArrayList[str]: ...

  def getTableName(self) -> str: ...

  def getType(self) -> str: ...

  def getValues(self) -> HashMap[str, str]: ...

  def setColumns(self, columns: ArrayList[str]) -> None: ...

  def setTableName(self, tableName: str) -> None: ...

  def setType(self, type: str) -> None: ...

  def __init__(self): ...


class DBSchema:

  def getFullTable(self) -> KahluaTable: ...

  def getSchema(self) -> HashMap[str, HashMap[str, str]]: ...

  def setFullTable(self, fullTable: KahluaTable) -> None: ...

  def __init__(self, conn: Connection): ...


class DBTicket:

  def getAnswer(self) -> DBTicket: ...

  def getAuthor(self) -> str: ...

  def getMessage(self) -> str: ...

  def getTicketID(self) -> int: ...

  def isAnswer(self) -> bool: ...

  def isViewed(self) -> bool: ...

  def setAnswer(self, answer: DBTicket) -> None: ...

  def setAuthor(self, author: str) -> None: ...

  def setIsAnswer(self, isAnswer: bool) -> None: ...

  def setMessage(self, message: str) -> None: ...

  def setTicketID(self, ticketID: int) -> None: ...

  def setViewed(self, viewed: bool) -> None: ...

  def __init__(self, author: str, message: str, ticketID: int): ...


class DesktopBrowser:

  @staticmethod
  def openURL(arg0: str) -> bool: ...

  def __init__(self): ...


class DiscordBot:

  def connect(self, enabled: bool, token: str, channelName: str, channelID: str) -> None: ...

  def sendMessage(self, user: str, msg: str) -> None: ...

  def __init__(self, serverName: str, s: DiscordSender): ...

  class Connector:

    @overload
    def onFailure(self, arg0: Throwable) -> None: ...

    @overload
    def onFailure(self, arg0: Throwable) -> None: ...

    @overload
    def onSuccess(self, arg0: DiscordAPI) -> None: ...

    @overload
    def onSuccess(self, arg0: object) -> None: ...

    @overload
    def onSuccess(self, arg0: object) -> None: ...

  class Listener:

    @overload
    def onMessageCreate(self, arg0: DiscordAPI, arg1: Message) -> None: ...

    @overload
    def onMessageCreate(self, arg0: DiscordAPI, arg1: Message) -> None: ...


class DiscordSender:

  def sendMessageFromDiscord(self, user: str, msg: str) -> None: ...


class FakeClientManager:

  @staticmethod
  def ReadStringUTF(input: ByteBuffer) -> str: ...

  @staticmethod
  def WriteStringUTF(output: ByteBuffer, str: str) -> None: ...

  @staticmethod
  def getConnectedGUID() -> int: ...

  @staticmethod
  def getOnlineID() -> int: ...

  @staticmethod
  def isVOIPEnabled() -> bool: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self): ...

  class StringUTF: ...

  class Movement:

    def checkDisconnect(self) -> bool: ...

    def checkReconnect(self) -> bool: ...

    def connect(self, arg0: int) -> None: ...

    def disconnect(self, arg0: int) -> None: ...

    def doDisconnect(self) -> bool: ...

    def doReconnect(self) -> bool: ...

    def doTeleport(self) -> bool: ...

    def __init__(self, arg0: int, arg1: str, arg2: int, arg3: int, arg4: FakeClientManager.Movement.Motion, arg5: int, arg6: FakeClientManager.Movement.Type, arg7: int, arg8: int, arg9: int, arg10: IsoDirections, arg11: bool, arg12: int, arg13: int, arg14: int, arg15: int, arg16: FakeClientManager.HordeCreator, arg17: FakeClientManager.SoundMaker): ...

    class Motion(Enum):

      Aim: FakeClientManager.Movement.Motion

      Pedestrian: FakeClientManager.Movement.Motion

      Run: FakeClientManager.Movement.Motion

      Sneak: FakeClientManager.Movement.Motion

      SneakRun: FakeClientManager.Movement.Motion

      Sprint: FakeClientManager.Movement.Motion

      Vehicle: FakeClientManager.Movement.Motion

      Walk: FakeClientManager.Movement.Motion

      @staticmethod
      def valueOf(arg0: str) -> FakeClientManager.Movement.Motion: ...

      @staticmethod
      def values() -> list[FakeClientManager.Movement.Motion]: ...

    class Type(Enum):

      AIAttackZombies: FakeClientManager.Movement.Type

      AINormal: FakeClientManager.Movement.Type

      AIRunAwayFromZombies: FakeClientManager.Movement.Type

      AIRunToAnotherPlayers: FakeClientManager.Movement.Type

      Circle: FakeClientManager.Movement.Type

      Line: FakeClientManager.Movement.Type

      Stay: FakeClientManager.Movement.Type

      @staticmethod
      def valueOf(arg0: str) -> FakeClientManager.Movement.Type: ...

      @staticmethod
      def values() -> list[FakeClientManager.Movement.Type]: ...

  class Client:

    luaChecksum: str

    scriptChecksum: str

    def sendCommand(self, arg0: str) -> None: ...

    class State(Enum):

      CHECKSUM: FakeClientManager.Client.State

      CONNECT: FakeClientManager.Client.State

      DISCONNECT: FakeClientManager.Client.State

      LOAD: FakeClientManager.Client.State

      LOGIN: FakeClientManager.Client.State

      PLAYER_CONNECT: FakeClientManager.Client.State

      PLAYER_EXTRA_INFO: FakeClientManager.Client.State

      QUIT: FakeClientManager.Client.State

      RUN: FakeClientManager.Client.State

      WAIT: FakeClientManager.Client.State

      @staticmethod
      def valueOf(arg0: str) -> FakeClientManager.Client.State: ...

      @staticmethod
      def values() -> list[FakeClientManager.Client.State]: ...

    class Request: ...

  class ZombieSimulator:

    behaviour: FakeClientManager.ZombieSimulator.Behaviour

    canSeeZombieDistanceSquared: int

    deleteZombieDistanceSquared: int

    forgotZombieDistanceSquared: int

    maxZombiesPerUpdate: int

    seeZombieDistanceSquared: int

    def add(self, arg0: int) -> None: ...

    def becomeLocal(self, arg0: FakeClientManager.Zombie) -> None: ...

    def becomeRemote(self, arg0: FakeClientManager.Zombie) -> None: ...

    def clear(self) -> None: ...

    def process(self) -> None: ...

    def receivePacket(self, arg0: ByteBuffer) -> None: ...

    def send(self) -> None: ...

    def simulateAll(self) -> None: ...

    def update(self) -> None: ...

    def __init__(self, arg0: FakeClientManager.Player): ...

    class Behaviour(Enum):

      Attack: FakeClientManager.ZombieSimulator.Behaviour

      Normal: FakeClientManager.ZombieSimulator.Behaviour

      Stay: FakeClientManager.ZombieSimulator.Behaviour

      @staticmethod
      def valueOf(arg0: str) -> FakeClientManager.ZombieSimulator.Behaviour: ...

      @staticmethod
      def values() -> list[FakeClientManager.ZombieSimulator.Behaviour]: ...

  class Player:

    class Clothes: ...

  class HordeCreator:

    def getCommand(self, arg0: int, arg1: int, arg2: int) -> str: ...

    def __init__(self, arg0: int, arg1: int, arg2: int): ...

  class SoundMaker:

    def __init__(self, arg0: int, arg1: int, arg2: str): ...

  class Network: ...

  class PlayerManager:

    def __init__(self, arg0: FakeClientManager.Player):
      self.players: HashMap[Integer, FakeClientManager.PlayerManager.RemotePlayer]

    class RemotePlayer:

      def __init__(self, arg0: FakeClientManager.PlayerManager, arg1: int):
        self.onlineid: int
        self.playerpacket: PlayerPacket
        self.x: float
        self.y: float
        self.z: float

  class Zombie:

    def __init__(self, arg0: int):
      self.dir: IsoDirections
      self.droppositionx: float
      self.droppositiony: float
      self.health: float
      self.ismoving: bool
      self.lastupdate: int
      self.localownership: bool
      self.onlineid: int
      self.walktype: int
      self.x: float
      self.y: float
      self.z: float
      self.zombiepacket: ZombiePacket


class GameClient:

  allChatMuted: bool

  askPing: bool

  bClient: bool

  bCoopInvite: bool

  bFastForward: bool

  bIngame: bool

  checksum: str

  checksumValid: bool

  connection: UdpConnection

  count: int

  DEFAULT_PORT: int

  GameMap: str

  IDToPlayerMap: HashMap[Short, IsoPlayer]

  IDToZombieMap: TShortObjectHashMap[IsoZombie]

  instance: GameClient

  ip: str

  loadedCells: list[ClientServerMap]

  localIP: str

  password: str

  pingsList: List[Long]

  poisonousBerry: str

  poisonousMushroom: str

  port: int

  positions: Map[Short, Vector2]

  ServerName: str

  serverPassword: str

  ServerPredictedAhead: float

  startAuth: Calendar

  steamID: int

  username: str

  useSteamRelay: bool

  def GameLoadingRequestData(self) -> None: ...

  def PlaySound(self, name: str, loop: bool, object: IsoMovingObject) -> None: ...

  def PlayWorldSound(self, name: str, x: int, y: int, z: int) -> None: ...

  def Shutdown(self) -> None: ...

  def StopSound(self, object: IsoMovingObject, soundName: str, trigger: bool) -> None: ...

  def acceptTrading(self, you: IsoPlayer, other: IsoPlayer, accept: bool) -> None: ...

  def addDisconnectPacket(self, packet: int) -> None: ...

  def addIncoming(self, id: int, bb: ByteBuffer) -> None: ...

  def addToItemRemoveSendBuffer(self, parent: IsoObject, container: ItemContainer, item: InventoryItem) -> None: ...

  def addToItemSendBuffer(self, parent: IsoObject, container: ItemContainer, item: InventoryItem) -> None: ...

  def addUserlog(self, user: str, type: str, text: str) -> None: ...

  def addWarningPoint(self, user: str, reason: str, amount: int) -> None: ...

  def canConnect(self) -> bool: ...

  def checkAddedRemovedItems(self, aboutToRemove: IsoObject) -> None: ...

  def connectionLost(self) -> None: ...

  def disconnect(self) -> None: ...

  def doConnect(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, arg7: bool) -> None: ...

  def doConnectCoop(self, serverSteamID: str) -> None: ...

  def doDisconnect(self, string: str) -> None: ...

  def drink(self, player: IsoPlayer, drink: float) -> None: ...

  def eatFood(self, player: IsoPlayer, food: Food, percentage: float) -> None: ...

  def equip(self, player: IsoPlayer, i: int) -> None: ...

  def executeQuery(self, query: str, params: KahluaTable) -> None: ...

  def getConnectedPlayers(self) -> ArrayList[IsoPlayer]: ...

  def getDBSchema(self) -> None: ...

  def getPlayerByOnlineID(self, id: int) -> IsoPlayer: ...

  def getPlayerFromUsername(self, username: str) -> IsoPlayer: ...

  def getPlayers(self) -> ArrayList[IsoPlayer]: ...

  def getReconnectCountdownTimer(self) -> str: ...

  def getServerSpawnRegions(self) -> KahluaTable: ...

  def getTableResult(self, tableName: str, numberPerPages: int) -> None: ...

  def heartBeat(self) -> None: ...

  def init(self) -> None: ...

  def loadResetID(self) -> None: ...

  def receivePlayerConnectWhileLoading(self, bb: ByteBuffer) -> bool: ...

  def removeUserlog(self, user: str, type: str, text: str) -> None: ...

  def removeZombieFromCache(self, z: IsoZombie) -> None: ...

  def requestPacketCounts(self) -> None: ...

  def requestTrading(self, you: IsoPlayer, other: IsoPlayer) -> None: ...

  def requestUserlog(self, user: str) -> None: ...

  def resetDisconnectTimer(self) -> None: ...

  def scoreboardUpdate(self) -> None: ...

  def sendAddXp(self, otherPlayer: IsoPlayer, perk: PerkFactory.Perk, amount: int) -> None: ...

  def sendAddedRemovedItems(self, force: bool) -> None: ...

  def sendAdditionalPain(self, onlineID: int, i: int, level: float) -> None: ...

  def sendAttachedItem(self, player: IsoPlayer, location: str, item: InventoryItem) -> None: ...

  def sendBandage(self, onlineID: int, i: int, bandaged: bool, bandageLife: float, isAlcoholic: bool, bandageType: str) -> None: ...

  def sendCataplasm(self, onlineID: int, i: int, plantainFactor: float, comfreyFactor: float, garlicFactor: float) -> None: ...

  def sendChangedPlayerStats(self, otherPlayer: IsoPlayer) -> None: ...

  def sendCleanBurn(self, _wielder: IsoGameCharacter, _target: IsoGameCharacter, bodyPart: BodyPart, _bandage: InventoryItem) -> None: ...

  def sendClientCommand(self, player: IsoPlayer, module: str, command: str, args: KahluaTable) -> None: ...

  def sendClientCommandV(self, arg0: IsoPlayer, arg1: str, arg2: str, arg3: list[object]) -> None: ...

  def sendClothing(self, player: IsoPlayer, location: str, item: InventoryItem) -> None: ...

  def sendCustomColor(self, item: IsoObject) -> None: ...

  def sendDisinfect(self, wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, alcohol: InventoryItem) -> None: ...

  def sendItemStats(self, item: InventoryItem) -> None: ...

  def sendLoginQueueDone2(self, dt: int) -> None: ...

  def sendLoginQueueRequest2(self) -> None: ...

  def sendPersonalColor(self, player: IsoPlayer) -> None: ...

  def sendPlayer(self, isoPlayer: IsoPlayer) -> None: ...

  def sendPlayer2(self, isoPlayer: IsoPlayer) -> None: ...

  def sendPlayerConnect(self, player: IsoPlayer) -> None: ...

  def sendPlayerSave(self, player: IsoPlayer) -> None: ...

  def sendRemoveBullet(self, wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart) -> None: ...

  def sendRemoveGlass(self, wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, handPain: bool) -> None: ...

  def sendReplaceOnCooked(self, item: InventoryItem) -> None: ...

  def sendSandboxOptionsToServer(self, options: SandboxOptions) -> None: ...

  def sendSplint(self, onlineID: int, i: int, doIt: bool, factor: float, splintItem: str) -> None: ...

  def sendStitch(self, wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, item: InventoryItem, doIt: bool) -> None: ...

  def sendSyncXp(self, player: IsoPlayer) -> None: ...

  def sendTransactionID(self, player: IsoPlayer) -> None: ...

  def sendVisual(self, player: IsoPlayer) -> None: ...

  def sendWeaponHit(self, player: IsoPlayer, weapon: HandWeapon, object: IsoObject) -> None: ...

  def sendWorldMessage(self, line: str) -> None: ...

  @overload
  def sendWorldSound(self, sound: WorldSoundManager.WorldSound) -> None: ...

  @overload
  def sendWorldSound(self, source: object, x: int, y: int, z: int, radius: int, volume: int, stressHumans: bool, zombieIgnoreDist: float, stressMod: float) -> None: ...

  def sendWoundInfection(self, onlineID: int, i: int, infected: bool) -> None: ...

  def setRequest(self, request: GameClient.RequestState) -> None: ...

  def setResetID(self, resetID: int) -> None: ...

  def smashWindow(self, isoWindow: IsoWindow, action: int) -> None: ...

  def startClient(self) -> None: ...

  def startLocalServer(self) -> None: ...

  def tradingUISendAddItem(self, you: IsoPlayer, other: IsoPlayer, item: InventoryItem) -> None: ...

  def tradingUISendRemoveItem(self, you: IsoPlayer, other: IsoPlayer, index: int) -> None: ...

  def tradingUISendUpdateState(self, you: IsoPlayer, other: IsoPlayer, state: int) -> None: ...

  def update(self) -> None: ...

  def wakeUpPlayer(self, chr: IsoPlayer) -> None: ...

  def writePlayerConnectData(self, b: ByteBufferWriter, player: IsoPlayer) -> None: ...

  @staticmethod
  def IsClientPaused() -> bool: ...

  @staticmethod
  def SendCommandToServer(command: str) -> None: ...

  @staticmethod
  def acceptFactionInvite(faction: Faction, host: str) -> None: ...

  @staticmethod
  def acceptSafehouseInvite(safehouse: SafeHouse, host: str) -> None: ...

  @staticmethod
  def addTicket(author: str, message: str, ticketID: int) -> None: ...

  @staticmethod
  def canModifyPlayerStats() -> bool: ...

  @staticmethod
  def canSeePlayerStats() -> bool: ...

  @staticmethod
  def checksumServer() -> None: ...

  @staticmethod
  def destroy(obj: IsoObject) -> None: ...

  @staticmethod
  def getCustomModData() -> None: ...

  @staticmethod
  def getServerStatisticEnable() -> bool: ...

  @staticmethod
  def getTickets(author: str) -> None: ...

  @staticmethod
  def getZombie(id: int) -> IsoZombie: ...

  @staticmethod
  def invMngRequestItem(itemId: int, itemType: str, player: IsoPlayer) -> None: ...

  @staticmethod
  def invMngRequestRemoveItem(itemId: int, player: IsoPlayer) -> None: ...

  @staticmethod
  def receiveEatBody(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receivePlayerTimeout(playerID: int) -> None: ...

  @staticmethod
  def receiveRadioDeviceDataState(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveRadioPostSilence(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveRadioServerData(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveSyncCustomLightSettings(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveSyncRadioData(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveThump(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveWaveSignal(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def registerZone(zone: IsoMetaGrid.Zone, transmitToOthers: bool) -> None: ...

  @staticmethod
  def removeTicket(ticketID: int) -> None: ...

  @staticmethod
  def sendAction(action: BaseAction, operation: bool) -> None: ...

  @staticmethod
  def sendBuildingStashToDo(stashName: str) -> None: ...

  @staticmethod
  def sendBurnCorpse(playerId: int, objectId: int) -> None: ...

  @staticmethod
  def sendChangeSafety(safety: Safety) -> None: ...

  @staticmethod
  def sendCompost(isoCompost: IsoCompost) -> None: ...

  @staticmethod
  def sendEatBody(zombie: IsoZombie, target: IsoMovingObject) -> None: ...

  @staticmethod
  def sendEquippedRadioFreq(plyr: IsoPlayer) -> None: ...

  @staticmethod
  def sendEvent(isoPlayer: IsoPlayer, event: str) -> None: ...

  @staticmethod
  def sendFaction(faction: Faction, remove: bool) -> None: ...

  @staticmethod
  def sendFactionInvite(faction: Faction, host: IsoPlayer, invited: str) -> None: ...

  @staticmethod
  def sendFurnaceChange(furnace: BSFurnace) -> None: ...

  @staticmethod
  def sendGetItemInvMng(itemId: int) -> None: ...

  @staticmethod
  def sendHitCharacter(wielder: IsoGameCharacter, target: IsoMovingObject, weapon: HandWeapon, damage: float, ignoreDamage: bool, range: float, isCriticalHit: bool, helmetFall: bool, hitHead: bool) -> bool: ...

  @staticmethod
  def sendHitVehicle(wielder: IsoPlayer, target: IsoGameCharacter, vehicle: BaseVehicle, damage: float, isTargetHitFromBehind: bool, vehicleDamage: int, vehicleSpeed: float, isVehicleHitFromBehind: bool) -> None: ...

  @staticmethod
  def sendIsoRegionDataRequest() -> None: ...

  @staticmethod
  def sendIsoWaveSignal(sourceX: int, sourceY: int, channel: int, msg: str, guid: str, codes: str, r: float, g: float, b: float, signalStrength: int, isTV: bool) -> None: ...

  @staticmethod
  def sendItemListNet(sender: IsoPlayer, items: ArrayList[InventoryItem], receiver: IsoPlayer, sessionID: str, custom: str) -> bool: ...

  @staticmethod
  def sendKickOutOfSafehouse(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendNonPvpZone(nonPvpZone: NonPvpZone, remove: bool) -> None: ...

  @staticmethod
  def sendPerks(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendPing() -> None: ...

  @staticmethod
  def sendPlayerDamage(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendPlayerDeath(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendPlayerExtraInfo(p: IsoPlayer) -> None: ...

  @staticmethod
  def sendPlayerInjuries(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendPlayerListensChannel(channel: int, listenmode: bool, isTV: bool) -> None: ...

  @staticmethod
  def sendRadioServerDataRequest() -> None: ...

  @staticmethod
  def sendRemoveCorpseFromMap(deadBody: IsoDeadBody) -> None: ...

  @staticmethod
  def sendRequestInventory(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendSafehouse(safehouse: SafeHouse, remove: bool) -> None: ...

  @staticmethod
  def sendSafehouseInvite(safehouse: SafeHouse, host: IsoPlayer, invited: str) -> None: ...

  @staticmethod
  def sendServerPing(timestamp: int) -> None: ...

  @staticmethod
  def sendSneezingCoughing(playerId: int, sneezingCoughing: int, sneezeVar: int) -> None: ...

  @staticmethod
  @overload
  def sendStopFire(chr: IsoGameCharacter) -> None: ...

  @staticmethod
  @overload
  def sendStopFire(sq: IsoGridSquare) -> None: ...

  @staticmethod
  def sendTeleport(player: IsoPlayer, x: float, y: float, z: float) -> None: ...

  @staticmethod
  def sendThump(zombie: IsoGameCharacter, thumpable: Thumpable) -> None: ...

  @staticmethod
  def sendValidatePacket(packet: ValidatePacket) -> None: ...

  @staticmethod
  def sendWeight(player: IsoPlayer) -> None: ...

  @staticmethod
  def sendZombieDeath(zombie: IsoZombie) -> None: ...

  @staticmethod
  def sendZombieHelmetFall(player: IsoPlayer, zombie: IsoGameCharacter, item: InventoryItem) -> None: ...

  @staticmethod
  def setServerStatisticEnable(enable: bool) -> None: ...

  def __init__(self):
    self.bconnected: bool
    self.bplayerconnectsent: bool
    self.debug_ping: int
    self.erosionconfig: ErosionConfig
    self.id: int
    self.idmapdirty: bool
    self.objectsyncreq: IsoObjectSyncRequests
    self.ping: int
    self.sendzombierequeststimer: UpdateLimit
    self.sendzombietimer: UpdateLimit
    self.servermods: ArrayList[str]
    self.serverspawnregions: KahluaTable
    self.timesincekeepalive: float
    self.timesincelastupdate: int
    self.udpengine: UdpEngine
    self.worldobjectssyncreq: ObjectsSyncRequests

  class RequestState(Enum):

    Complete: GameClient.RequestState

    Loading: GameClient.RequestState

    Start: GameClient.RequestState

    @staticmethod
    def valueOf(arg0: str) -> GameClient.RequestState: ...

    @staticmethod
    def values() -> list[GameClient.RequestState]: ...


class GameServer:

  bCoop: bool

  bDebug: bool

  bFastForward: bool

  bServer: bool

  bSoftReset: bool

  checksum: str

  DebugPlayer: HashSet[UdpConnection]

  DEFAULT_PORT: int

  discordBot: DiscordBot

  FPS: int

  GameMap: str

  GUICommandline: bool

  IDToAddressMap: HashMap[Short, Long]

  IDToPlayerMap: HashMap[Short, IsoPlayer]

  ip: str

  IPCommandline: str

  loginQueue: LoginQueue

  MainThread: Thread

  MAX_PLAYERS: int

  MaxTicksSinceKeepAliveBeforeStall: int

  PacketsUpdateRate: int

  Players: ArrayList[IsoPlayer]

  PortCommandline: int

  removeZombiesConnection: UdpConnection

  ResetID: int

  ServerMods: ArrayList[str]

  ServerName: str

  SteamVACCommandline: Boolean

  tempPlayers: ArrayList[IsoPlayer]

  test: int

  TimeLimitForProcessPackets: int

  timeSinceKeepAlive: float

  transactionIDMap: HashMap[str, Integer]

  udpEngine: UdpEngine

  UDPPort: int

  UDPPortCommandline: int

  WorkshopInstallFolders: list[str]

  WorkshopItems: ArrayList[Long]

  WorkshopTimeStamps: list[int]

  worldObjectsServerSyncReq: ObjectsSyncRequests

  def getDifficulty(self) -> str: ...

  def getPoisonousBerry(self) -> str: ...

  def getPoisonousMushroom(self) -> str: ...

  def setDifficulty(self, difficulty: str) -> None: ...

  def setPoisonousBerry(self, poisonousBerry: str) -> None: ...

  def setPoisonousMushroom(self, poisonousMushroom: str) -> None: ...

  @staticmethod
  def AddExplosiveTrap(weapon: HandWeapon, sq: IsoGridSquare, sensor: bool) -> None: ...

  @staticmethod
  def PauseAllClients() -> None: ...

  @staticmethod
  @overload
  def PlaySoundAtEveryPlayer(name: str) -> None: ...

  @staticmethod
  @overload
  def PlaySoundAtEveryPlayer(name: str, x: int, y: int, z: int) -> None: ...

  @staticmethod
  @overload
  def PlaySoundAtEveryPlayer(name: str, x: int, y: int, z: int, usePlrCoords: bool) -> None: ...

  @staticmethod
  @overload
  def PlayWorldSoundServer(name: str, loop: bool, source: IsoGridSquare, pitchVar: float, radius: float, maxGain: float, ignoreOutside: bool) -> None: ...

  @staticmethod
  @overload
  def PlayWorldSoundServer(character: IsoGameCharacter, name: str, loop: bool, source: IsoGridSquare, pitchVar: float, radius: float, maxGain: float, ignoreOutside: bool) -> None: ...

  @staticmethod
  def PlayWorldSoundWavServer(name: str, loop: bool, source: IsoGridSquare, pitchVar: float, radius: float, maxGain: float, ignoreOutside: bool) -> None: ...

  @staticmethod
  def RemoveItemFromMap(obj: IsoObject) -> int: ...

  @staticmethod
  @overload
  def SyncObjectChunkHashes(bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def SyncObjectChunkHashes(ch: IsoChunk, connection: UdpConnection) -> None: ...

  @staticmethod
  def SyncObjectsGridSquareRequest(bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  def SyncObjectsRequest(bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  def UnPauseAllClients() -> None: ...

  @staticmethod
  def addConnection(con: UdpConnection) -> None: ...

  @staticmethod
  def addDisconnect(con: UdpConnection) -> None: ...

  @staticmethod
  def addIncoming(id: int, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  def addXp(p: IsoPlayer, perk: PerkFactory.Perk, xp: int) -> None: ...

  @staticmethod
  def disconnect(connection: UdpConnection, description: str) -> None: ...

  @staticmethod
  def disconnectPlayer(player: IsoPlayer, connection: UdpConnection) -> None: ...

  @staticmethod
  def doMinimumInit() -> None: ...

  @staticmethod
  def doZomboidDataInMainLoop(d: ZomboidNetData) -> None: ...

  @staticmethod
  def getAnyPlayerFromConnection(connection: UdpConnection) -> IsoPlayer: ...

  @staticmethod
  def getConnectionByPlayerOnlineID(onlineID: int) -> UdpConnection: ...

  @staticmethod
  def getConnectionFromPlayer(player: IsoPlayer) -> UdpConnection: ...

  @staticmethod
  def getFreeSlot() -> int: ...

  @staticmethod
  def getPlayerByRealUserName(username: str) -> IsoPlayer: ...

  @staticmethod
  def getPlayerByUserName(username: str) -> IsoPlayer: ...

  @staticmethod
  def getPlayerByUserNameForCommand(username: str) -> IsoPlayer: ...

  @staticmethod
  def getPlayerCount() -> int: ...

  @staticmethod
  def getPlayerFromConnection(connection: UdpConnection, playerIndex: int) -> IsoPlayer: ...

  @staticmethod
  @overload
  def getPlayers() -> ArrayList[IsoPlayer]: ...

  @staticmethod
  @overload
  def getPlayers(players: ArrayList[IsoPlayer]) -> ArrayList[IsoPlayer]: ...

  @staticmethod
  def getStatisticFromClients() -> None: ...

  @staticmethod
  def heartBeat() -> None: ...

  @staticmethod
  def initClientCommandFilter() -> None: ...

  @staticmethod
  def isServerDropPackets() -> bool: ...

  @staticmethod
  def isSpawnBuilding(arg0: BuildingDef) -> bool: ...

  @staticmethod
  def kick(connection: UdpConnection, description: str, reason: str) -> None: ...

  @staticmethod
  def loadModData(sq: IsoGridSquare) -> None: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  @staticmethod
  def rcon(command: str) -> str: ...

  @staticmethod
  def receiveClientConnect(connection: UdpConnection, r: ServerWorldDatabase.LogonResult) -> None: ...

  @staticmethod
  def receiveEatBody(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveKickOutOfSafehouse(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receivePlayerListensChannel(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveRadioDeviceDataState(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveRadioServerData(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveSyncCustomLightSettings(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveSyncRadioData(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveThump(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveWaveSignal(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveWorldMapPlayerPosition(arg0: ByteBuffer, arg1: UdpConnection, arg2: int) -> None: ...

  @staticmethod
  def sendAddItemToContainer(container: ItemContainer, item: InventoryItem) -> None: ...

  @staticmethod
  def sendAdminMessage(message: str, x: int, y: int, z: int) -> None: ...

  @staticmethod
  def sendAlarm(x: int, y: int) -> None: ...

  @staticmethod
  def sendAmbient(name: str, x: int, y: int, radius: int, volume: float) -> None: ...

  @staticmethod
  def sendBecomeCorpse(body: IsoDeadBody) -> None: ...

  @staticmethod
  def sendBloodSplatter(weapon: HandWeapon, x: float, y: float, z: float, hitDir: Vector2, closeKilled: bool, radial: bool) -> None: ...

  @staticmethod
  def sendChangeSafety(safety: Safety) -> None: ...

  @staticmethod
  def sendCompost(compost: IsoCompost, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendCorpse(body: IsoDeadBody) -> None: ...

  @staticmethod
  def sendFuranceChange(furnace: BSFurnace, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendHelicopter(x: float, y: float, active: bool) -> None: ...

  @staticmethod
  def sendIsoWaveSignal(source: int, sourceX: int, sourceY: int, channel: int, msg: str, guid: str, codes: str, r: float, g: float, b: float, signalStrength: int, isTV: bool) -> None: ...

  @staticmethod
  def sendItemListNet(ignore: UdpConnection, sender: IsoPlayer, items: ArrayList[InventoryItem], receiver: IsoPlayer, sessionID: str, custom: str) -> bool: ...

  @staticmethod
  def sendItemsInContainer(o: IsoObject, container: ItemContainer) -> None: ...

  @staticmethod
  @overload
  def sendMetaGrid(cellX: int, cellY: int, roomID: int) -> None: ...

  @staticmethod
  @overload
  def sendMetaGrid(cellX: int, cellY: int, roomID: int, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendNonPvpZone(zone: NonPvpZone, remove: bool, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendObjectChange(arg0: IsoObject, arg1: str, arg2: list[object]) -> None: ...

  @staticmethod
  @overload
  def sendObjectChange(o: IsoObject, change: str, tbl: KahluaTable) -> None: ...

  @staticmethod
  def sendObjectModData(o: IsoObject) -> None: ...

  @staticmethod
  def sendOptionsToClients() -> None: ...

  @staticmethod
  def sendPlayerConnect(p: IsoPlayer, c: UdpConnection) -> None: ...

  @staticmethod
  def sendPlayerDamage(player: IsoPlayer, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendPlayerDamagedByCarCrash(chr: IsoPlayer, damage: float) -> None: ...

  @staticmethod
  def sendPlayerDeath(packet: DeadPlayerPacket, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendPlayerExtraInfo(p: IsoPlayer, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendRadioPostSilence() -> None: ...

  @staticmethod
  @overload
  def sendRadioPostSilence(c: UdpConnection) -> None: ...

  @staticmethod
  def sendReanimatedZombieID(player: IsoPlayer, zombie: IsoZombie) -> None: ...

  @staticmethod
  def sendRemoveCorpseFromMap(deadBody: IsoDeadBody) -> None: ...

  @staticmethod
  def sendRemoveItemFromContainer(container: ItemContainer, item: InventoryItem) -> None: ...

  @staticmethod
  def sendSafehouse(packet: SyncSafehousePacket, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendServerCommand(module: str, command: str, args: KahluaTable) -> None: ...

  @staticmethod
  @overload
  def sendServerCommand(module: str, command: str, args: KahluaTable, c: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendServerCommand(player: IsoPlayer, module: str, command: str, args: KahluaTable) -> None: ...

  @staticmethod
  def sendServerCommandV(arg0: str, arg1: str, arg2: list[object]) -> None: ...

  @staticmethod
  @overload
  def sendShortStatistic() -> None: ...

  @staticmethod
  @overload
  def sendShortStatistic(c: UdpConnection) -> None: ...

  @staticmethod
  def sendSlowFactor(chr: IsoGameCharacter) -> None: ...

  @staticmethod
  @overload
  def sendStatistic() -> None: ...

  @staticmethod
  @overload
  def sendStatistic(c: UdpConnection) -> None: ...

  @staticmethod
  def sendTeleport(player: IsoPlayer, x: float, y: float, z: float) -> None: ...

  @staticmethod
  def sendValidatePacket(connection: UdpConnection, queued: bool, done: bool, details: bool) -> None: ...

  @staticmethod
  def sendWakeUpPlayer(player: IsoPlayer, connection: UdpConnection) -> None: ...

  @staticmethod
  def sendWeather() -> None: ...

  @staticmethod
  def sendWorldMapPlayerPosition() -> None: ...

  @staticmethod
  @overload
  def sendWorldSound(sound: WorldSoundManager.WorldSound, connection: UdpConnection) -> None: ...

  @staticmethod
  @overload
  def sendWorldSound(connection: UdpConnection, sound: WorldSoundManager.WorldSound) -> None: ...

  @staticmethod
  def sendZombieDeath(zombie: IsoZombie) -> None: ...

  @staticmethod
  def sendZombieSound(sound: IsoZombie.ZombieSound, zombie: IsoZombie) -> None: ...

  @staticmethod
  def sendZone(zone: IsoMetaGrid.Zone, connection: UdpConnection) -> None: ...

  @staticmethod
  def setupCoop() -> None: ...

  @staticmethod
  def smashWindow(isoWindow: IsoWindow, action: int) -> None: ...

  @staticmethod
  def startFireOnClient(gridSquare: IsoGridSquare, fireStartingEnergy: int, igniteOnAny: bool, Life: int, smoke: bool) -> None: ...

  @staticmethod
  def startRain() -> None: ...

  @staticmethod
  def startServer() -> None: ...

  @staticmethod
  def stopRain() -> None: ...

  @staticmethod
  def syncClock() -> None: ...

  @staticmethod
  def transmitBrokenGlass(sq: IsoGridSquare) -> None: ...

  @staticmethod
  def updateOverlayForClients(object: IsoObject, spriteName: str, r: float, g: float, b: float, a: float, playerConnection: UdpConnection) -> None: ...

  @staticmethod
  def updateZombieControl(zombie: IsoZombie, variableParam: int, value: int) -> None: ...

  def __init__(self): ...

  class DelayedConnection:

    @overload
    def isConnect(self) -> bool: ...

    @overload
    def isConnect(self) -> bool: ...

    @overload
    def isDisconnect(self) -> bool: ...

    @overload
    def isDisconnect(self) -> bool: ...

    def __init__(self, arg0: UdpConnection, arg1: bool):
      self.connect: bool
      self.connection: UdpConnection
      self.hoststring: str

  class s_performance: ...

  class CCFilter: ...


class GameServerWorkshopItems:

  @staticmethod
  def Install(itemIDList: ArrayList[Long]) -> bool: ...

  def __init__(self): ...

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

  class WorkshopInstallState(Enum):

    CheckItemState: GameServerWorkshopItems.WorkshopInstallState

    DownloadPending: GameServerWorkshopItems.WorkshopInstallState

    Fail: GameServerWorkshopItems.WorkshopInstallState

    Ready: GameServerWorkshopItems.WorkshopInstallState

    @staticmethod
    def valueOf(arg0: str) -> GameServerWorkshopItems.WorkshopInstallState: ...

    @staticmethod
    def values() -> list[GameServerWorkshopItems.WorkshopInstallState]: ...

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


class ICoopServerMessageListener:

  def OnCoopServerMessage(self, tag: str, cookie: str, payload: str) -> None: ...


class IZomboidPacket:

  def isConnect(self) -> bool: ...

  def isDisconnect(self) -> bool: ...


class IsoObjectID[T]:

  incorrect: int

  def allocateID(self) -> int: ...

  def clear(self) -> None: ...

  def forEach(self, arg0: Consumer[T]) -> None: ...

  def get(self, id: int) -> object: ...

  def getObjects(self, out: Collection[T]) -> None: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  @overload
  def iterator(self) -> Iterator[T]: ...

  def put(self, arg0: int, arg1: object) -> None: ...

  @overload
  def remove(self, arg0: object) -> None: ...

  @overload
  def remove(self, id: int) -> None: ...

  def size(self) -> int: ...

  def spliterator(self) -> Spliterator[T]: ...

  def __init__(self, cls: Class[T]): ...


class ItemTransactionManager:

  @staticmethod
  def createItemTransaction(itemID: int, srcID: int, dstID: int) -> None: ...

  @staticmethod
  def isConsistent(itemID: int, srcID: int, dstID: int) -> bool: ...

  @staticmethod
  def receiveOnClient(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveOnServer(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def removeItemTransaction(itemID: int, srcID: int, dstID: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...

  class ItemRequest: ...


class LoginQueue:

  @staticmethod
  def disconnect(connection: UdpConnection) -> None: ...

  @staticmethod
  def getDescription() -> str: ...

  @staticmethod
  def isInTheQueue(connection: UdpConnection) -> bool: ...

  @staticmethod
  def receiveClientLoginQueueRequest(bb: ByteBuffer, packetType: int) -> None: ...

  @staticmethod
  def receiveLogin(connection: UdpConnection) -> bool: ...

  @staticmethod
  def receiveLoginQueueDone(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def receiveServerLoginQueueRequest(bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...

  class LoginQueueMessageType(Enum):

    ConnectionImmediate: LoginQueue.LoginQueueMessageType

    PlaceInQueue: LoginQueue.LoginQueueMessageType

    @staticmethod
    def valueOf(arg0: str) -> LoginQueue.LoginQueueMessageType: ...

    @staticmethod
    def values() -> list[LoginQueue.LoginQueueMessageType]: ...


class MD5Checksum:

  @staticmethod
  def createChecksum(filename: str) -> int: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self): ...


class MPStatistic:

  clientStatisticEnable: bool

  instance: MPStatistic

  def IncrementLoadCellFromDisk(self) -> None: ...

  def IncrementSaveCellToDisk(self) -> None: ...

  def IncrementServerChunkThreadSaveNow(self) -> None: ...

  def addIncomePacket(self, packetType: PacketTypes.PacketType, size: int) -> None: ...

  def addOutcomePacket(self, ID: int, size: int) -> None: ...

  def count1(self, counter: int) -> None: ...

  def count2(self, counter: int) -> None: ...

  def count3(self, counter: int) -> None: ...

  def getStatisticTable(self, bb: ByteBuffer) -> None: ...

  def getStatisticTableForLua(self) -> KahluaTable: ...

  def printEnabled(self, enabled: bool) -> None: ...

  def process(self, updatePeriod: int) -> None: ...

  def setPacketsLength(self, size: int) -> None: ...

  def setPeriod(self, period: int) -> None: ...

  def setStatisticTable(self, bb: ByteBuffer) -> None: ...

  def teleport(self) -> None: ...

  def write(self, bb: ByteBufferWriter) -> None: ...

  def writeEnabled(self, enabled: bool) -> None: ...

  @staticmethod
  def getInstance() -> MPStatistic: ...

  @staticmethod
  def getStatisticDir() -> str: ...

  def __init__(self):
    self.animationplayerupdate: MPStatistic.ProbeStatistic
    self.bullet: MPStatistic.ProbeStatistic
    self.chunkchecksum: MPStatistic.ProbeStatistic
    self.ingamestateupdate: MPStatistic.ProbeStatistic
    self.loaderthread: MPStatistic.ThreadStatistic
    self.loaderthreadtasks: MPStatistic.TasksStatistic
    self.main: MPStatistic.MainThreadStatistic
    self.mapcollisionthread: MPStatistic.ThreadStatistic
    self.playerdownloadserver: MPStatistic.ThreadStatistic
    self.polypaththread: MPStatistic.ThreadStatistic
    self.recalcallthread: MPStatistic.ThreadStatistic
    self.recalcthreadtasks: MPStatistic.TasksStatistic
    self.savetasks: MPStatistic.SaveTasksStatistic
    self.savethread: MPStatistic.ThreadStatistic
    self.serverlos: MPStatistic.ThreadStatistic
    self.servermaploaded2: MPStatistic.ServerCellStatistic
    self.servermaploadedcells: MPStatistic.ServerCellStatistic
    self.servermappostupdate: MPStatistic.ProbeStatistic
    self.servermappreupdate: MPStatistic.ProbeStatistic
    self.servermaptoload: MPStatistic.ServerCellStatistic
    self.worldreuser: MPStatistic.ThreadStatistic

  class TasksStatistic:

    def Added(self) -> None: ...

    def Clear(self) -> None: ...

    def Print(self) -> str: ...

    def PrintTitle(self, name: str) -> str: ...

    def Processed(self) -> None: ...

    def __init__(self): ...

  class SaveTasksStatistic(MPStatistic.TasksStatistic):

    def Clear(self) -> None: ...

    def Print(self) -> str: ...

    def PrintTitle(self, name: str) -> str: ...

    def QuitThreadTasksAdded(self) -> None: ...

    def SaveGameTimeTasksAdded(self) -> None: ...

    def SaveLoadedTasksAdded(self) -> None: ...

    def SaveUnloadedTasksAdded(self) -> None: ...

    def __init__(self): ...

  class ServerCellStatistic:

    @overload
    def Added(self) -> None: ...

    @overload
    def Added(self, n: int) -> None: ...

    def Canceled(self) -> None: ...

    def Clear(self) -> None: ...

    def Print(self) -> str: ...

    def PrintTitle(self, name: str) -> str: ...

    def __init__(self): ...

  class MainThreadStatistic(MPStatistic.ThreadStatistic):

    def End(self) -> None: ...

    def EndSleep(self) -> None: ...

    def Start(self) -> None: ...

    def StartSleep(self) -> None: ...

    def __init__(self, arg0: MPStatistic): ...

  class ThreadStatistic:

    def Clear(self) -> None: ...

    def End(self) -> None: ...

    def Print(self) -> str: ...

    def PrintTitle(self, name: str) -> str: ...

    def Start(self) -> None: ...

    def __init__(self): ...

  class ProbeStatistic:

    def Clear(self) -> None: ...

    def End(self) -> None: ...

    def Print(self) -> str: ...

    def PrintTitle(self, name: str) -> str: ...

    def Start(self) -> None: ...

    def __init__(self): ...


class MPStatisticClient:

  instance: MPStatisticClient

  def fpsProcess(self) -> None: ...

  def getFPS(self) -> float: ...

  def incrementRemotePlayersTeleports(self) -> None: ...

  def incrementZombiesTeleports(self) -> None: ...

  def send(self, b: ByteBufferWriter) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def getInstance() -> MPStatisticClient: ...

  def __init__(self): ...


class MPStatistics:

  @staticmethod
  def Init() -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def Update() -> None: ...

  @staticmethod
  def clientZombieCulled() -> None: ...

  @staticmethod
  def clientZombieUpdated() -> None: ...

  @staticmethod
  def countChunkRequests(sent: int, requested1: int, requested2: int, pending1: int, pending2: int) -> None: ...

  @staticmethod
  def countServerNetworkingFPS() -> None: ...

  @staticmethod
  def decreaseRelevantChunk() -> None: ...

  @staticmethod
  def decreaseStoredChunk() -> None: ...

  @staticmethod
  def doKick(connection: UdpConnection, ping: int) -> bool: ...

  @staticmethod
  def doKickWhileLoading(connection: UdpConnection, ping: int) -> bool: ...

  @staticmethod
  def getLuaStatistics() -> KahluaTable: ...

  @staticmethod
  def getLuaStatus() -> KahluaTable: ...

  @staticmethod
  def increaseRelevantChunk() -> None: ...

  @staticmethod
  def increaseStoredChunk() -> None: ...

  @staticmethod
  def parse(bb: ByteBuffer) -> None: ...

  @staticmethod
  def requested() -> None: ...

  @staticmethod
  def serverZombieCulled() -> None: ...

  @staticmethod
  def serverZombieUpdated() -> None: ...

  @staticmethod
  def setVOIPSource(source: VoiceManagerData.VoiceDataSource, freq: int) -> None: ...

  @staticmethod
  def write(connection: UdpConnection, bb: ByteBuffer) -> None: ...

  def __init__(self): ...


class MPStatisticsTest:

  def TestAveragePingIsEqualToLimit(self) -> None: ...

  def TestAveragePingIsGreaterThanLimit(self) -> None: ...

  def TestAveragePingIsLessThanLimit(self) -> None: ...

  def TestAveragePingIsSlightlyGreaterThanLimit(self) -> None: ...

  def TestAveragePingIsSlightlyLessThanLimit(self) -> None: ...

  def TestEnoughPingIntervals(self) -> None: ...

  def TestEnoughPingSpikes(self) -> None: ...

  def TestKick(self) -> None: ...

  def TestKickGraceInterval(self) -> None: ...

  def TestKickIsNotFullyConnected(self) -> None: ...

  def TestKickWhileLoadingWhenConnectionIsAdmin(self) -> None: ...

  def TestKickWhileLoadingWhenConnectionIsPreferredInQueue(self) -> None: ...

  def TestKickWhileLoadingWhenKickIsDisabledViaMinValue(self) -> None: ...

  def TestNotEnoughPingIntervals(self) -> None: ...

  def TestNotEnoughPingSpikes(self) -> None: ...

  def TestSeveralHugeSpikesDoesNotExceedTheLimit(self) -> None: ...

  def TestSeveralHugeSpikesEqualToLimit(self) -> None: ...

  def TestSeveralHugeSpikesExceedTheLimit(self) -> None: ...

  def TestTheLatestDataIsUsedForCounting(self) -> None: ...

  def reset(self) -> None: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class NetChecksum:

  checksummer: NetChecksum.Checksummer

  comparer: NetChecksum.Comparer

  def __init__(self): ...

  class Checksummer:

    def addFile(self, relPath: str, absPath: str) -> None: ...

    def checksumToString(self) -> str: ...

    def reset(self, convertLineEndings: bool) -> None: ...

    def toString(self) -> str: ...

    def __init__(self): ...

  class Comparer:

    def beginCompare(self) -> None: ...

    def clientPacket(self, bb: ByteBuffer) -> None: ...

    def getReason(self, arg0: int) -> str: ...

    def serverPacket(self, bb: ByteBuffer, connection: UdpConnection) -> None: ...

    def update(self) -> None: ...

    def __init__(self): ...

    class State(Enum):

      Failed: NetChecksum.Comparer.State

      Init: NetChecksum.Comparer.State

      SentFileChecksums: NetChecksum.Comparer.State

      SentGroupChecksum: NetChecksum.Comparer.State

      SentTotalChecksum: NetChecksum.Comparer.State

      Success: NetChecksum.Comparer.State

      @staticmethod
      def valueOf(arg0: str) -> NetChecksum.Comparer.State: ...

      @staticmethod
      def values() -> list[NetChecksum.Comparer.State]: ...

  class GroupOfFiles:

    def toString(self) -> str: ...

    @staticmethod
    def finishChecksum() -> None: ...

    @staticmethod
    def gc() -> None: ...

    @staticmethod
    def initChecksum() -> None: ...


class NetworkAIParams:

  CHARACTER_EXTRAPOLATION_UPDATE_INTERVAL_MS: int

  CHARACTER_PREDICTION_INTERVAL_MS: int

  CHARACTER_UPDATE_RATE_MS: int

  MAX_RECONNECT_DISTANCE_SQ: float

  MAX_TOWING_CAR_DISTANCE_SQ: float

  MAX_TOWING_TRAILER_DISTANCE_SQ: float

  TIME_VALIDATION_DELAY: int

  TIME_VALIDATION_INTERVAL: int

  TIME_VALIDATION_TIMEOUT: int

  TOWING_DISTANCE: float

  VEHICLE_BUFFER_DELAY_MS: int

  VEHICLE_BUFFER_HISTORY_MS: int

  VEHICLE_MOVING_MP_PHYSIC_UPDATE_RATE: int

  VEHICLE_MP_PHYSIC_UPDATE_RATE: int

  VEHICLE_SPEED_CAP: int

  ZOMBIE_ANTICIPATORY_UPDATE_MULTIPLIER: float

  ZOMBIE_MAX_UPDATE_INTERVAL_MS: int

  ZOMBIE_MIN_UPDATE_INTERVAL_MS: int

  ZOMBIE_OWNERSHIP_INTERVAL: int

  ZOMBIE_REMOVE_INTERVAL_MS: int

  ZOMBIE_TELEPORT_DISTANCE_SQ: int

  ZOMBIE_TELEPORT_PLAYER: int

  ZOMBIE_UPDATE_INFO_BUNCH_RATE_MS: int

  @staticmethod
  def Init() -> None: ...

  @staticmethod
  def isShowConnectionInfo() -> bool: ...

  @staticmethod
  def isShowPingInfo() -> bool: ...

  @staticmethod
  def isShowServerInfo() -> bool: ...

  @staticmethod
  def setShowConnectionInfo(enabled: bool) -> None: ...

  @staticmethod
  def setShowPingInfo(enabled: bool) -> None: ...

  @staticmethod
  def setShowServerInfo(enabled: bool) -> None: ...

  def __init__(self): ...


class NetworkVariables:

  def __init__(self): ...

  class ZombieState(Enum):

    Attack: NetworkVariables.ZombieState

    AttackNetwork: NetworkVariables.ZombieState

    AttackVehicle: NetworkVariables.ZombieState

    AttackVehicleNetwork: NetworkVariables.ZombieState

    Bumped: NetworkVariables.ZombieState

    ClimbFence: NetworkVariables.ZombieState

    ClimbWindow: NetworkVariables.ZombieState

    EatBody: NetworkVariables.ZombieState

    FaceTarget: NetworkVariables.ZombieState

    FakeDead: NetworkVariables.ZombieState

    FakeDeadAttack: NetworkVariables.ZombieState

    FakeDeadAttackNetwork: NetworkVariables.ZombieState

    FakeZombieAttack: NetworkVariables.ZombieState

    FakeZombieNormal: NetworkVariables.ZombieState

    FakeZombieStay: NetworkVariables.ZombieState

    FallDown: NetworkVariables.ZombieState

    Falling: NetworkVariables.ZombieState

    GetDown: NetworkVariables.ZombieState

    Getup: NetworkVariables.ZombieState

    HitReaction: NetworkVariables.ZombieState

    HitReactionHit: NetworkVariables.ZombieState

    HitWhileStaggered: NetworkVariables.ZombieState

    Idle: NetworkVariables.ZombieState

    Lunge: NetworkVariables.ZombieState

    LungeNetwork: NetworkVariables.ZombieState

    OnGround: NetworkVariables.ZombieState

    PathFind: NetworkVariables.ZombieState

    Sitting: NetworkVariables.ZombieState

    StaggerBack: NetworkVariables.ZombieState

    Thump: NetworkVariables.ZombieState

    TurnAlerted: NetworkVariables.ZombieState

    WalkToward: NetworkVariables.ZombieState

    WalkTowardNetwork: NetworkVariables.ZombieState

    def toString(self) -> str: ...

    @staticmethod
    def fromByte(zombieState: Byte) -> NetworkVariables.ZombieState: ...

    @staticmethod
    def fromString(zombieState: str) -> NetworkVariables.ZombieState: ...

    @staticmethod
    def valueOf(arg0: str) -> NetworkVariables.ZombieState: ...

    @staticmethod
    def values() -> list[NetworkVariables.ZombieState]: ...

  class ThumpType(Enum):

    TTBang: NetworkVariables.ThumpType

    TTClaw: NetworkVariables.ThumpType

    TTDoor: NetworkVariables.ThumpType

    TTNone: NetworkVariables.ThumpType

    def toString(self) -> str: ...

    @staticmethod
    def fromByte(thumpType: Byte) -> NetworkVariables.ThumpType: ...

    @staticmethod
    def fromString(thumpType: str) -> NetworkVariables.ThumpType: ...

    @staticmethod
    def valueOf(arg0: str) -> NetworkVariables.ThumpType: ...

    @staticmethod
    def values() -> list[NetworkVariables.ThumpType]: ...

  class WalkType(Enum):

    WT1: NetworkVariables.WalkType

    WT2: NetworkVariables.WalkType

    WT3: NetworkVariables.WalkType

    WT4: NetworkVariables.WalkType

    WT5: NetworkVariables.WalkType

    WTSlow1: NetworkVariables.WalkType

    WTSlow2: NetworkVariables.WalkType

    WTSlow3: NetworkVariables.WalkType

    WTSprint1: NetworkVariables.WalkType

    WTSprint2: NetworkVariables.WalkType

    WTSprint3: NetworkVariables.WalkType

    WTSprint4: NetworkVariables.WalkType

    WTSprint5: NetworkVariables.WalkType

    def toString(self) -> str: ...

    @staticmethod
    def fromByte(walkType: int) -> NetworkVariables.WalkType: ...

    @staticmethod
    def fromString(walkType: str) -> NetworkVariables.WalkType: ...

    @staticmethod
    def valueOf(arg0: str) -> NetworkVariables.WalkType: ...

    @staticmethod
    def values() -> list[NetworkVariables.WalkType]: ...

  class PredictionTypes(Enum):

    Climb: NetworkVariables.PredictionTypes

    Lunge: NetworkVariables.PredictionTypes

    LungeHalf: NetworkVariables.PredictionTypes

    Moving: NetworkVariables.PredictionTypes

    # None: NetworkVariables.PredictionTypes

    PathFind: NetworkVariables.PredictionTypes

    Static: NetworkVariables.PredictionTypes

    Thump: NetworkVariables.PredictionTypes

    Walk: NetworkVariables.PredictionTypes

    WalkHalf: NetworkVariables.PredictionTypes

    @staticmethod
    def fromByte(moveType: int) -> NetworkVariables.PredictionTypes: ...

    @staticmethod
    def valueOf(arg0: str) -> NetworkVariables.PredictionTypes: ...

    @staticmethod
    def values() -> list[NetworkVariables.PredictionTypes]: ...


class PacketTypes:

  ContainerDeadBody: int

  ContainerObject: int

  ContainerVehicle: int

  ContainerWorldObject: int

  packetCountTable: KahluaTable

  packetTypes: Map[Short, PacketTypes.PacketType]

  @staticmethod
  def doPingPacket(bb: ByteBufferWriter) -> None: ...

  @staticmethod
  def getPacketCounts(category: int) -> KahluaTable: ...

  def __init__(self): ...

  class PacketType(Enum):

    AcceptedFactionInvite: PacketTypes.PacketType

    AcceptedSafehouseInvite: PacketTypes.PacketType

    AccessDenied: PacketTypes.PacketType

    ActionPacket: PacketTypes.PacketType

    AddAlarm: PacketTypes.PacketType

    AddAmbient: PacketTypes.PacketType

    AddBrokenGlass: PacketTypes.PacketType

    AddChatTab: PacketTypes.PacketType

    AddCoopPlayer: PacketTypes.PacketType

    AddCorpseToMap: PacketTypes.PacketType

    AddExplosiveTrap: PacketTypes.PacketType

    AddInventoryItemToContainer: PacketTypes.PacketType

    AddItemInInventory: PacketTypes.PacketType

    AddItemToMap: PacketTypes.PacketType

    AdditionalPain: PacketTypes.PacketType

    AddTicket: PacketTypes.PacketType

    AddUserlog: PacketTypes.PacketType

    AddWarningPoint: PacketTypes.PacketType

    AddXP: PacketTypes.PacketType

    AddXpCommand: PacketTypes.PacketType

    AddXpFromPlayerStatsUI: PacketTypes.PacketType

    Bandage: PacketTypes.PacketType

    BecomeCorpse: PacketTypes.PacketType

    BloodSplatter: PacketTypes.PacketType

    BodyDamageUpdate: PacketTypes.PacketType

    BurnCorpse: PacketTypes.PacketType

    Cataplasm: PacketTypes.PacketType

    ChangePlayerStats: PacketTypes.PacketType

    ChangeSafety: PacketTypes.PacketType

    ChangeTextColor: PacketTypes.PacketType

    ChatMessageFromPlayer: PacketTypes.PacketType

    ChatMessageToPlayer: PacketTypes.PacketType

    Checksum: PacketTypes.PacketType

    ChunkObjectState: PacketTypes.PacketType

    CleanBurn: PacketTypes.PacketType

    ClientCommand: PacketTypes.PacketType

    ClimateManagerPacket: PacketTypes.PacketType

    ConstructedZone: PacketTypes.PacketType

    Disinfect: PacketTypes.PacketType

    Drink: PacketTypes.PacketType

    EatBody: PacketTypes.PacketType

    EatFood: PacketTypes.PacketType

    Equip: PacketTypes.PacketType

    EventPacket: PacketTypes.PacketType

    ExecuteQuery: PacketTypes.PacketType

    ExtraInfo: PacketTypes.PacketType

    GetDBSchema: PacketTypes.PacketType

    getModData: PacketTypes.PacketType

    GetTableResult: PacketTypes.PacketType

    GlobalModData: PacketTypes.PacketType

    GlobalModDataRequest: PacketTypes.PacketType

    GlobalObjects: PacketTypes.PacketType

    Helicopter: PacketTypes.PacketType

    HitCharacter: PacketTypes.PacketType

    HumanVisual: PacketTypes.PacketType

    InitPlayerChat: PacketTypes.PacketType

    InvMngGetItem: PacketTypes.PacketType

    InvMngRemoveItem: PacketTypes.PacketType

    InvMngReqItem: PacketTypes.PacketType

    IsoRegionClientRequestFullUpdate: PacketTypes.PacketType

    IsoRegionServerPacket: PacketTypes.PacketType

    ItemStats: PacketTypes.PacketType

    ItemTransaction: PacketTypes.PacketType

    KeepAlive: PacketTypes.PacketType

    Kicked: PacketTypes.PacketType

    KickOutOfSafehouse: PacketTypes.PacketType

    KillZombie: PacketTypes.PacketType

    LoadPlayerProfile: PacketTypes.PacketType

    Login: PacketTypes.PacketType

    LoginQueueDone2: PacketTypes.PacketType

    LoginQueueRequest2: PacketTypes.PacketType

    MessageForAdmin: PacketTypes.PacketType

    MetaGrid: PacketTypes.PacketType

    NotRequiredInZip: PacketTypes.PacketType

    ObjectChange: PacketTypes.PacketType

    ObjectModData: PacketTypes.PacketType

    PacketCounts: PacketTypes.PacketType

    PacketTypeShort: PacketTypes.PacketType

    PassengerMap: PacketTypes.PacketType

    Ping: PacketTypes.PacketType

    PingFromClient: PacketTypes.PacketType

    PlayerAttachedItem: PacketTypes.PacketType

    PlayerConnect: PacketTypes.PacketType

    PlayerConnectedToChat: PacketTypes.PacketType

    PlayerDamage: PacketTypes.PacketType

    PlayerDamageFromCarCrash: PacketTypes.PacketType

    PlayerDataRequest: PacketTypes.PacketType

    PlayerDeath: PacketTypes.PacketType

    PlayerJoinChat: PacketTypes.PacketType

    PlayerLeaveChat: PacketTypes.PacketType

    PlayerListensChannel: PacketTypes.PacketType

    PlayerNotFound: PacketTypes.PacketType

    PlayerSave: PacketTypes.PacketType

    PlayerStartPMChat: PacketTypes.PacketType

    PlayerTimeout: PacketTypes.PacketType

    PlayerUpdate: PacketTypes.PacketType

    PlayerUpdateReliable: PacketTypes.PacketType

    PlaySound: PacketTypes.PacketType

    PlaySoundEveryPlayer: PacketTypes.PacketType

    PlayWorldSound: PacketTypes.PacketType

    RadioDeviceDataState: PacketTypes.PacketType

    RadioPostSilenceEvent: PacketTypes.PacketType

    RadioServerData: PacketTypes.PacketType

    ReadAnnotedMap: PacketTypes.PacketType

    ReceiveCommand: PacketTypes.PacketType

    ReceiveModData: PacketTypes.PacketType

    RegisterZone: PacketTypes.PacketType

    ReloadOptions: PacketTypes.PacketType

    RemoveBlood: PacketTypes.PacketType

    RemoveBullet: PacketTypes.PacketType

    RemoveChatTab: PacketTypes.PacketType

    RemoveContestedItemsFromInventory: PacketTypes.PacketType

    RemoveCorpseFromMap: PacketTypes.PacketType

    RemoveGlass: PacketTypes.PacketType

    RemoveInventoryItemFromContainer: PacketTypes.PacketType

    RemoveItemFromSquare: PacketTypes.PacketType

    RemoveTicket: PacketTypes.PacketType

    RemoveUserlog: PacketTypes.PacketType

    ReplaceOnCooked: PacketTypes.PacketType

    RequestData: PacketTypes.PacketType

    RequestInventory: PacketTypes.PacketType

    RequestItemsForContainer: PacketTypes.PacketType

    RequestLargeAreaZip: PacketTypes.PacketType

    RequestPlayerData: PacketTypes.PacketType

    RequestTrading: PacketTypes.PacketType

    RequestZipList: PacketTypes.PacketType

    SandboxOptions: PacketTypes.PacketType

    ScoreboardUpdate: PacketTypes.PacketType

    SendCustomColor: PacketTypes.PacketType

    SendFactionInvite: PacketTypes.PacketType

    SendInventory: PacketTypes.PacketType

    SendItemListNet: PacketTypes.PacketType

    SendModData: PacketTypes.PacketType

    SendPlayerProfile: PacketTypes.PacketType

    SendSafehouseInvite: PacketTypes.PacketType

    SendTransactionID: PacketTypes.PacketType

    SentChunk: PacketTypes.PacketType

    ServerMap: PacketTypes.PacketType

    ServerQuit: PacketTypes.PacketType

    SledgehammerDestroy: PacketTypes.PacketType

    SlowFactor: PacketTypes.PacketType

    SmashWindow: PacketTypes.PacketType

    SneezeCough: PacketTypes.PacketType

    SpawnRegion: PacketTypes.PacketType

    Splint: PacketTypes.PacketType

    StartFire: PacketTypes.PacketType

    StartPause: PacketTypes.PacketType

    StartRain: PacketTypes.PacketType

    Statistic: PacketTypes.PacketType

    StatisticRequest: PacketTypes.PacketType

    Stitch: PacketTypes.PacketType

    StopFire: PacketTypes.PacketType

    StopPause: PacketTypes.PacketType

    StopRain: PacketTypes.PacketType

    StopSound: PacketTypes.PacketType

    SyncAlarmClock: PacketTypes.PacketType

    SyncClock: PacketTypes.PacketType

    SyncClothing: PacketTypes.PacketType

    SyncCompost: PacketTypes.PacketType

    SyncCustomLightSettings: PacketTypes.PacketType

    SyncDoorKey: PacketTypes.PacketType

    SyncEquippedRadioFreq: PacketTypes.PacketType

    SyncFaction: PacketTypes.PacketType

    SyncFurnace: PacketTypes.PacketType

    SyncInjuries: PacketTypes.PacketType

    SyncIsoObject: PacketTypes.PacketType

    SyncIsoObjectReq: PacketTypes.PacketType

    SyncNonPvpZone: PacketTypes.PacketType

    SyncObjects: PacketTypes.PacketType

    SyncPerks: PacketTypes.PacketType

    SyncRadioData: PacketTypes.PacketType

    SyncSafehouse: PacketTypes.PacketType

    SyncThumpable: PacketTypes.PacketType

    SyncWeight: PacketTypes.PacketType

    SyncWorldObjectsReq: PacketTypes.PacketType

    SyncXP: PacketTypes.PacketType

    Teleport: PacketTypes.PacketType

    Thump: PacketTypes.PacketType

    TimeSync: PacketTypes.PacketType

    TradingUIAddItem: PacketTypes.PacketType

    TradingUIRemoveItem: PacketTypes.PacketType

    TradingUIUpdateState: PacketTypes.PacketType

    UpdateItemSprite: PacketTypes.PacketType

    UpdateOverlaySprite: PacketTypes.PacketType

    Userlog: PacketTypes.PacketType

    Validate: PacketTypes.PacketType

    VehicleAuthorization: PacketTypes.PacketType

    Vehicles: PacketTypes.PacketType

    VehiclesUnreliable: PacketTypes.PacketType

    ViewTickets: PacketTypes.PacketType

    WakeUpPlayer: PacketTypes.PacketType

    WaveSignal: PacketTypes.PacketType

    WeaponHit: PacketTypes.PacketType

    Weather: PacketTypes.PacketType

    WorldMapPlayerPosition: PacketTypes.PacketType

    WorldMessage: PacketTypes.PacketType

    WorldSound: PacketTypes.PacketType

    WoundInfection: PacketTypes.PacketType

    WriteLog: PacketTypes.PacketType

    ZombieControl: PacketTypes.PacketType

    ZombieDeath: PacketTypes.PacketType

    ZombieDescriptors: PacketTypes.PacketType

    ZombieHelmetFalling: PacketTypes.PacketType

    ZombieSimulation: PacketTypes.PacketType

    ZombieSimulationReliable: PacketTypes.PacketType

    ZombieSound: PacketTypes.PacketType

    def doPacket(self, bb: ByteBufferWriter) -> None: ...

    def getId(self) -> int: ...

    def onGameLoadingDealWithNetData(self, bb: ByteBuffer) -> bool: ...

    def onMainLoopHandlePacketInternal(self, bb: ByteBuffer) -> None: ...

    def onServerPacket(self, bb: ByteBuffer, connection: UdpConnection) -> None: ...

    def onUnauthorized(self, connection: UdpConnection) -> None: ...

    def resetStatistics(self) -> None: ...

    def send(self, connection: UdpConnection) -> None: ...

    @staticmethod
    def valueOf(arg0: str) -> PacketTypes.PacketType: ...

    @staticmethod
    def values() -> list[PacketTypes.PacketType]: ...

  class CallbackClientProcess:

    def call(self, bb: ByteBuffer, packetType: int) -> None: ...

  class CallbackServerProcess:

    def call(self, bb: ByteBuffer, connection: UdpConnection, packetType: int) -> None: ...

  class PacketAuthorization:

    class Policy(Enum):

      Ban: PacketTypes.PacketAuthorization.Policy

      Kick: PacketTypes.PacketAuthorization.Policy

      Log: PacketTypes.PacketAuthorization.Policy

      @staticmethod
      def valueOf(arg0: str) -> PacketTypes.PacketAuthorization.Policy: ...

      @staticmethod
      def values() -> list[PacketTypes.PacketAuthorization.Policy]: ...

    class UnauthorizedPacketPolicy:

      def call(self, arg0: UdpConnection, arg1: str) -> None: ...


class PacketValidator:

  def checkSuspiciousActivity(self, arg0: str) -> bool: ...

  def failChecksum(self) -> None: ...

  def failTimeMultiplier(self, multiplier: float) -> None: ...

  def getDescription(self) -> str: ...

  def getSalt(self) -> int: ...

  def isFailed(self) -> bool: ...

  def reset(self) -> None: ...

  def sendChecksum(self, queued: bool, done: bool, details: bool) -> None: ...

  def successChecksum(self) -> None: ...

  def successTimeMultiplier(self) -> None: ...

  def timeoutTimeMultiplier(self) -> None: ...

  def update(self) -> None: ...

  def updateSuspiciousActivityCounter(self) -> None: ...

  @staticmethod
  def checkDamage(connection: UdpConnection, hit: Hit, issuedBy: str) -> bool: ...

  @staticmethod
  def checkLongDistance(connection: UdpConnection, wielder: IPositional, target: IPositional, issuedBy: str) -> bool: ...

  @staticmethod
  def checkOwner(connection: UdpConnection, wielder: Zombie, issuedBy: str) -> bool: ...

  @staticmethod
  def checkPVP(connection: UdpConnection, wielder: str, target: str, issuedBy: str) -> bool: ...

  @staticmethod
  def checkSafehouseAuth(connection: UdpConnection, playerName: str, issuedBy: str) -> bool: ...

  @staticmethod
  def checkShortDistance(connection: UdpConnection, wielder: IPositional, target: IPositional, issuedBy: str) -> bool: ...

  @staticmethod
  def checkSpeed(connection: UdpConnection, movable: IMovable, issuedBy: str) -> bool: ...

  @staticmethod
  def checkTarget(connection: UdpConnection, target: Player, issuedBy: str) -> bool: ...

  @staticmethod
  def checkUser(connection: UdpConnection) -> bool: ...

  @staticmethod
  def doAntiCheatProtection() -> bool: ...

  @staticmethod
  def doBanUser(connection: UdpConnection, issuedBy: str, reason: str) -> None: ...

  @staticmethod
  def doKickUser(arg0: UdpConnection, arg1: str, arg2: str, arg3: str) -> None: ...

  @staticmethod
  def doLogUser(arg0: UdpConnection, arg1: Userlog.UserlogType, arg2: str, arg3: str) -> None: ...

  def __init__(self, connection: UdpConnection):
    self.details: HashMap[str, PacketValidator.RecipeDetails]
    self.detailsfromclient: HashMap[str, PacketValidator.RecipeDetails]

  class RecipeDetails:

    def getCRC(self) -> int: ...

    def getDescription(self) -> str: ...

    def write(self, b: ByteBufferWriter) -> None: ...

    @overload
    def __init__(self, b: ByteBuffer): ...
    @overload
    def __init__(self, name: str, crc: int, timeToMake: int, skills: ArrayList[Recipe.RequiredSkill], sources: ArrayList[Recipe.Source], type: str, module: str, count: int): ...

    class Skill:

      def __init__(self, name: str, value: int): ...

  class CheckState(Enum):

    # None: PacketValidator.CheckState

    Sent: PacketValidator.CheckState

    Success: PacketValidator.CheckState

    @staticmethod
    def valueOf(arg0: str) -> PacketValidator.CheckState: ...

    @staticmethod
    def values() -> list[PacketValidator.CheckState]: ...


class PassengerMap:

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def clientReceivePacket(bb: ByteBuffer) -> None: ...

  @staticmethod
  def isChunkLoaded(vehicle: BaseVehicle, wx: int, wy: int) -> bool: ...

  @staticmethod
  def render(playerIndex: int) -> None: ...

  @staticmethod
  def serverReceivePacket(bb: ByteBuffer, connection: UdpConnection) -> None: ...

  @staticmethod
  def updatePassenger(player: IsoPlayer) -> None: ...

  def __init__(self): ...

  class PassengerLocal: ...

  class DriverLocal: ...

  class PassengerRemote: ...


class PlayerDownloadServer:

  def destroy(self) -> None: ...

  def getWaitingRequests(self) -> int: ...

  def receiveCancelRequest(self, bb: ByteBuffer) -> None: ...

  def receiveRequestArray(self, bb: ByteBuffer) -> None: ...

  def receiveRequestLargeArea(self, bb: ByteBuffer) -> None: ...

  def startConnectionTest(self) -> None: ...

  def update(self) -> None: ...

  def __init__(self, connection: UdpConnection): ...

  class WorkerThread(Thread):

    def run(self) -> None: ...

  class EThreadCommand(Enum):

    Quit: PlayerDownloadServer.EThreadCommand

    RequestLargeArea: PlayerDownloadServer.EThreadCommand

    RequestZipArray: PlayerDownloadServer.EThreadCommand

    @staticmethod
    def valueOf(arg0: str) -> PlayerDownloadServer.EThreadCommand: ...

    @staticmethod
    def values() -> list[PlayerDownloadServer.EThreadCommand]: ...

  class WorkerThreadCommand: ...


class RCONClient:

  def auth(self, password: str) -> bool: ...

  def connect(self, ip: str, port: str) -> bool: ...

  def disconnect(self) -> bool: ...

  def exec(self, command: str) -> str: ...

  def send(self, url: str, text: str) -> bool: ...

  @staticmethod
  def main(args: list[str]) -> None: ...

  def __init__(self): ...

  class RCONMessage: ...


class RCONServer:

  SERVERDATA_AUTH: int

  SERVERDATA_AUTH_RESPONSE: int

  SERVERDATA_EXECCOMMAND: int

  SERVERDATA_RESPONSE_VALUE: int

  def quit(self) -> None: ...

  @staticmethod
  def init(port: int, password: str, isLocal: bool) -> None: ...

  @staticmethod
  def shutdown() -> None: ...

  @staticmethod
  def update() -> None: ...

  class ServerThread(Thread):

    def quit(self) -> None: ...

    def run(self) -> None: ...

    def __init__(self, arg0: RCONServer):
      self.bquit: bool

  class ExecCommand:

    def update(self) -> None: ...

    def __init__(self, arg0: int, arg1: str, arg2: RCONServer.ClientThread):
      self.command: str
      self.id: int
      self.response: str
      self.thread: RCONServer.ClientThread

  class ClientThread(Thread):

    def handleResponse(self, arg0: RCONServer.ExecCommand) -> None: ...

    def quit(self) -> None: ...

    def run(self) -> None: ...

    def __init__(self, arg0: Socket, arg1: str):
      self.bauth: bool
      self.bquit: bool
      self.socket: Socket


class ReplayManager:

  def getState(self) -> ReplayManager.State: ...

  def isPlay(self) -> bool: ...

  def recordPlayerPacket(self, pp: PlayerPacket) -> None: ...

  def startPlayReplay(self, _player: IsoPlayer, filename: str, connection: UdpConnection) -> bool: ...

  def startRecordReplay(self, _player: IsoPlayer, filename: str) -> bool: ...

  def stopPlayReplay(self) -> bool: ...

  def stopRecordReplay(self) -> bool: ...

  def update(self) -> None: ...

  def __init__(self, _player: IsoPlayer): ...

  class State(Enum):

    Playing: ReplayManager.State

    Recording: ReplayManager.State

    Stop: ReplayManager.State

    @staticmethod
    def valueOf(arg0: str) -> ReplayManager.State: ...

    @staticmethod
    def values() -> list[ReplayManager.State]: ...


class RequestDataManager:

  maxLargeFileSize: int

  packSize: int

  smallFileSize: int

  def ACKWasReceived(self, id: RequestDataPacket.RequestID, connection: UdpConnection, bytesTransmitted: int) -> None: ...

  def clear(self) -> None: ...

  def disconnect(self, connection: UdpConnection) -> None: ...

  def putDataForTransmit(self, id: RequestDataPacket.RequestID, connection: UdpConnection, bb: ByteBuffer) -> None: ...

  def receiveClientData(self, id: RequestDataPacket.RequestID, bb: ByteBuffer, fileSize: int, bytesTransmitted: int) -> ByteBuffer: ...

  @staticmethod
  def getInstance() -> RequestDataManager: ...

  class RequestData:

    @overload
    def __init__(self, arg0: RequestDataPacket.RequestID, arg1: int, arg2: int): ...
    @overload
    def __init__(self, arg0: RequestDataPacket.RequestID, arg1: ByteBuffer, arg2: int): ...


class Server:

  def getDescription(self) -> str: ...

  def getIp(self) -> str: ...

  def getLastUpdate(self) -> int: ...

  def getLocalIP(self) -> str: ...

  def getMaxPlayers(self) -> str: ...

  def getMods(self) -> str: ...

  def getName(self) -> str: ...

  def getPing(self) -> str: ...

  def getPlayers(self) -> str: ...

  def getPort(self) -> str: ...

  def getPwd(self) -> str: ...

  def getServerPassword(self) -> str: ...

  def getSteamId(self) -> str: ...

  def getUseSteamRelay(self) -> bool: ...

  def getUserName(self) -> str: ...

  def getVersion(self) -> str: ...

  def isHosted(self) -> bool: ...

  def isOpen(self) -> bool: ...

  def isPasswordProtected(self) -> bool: ...

  def isPublic(self) -> bool: ...

  def setDescription(self, description: str) -> None: ...

  def setHosted(self, hosted: bool) -> None: ...

  def setIp(self, ip: str) -> None: ...

  def setLastUpdate(self, lastUpdate: int) -> None: ...

  def setLocalIP(self, ip: str) -> None: ...

  def setMaxPlayers(self, maxPlayers: str) -> None: ...

  def setMods(self, mods: str) -> None: ...

  def setName(self, name: str) -> None: ...

  def setOpen(self, open: bool) -> None: ...

  def setPasswordProtected(self, pp: bool) -> None: ...

  def setPing(self, ping: str) -> None: ...

  def setPlayers(self, players: str) -> None: ...

  def setPort(self, port: str) -> None: ...

  def setPublic(self, bPublic: bool) -> None: ...

  def setPwd(self, pwd: str) -> None: ...

  def setServerPassword(self, pwd: str) -> None: ...

  def setSteamId(self, steamId: str) -> None: ...

  def setUseSteamRelay(self, arg0: bool) -> None: ...

  def setUserName(self, userName: str) -> None: ...

  def setVersion(self, version: str) -> None: ...

  def __init__(self): ...


class ServerChunkLoader:

  def addJob(self, cell: ServerMap.ServerCell) -> None: ...

  def addRecalcJob(self, cell: ServerMap.ServerCell) -> None: ...

  def addSaveLoadedJob(self, chunk: IsoChunk) -> None: ...

  def addSaveUnloadedJob(self, chunk: IsoChunk) -> None: ...

  def getLoaded(self, loaded: ArrayList[ServerMap.ServerCell]) -> None: ...

  def getRecalc(self, loaded: ArrayList[ServerMap.ServerCell]) -> None: ...

  def quit(self) -> None: ...

  def saveLater(self, gameTime: GameTime) -> None: ...

  def updateSaved(self) -> None: ...

  def __init__(self): ...

  class LoaderThread(Thread):

    def quit(self) -> None: ...

    def run(self) -> None: ...

  class RecalcAllThread(Thread):

    def run(self) -> None: ...

  class SaveChunkThread(Thread):

    def addLoadedJob(self, arg0: IsoChunk) -> None: ...

    def addUnloadedJob(self, arg0: IsoChunk) -> None: ...

    def quit(self) -> None: ...

    def run(self) -> None: ...

    def saveLater(self, arg0: GameTime) -> None: ...

    def saveNow(self, arg0: int, arg1: int) -> None: ...

    def update(self) -> None: ...

  class GetSquare:

    def EnsureSurroundNotNull(self, arg0: int, arg1: int, arg2: int) -> None: ...

    def contains(self, arg0: int, arg1: int, arg2: int) -> bool: ...

    def getChunkForSquare(self, arg0: int, arg1: int) -> IsoChunk: ...

    @overload
    def getGridSquare(self, arg0: int, arg1: int, arg2: int) -> IsoGridSquare: ...

    @overload
    def getGridSquare(self, arg0: int, arg1: int, arg2: int) -> IsoGridSquare: ...

  class QuitThreadTask:

    @overload
    def release(self) -> None: ...

    @overload
    def release(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    @overload
    def wy(self) -> int: ...

  class SaveGameTimeTask:

    @overload
    def release(self) -> None: ...

    @overload
    def release(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    def __init__(self, arg0: ServerChunkLoader, arg1: GameTime): ...

  class SaveLoadedTask:

    @overload
    def release(self) -> None: ...

    @overload
    def release(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    def __init__(self, arg0: ServerChunkLoader, arg1: ClientChunkRequest, arg2: ClientChunkRequest.Chunk): ...

  class SaveUnloadedTask:

    @overload
    def release(self) -> None: ...

    @overload
    def release(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wx(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    @overload
    def wy(self) -> int: ...

    def __init__(self, arg0: ServerChunkLoader, arg1: IsoChunk): ...

  class SaveTask:

    def release(self) -> None: ...

    def save(self) -> None: ...

    def wx(self) -> int: ...

    def wy(self) -> int: ...


class ServerGUI:

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def init2() -> None: ...

  @staticmethod
  def isCreated() -> bool: ...

  @staticmethod
  def shutdown() -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self): ...


class ServerLOS:

  instance: ServerLOS

  def addPlayer(self, player: IsoPlayer) -> None: ...

  def doServerZombieLOS(self, player: IsoPlayer) -> None: ...

  def isCouldSee(self, player: IsoPlayer, sq: IsoGridSquare) -> bool: ...

  def removePlayer(self, player: IsoPlayer) -> None: ...

  def resume(self) -> None: ...

  def start(self) -> None: ...

  def suspend(self) -> None: ...

  def updateLOS(self, player: IsoPlayer) -> None: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...

  class LOSThread(Thread):

    def run(self) -> None: ...

  class PlayerData:

    def __init__(self, arg0: ServerLOS, arg1: IsoPlayer):
      self.player: IsoPlayer
      self.px: int
      self.py: int
      self.pz: int
      self.status: ServerLOS.UpdateStatus
      self.visible: list[list[list[bool]]]

  class UpdateStatus(Enum):

    BusyInLOS: ServerLOS.UpdateStatus

    BusyInMain: ServerLOS.UpdateStatus

    NeverDone: ServerLOS.UpdateStatus

    ReadyInLOS: ServerLOS.UpdateStatus

    ReadyInMain: ServerLOS.UpdateStatus

    WaitingInLOS: ServerLOS.UpdateStatus

    @staticmethod
    def valueOf(arg0: str) -> ServerLOS.UpdateStatus: ...

    @staticmethod
    def values() -> list[ServerLOS.UpdateStatus]: ...

  class ServerLighting:

    @overload
    def bCanSee(self) -> bool: ...

    @overload
    def bCanSee(self) -> bool: ...

    @overload
    def bCanSee(self, canSee: bool) -> None: ...

    @overload
    def bCanSee(self, canSee: bool) -> None: ...

    @overload
    def bCouldSee(self) -> bool: ...

    @overload
    def bCouldSee(self) -> bool: ...

    @overload
    def bCouldSee(self, couldSee: bool) -> None: ...

    @overload
    def bCouldSee(self, couldSee: bool) -> None: ...

    @overload
    def bSeen(self) -> bool: ...

    @overload
    def bSeen(self) -> bool: ...

    @overload
    def bSeen(self, seen: bool) -> None: ...

    @overload
    def bSeen(self, seen: bool) -> None: ...

    @overload
    def darkMulti(self) -> float: ...

    @overload
    def darkMulti(self) -> float: ...

    @overload
    def darkMulti(self, f: float) -> None: ...

    @overload
    def darkMulti(self, f: float) -> None: ...

    @overload
    def getResultLight(self, index: int) -> IsoGridSquare.ResultLight: ...

    @overload
    def getResultLight(self, index: int) -> IsoGridSquare.ResultLight: ...

    @overload
    def lampostTotalB(self) -> float: ...

    @overload
    def lampostTotalB(self) -> float: ...

    @overload
    def lampostTotalB(self, b: float) -> None: ...

    @overload
    def lampostTotalB(self, b: float) -> None: ...

    @overload
    def lampostTotalG(self) -> float: ...

    @overload
    def lampostTotalG(self) -> float: ...

    @overload
    def lampostTotalG(self, g: float) -> None: ...

    @overload
    def lampostTotalG(self, g: float) -> None: ...

    @overload
    def lampostTotalR(self) -> float: ...

    @overload
    def lampostTotalR(self) -> float: ...

    @overload
    def lampostTotalR(self, r: float) -> None: ...

    @overload
    def lampostTotalR(self, r: float) -> None: ...

    @overload
    def lightInfo(self) -> ColorInfo: ...

    @overload
    def lightInfo(self) -> ColorInfo: ...

    @overload
    def lightverts(self, i: int) -> int: ...

    @overload
    def lightverts(self, i: int) -> int: ...

    @overload
    def lightverts(self, i: int, value: int) -> None: ...

    @overload
    def lightverts(self, i: int, value: int) -> None: ...

    @overload
    def reset(self) -> None: ...

    @overload
    def reset(self) -> None: ...

    @overload
    def resultLightCount(self) -> int: ...

    @overload
    def resultLightCount(self) -> int: ...

    @overload
    def targetDarkMulti(self) -> float: ...

    @overload
    def targetDarkMulti(self) -> float: ...

    @overload
    def targetDarkMulti(self, f: float) -> None: ...

    @overload
    def targetDarkMulti(self, f: float) -> None: ...

    def __init__(self): ...


class ServerMap:

  CellSize: int

  ChunksPerCellWidth: int

  instance: ServerMap

  LOSTick: OnceEvery

  TimeTick: OnceEvery

  def QueueQuit(self) -> None: ...

  def QueueSaveAll(self) -> None: ...

  def SaveAll(self) -> None: ...

  @overload
  def characterIn(self, p: IsoPlayer) -> None: ...

  @overload
  def characterIn(self, wx: int, wy: int, chunkGridWidth: int) -> None: ...

  def clearSoftResetChunk(self, chunk: IsoChunk) -> None: ...

  def getCell(self, x: int, y: int) -> ServerMap.ServerCell: ...

  def getChunk(self, wx: int, wy: int) -> IsoChunk: ...

  def getGridSquare(self, x: int, y: int, z: int) -> IsoGridSquare: ...

  def getMaxX(self) -> int: ...

  def getMaxY(self) -> int: ...

  def getMinX(self) -> int: ...

  def getMinY(self) -> int: ...

  def getStartLocation(self, r: ServerWorldDatabase.LogonResult) -> Vector3: ...

  def getUniqueZombieId(self) -> int: ...

  def init(self, metaGrid: IsoMetaGrid) -> None: ...

  def isInLoaded(self, x: float, y: float) -> bool: ...

  def isValidCell(self, x: int, y: int) -> bool: ...

  def loadMapChunk(self, ix: int, iy: int) -> None: ...

  def loadOrKeepRelevent(self, x: int, y: int) -> None: ...

  def physicsCheck(self, x: int, y: int) -> None: ...

  def postupdate(self) -> None: ...

  def preupdate(self) -> None: ...

  def saveZoneInsidePlayerInfluence(self, playerOID: int) -> None: ...

  def setGridSquare(self, x: int, y: int, z: int, sq: IsoGridSquare) -> None: ...

  def setSoftResetChunk(self, chunk: IsoChunk) -> None: ...

  def toServerCellX(self, x: int) -> int: ...

  def toServerCellY(self, y: int) -> int: ...

  def toWorldCellX(self, x: int) -> int: ...

  def toWorldCellY(self, y: int) -> int: ...

  def __init__(self):
    self.bqueuedquit: bool
    self.bqueuedsaveall: bool
    self.bupdatelosthisframe: bool
    self.cellmap: list[ServerMap.ServerCell]
    self.lastsaved: int
    self.loadedcells: ArrayList[ServerMap.ServerCell]
    self.releventnow: ArrayList[ServerMap.ServerCell]
    self.zombiemap: IsoObjectID[IsoZombie]

  class ServerCell:

    def Load2(self) -> bool: ...

    def RecalcAll2(self) -> None: ...

    def Save(self) -> None: ...

    def Unload(self) -> None: ...

    def getChunk(self, arg0: int, arg1: int) -> IsoChunk: ...

    def getWX(self) -> int: ...

    def getWY(self) -> int: ...

    def update(self) -> None: ...

    def __init__(self):
      self.bcancelloading: bool
      self.bloaded: bool
      self.bloadingwascancelled: bool
      self.bphysicscheck: bool
      self.chunks: list[list[IsoChunk]]
      self.wx: int
      self.wy: int

  class DistToCellComparator:

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: object, arg1: object) -> int: ...

    @overload
    def compare(self, arg0: ServerMap.ServerCell, arg1: ServerMap.ServerCell) -> int: ...

    def equals(self, arg0: object) -> bool: ...

    def init(self) -> None: ...

    def reversed(self) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Comparator[T]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U]) -> Comparator[T]: ...

    @overload
    def thenComparing(self, arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    def thenComparingDouble(self, arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    def thenComparingInt(self, arg0: ToIntFunction[T]) -> Comparator[T]: ...

    def thenComparingLong(self, arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U]) -> Comparator[T]: ...

    @staticmethod
    @overload
    def comparing(arg0: Function[T, U], arg1: Comparator[U]) -> Comparator[T]: ...

    @staticmethod
    def comparingDouble(arg0: ToDoubleFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingInt(arg0: ToIntFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def comparingLong(arg0: ToLongFunction[T]) -> Comparator[T]: ...

    @staticmethod
    def naturalOrder() -> Comparator[T]: ...

    @staticmethod
    def nullsFirst(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def nullsLast(arg0: Comparator[T]) -> Comparator[T]: ...

    @staticmethod
    def reverseOrder() -> Comparator[T]: ...

    def __init__(self): ...


class ServerOptions:

  cardList: ArrayList[str]

  clientOptionsList: HashMap[str, str]

  instance: ServerOptions

  MAX_PORT: int

  def addOption(self, option: ServerOptions.ServerOption) -> None: ...

  def changeOption(self, key: str, value: str) -> str: ...

  def getBoolean(self, key: str) -> Boolean: ...

  def getDouble(self, key: str) -> Double: ...

  def getFloat(self, key: str) -> Float: ...

  def getInteger(self, key: str) -> Integer: ...

  def getMaxPlayers(self) -> int: ...

  def getNumOptions(self) -> int: ...

  def getOption(self, key: str) -> str: ...

  def getOptionByIndex(self, index: int) -> ServerOptions.ServerOption: ...

  def getOptionByName(self, name: str) -> ServerOptions.ServerOption: ...

  def getOptions(self) -> ArrayList[ServerOptions.ServerOption]: ...

  def getPublicOptions(self) -> ArrayList[str]: ...

  def init(self) -> None: ...

  def loadServerTextFile(self, serverName: str) -> bool: ...

  def putOption(self, key: str, value: str) -> None: ...

  def putSaveOption(self, key: str, value: str) -> None: ...

  def resetRegionFile(self) -> None: ...

  def saveServerTextFile(self, serverName: str) -> bool: ...

  @staticmethod
  def getClientCommandList(doLine: bool) -> ArrayList[str]: ...

  @staticmethod
  def getInstance() -> ServerOptions: ...

  @staticmethod
  def getRandomCard() -> str: ...

  @staticmethod
  def initClientCommandsHelp() -> None: ...

  def __init__(self):
    self.adminsafehouse: ServerOptions.BooleanServerOption
    self.allowcoop: ServerOptions.BooleanServerOption
    self.allowdestructionbysledgehammer: ServerOptions.BooleanServerOption
    self.allownonasciiusername: ServerOptions.BooleanServerOption
    self.announcedeath: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype1: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype10: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype11: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype12: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype13: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype14: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype15: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype15thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype16: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype17: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype18: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype19: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype2: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype20: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype20thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype21: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype22: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype22thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype23: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype24: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype24thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype2thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype3: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype3thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype4: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype4thresholdmultiplier: ServerOptions.DoubleServerOption
    self.anticheatprotectiontype5: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype6: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype7: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype8: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype9: ServerOptions.BooleanServerOption
    self.anticheatprotectiontype9thresholdmultiplier: ServerOptions.DoubleServerOption
    self.autocreateuserinwhitelist: ServerOptions.BooleanServerOption
    self.backupscount: ServerOptions.IntegerServerOption
    self.backupsonstart: ServerOptions.BooleanServerOption
    self.backupsonversionchange: ServerOptions.BooleanServerOption
    self.backupsperiod: ServerOptions.IntegerServerOption
    self.bankickglobalsound: ServerOptions.BooleanServerOption
    self.bloodsplatlifespandays: ServerOptions.IntegerServerOption
    self.carengineattractionmodifier: ServerOptions.DoubleServerOption
    self.chatstreams: ServerOptions.StringServerOption
    self.clientactionlogs: ServerOptions.StringServerOption
    self.clientcommandfilter: ServerOptions.StringServerOption
    self.constructionpreventslootrespawn: ServerOptions.BooleanServerOption
    self.defaultport: ServerOptions.IntegerServerOption
    self.denyloginonoverloadedserver: ServerOptions.BooleanServerOption
    self.disableradioadmin: ServerOptions.BooleanServerOption
    self.disableradiogm: ServerOptions.BooleanServerOption
    self.disableradioinvisible: ServerOptions.BooleanServerOption
    self.disableradiomoderator: ServerOptions.BooleanServerOption
    self.disableradiooverseer: ServerOptions.BooleanServerOption
    self.disableradiostaff: ServerOptions.BooleanServerOption
    self.disablesafehousewhenplayerconnected: ServerOptions.BooleanServerOption
    self.discordchannel: ServerOptions.StringServerOption
    self.discordchannelid: ServerOptions.StringServerOption
    self.discordenable: ServerOptions.BooleanServerOption
    self.discordtoken: ServerOptions.StringServerOption
    self.displayusername: ServerOptions.BooleanServerOption
    self.doluachecksum: ServerOptions.BooleanServerOption
    self.dropoffwhitelistafterdeath: ServerOptions.BooleanServerOption
    self.faction: ServerOptions.BooleanServerOption
    self.factiondaysurvivedtocreate: ServerOptions.IntegerServerOption
    self.factionplayersrequiredfortag: ServerOptions.IntegerServerOption
    self.fastforwardmultiplier: ServerOptions.DoubleServerOption
    self.globalchat: ServerOptions.BooleanServerOption
    self.hideplayersbehindyou: ServerOptions.BooleanServerOption
    self.hoursforlootrespawn: ServerOptions.IntegerServerOption
    self.itemnumberslimitpercontainer: ServerOptions.IntegerServerOption
    self.kickfastplayers: ServerOptions.BooleanServerOption
    self.knockeddownallowed: ServerOptions.BooleanServerOption
    self.loginqueueconnecttimeout: ServerOptions.IntegerServerOption
    self.loginqueueenabled: ServerOptions.BooleanServerOption
    self.map: ServerOptions.StringServerOption
    self.mapremoteplayervisibility: ServerOptions.IntegerServerOption
    self.maxaccountsperuser: ServerOptions.IntegerServerOption
    self.maxitemsforlootrespawn: ServerOptions.IntegerServerOption
    self.maxplayers: ServerOptions.IntegerServerOption
    self.minutesperpage: ServerOptions.DoubleServerOption
    self.mods: ServerOptions.StringServerOption
    self.mouseovertoseedisplayname: ServerOptions.BooleanServerOption
    self.nofire: ServerOptions.BooleanServerOption
    self.open: ServerOptions.BooleanServerOption
    self.password: ServerOptions.StringServerOption
    self.pauseempty: ServerOptions.BooleanServerOption
    self.perklogs: ServerOptions.BooleanServerOption
    self.pinglimit: ServerOptions.IntegerServerOption
    self.playerbumpplayer: ServerOptions.BooleanServerOption
    self.playerrespawnwithother: ServerOptions.BooleanServerOption
    self.playerrespawnwithself: ServerOptions.BooleanServerOption
    self.playersafehouse: ServerOptions.BooleanServerOption
    self.public: ServerOptions.BooleanServerOption
    self.publicdescription: ServerOptions.TextServerOption
    self.publicname: ServerOptions.StringServerOption
    self.pvp: ServerOptions.BooleanServerOption
    self.pvpfirearmdamagemodifier: ServerOptions.DoubleServerOption
    self.pvpmeleedamagemodifier: ServerOptions.DoubleServerOption
    self.pvpmeleewhilehitreaction: ServerOptions.BooleanServerOption
    self.rconpassword: ServerOptions.StringServerOption
    self.rconport: ServerOptions.IntegerServerOption
    self.removeplayercorpsesoncorpseremoval: ServerOptions.BooleanServerOption
    self.resetid: ServerOptions.IntegerServerOption
    self.safehouseallowfire: ServerOptions.BooleanServerOption
    self.safehouseallowloot: ServerOptions.BooleanServerOption
    self.safehouseallownonresidential: ServerOptions.BooleanServerOption
    self.safehouseallowrespawn: ServerOptions.BooleanServerOption
    self.safehouseallowtrepass: ServerOptions.BooleanServerOption
    self.safehousedaysurvivedtoclaim: ServerOptions.IntegerServerOption
    self.safehouseremovaltime: ServerOptions.IntegerServerOption
    self.safetycooldowntimer: ServerOptions.IntegerServerOption
    self.safetysystem: ServerOptions.BooleanServerOption
    self.safetytoggletimer: ServerOptions.IntegerServerOption
    self.saveworldeveryminutes: ServerOptions.IntegerServerOption
    self.server_browser_announced_ip: ServerOptions.StringServerOption
    self.serverplayerid: ServerOptions.StringServerOption
    self.serverwelcomemessage: ServerOptions.TextServerOption
    self.showfirstandlastname: ServerOptions.BooleanServerOption
    self.showsafety: ServerOptions.BooleanServerOption
    self.sledgehammeronlyinsafehouse: ServerOptions.BooleanServerOption
    self.sleepallowed: ServerOptions.BooleanServerOption
    self.sleepneeded: ServerOptions.BooleanServerOption
    self.sneakmodehidefromotherplayers: ServerOptions.BooleanServerOption
    self.spawnitems: ServerOptions.StringServerOption
    self.spawnpoint: ServerOptions.StringServerOption
    self.speedlimit: ServerOptions.DoubleServerOption
    self.steamscoreboard: ServerOptions.StringServerOption
    self.steamvac: ServerOptions.BooleanServerOption
    self.trashdeleteall: ServerOptions.BooleanServerOption
    self.udpport: ServerOptions.IntegerServerOption
    self.upnp: ServerOptions.BooleanServerOption
    self.voice3d: ServerOptions.BooleanServerOption
    self.voiceenable: ServerOptions.BooleanServerOption
    self.voicemaxdistance: ServerOptions.DoubleServerOption
    self.voicemindistance: ServerOptions.DoubleServerOption
    self.workshopitems: ServerOptions.StringServerOption

  class BooleanServerOption(BooleanConfigOption):

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def getTooltip(self) -> str: ...

    @overload
    def getTooltip(self) -> str: ...

    def __init__(self, owner: ServerOptions, name: str, defaultValue: bool): ...

  class StringServerOption(StringConfigOption):

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def getTooltip(self) -> str: ...

    @overload
    def getTooltip(self) -> str: ...

    def __init__(self, owner: ServerOptions, name: str, defaultValue: str, maxLength: int): ...

  class TextServerOption(StringConfigOption):

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def getTooltip(self) -> str: ...

    @overload
    def getTooltip(self) -> str: ...

    def getType(self) -> str: ...

    def __init__(self, owner: ServerOptions, name: str, defaultValue: str, maxLength: int): ...

  class IntegerServerOption(IntegerConfigOption):

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def getTooltip(self) -> str: ...

    @overload
    def getTooltip(self) -> str: ...

    def __init__(self, owner: ServerOptions, name: str, min: int, max: int, defaultValue: int): ...

  class DoubleServerOption(DoubleConfigOption):

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def asConfigOption(self) -> ConfigOption: ...

    @overload
    def getTooltip(self) -> str: ...

    @overload
    def getTooltip(self) -> str: ...

    def __init__(self, owner: ServerOptions, name: str, min: float, max: float, defaultValue: float): ...

  class ServerOption:

    def asConfigOption(self) -> ConfigOption: ...

    def getTooltip(self) -> str: ...


class ServerPlayersVehicles:

  instance: ServerPlayersVehicles

  def init(self) -> None: ...

  def stop(self) -> None: ...

  def __init__(self): ...

  class SPVThread(Thread):

    def run(self) -> None: ...


class ServerSettings:

  def addSpawnRegion(self, name: str, file: str) -> None: ...

  def clearSpawnRegions(self) -> None: ...

  def deleteFiles(self) -> bool: ...

  def duplicateFiles(self, newName: str) -> bool: ...

  def getErrorMsg(self) -> str: ...

  def getName(self) -> str: ...

  def getNumSpawnRegions(self) -> int: ...

  def getSandboxOptions(self) -> SandboxOptions: ...

  def getServerOptions(self) -> ServerOptions: ...

  def getSpawnRegionFile(self, index: int) -> str: ...

  def getSpawnRegionName(self, index: int) -> str: ...

  def isValid(self) -> bool: ...

  def loadFiles(self) -> bool: ...

  def loadSpawnPointsFile(self, file: str) -> KahluaTable: ...

  def removeSpawnRegion(self, index: int) -> None: ...

  def rename(self, newName: str) -> bool: ...

  def resetToDefault(self) -> None: ...

  def saveFiles(self) -> bool: ...

  def saveSpawnPointsFile(self, file: str, professionsTable: KahluaTable) -> bool: ...

  def __init__(self, name: str): ...


class ServerSettingsManager:

  instance: ServerSettingsManager

  def getNameInSettingsFolder(self, name: str) -> str: ...

  def getSettingsByIndex(self, index: int) -> ServerSettings: ...

  def getSettingsCount(self) -> int: ...

  def getSettingsFolder(self) -> str: ...

  def getSuffixes(self) -> ArrayList[str]: ...

  def isValidName(self, name: str) -> bool: ...

  def isValidNewName(self, newName: str) -> bool: ...

  def readAllSettings(self) -> None: ...

  def __init__(self): ...


class ServerWorldDatabase:

  instance: ServerWorldDatabase

  def addTicket(self, author: str, message: str, ticketID: int) -> None: ...

  def addUser(self, user: str, arg1: str) -> str: ...

  def addUserlog(self, username: str, type: Userlog.UserlogType, text: str, issuedBy: str, amount: int) -> None: ...

  def addWarningPoint(self, username: str, reason: str, amount: int, issuedBy: str) -> str: ...

  @overload
  def authClient(self, steamID: int) -> ServerWorldDatabase.LogonResult: ...

  @overload
  def authClient(self, user: str, arg1: str, ip: str, steamID: int) -> ServerWorldDatabase.LogonResult: ...

  def authOwner(self, steamID: int, ownerID: int) -> ServerWorldDatabase.LogonResult: ...

  def banIp(self, ip: str, username: str, reason: str, ban: bool) -> str: ...

  def banSteamID(self, steamID: str, reason: str, ban: bool) -> str: ...

  def banUser(self, username: str, ban: bool) -> str: ...

  def changePwd(self, username: str, previousPwd: str, newPwd: str) -> str: ...

  def changeUsername(self, user: str, newUsername: str) -> str: ...

  def close(self) -> None: ...

  def containsCaseinsensitiveUser(self, user: str) -> bool: ...

  def containsUser(self, user: str) -> bool: ...

  def create(self) -> None: ...

  def executeQuery(self, query: str, params: KahluaTable) -> None: ...

  def getDBSchema(self) -> DBSchema: ...

  def getDisplayName(self, username: str) -> str: ...

  def getTableResult(self, table: str) -> ArrayList[DBResult]: ...

  def getTickets(self, playerName: str) -> ArrayList[DBTicket]: ...

  def getUserlog(self, username: str) -> ArrayList[Userlog]: ...

  def grantAdmin(self, username: str, setAdmin: bool) -> str: ...

  def removeTicket(self, ticketID: int) -> None: ...

  def removeUser(self, username: str) -> str: ...

  def removeUserLog(self, username: str, type: str, text: str) -> None: ...

  def saveAllTransactionsID(self, map: HashMap[str, Integer]) -> None: ...

  def saveTransactionID(self, username: str, transactionID: Integer) -> None: ...

  def setAccessLevel(self, username: str, accessLevel: str) -> str: ...

  def setPassword(self, username: str, password: str) -> None: ...

  def setUserSteamID(self, user: str, steamID: str) -> str: ...

  def updateDisplayName(self, user: str, displayName: str) -> None: ...

  def updateLastConnectionDate(self, u: str, p: str) -> None: ...

  @staticmethod
  def encrypt(previousPwd: str) -> str: ...

  @staticmethod
  def isValidUserName(user: str) -> bool: ...

  def __init__(self):
    self.commandlineadminpassword: str
    self.commandlineadminusername: str
    self.dbschema: DBSchema
    self.doadmin: bool

  class LogonResult:

    def __init__(self, arg0: ServerWorldDatabase):
      self.accesslevel: str
      self.admin: bool
      self.banned: bool
      self.bannedreason: str
      self.bauthorized: bool
      self.dcreason: str
      self.newuser: bool
      self.priority: bool
      self.transactionid: int
      self.x: int
      self.y: int
      self.z: int


class SpawnRegions:

  def getDefaultServerPoints(self) -> ArrayList[SpawnRegions.Profession]: ...

  def getDefaultServerRegions(self) -> ArrayList[SpawnRegions.Region]: ...

  def loadPointsFile(self, fileName: str) -> ArrayList[SpawnRegions.Profession]: ...

  def loadPointsTable(self, fileName: str) -> KahluaTable: ...

  def loadRegionsFile(self, fileName: str) -> ArrayList[SpawnRegions.Region]: ...

  def savePointsFile(self, fileName: str, professions: ArrayList[SpawnRegions.Profession]) -> bool: ...

  def savePointsTable(self, fileName: str, professionsTable: KahluaTable) -> bool: ...

  def saveRegionsFile(self, fileName: str, regions: ArrayList[SpawnRegions.Region]) -> bool: ...

  def __init__(self): ...

  class Region:

    def __init__(self):
      self.file: str
      self.name: str
      self.professions: ArrayList[SpawnRegions.Profession]
      self.serverfile: str

  class Profession:

    def __init__(self):
      self.name: str
      self.points: ArrayList[SpawnRegions.Point]

  class Point:

    def __init__(self):
      self.posx: int
      self.posy: int
      self.posz: int
      self.worldx: int
      self.worldy: int


class TableNetworkUtils:

  @staticmethod
  def canSave(key: object, value: object) -> bool: ...

  @staticmethod
  @overload
  def load(input: ByteBuffer, sbyt: int) -> object: ...

  @staticmethod
  @overload
  def load(tbl: KahluaTable, input: ByteBuffer) -> None: ...

  @staticmethod
  def save(tbl: KahluaTable, output: ByteBuffer) -> None: ...

  @staticmethod
  def saveSome(tbl: KahluaTable, output: ByteBuffer, keys: HashSet[Any]) -> None: ...

  def __init__(self): ...


class Userlog:

  def getAmount(self) -> int: ...

  def getIssuedBy(self) -> str: ...

  def getLastUpdate(self) -> str: ...

  def getText(self) -> str: ...

  def getType(self) -> str: ...

  def getUsername(self) -> str: ...

  def setAmount(self, amount: int) -> None: ...

  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: int, arg5: str): ...

  class UserlogType(Enum):

    AdminLog: Userlog.UserlogType

    Banned: Userlog.UserlogType

    DupeItem: Userlog.UserlogType

    Kicked: Userlog.UserlogType

    LuaChecksum: Userlog.UserlogType

    SuspiciousActivity: Userlog.UserlogType

    UnauthorizedPacket: Userlog.UserlogType

    WarningPoint: Userlog.UserlogType

    def index(self) -> int: ...

    @staticmethod
    def FromString(str: str) -> Userlog.UserlogType: ...

    @staticmethod
    def fromIndex(value: int) -> Userlog.UserlogType: ...

    @staticmethod
    def valueOf(arg0: str) -> Userlog.UserlogType: ...

    @staticmethod
    def values() -> list[Userlog.UserlogType]: ...


class WorldItemTypes:

  @staticmethod
  def createFromBuffer(bb: ByteBuffer) -> IsoObject: ...

  def __init__(self): ...


class ZomboidNetData:

  @overload
  def isConnect(self) -> bool: ...

  @overload
  def isConnect(self) -> bool: ...

  @overload
  def isDisconnect(self) -> bool: ...

  @overload
  def isDisconnect(self) -> bool: ...

  def read(self, id: int, bb: ByteBuffer, connection: UdpConnection) -> None: ...

  def reset(self) -> None: ...

  @overload
  def __init__(self):
    self.buffer: ByteBuffer

    self.connection: int

    self.length: int

    self.time: int

    self.type: PacketTypes.PacketType

  @overload
  def __init__(self, size: int): ...


class ZomboidNetDataPool:

  instance: ZomboidNetDataPool

  def discard(self, data: ZomboidNetData) -> None: ...

  def get(self) -> ZomboidNetData: ...

  def getLong(self, len: int) -> ZomboidNetData: ...

  def __init__(self): ...

