from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Throwable, Exception
from java.nio.file import FileSystem
from zombie.characters import IsoPlayer
from zombie.debug import DebugLogStream, LogSeverity

class ExceptionLogger:

  @staticmethod
  @overload
  def logException(ex: Throwable) -> None: ...

  @staticmethod
  @overload
  def logException(ex: Throwable, errorMessage: str) -> None: ...

  @staticmethod
  @overload
  def logException(ex: Throwable, errorMessage: str, out: DebugLogStream, severity: LogSeverity) -> None: ...

  @staticmethod
  def render() -> None: ...

  @staticmethod
  def showPopup() -> None: ...

  def __init__(self): ...


class LoggerManager:

  @staticmethod
  def createLogger(loggerName: str, useConsole: bool) -> None: ...

  @staticmethod
  def getLogger(loggerName: str) -> ZLogger: ...

  @staticmethod
  def getLogsDir() -> str: ...

  @staticmethod
  def getPlayerCoords(player: IsoPlayer) -> str: ...

  @staticmethod
  def init() -> None: ...

  def __init__(self): ...


class ZLogger:

  @overload
  def write(self, ex: Exception) -> None: ...

  @overload
  def write(self, logs: str) -> None: ...

  @overload
  def write(self, logs: str, level: str) -> None: ...

  @overload
  def write(self, arg0: str, arg1: str, arg2: bool) -> None: ...

  def writeUnsafe(self, arg0: str, arg1: str, arg2: bool) -> None: ...

  def __init__(self, name: str, useConsole: bool): ...

  class OutputStreams:

    def println(self, arg0: str) -> None: ...


class ZipLogs:

  @staticmethod
  def addDirToZip(zipfs: FileSystem, filenameInternal: str, filename: str) -> None: ...

  @staticmethod
  def addToZip(zipfs: FileSystem, filenameInternal: str, filename: str) -> None: ...

  @staticmethod
  def addZipFile(saveTheSaveData: bool) -> None: ...

  @staticmethod
  def putTextFile(zipfs: FileSystem, filename: str, text: str) -> None: ...

  def __init__(self): ...

