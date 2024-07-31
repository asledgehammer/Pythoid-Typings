from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum

class ZipBackup:

  @staticmethod
  def makeBackupFile(ServerName: str, type: ZipBackup.BackupTypes) -> None: ...

  @staticmethod
  def onPeriod() -> None: ...

  @staticmethod
  def onStartup() -> None: ...

  @staticmethod
  def onVersion() -> None: ...

  def __init__(self): ...

  class BackupTypes(Enum):

    period: ZipBackup.BackupTypes

    startup: ZipBackup.BackupTypes

    version: ZipBackup.BackupTypes

    @staticmethod
    def valueOf(arg0: str) -> ZipBackup.BackupTypes: ...

    @staticmethod
    def values() -> list[ZipBackup.BackupTypes]: ...

