from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Integer
from java.util import Locale, Map, ResourceBundle

class CalendarDataProvider(LocaleServiceProvider):

  def getFirstDayOfWeek(self, arg0: Locale) -> int: ...

  def getMinimalDaysInFirstWeek(self, arg0: Locale) -> int: ...


class CalendarNameProvider(LocaleServiceProvider):

  def getDisplayName(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: Locale) -> str: ...

  def getDisplayNames(self, arg0: str, arg1: int, arg2: int, arg3: Locale) -> Map[str, Integer]: ...


class CurrencyNameProvider(LocaleServiceProvider):

  def getDisplayName(self, arg0: str, arg1: Locale) -> str: ...

  def getSymbol(self, arg0: str, arg1: Locale) -> str: ...


class LocaleNameProvider(LocaleServiceProvider):

  def getDisplayCountry(self, arg0: str, arg1: Locale) -> str: ...

  def getDisplayLanguage(self, arg0: str, arg1: Locale) -> str: ...

  def getDisplayScript(self, arg0: str, arg1: Locale) -> str: ...

  def getDisplayUnicodeExtensionKey(self, arg0: str, arg1: Locale) -> str: ...

  def getDisplayUnicodeExtensionType(self, arg0: str, arg1: str, arg2: Locale) -> str: ...

  def getDisplayVariant(self, arg0: str, arg1: Locale) -> str: ...


class LocaleServiceProvider:

  def getAvailableLocales(self) -> list[Locale]: ...

  def isSupportedLocale(self, arg0: Locale) -> bool: ...


class ResourceBundleControlProvider:

  def getControl(self, arg0: str) -> ResourceBundle.Control: ...


class TimeZoneNameProvider(LocaleServiceProvider):

  def getDisplayName(self, arg0: str, arg1: bool, arg2: int, arg3: Locale) -> str: ...

  def getGenericDisplayName(self, arg0: str, arg1: int, arg2: Locale) -> str: ...

