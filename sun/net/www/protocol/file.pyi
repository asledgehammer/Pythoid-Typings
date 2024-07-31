from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.net import URLStreamHandler, URL, URLConnection, Proxy

class Handler(URLStreamHandler):

  @overload
  def openConnection(self, arg0: URL) -> URLConnection: ...

  @overload
  def openConnection(self, arg0: URL, arg1: Proxy) -> URLConnection: ...

  def __init__(self): ...

