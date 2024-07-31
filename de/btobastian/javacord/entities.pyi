from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.common.util.concurrent import FutureCallback
from de.btobastian.javacord.entities.message import Message, MessageHistory
from de.btobastian.javacord.entities.message.embed import EmbedBuilder
from de.btobastian.javacord.entities.permissions import Role, Permissions
from java.awt.image import BufferedImage
from java.io import File, InputStream
from java.lang import Void, Enum
from java.net import URL
from java.util import Calendar, Collection, Set
from java.util.concurrent import Future

class Channel:

  @overload
  def bulkDelete(self, arg0: list[Message]) -> Future[Void]: ...

  @overload
  def bulkDelete(self, arg0: list[str]) -> Future[Void]: ...

  def delete(self) -> Future[Void]: ...

  @overload
  def deleteOverwrittenPermissions(self, arg0: User) -> Future[Void]: ...

  @overload
  def deleteOverwrittenPermissions(self, arg0: Role) -> Future[Void]: ...

  def getCreationDate(self) -> Calendar: ...

  @overload
  def getId(self) -> str: ...

  @overload
  def getId(self) -> str: ...

  def getInviteBuilder(self) -> InviteBuilder: ...

  def getMentionTag(self) -> str: ...

  def getMessageById(self, arg0: str) -> Future[Message]: ...

  @overload
  def getMessageHistory(self, arg0: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistory(self, arg0: int, arg1: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  def getName(self) -> str: ...

  @overload
  def getOverwrittenPermissions(self, arg0: User) -> Permissions: ...

  @overload
  def getOverwrittenPermissions(self, arg0: Role) -> Permissions: ...

  def getParentId(self) -> str: ...

  def getPosition(self) -> int: ...

  def getServer(self) -> Server: ...

  def getTopic(self) -> str: ...

  @overload
  def sendFile(self, arg0: File) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str, arg4: FutureCallback[Message]) -> Future[Message]: ...

  def type(self) -> None: ...

  def update(self, arg0: str, arg1: str, arg2: int) -> Future[Void]: ...

  def updateName(self, arg0: str) -> Future[Void]: ...

  @overload
  def updateOverwrittenPermissions(self, arg0: User, arg1: Permissions) -> Future[Void]: ...

  @overload
  def updateOverwrittenPermissions(self, arg0: Role, arg1: Permissions) -> Future[Void]: ...

  def updatePosition(self, arg0: int) -> Future[Void]: ...

  def updateTopic(self, arg0: str) -> Future[Void]: ...


class CustomEmoji:

  def delete(self) -> Future[Void]: ...

  def getCreationDate(self) -> Calendar: ...

  @overload
  def getEmoji(self) -> Future[BufferedImage]: ...

  @overload
  def getEmoji(self, arg0: FutureCallback[BufferedImage]) -> Future[BufferedImage]: ...

  @overload
  def getEmojiAsByteArray(self) -> Future[byte]: ...

  @overload
  def getEmojiAsByteArray(self, arg0: FutureCallback[byte]) -> Future[byte]: ...

  def getId(self) -> str: ...

  def getImageUrl(self) -> URL: ...

  def getMentionTag(self) -> str: ...

  def getName(self) -> str: ...

  def getRoles(self) -> Collection[Role]: ...

  def getServer(self) -> Server: ...

  def isManaged(self) -> bool: ...

  def requiresColons(self) -> bool: ...


class Invite:

  @overload
  def acceptInvite(self) -> Future[Server]: ...

  @overload
  def acceptInvite(self, arg0: FutureCallback[Server]) -> Future[Server]: ...

  def delete(self) -> Future[Void]: ...

  def getChannel(self) -> Channel: ...

  def getChannelId(self) -> str: ...

  def getChannelName(self) -> str: ...

  def getCode(self) -> str: ...

  def getCreationDate(self) -> Calendar: ...

  def getCreator(self) -> User: ...

  def getInviteUrl(self) -> URL: ...

  def getMaxAge(self) -> int: ...

  def getMaxUses(self) -> int: ...

  def getServer(self) -> Server: ...

  def getServerId(self) -> str: ...

  def getServerName(self) -> str: ...

  def getUses(self) -> int: ...

  def getVoiceChannel(self) -> VoiceChannel: ...

  def isRevoked(self) -> bool: ...

  def isTemporary(self) -> bool: ...

  def isVoiceChannel(self) -> bool: ...


class InviteBuilder:

  @overload
  def create(self) -> Future[Invite]: ...

  @overload
  def create(self, arg0: FutureCallback[Invite]) -> Future[Invite]: ...

  def setMaxAge(self, arg0: int) -> InviteBuilder: ...

  def setMaxUses(self, arg0: int) -> InviteBuilder: ...

  def setTemporary(self, arg0: bool) -> InviteBuilder: ...


class Region(Enum):

  AMSTERDAM: Region

  BRAZIL: Region

  EU_CENTRAL: Region

  EU_WEST: Region

  FRANKFURT: Region

  LONDON: Region

  SINGAPORE: Region

  SYDNEY: Region

  UNKNOWN: Region

  US_CENTRAL: Region

  US_EAST: Region

  US_SOUTH: Region

  US_WEST: Region

  def getKey(self) -> str: ...

  def getName(self) -> str: ...

  @staticmethod
  def getRegionByKey(arg0: str) -> Region: ...

  @staticmethod
  def valueOf(arg0: str) -> Region: ...

  @staticmethod
  def values() -> list[Region]: ...


class Server:

  @overload
  def banUser(self, arg0: User) -> Future[Void]: ...

  @overload
  def banUser(self, arg0: str) -> Future[Void]: ...

  @overload
  def banUser(self, arg0: User, arg1: int) -> Future[Void]: ...

  @overload
  def banUser(self, arg0: str, arg1: int) -> Future[Void]: ...

  @overload
  def createChannel(self, arg0: str) -> Future[Channel]: ...

  @overload
  def createChannel(self, arg0: str, arg1: FutureCallback[Channel]) -> Future[Channel]: ...

  @overload
  def createRole(self) -> Future[Role]: ...

  @overload
  def createRole(self, arg0: FutureCallback[Role]) -> Future[Role]: ...

  @overload
  def createVoiceChannel(self, arg0: str) -> Future[VoiceChannel]: ...

  @overload
  def createVoiceChannel(self, arg0: str, arg1: FutureCallback[VoiceChannel]) -> Future[VoiceChannel]: ...

  def delete(self) -> Future[Void]: ...

  @overload
  def getBans(self) -> Future[Ban]: ...

  @overload
  def getBans(self, arg0: FutureCallback[Ban]) -> Future[Ban]: ...

  def getChannelById(self, arg0: str) -> Channel: ...

  def getChannels(self) -> Collection[Channel]: ...

  def getCreationDate(self) -> Calendar: ...

  def getCustomEmojiById(self, arg0: str) -> CustomEmoji: ...

  def getCustomEmojiByName(self, arg0: str) -> CustomEmoji: ...

  def getCustomEmojis(self) -> Collection[CustomEmoji]: ...

  @overload
  def getIcon(self) -> Future[byte]: ...

  @overload
  def getIcon(self, arg0: FutureCallback[byte]) -> Future[byte]: ...

  def getIconUrl(self) -> URL: ...

  def getId(self) -> str: ...

  @overload
  def getInvites(self) -> Future[Invite]: ...

  @overload
  def getInvites(self, arg0: FutureCallback[Invite]) -> Future[Invite]: ...

  def getMemberById(self, arg0: str) -> User: ...

  def getMemberCount(self) -> int: ...

  def getMembers(self) -> Collection[User]: ...

  def getName(self) -> str: ...

  def getNickname(self, arg0: User) -> str: ...

  def getOwner(self) -> Future[User]: ...

  def getOwnerId(self) -> str: ...

  def getRegion(self) -> Region: ...

  def getRoleById(self, arg0: str) -> Role: ...

  def getRoles(self) -> Collection[Role]: ...

  def getVoiceChannelById(self, arg0: str) -> VoiceChannel: ...

  def getVoiceChannels(self) -> Collection[VoiceChannel]: ...

  def hasNickname(self, arg0: User) -> bool: ...

  def isLarge(self) -> bool: ...

  @overload
  def isMember(self, arg0: User) -> bool: ...

  @overload
  def isMember(self, arg0: str) -> bool: ...

  @overload
  def kickUser(self, arg0: User) -> Future[Void]: ...

  @overload
  def kickUser(self, arg0: str) -> Future[Void]: ...

  def leave(self) -> Future[Void]: ...

  def unbanUser(self, arg0: str) -> Future[Void]: ...

  def update(self, arg0: str, arg1: Region, arg2: BufferedImage) -> Future[Void]: ...

  def updateIcon(self, arg0: BufferedImage) -> Future[Void]: ...

  def updateName(self, arg0: str) -> Future[Void]: ...

  def updateNickname(self, arg0: User, arg1: str) -> Future[Void]: ...

  def updateRegion(self, arg0: Region) -> Future[Void]: ...

  def updateRoles(self, arg0: User, arg1: list[Role]) -> Future[Void]: ...


class User:

  @overload
  def getAvatar(self) -> Future[BufferedImage]: ...

  @overload
  def getAvatar(self, arg0: FutureCallback[BufferedImage]) -> Future[BufferedImage]: ...

  @overload
  def getAvatarAsByteArray(self) -> Future[byte]: ...

  @overload
  def getAvatarAsByteArray(self, arg0: FutureCallback[byte]) -> Future[byte]: ...

  def getAvatarId(self) -> str: ...

  def getAvatarUrl(self) -> URL: ...

  def getCreationDate(self) -> Calendar: ...

  def getDiscriminator(self) -> str: ...

  def getGame(self) -> str: ...

  @overload
  def getId(self) -> str: ...

  @overload
  def getId(self) -> str: ...

  def getMentionTag(self) -> str: ...

  @overload
  def getMessageHistory(self, arg0: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistory(self, arg0: int, arg1: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryAfter(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: Message, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  @overload
  def getMessageHistoryBefore(self, arg0: str, arg1: int, arg2: FutureCallback[MessageHistory]) -> Future[MessageHistory]: ...

  def getName(self) -> str: ...

  def getNickname(self, arg0: Server) -> str: ...

  def getRoles(self, arg0: Server) -> Collection[Role]: ...

  def getStatus(self) -> UserStatus: ...

  def getVoiceChannel(self) -> VoiceChannel: ...

  def hasNickname(self, arg0: Server) -> bool: ...

  def isBot(self) -> bool: ...

  def isYourself(self) -> bool: ...

  @overload
  def sendFile(self, arg0: File) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: File, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str) -> Future[Message]: ...

  @overload
  def sendFile(self, arg0: InputStream, arg1: str, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: str, arg2: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: bool, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: str, arg3: FutureCallback[Message]) -> Future[Message]: ...

  @overload
  def sendMessage(self, arg0: str, arg1: EmbedBuilder, arg2: bool, arg3: str, arg4: FutureCallback[Message]) -> Future[Message]: ...

  def type(self) -> None: ...

  def updateNickname(self, arg0: Server, arg1: str) -> Future[Void]: ...


class UserStatus(Enum):

  DO_NOT_DISTURB: UserStatus

  IDLE: UserStatus

  OFFLINE: UserStatus

  ONLINE: UserStatus

  @staticmethod
  def fromString(arg0: str) -> UserStatus: ...

  @staticmethod
  def valueOf(arg0: str) -> UserStatus: ...

  @staticmethod
  def values() -> list[UserStatus]: ...


class VoiceChannel:

  def delete(self) -> Future[Void]: ...

  @overload
  def deleteOverwrittenPermissions(self, arg0: User) -> Future[Void]: ...

  @overload
  def deleteOverwrittenPermissions(self, arg0: Role) -> Future[Void]: ...

  def getConnectedUsers(self) -> Set[User]: ...

  def getCreationDate(self) -> Calendar: ...

  def getId(self) -> str: ...

  def getInviteBuilder(self) -> InviteBuilder: ...

  def getName(self) -> str: ...

  @overload
  def getOverwrittenPermissions(self, arg0: User) -> Permissions: ...

  @overload
  def getOverwrittenPermissions(self, arg0: Role) -> Permissions: ...

  def getParentId(self) -> str: ...

  def getPosition(self) -> int: ...

  def getServer(self) -> Server: ...

  def update(self, arg0: str, arg1: int) -> Future[Void]: ...

  def updateName(self, arg0: str) -> Future[Void]: ...

  @overload
  def updateOverwrittenPermissions(self, arg0: User, arg1: Permissions) -> Future[Void]: ...

  @overload
  def updateOverwrittenPermissions(self, arg0: Role, arg1: Permissions) -> Future[Void]: ...

  def updatePosition(self, arg0: int) -> Future[Void]: ...

