from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import FileWriter
from java.util import List
from zombie.world import ItemInfo

class Log:

  def __init__(self): ...

  class ModIDChangedItem(Log.BaseItemLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, itemInfo: ItemInfo, oldModId: str, newModId: str): ...

  class RemovedItem(Log.BaseItemLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, itemInfo: ItemInfo, isScriptMissing: bool): ...

  class ObsoleteItem(Log.BaseItemLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, itemInfo: ItemInfo): ...

  class ReinstateItem(Log.BaseItemLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, itemInfo: ItemInfo): ...

  class RegisterItem(Log.BaseItemLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, itemInfo: ItemInfo): ...

  class BaseItemLog(Log.BaseLog):

    def __init__(self, itemInfo: ItemInfo): ...

  class RegisterObject(Log.BaseLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, objectName: str, id: int): ...

  class Comment(Log.BaseLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, txt: str): ...

  class Info(Log.BaseLog):

    def saveAsText(self, w: FileWriter, padding: str) -> None: ...

    def __init__(self, timeStamp: str, saveWorld: str, worldVersion: int, mods: List[str]):
      self.haserrored: bool

  class BaseLog:

    def isIgnoreSaveCheck(self) -> bool: ...

    def __init__(self): ...


class WorldDictionaryLogger:

  @staticmethod
  @overload
  def log(msg: str) -> None: ...

  @staticmethod
  @overload
  def log(log: Log.BaseLog) -> None: ...

  @staticmethod
  @overload
  def log(msg: str, debugPrint: bool) -> None: ...

  @staticmethod
  def reset() -> None: ...

  @staticmethod
  def saveLog(saveFile: str) -> None: ...

  @staticmethod
  def startLogging() -> None: ...

  def __init__(self): ...

