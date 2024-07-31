from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.commands import CommandBase
from zombie.core.raknet import UdpConnection
from zombie.debug import DebugType, LogSeverity

class AddAllToWhiteListCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AddItemCommand(CommandBase):

  toMe: str

  toPlayer: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AddUserCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AddUserToWhiteListCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AddVehicleCommand(CommandBase):

  scriptCoordinate: str

  scriptOnly: str

  scriptPlayer: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AddXPCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class AlarmCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ArgType:

  AnyText: str

  Coordinates: str

  IP: str

  ItemName: str

  PlayerName: str

  Script: str

  TrueFalse: str

  Value: str

  def __init__(self): ...


class BanSteamIDCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class BanUserCommand(CommandBase):

  banUser: str

  banWithIP: str

  banWithReason: str

  banWithReasonIP: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ChangeOptionCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class CheckModsNeedUpdate(CommandBase):

  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: UdpConnection): ...


class ChopperCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ClearCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ConnectionsCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class CreateHorde2Command(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class CreateHordeCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class DebugPlayerCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class GodModeCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class GrantAdminCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class GunShotCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class HelpCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class InvisibleCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class KickUserCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class LightningCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class LogCommand(CommandBase):

  @staticmethod
  def getDebugType(debugType: str) -> DebugType: ...

  @staticmethod
  def getLogSeverity(logSeverity: str) -> LogSeverity: ...

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class NoClipCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class PlayersCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class QuitCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ReleaseSafehouseCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ReloadLuaCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ReloadOptionsCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class RemoveAdminCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class RemoveUserFromWhiteList(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class RemoveZombiesCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ReplayCommands(CommandBase):

  RecordPlay: str

  Stop: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class SaveCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ServerMessageCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class SetAccessLevelCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ShowOptionsCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class StartRainCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class StartStormCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class StatisticsCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class StopRainCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class StopWeatherCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class TeleportCommand(CommandBase):

  justToUser: str

  portUserToUser: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class TeleportToCommand(CommandBase):

  teleportMe: str

  teleportUser: str

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class ThunderCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class UnbanSteamIDCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class UnbanUserCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...


class VoiceBanCommand(CommandBase):

  def __init__(self, username: str, userAccessLevel: str, command: str, connection: UdpConnection): ...

