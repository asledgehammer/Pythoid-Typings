from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from zombie.characters import IsoGameCharacter
from zombie.core import Color

class Moodle:

  def SetLevel(self, val: int) -> None: ...

  def Update(self) -> bool: ...

  def chevronDifference(self, count: int, isup: bool, col: Color) -> bool: ...

  def getChevronColor(self) -> Color: ...

  def getChevronCount(self) -> int: ...

  def getLevel(self) -> int: ...

  def isChevronIsUp(self) -> bool: ...

  def setChevron(self, count: int, isup: bool, col: Color) -> None: ...

  @overload
  def __init__(self, ChosenType: MoodleType, parent: IsoGameCharacter): ...
  @overload
  def __init__(self, ChosenType: MoodleType, parent: IsoGameCharacter, maxChevrons: int): ...


class MoodleType(Enum):

  Angry: MoodleType

  Bleeding: MoodleType

  Bored: MoodleType

  CantSprint: MoodleType

  Dead: MoodleType

  Drunk: MoodleType

  Endurance: MoodleType

  FoodEaten: MoodleType

  HasACold: MoodleType

  HeavyLoad: MoodleType

  Hungry: MoodleType

  Hyperthermia: MoodleType

  Hypothermia: MoodleType

  Injured: MoodleType

  MAX: MoodleType

  Pain: MoodleType

  Panic: MoodleType

  Sick: MoodleType

  Stress: MoodleType

  Thirst: MoodleType

  Tired: MoodleType

  Unhappy: MoodleType

  Wet: MoodleType

  Windchill: MoodleType

  Zombie: MoodleType

  @staticmethod
  def FromIndex(index: int) -> MoodleType: ...

  @staticmethod
  def FromString(str: str) -> MoodleType: ...

  @staticmethod
  def GoodBadNeutral(MT: MoodleType) -> int: ...

  @staticmethod
  def ToIndex(MT: MoodleType) -> int: ...

  @staticmethod
  def getDescriptionText(MT: MoodleType, Level: int) -> str: ...

  @staticmethod
  def getDisplayName(MT: MoodleType, Level: int) -> str: ...

  @staticmethod
  def valueOf(arg0: str) -> MoodleType: ...

  @staticmethod
  def values() -> list[MoodleType]: ...


class Moodles:

  def Randomise(self) -> None: ...

  def UI_RefreshNeeded(self) -> bool: ...

  def Update(self) -> None: ...

  def getGoodBadNeutral(self, MoodleIndex: int) -> int: ...

  def getMoodleChevronColor(self, moodleIndex: int) -> Color: ...

  def getMoodleChevronCount(self, moodleIndex: int) -> int: ...

  def getMoodleChevronIsUp(self, moodleIndex: int) -> bool: ...

  def getMoodleDescriptionString(self, MoodleIndex: int) -> str: ...

  def getMoodleDisplayString(self, MoodleIndex: int) -> str: ...

  @overload
  def getMoodleLevel(self, MoodleIndex: int) -> int: ...

  @overload
  def getMoodleLevel(self, MType: MoodleType) -> int: ...

  def getMoodleType(self, MoodleIndex: int) -> MoodleType: ...

  def getNumMoodles(self) -> int: ...

  def setMoodlesStateChanged(self, refresh: bool) -> None: ...

  def __init__(self, parent: IsoGameCharacter): ...

