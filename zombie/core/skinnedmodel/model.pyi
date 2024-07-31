from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from jassimp import AiPostProcessSteps
from java.lang import Integer, Enum
from java.nio import FloatBuffer, IntBuffer, ByteBuffer
from java.util import EnumSet, HashMap, ArrayList, List
from java.util.function import Consumer
from org.joml import Matrix4f, Vector3f
from org.lwjgl.util.vector import Matrix4f, Vector3f
from zombie.asset import Asset, AssetType, AssetManager, AssetPath
from zombie.characterTextures import BloodBodyPartType
from zombie.characters import IsoGameCharacter
from zombie.core import Color, ImmutableColor
from zombie.core.VBO import IGLBufferObject
from zombie.core.skinnedmodel import ModelManager, Vector3, Vector4
from zombie.core.skinnedmodel.animation import AnimationClip, AnimationPlayer
from zombie.core.skinnedmodel.model.jassimp import ProcessedAiScene
from zombie.core.skinnedmodel.shader import Shader
from zombie.core.skinnedmodel.visual import ItemVisual, BaseVisual, ItemVisuals, HumanVisual
from zombie.core.textures import Texture, TextureDraw, ColorInfo, TextureFBO
from zombie.fileSystem import FileTask, IFileTaskCallback, FileSystem
from zombie.inventory import InventoryItem
from zombie.iso import IsoLightSource, Vector3, Vector2, IsoMovingObject, IsoGridSquare
from zombie.scripting.objects import ModelAttachment, ModelScript
from zombie.util import PooledObject
from zombie.vehicles import BaseVehicle

class AiSceneAsset(Asset):

  ASSET_TYPE: AssetType

  def getType(self) -> AssetType: ...

  class AiSceneAssetParams(AssetManager.AssetParams):

    def __init__(self): ...


class AiSceneAssetManager(AssetManager):

  instance: AiSceneAssetManager

  def onFileTaskFinished(self, asset: AiSceneAsset, result: object) -> None: ...

  def __init__(self): ...

  class FileTask_LoadAiScene(FileTask):

    def call(self) -> object: ...

    def done(self) -> None: ...

    def getErrorMessage(self) -> str: ...

    def __init__(self, arg0: str, arg1: EnumSet[AiPostProcessSteps], arg2: IFileTaskCallback, arg3: FileSystem): ...


class AnimationAsset(Asset):

  ASSET_TYPE: AssetType

  def getType(self) -> AssetType: ...

  def onBeforeReady(self) -> None: ...

  def setAssetParams(self, params: AssetManager.AssetParams) -> None: ...

  def __init__(self, path: AssetPath, manager: AssetManager, params: AnimationAsset.AnimationAssetParams):
    self.animationclips: HashMap[str, AnimationClip]
    self.assetparams: AnimationAsset.AnimationAssetParams
    self.modanimations: ModelManager.ModAnimations
    self.modelmanagerkey: str
    self.skinningdata: SkinningData

  class AnimationAssetParams(AssetManager.AssetParams):

    def __init__(self):
      self.animationsmesh: ModelMesh


class AnimationAssetManager(AssetManager):

  instance: AnimationAssetManager

  def __init__(self): ...


class CharacterMask:

  def contentsToString(self) -> str: ...

  def copyFrom(self, rhs: CharacterMask) -> None: ...

  def forEachVisible(self, action: Consumer[CharacterMask.Part]) -> None: ...

  def isAllVisible(self) -> bool: ...

  def isBloodBodyPartVisible(self, bpt: BloodBodyPartType) -> bool: ...

  def isNothingVisible(self) -> bool: ...

  def isPartVisible(self, part: CharacterMask.Part) -> bool: ...

  def isTorsoVisible(self) -> bool: ...

  def setAllVisible(self, isVisible: bool) -> None: ...

  def setPartVisible(self, part: CharacterMask.Part, isVisible: bool) -> None: ...

  def setPartsVisible(self, parts: ArrayList[Integer], isVisible: bool) -> None: ...

  def toString(self) -> str: ...

  def __init__(self): ...

  class Part(Enum):

    Belt: CharacterMask.Part

    Chest: CharacterMask.Part

    Crotch: CharacterMask.Part

    Dress: CharacterMask.Part

    Head: CharacterMask.Part

    LeftArm: CharacterMask.Part

    LeftFoot: CharacterMask.Part

    LeftHand: CharacterMask.Part

    LeftLeg: CharacterMask.Part

    Pelvis: CharacterMask.Part

    RightArm: CharacterMask.Part

    RightFoot: CharacterMask.Part

    RightHand: CharacterMask.Part

    RightLeg: CharacterMask.Part

    Torso: CharacterMask.Part

    Waist: CharacterMask.Part

    def getBloodBodyPartTypes(self) -> list[BloodBodyPartType]: ...

    def getParent(self) -> CharacterMask.Part: ...

    def getValue(self) -> int: ...

    def hasSubdivisions(self) -> bool: ...

    def isSubdivision(self) -> bool: ...

    def subDivisions(self) -> list[CharacterMask.Part]: ...

    @staticmethod
    def count() -> int: ...

    @staticmethod
    def fromInt(index: int) -> CharacterMask.Part: ...

    @staticmethod
    def leaves() -> list[CharacterMask.Part]: ...

    @staticmethod
    def valueOf(arg0: str) -> CharacterMask.Part: ...

    @staticmethod
    def values() -> list[CharacterMask.Part]: ...


class FileTask_AbstractLoadModel(FileTask):

  def call(self) -> object: ...

  def getRawFileName(self) -> str: ...

  def loadFBX(self) -> ProcessedAiScene: ...

  def loadTxt(self) -> ModelTxt: ...

  def loadX(self) -> ProcessedAiScene: ...


class FileTask_LoadAnimation(FileTask_AbstractLoadModel):

  def done(self) -> None: ...

  def getErrorMessage(self) -> str: ...

  def getRawFileName(self) -> str: ...

  def loadFBX(self) -> ProcessedAiScene: ...

  def loadTxt(self) -> ModelTxt: ...

  def loadX(self) -> ProcessedAiScene: ...

  def __init__(self, anim: AnimationAsset, fileSystem: FileSystem, cb: IFileTaskCallback): ...


class FileTask_LoadMesh(FileTask_AbstractLoadModel):

  def done(self) -> None: ...

  def getErrorMessage(self) -> str: ...

  def getRawFileName(self) -> str: ...

  def loadFBX(self) -> ProcessedAiScene: ...

  def loadTxt(self) -> ModelTxt: ...

  def loadX(self) -> ProcessedAiScene: ...

  def __init__(self, mesh: ModelMesh, fileSystem: FileSystem, cb: IFileTaskCallback): ...

  class LoadMode(Enum):

    Assimp: FileTask_LoadMesh.LoadMode

    Missing: FileTask_LoadMesh.LoadMode

    Txt: FileTask_LoadMesh.LoadMode

    @staticmethod
    def valueOf(arg0: str) -> FileTask_LoadMesh.LoadMode: ...

    @staticmethod
    def values() -> list[FileTask_LoadMesh.LoadMode]: ...


class HeightTerrain:

  isoAngle: float

  scale: float

  def popView(self) -> None: ...

  def pushView(self, ox: int, oy: int, oz: int) -> None: ...

  def render(self) -> None: ...

  def __init__(self, widthTiles: int, heightTiles: int):
    self.vb: VertexBufferObject


class MeshAssetManager(AssetManager):

  instance: MeshAssetManager

  def addWatchedFile(self, fileName: str) -> None: ...


class Model(Asset):

  ASSET_TYPE: AssetType

  debugDrawColours: list[Color]

  m_staticReusableFloatBuffer: FloatBuffer

  def CreateShader(self, name: str) -> None: ...

  def DrawChar(self, slotData: ModelSlotRenderData, instData: ModelInstanceRenderData) -> None: ...

  def DrawVehicle(self, slotData: ModelSlotRenderData, instData: ModelInstanceRenderData) -> None: ...

  def debugDrawLightSource(self, ls: IsoLightSource, cx: float, cy: float, cz: float, radians: float) -> None: ...

  def getType(self) -> AssetType: ...

  @staticmethod
  @overload
  def BoneToWorldCoords(character: IsoGameCharacter, boneIndex: int, vec: Vector3) -> None: ...

  @staticmethod
  @overload
  def BoneToWorldCoords(slotData: ModelSlotRenderData, boneIndex: int, vec: Vector3) -> None: ...

  @staticmethod
  def BoneYDirectionToWorldCoords(character: IsoGameCharacter, boneIndex: int, vec: Vector3, length: float) -> None: ...

  @staticmethod
  def CharacterModelCameraBegin(slotData: ModelSlotRenderData) -> None: ...

  @staticmethod
  def CharacterModelCameraEnd() -> None: ...

  @staticmethod
  @overload
  def VectorToWorldCoords(character: IsoGameCharacter, vec: Vector3) -> None: ...

  @staticmethod
  @overload
  def VectorToWorldCoords(slotData: ModelSlotRenderData, vec: Vector3) -> None: ...

  @staticmethod
  def debugDrawAxis(x: float, y: float, z: float, length: float, thickness: float) -> None: ...

  @staticmethod
  def drawBoneMtx(boneMtx: Matrix4f) -> None: ...

  def __init__(self, path: AssetPath, manager: AssetManager, params: Model.ModelAssetParams):
    self.assetparams: Model.ModelAssetParams
    self.bstatic: bool
    self.effect: Shader
    self.mesh: ModelMesh
    self.name: str
    self.softwaremesh: SoftwareModelMesh
    self.tag: object
    self.tex: Texture

  class ModelAssetParams(AssetManager.AssetParams):

    def __init__(self):
      self.animationsmodel: ModelMesh
      self.bstatic: bool
      self.meshname: str
      self.shadername: str
      self.textureflags: int
      self.texturename: str


class ModelAssetManager(AssetManager):

  instance: ModelAssetManager

  def __init__(self): ...


class ModelFileExtensionType(Enum):

  Fbx: ModelFileExtensionType

  # None: ModelFileExtensionType

  Txt: ModelFileExtensionType

  X: ModelFileExtensionType

  @staticmethod
  def valueOf(arg0: str) -> ModelFileExtensionType: ...

  @staticmethod
  def values() -> list[ModelFileExtensionType]: ...


class ModelInstance:

  MODEL_LIGHT_MULT_OUTSIDE: float

  MODEL_LIGHT_MULT_ROOM: float

  def LoadTexture(self, name: str) -> None: ...

  def SetForceDir(self, dir: Vector2) -> None: ...

  def Update(self) -> None: ...

  def UpdateDir(self) -> None: ...

  def applyModelScriptScale(self, modelName: str) -> None: ...

  def clearOwner(self, expectedOwner: object) -> None: ...

  def destroySmartTextures(self) -> None: ...

  def dismember(self, bone: int) -> None: ...

  def getAttachment(self, index: int) -> ModelAttachment: ...

  def getAttachmentById(self, id: str) -> ModelAttachment: ...

  @overload
  def getAttachmentMatrix(self, index: int, out: Matrix4f) -> Matrix4f: ...

  @overload
  def getAttachmentMatrix(self, attachment: ModelAttachment, out: Matrix4f) -> Matrix4f: ...

  def getAttachmentMatrixById(self, id: str, out: Matrix4f) -> Matrix4f: ...

  def getItemVisual(self) -> ItemVisual: ...

  def getOwner(self) -> object: ...

  def getTextureInitializer(self) -> ModelInstanceTextureInitializer: ...

  def hasTextureCreator(self) -> bool: ...

  def init(self, model: Model, character: IsoGameCharacter, player: AnimationPlayer) -> ModelInstance: ...

  def isRendering(self) -> bool: ...

  def reset(self) -> None: ...

  def setInstanceSkip(self, c: int) -> None: ...

  def setItemVisual(self, itemVisual: ItemVisual) -> None: ...

  def setOwner(self, owner: object) -> None: ...

  def setTextureInitializer(self, textureInitializer: ModelInstanceTextureInitializer) -> None: ...

  def updateLights(self) -> None: ...

  def __init__(self):
    self.animplayer: AnimationPlayer
    self.attachmentnameparent: str
    self.attachmentnameself: str
    self.bresetafterrender: bool
    self.character: IsoGameCharacter
    self.data: SkinningData
    self.depthbias: float
    self.hue: float
    self.m_lock: object
    self.m_modelscript: ModelScript
    self.m_textureinitializer: ModelInstanceTextureInitializer
    self.maskvariablevalue: str
    self.matrixmodel: ModelInstance
    self.model: Model
    self.object: IsoMovingObject
    self.parent: ModelInstance
    self.parentbone: int
    self.parentbonename: str
    self.playerdata: list[ModelInstance.PlayerData]
    self.renderrefcount: int
    self.scale: float
    self.softwaremesh: SoftwareModelMeshInstance
    self.sub: ArrayList[ModelInstance]
    self.tex: Texture
    self.tintb: float
    self.tintg: float
    self.tintr: float

  class PlayerData:

    def __init__(self): ...

  class FrameLightInfo:

    def __init__(self):
      self.active: bool
      self.b: float
      self.currentcolor: Vector3f
      self.distsq: float
      self.flags: int
      self.foundthisframe: bool
      self.g: float
      self.id: int
      self.r: float
      self.radius: int
      self.stage: ModelInstance.FrameLightBlendStatus
      self.targetcolor: Vector3f
      self.x: int
      self.y: int
      self.z: int

  class FrameLightBlendStatus(Enum):

    During: ModelInstance.FrameLightBlendStatus

    Out: ModelInstance.FrameLightBlendStatus

    @staticmethod
    def valueOf(arg0: str) -> ModelInstance.FrameLightBlendStatus: ...

    @staticmethod
    def values() -> list[ModelInstance.FrameLightBlendStatus]: ...

  class EffectLight:

    def set(self, x: float, y: float, z: float, r: float, g: float, b: float, radius: int) -> None: ...

    def __init__(self):
      self.b: float
      self.g: float
      self.r: float
      self.radius: int
      self.x: float
      self.y: float
      self.z: float


class ModelInstanceDebugRenderData(PooledObject):

  def init(self, slotData: ModelSlotRenderData, instData: ModelInstanceRenderData) -> ModelInstanceDebugRenderData: ...

  def render(self) -> None: ...

  @staticmethod
  def alloc() -> ModelInstanceDebugRenderData: ...

  def __init__(self): ...


class ModelInstanceRenderData:

  def RenderCharacter(self, slotData: ModelSlotRenderData) -> None: ...

  def RenderVehicle(self, slotData: ModelSlotRenderData) -> None: ...

  def init(self, modelInstance: ModelInstance) -> ModelInstanceRenderData: ...

  def renderDebug(self) -> None: ...

  def transformToParent(self, parentData: ModelInstanceRenderData) -> ModelInstanceRenderData: ...

  @staticmethod
  def alloc() -> ModelInstanceRenderData: ...

  @staticmethod
  def applyBoneTransform(parentInstance: ModelInstance, boneName: str, transform: Matrix4f) -> None: ...

  @staticmethod
  def makeAttachmentTransform(attachment: ModelAttachment, attachmentXfrm: Matrix4f) -> Matrix4f: ...

  @staticmethod
  def release(objs: ArrayList[ModelInstanceRenderData]) -> None: ...

  def __init__(self):
    self.depthbias: float
    self.hue: float
    self.m_muzzleflash: bool
    self.matrixpalette: FloatBuffer
    self.model: Model
    self.modelinstance: ModelInstance
    self.parentbone: int
    self.softwaremesh: SoftwareModelMeshInstance
    self.tex: Texture
    self.tintb: float
    self.tintg: float
    self.tintr: float
    self.xfrm: Matrix4f


class ModelInstanceRenderDataList(ArrayList):

  def __init__(self): ...


class ModelInstanceTextureCreator(TextureDraw.GenericDrawer):

  @overload
  def init(self, chr: IsoGameCharacter) -> None: ...

  @overload
  def init(self, baseVisual: BaseVisual, itemVisuals: ItemVisuals, chrModelInstance: ModelInstance) -> None: ...

  @overload
  def init(self, humanVisual: HumanVisual, itemVisuals: ItemVisuals, chrModelInstance: ModelInstance) -> None: ...

  def isRendered(self) -> bool: ...

  def postRender(self) -> None: ...

  def render(self) -> None: ...

  @staticmethod
  def alloc() -> ModelInstanceTextureCreator: ...

  def __init__(self):
    self.renderrefcount: int
    self.testnotready: int

  class CharacterData: ...

  class ItemData: ...


class ModelInstanceTextureInitializer:

  @overload
  def init(self, modelInstance: ModelInstance, bloodLevel: float) -> None: ...

  @overload
  def init(self, modelInstance: ModelInstance, item: InventoryItem) -> None: ...

  def isDirty(self) -> bool: ...

  def isRendered(self) -> bool: ...

  def postRender(self) -> None: ...

  def release(self) -> None: ...

  def render(self) -> None: ...

  def renderMain(self) -> None: ...

  def setDirty(self) -> None: ...

  @staticmethod
  def alloc() -> ModelInstanceTextureInitializer: ...

  def __init__(self): ...

  class RenderData: ...


class ModelLoader:

  instance: ModelLoader

  def __init__(self): ...

  class LoadMode(Enum):

    Anim: ModelLoader.LoadMode

    BindPose: ModelLoader.LoadMode

    FaceData: ModelLoader.LoadMode

    InvBindPose: ModelLoader.LoadMode

    ModelName: ModelLoader.LoadMode

    NumberOfAnims: ModelLoader.LoadMode

    NumberOfBones: ModelLoader.LoadMode

    NumberOfFaces: ModelLoader.LoadMode

    SkeletonHierarchy: ModelLoader.LoadMode

    SkinOffsetMatrices: ModelLoader.LoadMode

    Version: ModelLoader.LoadMode

    VertexBuffer: ModelLoader.LoadMode

    VertexCount: ModelLoader.LoadMode

    VertexStrideData: ModelLoader.LoadMode

    VertexStrideElementCount: ModelLoader.LoadMode

    VertexStrideSize: ModelLoader.LoadMode

    @staticmethod
    def valueOf(arg0: str) -> ModelLoader.LoadMode: ...

    @staticmethod
    def values() -> list[ModelLoader.LoadMode]: ...


class ModelMesh(Asset):

  ASSET_TYPE: AssetType

  def Draw(self, shader: Shader) -> None: ...

  def SetVertexBuffer(self, vb: VertexBufferObject) -> None: ...

  def clear(self) -> None: ...

  def getType(self) -> AssetType: ...

  def isReady(self) -> bool: ...

  def onBeforeReady(self) -> None: ...

  def setAssetParams(self, params: AssetManager.AssetParams) -> None: ...

  def __init__(self, path: AssetPath, manager: AssetManager, params: ModelMesh.MeshAssetParams):
    self.assetparams: ModelMesh.MeshAssetParams
    self.m_animationsmesh: ModelMesh
    self.m_bhasvbo: bool
    self.m_fullpath: str
    self.m_transform: Matrix4f
    self.maxxyz: Vector3f
    self.minxyz: Vector3f
    self.skinningdata: SkinningData
    self.softwaremesh: SoftwareModelMesh
    self.vb: VertexBufferObject

  class MeshAssetParams(AssetManager.AssetParams):

    def __init__(self):
      self.animationsmesh: ModelMesh
      self.bstatic: bool


class ModelOutlines:

  instance: ModelOutlines

  def beginRenderOutline(self, outlineColor: ColorInfo) -> bool: ...

  def checkFBOs(self) -> None: ...

  def endFrame(self, playerIndex: int) -> None: ...

  def endFrameMain(self, playerIndex: int) -> None: ...

  def renderDebug(self) -> None: ...

  def setPlayerRenderData(self, slotData: ModelSlotRenderData) -> None: ...

  def startFrame(self, playerIndex: int) -> None: ...

  def startFrameMain(self, playerIndex: int) -> None: ...

  def __init__(self):
    self.m_dirty: bool
    self.m_fboa: TextureFBO
    self.m_fbob: TextureFBO
    self.m_fboc: TextureFBO

  class Drawer(TextureDraw.GenericDrawer):

    def postRender(self) -> None: ...

    def render(self) -> None: ...

    def __init__(self): ...


class ModelSlotDebugRenderData(PooledObject):

  def init(self, slotData: ModelSlotRenderData) -> ModelSlotDebugRenderData: ...

  def render(self) -> None: ...

  @staticmethod
  def alloc() -> ModelSlotDebugRenderData: ...

  def __init__(self): ...


class ModelSlotRenderData(TextureDraw.GenericDrawer):

  def init(self, modelSlot: ModelManager.ModelSlot) -> ModelSlotRenderData: ...

  def postRender(self) -> None: ...

  def render(self) -> None: ...

  def renderDebug(self) -> None: ...

  @staticmethod
  def alloc() -> ModelSlotRenderData: ...

  def __init__(self):
    self.alpha: float
    self.ambientb: float
    self.ambientg: float
    self.ambientr: float
    self.animplayer: AnimationPlayer
    self.animplayerangle: float
    self.binvehicle: bool
    self.boutside: bool
    self.centerofmassy: float
    self.character: IsoGameCharacter
    self.effectlights: list[ModelInstance.EffectLight]
    self.invehiclex: float
    self.invehicley: float
    self.invehiclez: float
    self.modeldata: ModelInstanceRenderDataList
    self.object: IsoMovingObject
    self.render_to_texture: bool
    self.texturecreator: ModelInstanceTextureCreator
    self.vehicleanglex: float
    self.vehicleangley: float
    self.vehicleanglez: float
    self.vehicletransform: Matrix4f
    self.x: float
    self.y: float
    self.z: float


class ModelTxt:

  def __init__(self): ...


class SkinningBone:

  def forEachDescendant(self, consumer: Consumer[SkinningBone]) -> None: ...

  def toString(self) -> str: ...

  def __init__(self):
    self.children: list[SkinningBone]
    self.index: int
    self.name: str
    self.parent: SkinningBone


class SkinningBoneHierarchy:

  def buildBoneHiearchy(self, data: SkinningData) -> None: ...

  def getBoneAt(self, boneIdx: int) -> SkinningBone: ...

  def getRootBoneAt(self, idx: int) -> SkinningBone: ...

  def isValid(self) -> bool: ...

  def numRootBones(self) -> int: ...

  def __init__(self): ...


class SkinningData:

  def getBone(self, boneName: str) -> SkinningBone: ...

  def getBoneAt(self, boneIdx: int) -> SkinningBone: ...

  def getBoneHieararchy(self) -> SkinningBoneHierarchy: ...

  def getParentBoneIdx(self, boneIdx: int) -> int: ...

  def getRootBoneAt(self, idx: int) -> SkinningBone: ...

  def numBones(self) -> int: ...

  def numRootBones(self) -> int: ...

  def __init__(self, animationClips: HashMap[str, AnimationClip], bindPose: List[Matrix4f], inverseBindPose: List[Matrix4f], skinOffset: List[Matrix4f], skeletonHierarchy: List[Integer], boneIndices: HashMap[str, Integer]):
    self.animationclips: HashMap[str, AnimationClip]
    self.bindpose: List[Matrix4f]
    self.boneindices: HashMap[str, Integer]
    self.boneoffset: List[Matrix4f]
    self.inversebindpose: List[Matrix4f]
    self.skeletonhierarchy: List[Integer]


class SoftwareModelMesh:

  @overload
  def __init__(self, verticesUnskinned: list[VertexPositionNormalTangentTexture], elements: list[int]):
    self.indicesunskinned: list[int]

    self.texture: str

    self.vb: VertexBufferObject

    self.verticesunskinned: list[VertexPositionNormalTangentTextureSkin]

  @overload
  def __init__(self, verticesUnskinned: list[VertexPositionNormalTangentTextureSkin], elements: list[int]): ...


class SoftwareModelMeshInstance:

  def __init__(self, name: str, softwareMesh: SoftwareModelMesh):
    self.name: str
    self.softwaremesh: SoftwareModelMesh
    self.vb: VertexBufferObject


class UInt4:

  def __init__(self, x: int, y: int, z: int, w: int):
    self.w: int
    self.x: int
    self.y: int
    self.z: int


class Vbo:

  def __init__(self):
    self.b: IntBuffer
    self.eboid: int
    self.facedataonly: bool
    self.numelements: int
    self.vboid: int
    self.vertexstride: int


class VehicleModelInstance(ModelInstance):

  def UpdateLights(self) -> None: ...

  def getLights(self) -> list[IsoLightSource]: ...

  def reset(self) -> None: ...

  def setLights(self, lights: list[IsoLightSource]) -> None: ...

  def __init__(self):
    self.m_lightslock: object
    self.matrixblood1enables1: list[float]
    self.matrixblood1enables2: list[float]
    self.matrixblood2enables1: list[float]
    self.matrixblood2enables2: list[float]
    self.paincolor: Vector3f
    self.refbody: float
    self.refwindows: float
    self.texturedamage1enables1: list[float]
    self.texturedamage1enables2: list[float]
    self.texturedamage1overlay: Texture
    self.texturedamage1shell: Texture
    self.texturedamage2enables1: list[float]
    self.texturedamage2enables2: list[float]
    self.texturedamage2overlay: Texture
    self.texturedamage2shell: Texture
    self.texturelights: Texture
    self.texturelightsenables1: list[float]
    self.texturelightsenables2: list[float]
    self.texturemask: Texture
    self.texturerust: Texture
    self.texturerusta: float
    self.textureuninstall1: list[float]
    self.textureuninstall2: list[float]


class VehicleSubModelInstance(ModelInstance):

  def __init__(self):
    self.degrees: int
    self.modelinfo: BaseVehicle.ModelInfo


class VertexBufferObject:

  funcs: IGLBufferObject

  def Draw(self, shader: Shader) -> None: ...

  def DrawStrip(self, shader: Shader) -> None: ...

  def LoadSoftwareVBO(self, vertices: ByteBuffer, vbo: VertexBufferObject.Vbo, elements: list[int]) -> VertexBufferObject.Vbo: ...

  def clear(self) -> None: ...

  @overload
  def __init__(self):
    self.bstatic: bool

  @overload
  def __init__(self, vertices: list[VertexPositionNormalTangentTexture], elements: list[int]): ...
  @overload
  def __init__(self, vertices: VertexBufferObject.VertexArray, elements: list[int]): ...
  @overload
  def __init__(self, vertices: list[VertexPositionNormalTangentTextureSkin], elements: list[int], bReverse: bool): ...
  @overload
  def __init__(self, vertices: VertexBufferObject.VertexArray, elements: list[int], bReverse: bool): ...

  class VertexFormat:

    def calculate(self) -> None: ...

    def setElement(self, index: int, type: VertexBufferObject.VertexType, byteSize: int) -> None: ...

    def __init__(self, numElements: int): ...

  class VertexType(Enum):

    BlendIndexArray: VertexBufferObject.VertexType

    BlendWeightArray: VertexBufferObject.VertexType

    ColorArray: VertexBufferObject.VertexType

    IndexArray: VertexBufferObject.VertexType

    NormalArray: VertexBufferObject.VertexType

    TangentArray: VertexBufferObject.VertexType

    TextureCoordArray: VertexBufferObject.VertexType

    VertexArray: VertexBufferObject.VertexType

    @staticmethod
    def valueOf(arg0: str) -> VertexBufferObject.VertexType: ...

    @staticmethod
    def values() -> list[VertexBufferObject.VertexType]: ...

  class BeginMode(Enum):

    Triangles: VertexBufferObject.BeginMode

    @staticmethod
    def valueOf(arg0: str) -> VertexBufferObject.BeginMode: ...

    @staticmethod
    def values() -> list[VertexBufferObject.BeginMode]: ...

  class Vbo:

    def __init__(self):
      self.b: IntBuffer
      self.eboid: int
      self.facedataonly: bool
      self.numelements: int
      self.vboid: int
      self.vertexstride: int

  class VertexArray:

    @overload
    def setElement(self, vertex: int, element: int, v1: float, v2: float) -> None: ...

    @overload
    def setElement(self, vertex: int, element: int, v1: float, v2: float, v3: float) -> None: ...

    @overload
    def setElement(self, vertex: int, element: int, v1: float, v2: float, v3: float, v4: float) -> None: ...

    def __init__(self, format: VertexBufferObject.VertexFormat, numVertices: int):
      self.m_buffer: ByteBuffer
      self.m_format: VertexBufferObject.VertexFormat
      self.m_numvertices: int

  class VertexElement:

    def __init__(self):
      self.m_byteoffset: int
      self.m_bytesize: int
      self.m_type: VertexBufferObject.VertexType


class VertexDefinitions:

  def __init__(self): ...

  class VertexPositionNormalTangentTexture:

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: Vector3, arg2: Vector3, arg3: Vector3, arg4: Vector2):
      self.normal: Vector3

      self.position: Vector3

      self.tangent: Vector3

      self.texturecoordinates: Vector2

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float): ...

  class VertexPositionNormalTexture:

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: Vector3, arg2: Vector3, arg3: Vector2):
      self.normal: Vector3

      self.position: Vector3

      self.texturecoordinates: Vector2

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float): ...

  class VertexPositionNormal:

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: Vector3, arg2: Vector3, arg3: Vector2):
      self.normal: Vector3

      self.position: Vector3

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float): ...

  class VertexPositionColour:

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: Vector3, arg2: Color):
      self.colour: int

      self.position: Vector3

    @overload
    def __init__(self, arg0: VertexDefinitions, arg1: float, arg2: float, arg3: float, arg4: Color): ...


class VertexPositionNormalTangentTexture:

  def put(self, buf: ByteBuffer) -> None: ...

  @overload
  def __init__(self):
    self.normal: Vector3

    self.position: Vector3

    self.tangent: Vector3

    self.texturecoordinates: Vector2

  @overload
  def __init__(self, position: Vector3, normal: Vector3, tangent: Vector3, uv: Vector2): ...


class VertexPositionNormalTangentTextureSkin:

  def put(self, buf: ByteBuffer) -> None: ...

  @overload
  def __init__(self):
    self.blendindices: UInt4

    self.blendweights: Vector4

    self.normal: Vector3

    self.position: Vector3

    self.tangent: Vector3

    self.texturecoordinates: Vector2

  @overload
  def __init__(self, position: Vector3, normal: Vector3, tangent: Vector3, uv: Vector2, blendweights: Vector4, blendIndices: UInt4): ...


class VertexPositionNormalTextureColor:

  def put(self, buf: ByteBuffer) -> None: ...

  def __init__(self):
    self.color: Color
    self.normal: Vector3
    self.position: Vector3
    self.texturecoordinates: Vector2


class VertexStride:

  def __init__(self):
    self.offset: int
    self.type: VertexBufferObject.VertexType


class WorldItemAtlas:

  ATLAS_SIZE: int

  instance: WorldItemAtlas

  MATRIX_SIZE: int

  def Reset(self) -> None: ...

  @overload
  def getItemTexture(self, params: WorldItemAtlas.ItemParams) -> WorldItemAtlas.ItemTexture: ...

  @overload
  def getItemTexture(self, item: InventoryItem) -> WorldItemAtlas.ItemTexture: ...

  def render(self) -> None: ...

  def renderUI(self) -> None: ...

  def __init__(self): ...

  class ItemParams:

    class FoodState(Enum):

      Burnt: WorldItemAtlas.ItemParams.FoodState

      Cooked: WorldItemAtlas.ItemParams.FoodState

      Normal: WorldItemAtlas.ItemParams.FoodState

      Rotten: WorldItemAtlas.ItemParams.FoodState

      @staticmethod
      def valueOf(arg0: str) -> WorldItemAtlas.ItemParams.FoodState: ...

      @staticmethod
      def values() -> list[WorldItemAtlas.ItemParams.FoodState]: ...

  class Checksummer:

    def checksumToString(self) -> str: ...

    def reset(self) -> None: ...

    @overload
    def update(self, arg0: bool) -> None: ...

    @overload
    def update(self, arg0: int) -> None: ...

    @overload
    def update(self, arg0: int) -> None: ...

    @overload
    def update(self, arg0: str) -> None: ...

    @overload
    def update(self, arg0: ImmutableColor) -> None: ...

    @overload
    def update(self, arg0: IsoGridSquare.ResultLight, arg1: float, arg2: float, arg3: float) -> None: ...

  class ItemTexture:

    def isRenderMainOK(self) -> bool: ...

    def isStillValid(self, item: InventoryItem) -> bool: ...

    def isTooBig(self) -> bool: ...

    def render(self, x: float, y: float, r: float, g: float, b: float, a: float) -> None: ...

    def __init__(self): ...

  class AtlasEntry:

    def Reset(self) -> None: ...

  class RenderJob(TextureDraw.GenericDrawer):

    def Reset(self) -> None: ...

    def init(self, arg0: WorldItemAtlas.ItemParams, arg1: WorldItemAtlas.AtlasEntry) -> WorldItemAtlas.RenderJob: ...

    def postRender(self) -> None: ...

    def render(self) -> None: ...

    def renderMain(self) -> bool: ...

    @staticmethod
    def getNew() -> WorldItemAtlas.RenderJob: ...

  class Atlas:

    def Reset(self) -> None: ...

    def addEntry(self, arg0: WorldItemAtlas.AtlasEntry) -> None: ...

    def addItem(self, arg0: str) -> WorldItemAtlas.AtlasEntry: ...

    def isFull(self) -> bool: ...

    def __init__(self, arg0: WorldItemAtlas, arg1: int, arg2: int, arg3: int, arg4: int):
      self.clear: bool
      self.entry_hgt: int
      self.entry_wid: int
      self.entrylist: ArrayList[WorldItemAtlas.AtlasEntry]
      self.tex: Texture

  class WeaponPartParams: ...

  class ClearAtlasTexture(TextureDraw.GenericDrawer):

    def render(self) -> None: ...

  class ItemTextureDrawer(TextureDraw.GenericDrawer):

    def postRender(self) -> None: ...

    def render(self) -> None: ...


class WorldItemModelDrawer(TextureDraw.GenericDrawer):

  NEW_WAY: bool

  def postRender(self) -> None: ...

  def render(self) -> None: ...

  @staticmethod
  @overload
  def renderMain(item: InventoryItem, square: IsoGridSquare, x: float, y: float, z: float, flipAngle: float) -> bool: ...

  @staticmethod
  @overload
  def renderMain(item: InventoryItem, square: IsoGridSquare, x: float, y: float, z: float, flipAngle: float, forcedRotation: float) -> bool: ...

  def __init__(self): ...

  class WeaponPartParams: ...

