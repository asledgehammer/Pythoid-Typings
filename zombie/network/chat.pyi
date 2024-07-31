from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum, Integer
from java.nio import ByteBuffer
from java.util import ArrayList
from zombie.chat import ChatMessage
from zombie.chat.defaultChats import FactionChat, SafehouseChat
from zombie.core.raknet import UdpConnection

class ChatServer:

  def createFactionChat(self, name: str) -> FactionChat: ...

  def createRadiostationMessage(self, text: str, radioChannel: int) -> ChatMessage: ...

  def createSafehouseChat(self, safehouseID: str) -> SafehouseChat: ...

  def disconnectPlayer(self, playerID: int) -> None: ...

  def init(self) -> None: ...

  def initPlayer(self, playerID: int) -> None: ...

  def joinAdminChat(self, playerID: int) -> None: ...

  def leaveAdminChat(self, playerID: int) -> None: ...

  def processMessageFromPlayerPacket(self, bb: ByteBuffer) -> None: ...

  def processPlayerStartWhisperChatPacket(self, bb: ByteBuffer) -> None: ...

  def removeFactionChat(self, factionName: str) -> None: ...

  def removeSafehouseChat(self, safehouseName: str) -> None: ...

  def sendMessageFromDiscordToGeneralChat(self, author: str, msg: str) -> None: ...

  def sendMessageToAdminChat(self, msg: str) -> None: ...

  @overload
  def sendMessageToServerChat(self, msg: str) -> None: ...

  @overload
  def sendMessageToServerChat(self, connection: UdpConnection, msg: str) -> None: ...

  @overload
  def sendServerAlertMessageToServerChat(self, msg: str) -> None: ...

  @overload
  def sendServerAlertMessageToServerChat(self, author: str, msg: str) -> None: ...

  def syncFactionChatMembers(self, factionName: str, factionOwner: str, players: ArrayList[str]) -> None: ...

  def syncSafehouseChatMembers(self, safehouseID: str, safehouseOwner: str, players: ArrayList[str]) -> None: ...

  def unpackChatMessage(self, bb: ByteBuffer) -> ChatMessage: ...

  @staticmethod
  def getInstance() -> ChatServer: ...

  @staticmethod
  def isInited() -> bool: ...


class ChatType(Enum):

  admin: ChatType

  faction: ChatType

  general: ChatType

  notDefined: ChatType

  radio: ChatType

  safehouse: ChatType

  say: ChatType

  server: ChatType

  shout: ChatType

  whisper: ChatType

  def getTitleID(self) -> str: ...

  def getValue(self) -> int: ...

  @staticmethod
  @overload
  def valueOf(arg0: Integer) -> ChatType: ...

  @staticmethod
  @overload
  def valueOf(arg0: str) -> ChatType: ...

  @staticmethod
  def values() -> list[ChatType]: ...

