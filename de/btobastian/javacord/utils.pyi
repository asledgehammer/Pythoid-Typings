from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.google.common.util.concurrent import ListeningExecutorService
from java.util.concurrent import ExecutorService

class ThreadPool:

  def getExecutorService(self) -> ExecutorService: ...

  def getListeningExecutorService(self) -> ListeningExecutorService: ...

  def getSingleThreadExecutorService(self, arg0: str) -> ExecutorService: ...

  def __init__(self): ...

