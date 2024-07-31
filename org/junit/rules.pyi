from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from org.junit.runner import Description
from org.junit.runners.model import Statement

class TestRule:

  def apply(self, arg0: Statement, arg1: Description) -> Statement: ...

