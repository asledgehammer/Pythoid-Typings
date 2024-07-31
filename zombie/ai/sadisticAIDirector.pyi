from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from zombie.characters import IsoPlayer, IsoGameCharacter

class SleepingEvent:

  instance: SleepingEvent

  zombiesInvasion: bool

  def setPlayerFallAsleep(self, chr: IsoPlayer, sleepingTime: int) -> None: ...

  def update(self, chr: IsoPlayer) -> None: ...

  @overload
  def wakeUp(self, chr: IsoGameCharacter) -> None: ...

  @overload
  def wakeUp(self, chr: IsoGameCharacter, remote: bool) -> None: ...

  def __init__(self): ...


class SleepingEventData:

  def getHoursSinceRainStarted(self) -> float: ...

  def reset(self) -> None: ...

  def __init__(self): ...

