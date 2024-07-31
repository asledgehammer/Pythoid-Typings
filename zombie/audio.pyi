from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from fmod.fmod import FMODFootstep, FMODVoice, FMOD_STUDIO_PARAMETER_DESCRIPTION, FMOD_STUDIO_PARAMETER_ID, FMOD_STUDIO_EVENT_DESCRIPTION
from java.lang import Enum
from java.util import ArrayList
from zombie.characters import IsoGameCharacter
from zombie.iso import IsoObject, IsoGridSquare

class BaseSoundBank:

  instance: BaseSoundBank

  def addFootstep(self, alias: str, grass: str, wood: str, concrete: str, upstairs: str) -> None: ...

  def addVoice(self, alias: str, sound: str, priority: float) -> None: ...

  def getFootstep(self, alias: str) -> FMODFootstep: ...

  def getVoice(self, alias: str) -> FMODVoice: ...

  def __init__(self): ...


class BaseSoundEmitter:

  def hasSoundsToStart(self) -> bool: ...

  def hasSustainPoints(self, handle: int) -> bool: ...

  def isEmpty(self) -> bool: ...

  @overload
  def isPlaying(self, alias: str) -> bool: ...

  @overload
  def isPlaying(self, channel: int) -> bool: ...

  def playAmbientLoopedImpl(self, file: str) -> int: ...

  def playAmbientSound(self, name: str) -> int: ...

  def playClip(self, clip: GameSoundClip, parent: IsoObject) -> int: ...

  @overload
  def playSound(self, file: str) -> int: ...

  @overload
  def playSound(self, file: str, doWorldSound: bool) -> int: ...

  @overload
  def playSound(self, file: str, character: IsoGameCharacter) -> int: ...

  @overload
  def playSound(self, file: str, square: IsoGridSquare) -> int: ...

  @overload
  def playSound(self, file: str, parent: IsoObject) -> int: ...

  @overload
  def playSound(self, file: str, x: int, y: int, z: int) -> int: ...

  @overload
  def playSoundImpl(self, file: str, square: IsoGridSquare) -> int: ...

  @overload
  def playSoundImpl(self, file: str, parent: IsoObject) -> int: ...

  @overload
  def playSoundImpl(self, file: str, doWorldSound: bool, parent: IsoObject) -> int: ...

  def playSoundLooped(self, file: str) -> int: ...

  def playSoundLoopedImpl(self, file: str) -> int: ...

  def randomStart(self) -> None: ...

  def restart(self, handle: int) -> bool: ...

  def set3D(self, handle: int, is3D: bool) -> None: ...

  def setParameterValue(self, handle: int, parameterDescription: FMOD_STUDIO_PARAMETER_DESCRIPTION, value: float) -> None: ...

  def setPitch(self, handle: int, pitch: float) -> None: ...

  def setPos(self, x: float, y: float, z: float) -> None: ...

  def setTimelinePosition(self, handle: int, positionName: str) -> None: ...

  def setVolume(self, handle: int, volume: float) -> None: ...

  def setVolumeAll(self, volume: float) -> None: ...

  def stopAll(self) -> None: ...

  def stopOrTriggerSound(self, handle: int) -> None: ...

  def stopOrTriggerSoundByName(self, name: str) -> None: ...

  def stopSound(self, channel: int) -> int: ...

  def stopSoundByName(self, name: str) -> int: ...

  def stopSoundLocal(self, handle: int) -> None: ...

  def tick(self) -> None: ...

  def triggerCue(self, handle: int) -> None: ...

  def __init__(self): ...


class DummySoundBank(BaseSoundBank):

  def addFootstep(self, alias: str, grass: str, wood: str, concrete: str, upstairs: str) -> None: ...

  def addVoice(self, alias: str, sound: str, priority: float) -> None: ...

  def getFootstep(self, alias: str) -> FMODFootstep: ...

  def getVoice(self, alias: str) -> FMODVoice: ...

  def __init__(self): ...


class DummySoundEmitter(BaseSoundEmitter):

  def hasSoundsToStart(self) -> bool: ...

  def hasSustainPoints(self, handle: int) -> bool: ...

  def isEmpty(self) -> bool: ...

  @overload
  def isPlaying(self, alias: str) -> bool: ...

  @overload
  def isPlaying(self, channel: int) -> bool: ...

  def playAmbientLoopedImpl(self, file: str) -> int: ...

  def playAmbientSound(self, name: str) -> int: ...

  def playClip(self, clip: GameSoundClip, parent: IsoObject) -> int: ...

  @overload
  def playSound(self, file: str) -> int: ...

  @overload
  def playSound(self, file: str, doWorldSound: bool) -> int: ...

  @overload
  def playSound(self, file: str, character: IsoGameCharacter) -> int: ...

  @overload
  def playSound(self, file: str, square: IsoGridSquare) -> int: ...

  @overload
  def playSound(self, file: str, parent: IsoObject) -> int: ...

  @overload
  def playSound(self, file: str, x: int, y: int, z: int) -> int: ...

  @overload
  def playSoundImpl(self, file: str, square: IsoGridSquare) -> int: ...

  @overload
  def playSoundImpl(self, file: str, parent: IsoObject) -> int: ...

  @overload
  def playSoundImpl(self, file: str, doWorldSound: bool, parent: IsoObject) -> int: ...

  def playSoundLooped(self, file: str) -> int: ...

  def playSoundLoopedImpl(self, file: str) -> int: ...

  def randomStart(self) -> None: ...

  def restart(self, handle: int) -> bool: ...

  def set3D(self, handle: int, is3D: bool) -> None: ...

  def setParameterValue(self, handle: int, parameterDescription: FMOD_STUDIO_PARAMETER_DESCRIPTION, value: float) -> None: ...

  def setPitch(self, handle: int, volume: float) -> None: ...

  def setPos(self, x: float, y: float, z: float) -> None: ...

  def setTimelinePosition(self, handle: int, positionName: str) -> None: ...

  def setVolume(self, handle: int, volume: float) -> None: ...

  def setVolumeAll(self, volume: float) -> None: ...

  def stopAll(self) -> None: ...

  def stopOrTriggerSound(self, handle: int) -> None: ...

  def stopOrTriggerSoundByName(self, name: str) -> None: ...

  def stopSound(self, channel: int) -> int: ...

  def stopSoundByName(self, name: str) -> int: ...

  def stopSoundLocal(self, handle: int) -> None: ...

  def tick(self) -> None: ...

  def triggerCue(self, handle: int) -> None: ...

  def __init__(self): ...


class FMODGlobalParameter(FMODParameter):

  def setCurrentValue(self, value: float) -> None: ...

  def startEventInstance(self, eventInstance: int) -> None: ...

  def stopEventInstance(self, eventInstance: int) -> None: ...

  def __init__(self, name: str): ...


class FMODLocalParameter(FMODParameter):

  def calculateCurrentValue(self) -> float: ...

  def setCurrentValue(self, value: float) -> None: ...

  def startEventInstance(self, inst: int) -> None: ...

  def stopEventInstance(self, inst: int) -> None: ...

  def __init__(self, name: str): ...


class FMODParameter:

  def calculateCurrentValue(self) -> float: ...

  def getCurrentValue(self) -> float: ...

  def getName(self) -> str: ...

  def getParameterDescription(self) -> FMOD_STUDIO_PARAMETER_DESCRIPTION: ...

  def getParameterID(self) -> FMOD_STUDIO_PARAMETER_ID: ...

  def resetToDefault(self) -> None: ...

  def setCurrentValue(self, value: float) -> None: ...

  def startEventInstance(self, eventInstance: int) -> None: ...

  def stopEventInstance(self, eventInstance: int) -> None: ...

  def update(self) -> None: ...

  def __init__(self, name: str): ...


class FMODParameterList:

  def add(self, parameter: FMODParameter) -> None: ...

  def get(self, pdesc: FMOD_STUDIO_PARAMETER_DESCRIPTION) -> FMODParameter: ...

  def update(self) -> None: ...

  def __init__(self):
    self.parameterarray: list[FMODParameter]
    self.parameterlist: ArrayList[FMODParameter]


class GameSound:

  def getCategory(self) -> str: ...

  def getMasterName(self) -> str: ...

  def getName(self) -> str: ...

  def getRandomClip(self) -> GameSoundClip: ...

  def getUserVolume(self) -> float: ...

  def isLooped(self) -> bool: ...

  def numClipsUsingParameter(self, parameterName: str) -> int: ...

  def reset(self) -> None: ...

  def setUserVolume(self, gain: float) -> None: ...

  def __init__(self):
    self.category: str
    self.clips: ArrayList[GameSoundClip]
    self.is3d: bool
    self.loop: bool
    self.master: GameSound.MasterVolume
    self.maxinstancesperemitter: int
    self.name: str
    self.reloadepoch: int

  class MasterVolume(Enum):

    Ambient: GameSound.MasterVolume

    Music: GameSound.MasterVolume

    Primary: GameSound.MasterVolume

    VehicleEngine: GameSound.MasterVolume

    @staticmethod
    def valueOf(arg0: str) -> GameSound.MasterVolume: ...

    @staticmethod
    def values() -> list[GameSound.MasterVolume]: ...


class GameSoundClip:

  INIT_FLAG_DISTANCE_MAX: int

  INIT_FLAG_DISTANCE_MIN: int

  def checkReloaded(self) -> GameSoundClip: ...

  def getEffectiveVolume(self) -> float: ...

  def getEffectiveVolumeInMenu(self) -> float: ...

  def getEvent(self) -> str: ...

  def getFile(self) -> str: ...

  def getMaxDistance(self) -> float: ...

  def getMinDistance(self) -> float: ...

  def getPitch(self) -> float: ...

  def getVolume(self) -> float: ...

  def hasMaxDistance(self) -> bool: ...

  def hasMinDistance(self) -> bool: ...

  def hasParameter(self, parameterDescription: FMOD_STUDIO_PARAMETER_DESCRIPTION) -> bool: ...

  def hasSustainPoints(self) -> bool: ...

  def __init__(self, gameSound: GameSound):
    self.distancemax: float
    self.distancemin: float
    self.event: str
    self.eventdescription: FMOD_STUDIO_EVENT_DESCRIPTION
    self.eventdescriptionmp: FMOD_STUDIO_EVENT_DESCRIPTION
    self.file: str
    self.gamesound: GameSound
    self.initflags: int
    self.pitch: float
    self.priority: int
    self.reloadepoch: int
    self.reverbfactor: float
    self.reverbmaxrange: float
    self.volume: float


class ObjectAmbientEmitters:

  def render(self) -> None: ...

  def update(self) -> None: ...

  @staticmethod
  def Reset() -> None: ...

  @staticmethod
  def getInstance() -> ObjectAmbientEmitters: ...

  class Slot: ...

  class PowerPolicy(Enum):

    ExteriorOK: ObjectAmbientEmitters.PowerPolicy

    InteriorHydro: ObjectAmbientEmitters.PowerPolicy

    NotRequired: ObjectAmbientEmitters.PowerPolicy

    @staticmethod
    def valueOf(arg0: str) -> ObjectAmbientEmitters.PowerPolicy: ...

    @staticmethod
    def values() -> list[ObjectAmbientEmitters.PowerPolicy]: ...

  class DoorLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class WindowLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class ObjectWithDistance: ...

  class PerObjectLogic:

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def init(self, object: IsoObject) -> ObjectAmbientEmitters.PerObjectLogic: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self):
      self.object: IsoObject
      self.parametervalue1: float

  class ChunkData:

    def addObject(self, object: IsoObject, logic: ObjectAmbientEmitters.PerObjectLogic) -> None: ...

    def hasObject(self, object: IsoObject) -> bool: ...

    def removeObject(self, object: IsoObject) -> None: ...

    def reset(self) -> None: ...

    def __init__(self): ...

  class WaterDripLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class TreeAmbianceLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class TentAmbianceLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class AmbientSoundLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def init(self, object: IsoObject) -> ObjectAmbientEmitters.PerObjectLogic: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...

  class FridgeHumLogic(ObjectAmbientEmitters.PerObjectLogic):

    def checkParameters(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def getSoundName(self) -> str: ...

    def shouldPlaySound(self) -> bool: ...

    def startPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def stopPlaying(self, emitter: BaseSoundEmitter, instance: int) -> None: ...

    def __init__(self): ...
