from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.net import URLStreamHandler

class Handler(URLStreamHandler):

  def checkNestedProtocol(self, arg0: str) -> str: ...

  def __init__(self): ...

