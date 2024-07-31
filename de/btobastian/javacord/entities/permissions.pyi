from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from de.btobastian.javacord.entities import User, Channel, VoiceChannel, Server
from java.awt import Color
from java.lang import Enum, Void
from java.util import List
from java.util.concurrent import Future

class PermissionState(Enum):

  ALLOWED: PermissionState

  DENIED: PermissionState

  NONE: PermissionState

  @staticmethod
  def valueOf(arg0: str) -> PermissionState: ...

  @staticmethod
  def values() -> list[PermissionState]: ...


class PermissionType(Enum):

  ADD_REACTIONS: PermissionType

  ADMINISTRATOR: PermissionType

  ATTACH_FILE: PermissionType

  BAN_MEMBERS: PermissionType

  CHANGE_NICKNAME: PermissionType

  CREATE_INSTANT_INVITE: PermissionType

  EMBED_LINKS: PermissionType

  KICK_MEMBERS: PermissionType

  MANAGE_CHANNELS: PermissionType

  MANAGE_EMOJIS: PermissionType

  MANAGE_MESSAGES: PermissionType

  MANAGE_NICKNAMES: PermissionType

  MANAGE_ROLES: PermissionType

  MANAGE_SERVER: PermissionType

  MANAGE_WEBHOOKS: PermissionType

  MENTION_EVERYONE: PermissionType

  READ_MESSAGE_HISTORY: PermissionType

  READ_MESSAGES: PermissionType

  SEND_MESSAGES: PermissionType

  SEND_TTS_MESSAGES: PermissionType

  USE_EXTERNAL_EMOJIS: PermissionType

  VOICE_CONNECT: PermissionType

  VOICE_DEAFEN_MEMBERS: PermissionType

  VOICE_MOVE_MEMBERS: PermissionType

  VOICE_MUTE_MEMBERS: PermissionType

  VOICE_SPEAK: PermissionType

  VOICE_USE_VAD: PermissionType

  def getOffset(self) -> int: ...

  def isSet(self, arg0: int) -> bool: ...

  def set(self, arg0: int, arg1: bool) -> int: ...

  @staticmethod
  def valueOf(arg0: str) -> PermissionType: ...

  @staticmethod
  def values() -> list[PermissionType]: ...


class Permissions:

  def getState(self, arg0: PermissionType) -> PermissionState: ...


class PermissionsBuilder:

  def build(self) -> Permissions: ...

  def getState(self, arg0: PermissionType) -> PermissionState: ...

  def setState(self, arg0: PermissionType, arg1: PermissionState) -> PermissionsBuilder: ...


class Role:

  def addUser(self, arg0: User) -> Future[Void]: ...

  def delete(self) -> Future[Void]: ...

  def getColor(self) -> Color: ...

  def getHoist(self) -> bool: ...

  def getId(self) -> str: ...

  def getMentionTag(self) -> str: ...

  def getName(self) -> str: ...

  @overload
  def getOverwrittenPermissions(self, arg0: Channel) -> Permissions: ...

  @overload
  def getOverwrittenPermissions(self, arg0: VoiceChannel) -> Permissions: ...

  def getPermissions(self) -> Permissions: ...

  def getPosition(self) -> int: ...

  def getServer(self) -> Server: ...

  def getUsers(self) -> List[User]: ...

  def isManaged(self) -> bool: ...

  def isMentionable(self) -> bool: ...

  def removeUser(self, arg0: User) -> Future[Void]: ...

  def update(self, arg0: str, arg1: Color, arg2: bool, arg3: Permissions, arg4: bool) -> Future[Void]: ...

  def updateColor(self, arg0: Color) -> Future[Void]: ...

  def updateHoist(self, arg0: bool) -> Future[Void]: ...

  def updateMentionable(self, arg0: bool) -> Future[Void]: ...

  def updateName(self, arg0: str) -> Future[Void]: ...

  def updatePermissions(self, arg0: Permissions) -> Future[Void]: ...

