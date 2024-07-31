from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.lang import Enum
from java.util import HashMap, ArrayList, BitSet
from zombie.audio import BaseSoundEmitter, BaseSoundBank, FMODParameter, GameSoundClip, FMODParameterList
from zombie.characters import IsoGameCharacter
from zombie.iso import IsoObject, IsoGridSquare

class Audio:

  def getName(self) -> str: ...

  def isPlaying(self) -> bool: ...

  def pause(self) -> None: ...

  def setName(self, arg0: str) -> None: ...

  def setVolume(self, arg0: float) -> None: ...

  def start(self) -> None: ...

  def stop(self) -> None: ...


class BaseSoundListener:

  def setPos(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def tick(self) -> None: ...

  def __init__(self, arg0: int):
    self.index: int
    self.x: float
    self.y: float
    self.z: float


class DummySoundListener(BaseSoundListener):

  def tick(self) -> None: ...

  def __init__(self, arg0: int): ...


class EmitterType(Enum):

  Extra: EmitterType

  Footstep: EmitterType

  Voice: EmitterType

  @staticmethod
  def valueOf(arg0: str) -> EmitterType: ...

  @staticmethod
  def values() -> list[EmitterType]: ...


class FMODAudio:

  @overload
  def getName(self) -> str: ...

  @overload
  def getName(self) -> str: ...

  @overload
  def isPlaying(self) -> bool: ...

  @overload
  def isPlaying(self) -> bool: ...

  @overload
  def pause(self) -> None: ...

  @overload
  def pause(self) -> None: ...

  @overload
  def setName(self, arg0: str) -> None: ...

  @overload
  def setName(self, arg0: str) -> None: ...

  @overload
  def setVolume(self, arg0: float) -> None: ...

  @overload
  def setVolume(self, arg0: float) -> None: ...

  @overload
  def start(self) -> None: ...

  @overload
  def start(self) -> None: ...

  @overload
  def stop(self) -> None: ...

  @overload
  def stop(self) -> None: ...

  def __init__(self, arg0: BaseSoundEmitter):
    self.emitter: BaseSoundEmitter


class FMODFootstep:

  def getSoundToPlay(self, arg0: IsoGameCharacter) -> str: ...

  def isUpstairs(self, arg0: IsoGameCharacter) -> bool: ...

  def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str):
    self.concrete: str
    self.grass: str
    self.upstairs: str
    self.wood: str
    self.woodcreak: str


class FMODManager:

  FMOD_2D: int

  FMOD_3D: int

  FMOD_3D_CUSTOMROLLOFF: int

  FMOD_3D_HEADRELATIVE: int

  FMOD_3D_IGNOREGEOMETRY: int

  FMOD_3D_INVERSEROLLOFF: int

  FMOD_3D_INVERSETAPEREDROLLOFF: int

  FMOD_3D_LINEARROLLOFF: int

  FMOD_3D_LINEARSQUAREROLLOFF: int

  FMOD_3D_WORLDRELATIVE: int

  FMOD_ACCURATETIME: int

  FMOD_CREATECOMPRESSEDSAMPLE: int

  FMOD_CREATESAMPLE: int

  FMOD_CREATESTREAM: int

  FMOD_DEFAULT: int

  FMOD_HARDWARE: int

  FMOD_IGNORETAGS: int

  FMOD_INIT_3D_RIGHTHANDED: int

  FMOD_INIT_CHANNEL_DISTANCEFILTER: int

  FMOD_INIT_CHANNEL_LOWPASS: int

  FMOD_INIT_GEOMETRY_USECLOSEST: int

  FMOD_INIT_MIX_FROM_UPDATE: int

  FMOD_INIT_NORMAL: int

  FMOD_INIT_PREFER_DOLBY_DOWNMIX: int

  FMOD_INIT_PROFILE_ENABLE: int

  FMOD_INIT_PROFILE_METER_ALL: int

  FMOD_INIT_STREAM_FROM_UPDATE: int

  FMOD_INIT_THREAD_UNSAFE: int

  FMOD_INIT_VOL0_BECOMES_VIRTUAL: int

  FMOD_LOADSECONDARYRAM: int

  FMOD_LOOP_BIDI: int

  FMOD_LOOP_NORMAL: int

  FMOD_LOOP_OFF: int

  FMOD_LOWMEM: int

  FMOD_MPEGSEARCH: int

  FMOD_NONBLOCKING: int

  FMOD_OPENMEMORY: int

  FMOD_OPENMEMORY_POINT: int

  FMOD_OPENONLY: int

  FMOD_OPENRAW: int

  FMOD_OPENUSER: int

  FMOD_PRESET_ALLEY: int

  FMOD_PRESET_ARENA: int

  FMOD_PRESET_AUDITORIUM: int

  FMOD_PRESET_BATHROOM: int

  FMOD_PRESET_CARPETTEDHALLWAY: int

  FMOD_PRESET_CAVE: int

  FMOD_PRESET_CITY: int

  FMOD_PRESET_CONCERTHALL: int

  FMOD_PRESET_FOREST: int

  FMOD_PRESET_GENERIC: int

  FMOD_PRESET_HALLWAY: int

  FMOD_PRESET_HANGAR: int

  FMOD_PRESET_LIVINGROOM: int

  FMOD_PRESET_MOUNTAINS: int

  FMOD_PRESET_OFF: int

  FMOD_PRESET_PADDEDCELL: int

  FMOD_PRESET_PARKINGLOT: int

  FMOD_PRESET_PLAIN: int

  FMOD_PRESET_QUARRY: int

  FMOD_PRESET_ROOM: int

  FMOD_PRESET_SEWERPIPE: int

  FMOD_PRESET_STONECORRIDOR: int

  FMOD_PRESET_STONEROOM: int

  FMOD_PRESET_UNDERWATER: int

  FMOD_SOFTWARE: int

  FMOD_SOUND_FORMAT_BITSTREAM: int

  FMOD_SOUND_FORMAT_NONE: int

  FMOD_SOUND_FORMAT_PCM16: int

  FMOD_SOUND_FORMAT_PCM24: int

  FMOD_SOUND_FORMAT_PCM32: int

  FMOD_SOUND_FORMAT_PCM8: int

  FMOD_SOUND_FORMAT_PCMFLOAT: int

  FMOD_STUDIO_INIT_ALLOW_MISSING_PLUGINS: int

  FMOD_STUDIO_INIT_DEFERRED_CALLBACKS: int

  FMOD_STUDIO_INIT_LIVEUPDATE: int

  FMOD_STUDIO_INIT_NORMAL: int

  FMOD_STUDIO_INIT_SYNCHRONOUS_UPDATE: int

  FMOD_STUDIO_PLAYBACK_PLAYING: int

  FMOD_STUDIO_PLAYBACK_STARTING: int

  FMOD_STUDIO_PLAYBACK_STOPPED: int

  FMOD_STUDIO_PLAYBACK_STOPPING: int

  FMOD_STUDIO_PLAYBACK_SUSTAINING: int

  FMOD_TIMEUNIT_MS: int

  FMOD_TIMEUNIT_PCM: int

  FMOD_TIMEUNIT_PCMBYTES: int

  FMOD_UNIQUE: int

  FMOD_VIRTUAL_PLAYFROMSTART: int

  instance: FMODManager

  def applyDSP(self) -> None: ...

  def getEventDescription(self, arg0: str) -> FMOD_STUDIO_EVENT_DESCRIPTION: ...

  def getNumListeners(self) -> int: ...

  def getParameterCount(self) -> int: ...

  def getParameterDescription(self, arg0: str) -> FMOD_STUDIO_PARAMETER_DESCRIPTION: ...

  def getParameterID(self, arg0: str) -> FMOD_STUDIO_PARAMETER_ID: ...

  def init(self) -> None: ...

  def isPlaying(self, arg0: int) -> bool: ...

  @overload
  def loadSound(self, arg0: str) -> int: ...

  @overload
  def loadSound(self, arg0: str, arg1: bool) -> int: ...

  def loadTest(self) -> None: ...

  def playTest(self) -> None: ...

  def stopSound(self, arg0: int) -> None: ...

  def tick(self) -> None: ...

  def updateReverbPreset(self) -> None: ...

  def __init__(self):
    self.channelgroupingamenonbanksounds: int

  class TestZombieInfo:

    def createZombieInstance(self, arg0: int, arg1: float, arg2: float) -> int: ...

    def __init__(self, arg0: int, arg1: float, arg2: float):
      self.event: int
      self.inst: int
      self.x: float
      self.y: float


class FMODSoundBank(BaseSoundBank):

  def addFootstep(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str) -> None: ...

  def addVoice(self, arg0: str, arg1: str, arg2: float) -> None: ...

  def getFootstep(self, arg0: str) -> FMODFootstep: ...

  def getVoice(self, arg0: str) -> FMODVoice: ...

  def __init__(self):
    self.footstepmap: HashMap[str, FMODFootstep]
    self.voicemap: HashMap[str, FMODVoice]


class FMODSoundEmitter(BaseSoundEmitter):

  def addParameter(self, arg0: FMODParameter) -> None: ...

  def clearParameters(self) -> None: ...

  def hasSoundsToStart(self) -> bool: ...

  def hasSustainPoints(self, arg0: int) -> bool: ...

  def isEmpty(self) -> bool: ...

  @overload
  def isPlaying(self, arg0: str) -> bool: ...

  @overload
  def isPlaying(self, arg0: int) -> bool: ...

  def playAmbientLoopedImpl(self, arg0: str) -> int: ...

  def playAmbientSound(self, arg0: str) -> int: ...

  def playClip(self, arg0: GameSoundClip, arg1: IsoObject) -> int: ...

  @overload
  def playSound(self, arg0: str) -> int: ...

  @overload
  def playSound(self, arg0: str, arg1: bool) -> int: ...

  @overload
  def playSound(self, arg0: str, arg1: IsoGameCharacter) -> int: ...

  @overload
  def playSound(self, arg0: str, arg1: IsoGridSquare) -> int: ...

  @overload
  def playSound(self, arg0: str, arg1: IsoObject) -> int: ...

  @overload
  def playSound(self, arg0: str, arg1: int, arg2: int, arg3: int) -> int: ...

  @overload
  def playSoundImpl(self, arg0: str, arg1: IsoGridSquare) -> int: ...

  @overload
  def playSoundImpl(self, arg0: str, arg1: IsoObject) -> int: ...

  @overload
  def playSoundImpl(self, arg0: str, arg1: bool, arg2: IsoObject) -> int: ...

  def playSoundLooped(self, arg0: str) -> int: ...

  def playSoundLoopedImpl(self, arg0: str) -> int: ...

  def randomStart(self) -> None: ...

  def restart(self, arg0: int) -> bool: ...

  def set3D(self, arg0: int, arg1: bool) -> None: ...

  def setParameterValue(self, arg0: int, arg1: FMOD_STUDIO_PARAMETER_DESCRIPTION, arg2: float) -> None: ...

  def setPitch(self, arg0: int, arg1: float) -> None: ...

  def setPos(self, arg0: float, arg1: float, arg2: float) -> None: ...

  def setTimelinePosition(self, arg0: int, arg1: str) -> None: ...

  def setVolume(self, arg0: int, arg1: float) -> None: ...

  def setVolumeAll(self, arg0: float) -> None: ...

  def stopAll(self) -> None: ...

  def stopOrTriggerSound(self, arg0: int) -> None: ...

  def stopOrTriggerSoundByName(self, arg0: str) -> None: ...

  def stopSound(self, arg0: int) -> int: ...

  def stopSoundByName(self, arg0: str) -> int: ...

  def stopSoundLocal(self, arg0: int) -> None: ...

  def tick(self) -> None: ...

  def triggerCue(self, arg0: int) -> None: ...

  @staticmethod
  def update() -> None: ...

  def __init__(self):
    self.emittertype: EmitterType
    self.parameterupdater: IFMODParameterUpdater
    self.parent: IsoObject
    self.x: float
    self.y: float
    self.z: float

  class Sound: ...

  class FileSound(FMODSoundEmitter.Sound): ...

  class ParameterValue: ...

  class EventSound(FMODSoundEmitter.Sound): ...


class FMODVoice:

  def __init__(self, arg0: str, arg1: float):
    self.priority: float
    self.sound: str


class FMOD_GUID:

  def address(self) -> int: ...

  def __init__(self, arg0: int): ...


class FMOD_STUDIO_EVENT_CALLBACK:

  def started(self, arg0: int) -> None: ...

  def stopped(self, arg0: int) -> None: ...

  def timelineMarker(self, arg0: int, arg1: str, arg2: int) -> None: ...

  def __init__(self): ...


class FMOD_STUDIO_EVENT_CALLBACK_TYPE(Enum):

  FMOD_STUDIO_EVENT_CALLBACK_ALL: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_CREATE_PROGRAMMER_SOUND: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_CREATED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_DESTROY_PROGRAMMER_SOUND: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_DESTROYED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_PLUGIN_CREATED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_PLUGIN_DESTROYED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_REAL_TO_VIRTUAL: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_RESTARTED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_SOUND_PLAYED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_SOUND_STOPPED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_START_EVENT_COMMAND: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_START_FAILED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_STARTED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_STARTING: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_STOPPED: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_TIMELINE_BEAT: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_TIMELINE_MARKER: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  FMOD_STUDIO_EVENT_CALLBACK_VIRTUAL_TO_REAL: FMOD_STUDIO_EVENT_CALLBACK_TYPE

  @staticmethod
  def valueOf(arg0: str) -> FMOD_STUDIO_EVENT_CALLBACK_TYPE: ...

  @staticmethod
  def values() -> list[FMOD_STUDIO_EVENT_CALLBACK_TYPE]: ...


class FMOD_STUDIO_EVENT_DESCRIPTION:

  def hasParameter(self, arg0: FMOD_STUDIO_PARAMETER_DESCRIPTION) -> bool: ...

  def __init__(self, arg0: int, arg1: str, arg2: FMOD_GUID, arg3: bool, arg4: int):
    self.address: int
    self.bhassustainpoints: bool
    self.id: FMOD_GUID
    self.length: int
    self.parameters: ArrayList[FMOD_STUDIO_PARAMETER_DESCRIPTION]
    self.path: str


class FMOD_STUDIO_PARAMETER_DESCRIPTION:

  def isGlobal(self) -> bool: ...

  def __init__(self, arg0: str, arg1: FMOD_STUDIO_PARAMETER_ID, arg2: int, arg3: int):
    self.flags: int
    self.globalindex: int
    self.id: FMOD_STUDIO_PARAMETER_ID
    self.name: str


class FMOD_STUDIO_PARAMETER_FLAGS(Enum):

  FMOD_STUDIO_PARAMETER_AUTOMATIC: FMOD_STUDIO_PARAMETER_FLAGS

  FMOD_STUDIO_PARAMETER_DISCRETE: FMOD_STUDIO_PARAMETER_FLAGS

  FMOD_STUDIO_PARAMETER_GLOBAL: FMOD_STUDIO_PARAMETER_FLAGS

  FMOD_STUDIO_PARAMETER_READONLY: FMOD_STUDIO_PARAMETER_FLAGS

  @staticmethod
  def valueOf(arg0: str) -> FMOD_STUDIO_PARAMETER_FLAGS: ...

  @staticmethod
  def values() -> list[FMOD_STUDIO_PARAMETER_FLAGS]: ...


class FMOD_STUDIO_PARAMETER_ID:

  def address(self) -> int: ...

  def __init__(self, arg0: int): ...


class FMOD_STUDIO_PLAYBACK_STATE(Enum):

  FMOD_STUDIO_PLAYBACK_PLAYING: FMOD_STUDIO_PLAYBACK_STATE

  FMOD_STUDIO_PLAYBACK_STARTING: FMOD_STUDIO_PLAYBACK_STATE

  FMOD_STUDIO_PLAYBACK_STATE: FMOD_STUDIO_PLAYBACK_STATE

  FMOD_STUDIO_PLAYBACK_STOPPED: FMOD_STUDIO_PLAYBACK_STATE

  FMOD_STUDIO_PLAYBACK_STOPPING: FMOD_STUDIO_PLAYBACK_STATE

  FMOD_STUDIO_PLAYBACK_SUSTAINING: FMOD_STUDIO_PLAYBACK_STATE

  @staticmethod
  def valueOf(arg0: str) -> FMOD_STUDIO_PLAYBACK_STATE: ...

  @staticmethod
  def values() -> list[FMOD_STUDIO_PLAYBACK_STATE]: ...


class IFMODListener: ...


class IFMODParameterUpdater:

  def getFMODParameters(self) -> FMODParameterList: ...

  def startEvent(self, arg0: int, arg1: GameSoundClip, arg2: BitSet) -> None: ...

  def stopEvent(self, arg0: int, arg1: GameSoundClip, arg2: BitSet) -> None: ...

  def updateEvent(self, arg0: int, arg1: GameSoundClip) -> None: ...


class SoundListener(BaseSoundListener):

  def tick(self) -> None: ...

  def __init__(self, arg0: int):
    self.lx: float
    self.ly: float
    self.lz: float

