from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from jassimp import AiMesh, AiScene, JassimpLibraryLoader
from java.lang import Enum
from zombie.core.skinnedmodel.model import AnimationAsset, ModelMesh, SkinningData

class ImportedSkeleton:

  def getNumBoneAncestors(self, boneIdx: int) -> int: ...

  @staticmethod
  def process(params: ImportedSkeletonParams) -> ImportedSkeleton: ...


class ImportedSkeletonParams(ProcessedAiSceneParams):

  @staticmethod
  def create(aiSceneParams: ProcessedAiSceneParams, mesh: AiMesh) -> ImportedSkeletonParams: ...


class ImportedSkinnedMesh:

  def __init__(self, skeleton: ImportedSkeleton, mesh: AiMesh): ...


class ImportedStaticMesh:

  def __init__(self, mesh: AiMesh): ...


class JAssImpImporter:

  @staticmethod
  def Init() -> None: ...

  @staticmethod
  def getSharedString(str: str, countKey: str) -> str: ...

  @staticmethod
  def takeOutTheTrash(scene: AiScene) -> None: ...

  def __init__(self): ...

  class LibraryLoader(JassimpLibraryLoader):

    def loadLibrary(self) -> None: ...

  class LoadMode(Enum):

    AnimationOnly: JAssImpImporter.LoadMode

    Normal: JAssImpImporter.LoadMode

    StaticMesh: JAssImpImporter.LoadMode

    @staticmethod
    def valueOf(arg0: str) -> JAssImpImporter.LoadMode: ...

    @staticmethod
    def values() -> list[JAssImpImporter.LoadMode]: ...


class ProcessedAiScene:

  def applyToAnimation(self, anim: AnimationAsset) -> None: ...

  def applyToMesh(self, mesh: ModelMesh, mode: JAssImpImporter.LoadMode, bReverse: bool, skinnedTo: SkinningData) -> None: ...

  @staticmethod
  def process(params: ProcessedAiSceneParams) -> ProcessedAiScene: ...


class ProcessedAiSceneParams:

  @staticmethod
  def create() -> ProcessedAiSceneParams: ...

