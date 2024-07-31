from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.util import ArrayList
from zombie.erosion.season import ErosionSeason
from zombie.iso.weather import ClimateManager

class ClimMngrDebug(ClimateManager):

  def SimulateDays(self, amountOfDays: int, totalRuns: int) -> None: ...

  def getDayMeanTemperature(self) -> float: ...

  def getSeason(self) -> ErosionSeason: ...

  def resetOverrides(self) -> None: ...

  def setRainModOverride(self, rainmod: int) -> None: ...

  def triggerCustomWeatherStage(self, stage: int, duration: float) -> bool: ...

  def unsetRainModOverride(self) -> None: ...

  def __init__(self):
    self.runs: ArrayList[ClimMngrDebug.RunInfo]

  class RunInfo:

    @overload
    def addRecord(self, arg0: float) -> ClimMngrDebug.RecordInfo: ...

    @overload
    def addRecord(self, arg0: int, arg1: float, arg2: float, arg3: bool, arg4: bool, arg5: bool) -> ClimMngrDebug.RecordInfo: ...

    def calculate(self) -> None: ...

  class RecordInfo: ...

