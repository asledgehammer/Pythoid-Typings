from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import Locale
from java.util.spi import LocaleServiceProvider

class JavaTimeDateTimePatternProvider(LocaleServiceProvider):

  def getJavaTimeDateTimePattern(self, arg0: int, arg1: int, arg2: str, arg3: Locale) -> str: ...

