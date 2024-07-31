from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.nio import ByteBuffer
from java.nio.file import Path
from java.util import List, ArrayList
from se.krka.kahlua.vm import KahluaTable
from zombie.core.textures import Texture
from zombie.debug import LogSeverity

class CallbackManager:

  @overload
  def onJoinRequest(self, friendSteamID: int, connectionString: str) -> None: ...

  @overload
  def onJoinRequest(self, friendSteamID: int, connectionString: str) -> None: ...

  def __init__(self): ...


class GameServerDetails:

  @overload
  def __init__(self):
    self.address: str

    self.gamedescription: str

    self.gamedir: str

    self.map: str

    self.maxplayers: int

    self.name: str

    self.numplayers: int

    self.passwordprotected: bool

    self.ping: int

    self.port: int

    self.steamid: int

    self.tags: str

    self.version: int

  @overload
  def __init__(self, address: str, port: int, steamId: int, name: str, gamedir: str, map: str, gameDescription: str, tags: str, ping: int, numPlayers: int, maxPlayers: int, passwordProtected: bool, version: int): ...


class IJoinRequestCallback:

  def onJoinRequest(self, friendSteamID: int, connectionString: str) -> None: ...


class IServerBrowserCallback:

  def OnRefreshComplete(self) -> None: ...

  @overload
  def OnServerFailedToRespond(self, serverIndex: int) -> None: ...

  @overload
  def OnServerFailedToRespond(self, host: str, port: int) -> None: ...

  @overload
  def OnServerResponded(self, serverIndex: int) -> None: ...

  @overload
  def OnServerResponded(self, host: str, port: int) -> None: ...

  def OnSteamRulesRefreshComplete(self, host: str, port: int) -> None: ...


class ISteamWorkshopCallback:

  def onItemCreated(self, itemID: int, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...

  def onItemDownloaded(self, itemID: int) -> None: ...

  def onItemNotCreated(self, result: int) -> None: ...

  def onItemNotDownloaded(self, itemID: int, result: int) -> None: ...

  def onItemNotSubscribed(self, itemID: int, result: int) -> None: ...

  def onItemNotUpdated(self, result: int) -> None: ...

  def onItemQueryCompleted(self, handle: int, numResults: int) -> None: ...

  def onItemQueryNotCompleted(self, handle: int, result: int) -> None: ...

  def onItemSubscribed(self, itemID: int) -> None: ...

  def onItemUpdated(self, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...


class PortMapper:

  @staticmethod
  @overload
  def addMapping(wanPort: int, lanPort: int, description: str, proto: str, leaseTime: int) -> bool: ...

  @staticmethod
  @overload
  def addMapping(wanPort: int, lanPort: int, description: str, proto: str, leaseTime: int, force: bool) -> bool: ...

  @staticmethod
  def discover() -> bool: ...

  @staticmethod
  def fetchMappings() -> None: ...

  @staticmethod
  @overload
  def getExternalAddress() -> str: ...

  @staticmethod
  @overload
  def getExternalAddress(forceUpdate: bool) -> str: ...

  @staticmethod
  def getGatewayInfo() -> str: ...

  @staticmethod
  def getMapping(index: int) -> PortMappingEntry: ...

  @staticmethod
  def igdFound() -> bool: ...

  @staticmethod
  def numMappings() -> int: ...

  @staticmethod
  def removeMapping(wanPort: int, proto: str) -> bool: ...

  @staticmethod
  def shutdown() -> None: ...

  @staticmethod
  def startup() -> None: ...

  def __init__(self): ...


class PortMappingEntry:

  def __init__(self): ...


class ServerBrowser:

  @staticmethod
  def GetServerCount() -> int: ...

  @staticmethod
  @overload
  def GetServerDetails(serverIndex: int) -> GameServerDetails: ...

  @staticmethod
  @overload
  def GetServerDetails(host: str, port: int) -> GameServerDetails: ...

  @staticmethod
  def GetServerDetailsSync(host: str, port: int) -> GameServerDetails: ...

  @staticmethod
  def GetServerList() -> List[GameServerDetails]: ...

  @staticmethod
  def IsRefreshing() -> bool: ...

  @staticmethod
  def QueryServer(host: str, port: int) -> bool: ...

  @staticmethod
  def RefreshInternetServers() -> None: ...

  @staticmethod
  def Release() -> None: ...

  @staticmethod
  def ReleaseServerQuery(host: str, port: int) -> None: ...

  @staticmethod
  def RequestServerRules(host: str, port: int) -> bool: ...

  @staticmethod
  def init() -> bool: ...

  @staticmethod
  def setCallbackInterface(callbackInterface: IServerBrowserCallback) -> None: ...

  @staticmethod
  def shutdown() -> None: ...

  def __init__(self): ...


class SteamFriend:

  def getAvatar(self) -> Texture: ...

  def getName(self) -> str: ...

  def getState(self) -> str: ...

  def getSteamID(self) -> str: ...

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, name: str, steamID: int): ...


class SteamFriends:

  k_EPersonaStateAway: int

  k_EPersonaStateBusy: int

  k_EPersonaStateLookingToPlay: int

  k_EPersonaStateLookingToTrade: int

  k_EPersonaStateOffline: int

  k_EPersonaStateOnline: int

  k_EPersonaStateSnooze: int

  @staticmethod
  def ActivateGameOverlay(dialog: str) -> None: ...

  @staticmethod
  def ActivateGameOverlayToUser(dialog: str, steamID: int) -> None: ...

  @staticmethod
  def ActivateGameOverlayToWebPage(url: str) -> None: ...

  @staticmethod
  def CreateSteamAvatar(steamID: int, data: ByteBuffer) -> int: ...

  @staticmethod
  def GetFriendByIndex(index: int) -> int: ...

  @staticmethod
  def GetFriendCount() -> int: ...

  @staticmethod
  def GetFriendList() -> List[SteamFriend]: ...

  @staticmethod
  def GetFriendPersonaName(steamID: int) -> str: ...

  @staticmethod
  def GetFriendPersonaState(steamID: int) -> int: ...

  @staticmethod
  def GetPersonaName() -> str: ...

  @staticmethod
  def InviteUserToGame(friendSteamID: int, connectString: str) -> bool: ...

  @staticmethod
  def SetPlayedWith(steamID: int) -> None: ...

  @staticmethod
  def UpdateRichPresenceConnectionInfo(status: str, connectString: str) -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def n_Init() -> None: ...

  @staticmethod
  def n_Shutdown() -> None: ...

  @staticmethod
  def shutdown() -> None: ...

  def __init__(self): ...


class SteamGameServer:

  STEAM_SERVERS_CONNECTED: int

  STEAM_SERVERS_CONNECTFAILURE: int

  STEAM_SERVERS_DISCONNECTED: int

  @staticmethod
  def BUpdateUserData(steamID: int, playerName: str, score: int) -> bool: ...

  @staticmethod
  def EnableHeartBeats(bActive: bool) -> None: ...

  @staticmethod
  def GetSteamID() -> int: ...

  @staticmethod
  def GetSteamServersConnectState() -> int: ...

  @staticmethod
  def Init(ip: str, gamePort: int, UDPPort: int, serverMode: int, version: str) -> bool: ...

  @staticmethod
  def LogOnAnonymous() -> None: ...

  @staticmethod
  def SetDedicatedServer(dedicated: bool) -> None: ...

  @staticmethod
  def SetGameDescription(description: str) -> None: ...

  @staticmethod
  def SetGameTags(gameTags: str) -> None: ...

  @staticmethod
  def SetKeyValue(key: str, value: str) -> None: ...

  @staticmethod
  def SetMapName(mapName: str) -> None: ...

  @staticmethod
  def SetMaxPlayerCount(playersMax: int) -> None: ...

  @staticmethod
  def SetModDir(modDir: str) -> None: ...

  @staticmethod
  def SetProduct(product: str) -> None: ...

  @staticmethod
  def SetRegion(region: str) -> None: ...

  @staticmethod
  def SetServerName(serverName: str) -> None: ...

  def __init__(self): ...


class SteamUGCDetails:

  def getChildID(self, index: int) -> int: ...

  def getChildren(self) -> list[int]: ...

  def getFileSize(self) -> int: ...

  def getID(self) -> int: ...

  def getIDString(self) -> str: ...

  def getNumChildren(self) -> int: ...

  def getState(self) -> str: ...

  def getTimeCreated(self) -> int: ...

  def getTimeUpdated(self) -> int: ...

  def getTitle(self) -> str: ...

  def __init__(self, ID: int, title: str, timeCreated: int, timeUpdated: int, fileSize: int, childIDs: list[int]): ...


class SteamUser:

  @staticmethod
  def GetSteamID() -> int: ...

  @staticmethod
  def GetSteamIDString() -> str: ...

  def __init__(self): ...


class SteamUtils:

  k_EFloatingGamepadTextInputModeEmail: int

  k_EFloatingGamepadTextInputModeMultipleLines: int

  k_EFloatingGamepadTextInputModeNumeric: int

  k_EFloatingGamepadTextInputModeSingleLine: int

  k_EGamepadTextInputLineModeMultipleLines: int

  k_EGamepadTextInputLineModeSingleLine: int

  k_EGamepadTextInputModeNormal: int

  k_EGamepadTextInputModePassword: int

  @staticmethod
  def addJoinRequestCallback(callback: IJoinRequestCallback) -> None: ...

  @staticmethod
  def convertSteamIDToString(steamID: int) -> str: ...

  @staticmethod
  def convertStringToSteamID(s: str) -> int: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def isFloatingGamepadTextInputVisible() -> bool: ...

  @staticmethod
  def isOverlayEnabled() -> bool: ...

  @staticmethod
  def isRunningOnSteamDeck() -> bool: ...

  @staticmethod
  def isSteamModeEnabled() -> bool: ...

  @staticmethod
  def isValidSteamID(s: str) -> bool: ...

  @staticmethod
  def removeJoinRequestCallback(callback: IJoinRequestCallback) -> None: ...

  @staticmethod
  def runLoop() -> None: ...

  @staticmethod
  def showFloatingGamepadTextInput(multipleLines: bool, x: int, y: int, width: int, height: int) -> bool: ...

  @staticmethod
  def showGamepadTextInput(password: bool, multipleLines: bool, description: str, maxChars: int, existingText: str) -> bool: ...

  @staticmethod
  def shutdown() -> None: ...

  def __init__(self): ...


class SteamWorkshop:

  instance: SteamWorkshop

  def CreateQueryUGCDetailsRequest(self, itemIDs: list[int], callback: ISteamWorkshopCallback) -> int: ...

  def CreateWorkshopItem(self, item: SteamWorkshopItem) -> bool: ...

  def DownloadItem(self, itemID: int, bHighPriority: bool, callback: ISteamWorkshopCallback) -> bool: ...

  def GetInstalledItemFolders(self) -> list[str]: ...

  def GetItemDownloadInfo(self, itemID: int, progress: list[int]) -> bool: ...

  def GetItemInstallFolder(self, itemID: int) -> str: ...

  def GetItemInstallTimeStamp(self, itemID: int) -> int: ...

  def GetItemState(self, itemID: int) -> int: ...

  def GetItemUpdateProgress(self, progress: list[int]) -> bool: ...

  def GetQueryUGCChildren(self, handle: int, index: int) -> list[int]: ...

  def GetQueryUGCResult(self, handle: int, index: int) -> SteamUGCDetails: ...

  def ReleaseQueryUGCRequest(self, handle: int) -> bool: ...

  def RemoveCallback(self, callback: ISteamWorkshopCallback) -> None: ...

  def SubmitWorkshopItem(self, item: SteamWorkshopItem) -> bool: ...

  def SubscribeItem(self, itemID: int, callback: ISteamWorkshopCallback) -> bool: ...

  def getIDFromItemInstallFolder(self, dir: str) -> str: ...

  def getStageFolders(self) -> ArrayList[str]: ...

  def getWorkshopFolder(self) -> str: ...

  def loadStagedItems(self) -> ArrayList[SteamWorkshopItem]: ...

  @overload
  def onItemCreated(self, itemID: int, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...

  @overload
  def onItemCreated(self, itemID: int, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...

  @overload
  def onItemDownloaded(self, itemID: int) -> None: ...

  @overload
  def onItemDownloaded(self, itemID: int) -> None: ...

  @overload
  def onItemNotCreated(self, result: int) -> None: ...

  @overload
  def onItemNotCreated(self, result: int) -> None: ...

  @overload
  def onItemNotDownloaded(self, itemID: int, result: int) -> None: ...

  @overload
  def onItemNotDownloaded(self, itemID: int, result: int) -> None: ...

  @overload
  def onItemNotSubscribed(self, itemID: int, result: int) -> None: ...

  @overload
  def onItemNotSubscribed(self, itemID: int, result: int) -> None: ...

  @overload
  def onItemNotUpdated(self, result: int) -> None: ...

  @overload
  def onItemNotUpdated(self, result: int) -> None: ...

  @overload
  def onItemQueryCompleted(self, handle: int, numResults: int) -> None: ...

  @overload
  def onItemQueryCompleted(self, handle: int, numResults: int) -> None: ...

  @overload
  def onItemQueryNotCompleted(self, handle: int, result: int) -> None: ...

  @overload
  def onItemQueryNotCompleted(self, handle: int, result: int) -> None: ...

  @overload
  def onItemSubscribed(self, itemID: int) -> None: ...

  @overload
  def onItemSubscribed(self, itemID: int) -> None: ...

  @overload
  def onItemUpdated(self, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...

  @overload
  def onItemUpdated(self, bUserNeedsToAcceptWorkshopLegalAgreement: bool) -> None: ...

  @staticmethod
  def init() -> None: ...

  @staticmethod
  def shutdown() -> None: ...

  def __init__(self): ...


class SteamWorkshopItem:

  def create(self) -> bool: ...

  def getChangeNote(self) -> str: ...

  def getContentFolder(self) -> str: ...

  def getDescription(self) -> str: ...

  def getExtendedErrorInfo(self, error: str) -> str: ...

  def getFolderName(self) -> str: ...

  def getID(self) -> str: ...

  def getPreviewImage(self) -> str: ...

  def getSubmitDescription(self) -> str: ...

  def getSubmitTags(self) -> list[str]: ...

  def getTags(self) -> ArrayList[str]: ...

  def getTitle(self) -> str: ...

  def getUpdateProgress(self, table: KahluaTable) -> bool: ...

  def getUpdateProgressTotal(self) -> int: ...

  def getVisibility(self) -> str: ...

  def getVisibilityInteger(self) -> int: ...

  def readWorkshopTxt(self) -> bool: ...

  def setChangeNote(self, changeNote: str) -> None: ...

  def setDescription(self, description: str) -> None: ...

  def setID(self, ID: str) -> None: ...

  def setTags(self, tags: ArrayList[str]) -> None: ...

  def setTitle(self, title: str) -> None: ...

  def setVisibility(self, visibility: str) -> None: ...

  def setVisibilityInteger(self, v: int) -> None: ...

  def submitUpdate(self) -> bool: ...

  def validateContents(self) -> str: ...

  def validatePreviewImage(self, path: Path) -> str: ...

  def writeWorkshopTxt(self) -> bool: ...

  @staticmethod
  def getAllowedTags() -> ArrayList[str]: ...

  def __init__(self, workshopFolder: str): ...

  class ItemState(Enum):

    Downloading: SteamWorkshopItem.ItemState

    DownloadPending: SteamWorkshopItem.ItemState

    Installed: SteamWorkshopItem.ItemState

    LegacyItem: SteamWorkshopItem.ItemState

    NeedsUpdate: SteamWorkshopItem.ItemState

    # None: SteamWorkshopItem.ItemState

    Subscribed: SteamWorkshopItem.ItemState

    def getValue(self) -> int: ...

    @staticmethod
    def toString(arg0: int) -> str: ...

    @staticmethod
    def valueOf(arg0: str) -> SteamWorkshopItem.ItemState: ...

    @staticmethod
    def values() -> list[SteamWorkshopItem.ItemState]: ...


class ZNet:

  @staticmethod
  @overload
  def SetLogLevel(level: int) -> None: ...

  @staticmethod
  @overload
  def SetLogLevel(severity: LogSeverity) -> None: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class ZNetSessionState:

  def getDescription(self) -> str: ...

  def __init__(self): ...


class ZNetStatistics:

  def __init__(self):
    self.bpslimitbycongestioncontrol: int
    self.bpslimitbyoutgoingbandwidthlimit: int
    self.bytesinresendbuffer: int
    self.bytesinsendbufferhigh: float
    self.bytesinsendbufferimmediate: float
    self.bytesinsendbufferlow: float
    self.bytesinsendbuffermedium: float
    self.connectionstarttime: int
    self.islimitedbycongestioncontrol: bool
    self.islimitedbyoutgoingbandwidthlimit: bool
    self.lastactualbytesreceived: int
    self.lastactualbytessent: int
    self.lastusermessagebytespushed: int
    self.lastusermessagebytesreceivedignored: int
    self.lastusermessagebytesreceivedprocessed: int
    self.lastusermessagebytesresent: int
    self.lastusermessagebytessent: int
    self.messageinsendbufferhigh: int
    self.messageinsendbufferimmediate: int
    self.messageinsendbufferlow: int
    self.messageinsendbuffermedium: int
    self.messagesinresendbuffer: int
    self.packetlosslastsecond: float
    self.packetlosstotal: float
    self.totalactualbytesreceived: int
    self.totalactualbytessent: int
    self.totalusermessagebytespushed: int
    self.totalusermessagebytesreceivedignored: int
    self.totalusermessagebytesreceivedprocessed: int
    self.totalusermessagebytesresent: int
    self.totalusermessagebytessent: int

