from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import File
from java.lang import Enum
from java.net import URI
from java.util import EventObject, List

class AboutEvent(AppEvent):

  def __init__(self): ...


class AboutHandler:

  def handleAbout(self, arg0: AboutEvent) -> None: ...


class AppEvent(EventObject): ...


class FilesEvent(AppEvent):

  def getFiles(self) -> List[File]: ...


class OpenFilesEvent(FilesEvent):

  def getSearchTerm(self) -> str: ...

  def __init__(self, arg0: List[File], arg1: str): ...


class OpenFilesHandler:

  def openFiles(self, arg0: OpenFilesEvent) -> None: ...


class OpenURIEvent(AppEvent):

  def getURI(self) -> URI: ...

  def __init__(self, arg0: URI): ...


class OpenURIHandler:

  def openURI(self, arg0: OpenURIEvent) -> None: ...


class PreferencesEvent(AppEvent):

  def __init__(self): ...


class PreferencesHandler:

  def handlePreferences(self, arg0: PreferencesEvent) -> None: ...


class PrintFilesEvent(FilesEvent):

  def __init__(self, arg0: List[File]): ...


class PrintFilesHandler:

  def printFiles(self, arg0: PrintFilesEvent) -> None: ...


class QuitEvent(AppEvent):

  def __init__(self): ...


class QuitHandler:

  def handleQuitRequestWith(self, arg0: QuitEvent, arg1: QuitResponse) -> None: ...


class QuitResponse:

  def cancelQuit(self) -> None: ...

  def performQuit(self) -> None: ...


class QuitStrategy(Enum):

  CLOSE_ALL_WINDOWS: QuitStrategy

  NORMAL_EXIT: QuitStrategy

  @staticmethod
  def valueOf(arg0: str) -> QuitStrategy: ...

  @staticmethod
  def values() -> list[QuitStrategy]: ...


class SystemEventListener: ...

