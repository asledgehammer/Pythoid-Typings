from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Throwable, System, Enum
from java.util import ResourceBundle
from java.util.function import Supplier

class PlatformLogger:

  @overload
  def config(self, arg0: str) -> None: ...

  @overload
  def config(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def config(self, arg0: str, arg1: Throwable) -> None: ...

  @overload
  def fine(self, arg0: str) -> None: ...

  @overload
  def fine(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def fine(self, arg0: str, arg1: Throwable) -> None: ...

  @overload
  def finer(self, arg0: str) -> None: ...

  @overload
  def finer(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def finer(self, arg0: str, arg1: Throwable) -> None: ...

  @overload
  def finest(self, arg0: str) -> None: ...

  @overload
  def finest(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def finest(self, arg0: str, arg1: Throwable) -> None: ...

  def getName(self) -> str: ...

  @overload
  def info(self, arg0: str) -> None: ...

  @overload
  def info(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def info(self, arg0: str, arg1: Throwable) -> None: ...

  def isEnabled(self) -> bool: ...

  def isLoggable(self, arg0: PlatformLogger.Level) -> bool: ...

  def level(self) -> PlatformLogger.Level: ...

  def setLevel(self, arg0: PlatformLogger.Level) -> None: ...

  @overload
  def severe(self, arg0: str) -> None: ...

  @overload
  def severe(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def severe(self, arg0: str, arg1: Throwable) -> None: ...

  @overload
  def warning(self, arg0: str) -> None: ...

  @overload
  def warning(self, arg0: str, arg1: list[object]) -> None: ...

  @overload
  def warning(self, arg0: str, arg1: Throwable) -> None: ...

  @staticmethod
  def getLogger(arg0: str) -> PlatformLogger: ...

  @staticmethod
  def toPlatformLevel(arg0: System.Logger.Level) -> PlatformLogger.Level: ...

  class Bridge:

    def getName(self) -> str: ...

    def isEnabled(self) -> bool: ...

    def isLoggable(self, arg0: PlatformLogger.Level) -> bool: ...

    @overload
    def log(self, arg0: PlatformLogger.Level, arg1: str) -> None: ...

    @overload
    def log(self, arg0: PlatformLogger.Level, arg1: Supplier[str]) -> None: ...

    @overload
    def log(self, arg0: PlatformLogger.Level, arg1: str, arg2: list[object]) -> None: ...

    @overload
    def log(self, arg0: PlatformLogger.Level, arg1: str, arg2: Throwable) -> None: ...

    @overload
    def log(self, arg0: PlatformLogger.Level, arg1: Throwable, arg2: Supplier[str]) -> None: ...

    @overload
    def logp(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: str) -> None: ...

    @overload
    def logp(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: Supplier[str]) -> None: ...

    @overload
    def logp(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: str, arg4: list[object]) -> None: ...

    @overload
    def logp(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: str, arg4: Throwable) -> None: ...

    @overload
    def logp(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: Throwable, arg4: Supplier[str]) -> None: ...

    @overload
    def logrb(self, arg0: PlatformLogger.Level, arg1: ResourceBundle, arg2: str, arg3: list[object]) -> None: ...

    @overload
    def logrb(self, arg0: PlatformLogger.Level, arg1: ResourceBundle, arg2: str, arg3: Throwable) -> None: ...

    @overload
    def logrb(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: ResourceBundle, arg4: str, arg5: list[object]) -> None: ...

    @overload
    def logrb(self, arg0: PlatformLogger.Level, arg1: str, arg2: str, arg3: ResourceBundle, arg4: str, arg5: Throwable) -> None: ...

    @staticmethod
    def convert(arg0: System.Logger) -> PlatformLogger.Bridge: ...

  class Level(Enum):

    ALL: PlatformLogger.Level

    CONFIG: PlatformLogger.Level

    FINE: PlatformLogger.Level

    FINER: PlatformLogger.Level

    FINEST: PlatformLogger.Level

    INFO: PlatformLogger.Level

    OFF: PlatformLogger.Level

    SEVERE: PlatformLogger.Level

    WARNING: PlatformLogger.Level

    def intValue(self) -> int: ...

    def systemLevel(self) -> System.Logger.Level: ...

    @staticmethod
    @overload
    def valueOf(arg0: int) -> PlatformLogger.Level: ...

    @staticmethod
    @overload
    def valueOf(arg0: str) -> PlatformLogger.Level: ...

    @staticmethod
    def values() -> list[PlatformLogger.Level]: ...

  class ConfigurableBridge:

    def getLoggerConfiguration(self) -> PlatformLogger.ConfigurableBridge.LoggerConfiguration: ...

    class LoggerConfiguration:

      def getPlatformLevel(self) -> PlatformLogger.Level: ...

      def setPlatformLevel(self, arg0: PlatformLogger.Level) -> None: ...

      def __init__(self): ...

