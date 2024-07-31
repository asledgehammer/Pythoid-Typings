from typing import Any, overload
from java.io import DataInputStream, DataOutputStream, File, BufferedReader
from java.lang import Class, Double, Integer, Boolean, Short
from java.lang.reflect import Field, Method
from java.util import ArrayList, HashMap, List, Stack
from java.util.function import Predicate
from se.krka.kahlua.vm import KahluaTable, LuaClosure, LuaCallFrame, Coroutine
from zombie import BaseAmbientStreamManager, GameTime, SandboxOptions, BaseSoundManager, WorldSoundManager
from zombie.Lua import LuaManager
from zombie.ai.sadisticAIDirector import SleepingEvent
from zombie.audio import BaseSoundBank
from zombie.characters import IsoPlayer, IsoGameCharacter, IsoZombie, Faction, SurvivorDesc
from zombie.characters.BodyDamage import BodyPart
from zombie.characters.skills import PerkFactory
from zombie.core import Core, PerformanceSettings, Language, SpriteRenderer
from zombie.core.raknet import UdpConnection
from zombie.core.skinnedmodel.model import Model
from zombie.core.skinnedmodel.population import BeardStyles, HairStyles
from zombie.core.textures import Texture
from zombie.core.znet import SteamWorkshopItem
from zombie.debug import DebugOptions
from zombie.erosion import ErosionMain
from zombie.gameStates import GameState, AnimationViewerState, AttachmentEditorState, ChooseGameInfo
from zombie.inventory import InventoryItem, ItemContainer
from zombie.iso import IsoGridSquare, IsoObject, BuildingDef, RoomDef, ContainerOverlays, TileOverlays, IsoDirections, IsoCell, IsoMarkers, IsoPuddles, SearchMode, IsoMetaGrid, IsoWorld, WorldMarkers
from zombie.iso.areas import SafeHouse
from zombie.iso.areas.isoregion import IsoRegionsRenderer
from zombie.iso.objects import IsoDeadBody
from zombie.iso.sprite import IsoSprite, IsoSpriteManager
from zombie.iso.weather import ClimateManager, ClimateMoon
from zombie.network import GameClient, ServerOptions, ServerSettingsManager, Server
from zombie.popman import ZombiePopulationRenderer
from zombie.radio import RadioAPI, ZomboidRadio
from zombie.radio.StorySounds import SLSoundManager
from zombie.scripting import ScriptManager
from zombie.scripting.objects import VehicleScript, Item, Recipe, EvolvedRecipe
from zombie.ui import UIElement, TextManager
from zombie.vehicles import BaseVehicle, EditVehicleState

class Pythoid:

    @staticmethod
    def expose(clazz: Any) -> None: ...

    @staticmethod
    def invoke(instance: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def invokeStatic(clazz: Class, methodName: str, *args) -> Any: ...

    @staticmethod
    def getField(instance: object, fieldName: str) -> Any: ...

    @staticmethod
    def getStaticField(clazz: Class, fieldName: str) -> Any: ... 


# @LuaMethod
def Render3DItem(self, item: InventoryItem, sq: IsoGridSquare, xoffset: float, yoffset: float, zoffset: float, rotation: float) -> None: ...

# @LuaMethod
def SyncXp(self, player: IsoPlayer) -> None: ...

# @LuaMethod
def addBloodSplat(self, sq: IsoGridSquare, nbr: int) -> None: ...

# @LuaMethod
def addSound(self, source: IsoObject, x: int, y: int, z: int, radius: int, volume: int) -> None: ...

# @LuaMethod
def addZombieSitting(self, x: int, y: int, z: int) -> None: ...

# @LuaMethod
def addZombiesEating(self, x: int, y: int, z: int, totalZombies: int, skeletonBody: bool) -> None: ...

# @LuaMethod
def addZombiesInBuilding(self, arg0: BuildingDef, totalZombies: int, outfit: str, room: RoomDef, femaleChance: Integer) -> ArrayList[IsoZombie]: ...

# @LuaMethod
def addZombiesInOutfitArea(self, x1: int, y1: int, x2: int, y2: int, z: int, totalZombies: int, outfit: str, femaleChance: Integer) -> ArrayList[IsoZombie]: ...

# @LuaMethod
def checkServerName(self, name: str) -> str: ...

# @LuaMethod
def getAverageFPS(self) -> Double: ...

# @LuaMethod
def getContainerOverlays(self) -> ContainerOverlays: ...

# @LuaMethod
def getTileOverlays(self) -> TileOverlays: ...

# @LuaMethod
def screenZoomIn(self) -> None: ...

# @LuaMethod
def screenZoomOut(self) -> None: ...

# @LuaMethod
def sendAddXp(self, player: IsoPlayer, perk: PerkFactory.Perk, amount: int) -> None: ...

# @LuaMethod
@staticmethod
def AddNoiseToken(sq: IsoGridSquare, radius: int) -> None: ...

# @LuaMethod
@staticmethod
def AddWorldSound(player: IsoPlayer, radius: int, volume: int) -> None: ...

# @LuaMethod
@staticmethod
def InvMngGetItem(itemId: int, itemType: str, player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def InvMngRemoveItem(itemId: int, player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def SendCommandToServer(command: str) -> None: ...

# @LuaMethod
@staticmethod
@overload
def ZombRand(max: float) -> float: ...

# @LuaMethod
@staticmethod
@overload
def ZombRand(min: float, max: float) -> float: ...

# @LuaMethod
@staticmethod
def ZombRandBetween(min: float, max: float) -> float: ...

# @LuaMethod
@staticmethod
def ZombRandFloat(min: float, max: float) -> float: ...

# @LuaMethod
@staticmethod
def acceptFactionInvite(faction: Faction, host: str) -> None: ...

# @LuaMethod
@staticmethod
def acceptSafehouseInvite(safehouse: SafeHouse, host: str) -> None: ...

# @LuaMethod
@staticmethod
def acceptTrading(you: IsoPlayer, other: IsoPlayer, accept: bool) -> None: ...

# @LuaMethod
@staticmethod
def activateJoypadOnSteamDeck() -> None: ...

# @LuaMethod
@staticmethod
def activateSteamOverlayToWebPage(url: str) -> None: ...

# @LuaMethod
@staticmethod
def activateSteamOverlayToWorkshop() -> None: ...

# @LuaMethod
@staticmethod
def activateSteamOverlayToWorkshopItem(itemID: str) -> None: ...

# @LuaMethod
@staticmethod
def activateSteamOverlayToWorkshopUser() -> None: ...

# @LuaMethod
@staticmethod
def addAllBurntVehicles() -> None: ...

# @LuaMethod
@staticmethod
def addAllSmashedVehicles() -> None: ...

# @LuaMethod
@staticmethod
@overload
def addAllVehicles() -> None: ...

@staticmethod
@overload
def addAllVehicles(predicate: Predicate[VehicleScript]) -> None: ...

# @LuaMethod
@staticmethod
def addCarCrash() -> None: ...

# @LuaMethod
@staticmethod
def addPhysicsObject() -> BaseVehicle: ...

# @LuaMethod
@staticmethod
def addTicket(author: str, message: str, ticketID: int) -> None: ...

# @LuaMethod
@staticmethod
def addUserlog(user: str, type: str, text: str) -> None: ...

# @LuaMethod
@staticmethod
def addVehicle(script: str) -> BaseVehicle: ...

# @LuaMethod
@staticmethod
def addVehicleDebug(scriptName: str, dir: IsoDirections, skinIndex: Integer, sq: IsoGridSquare) -> BaseVehicle: ...

# @LuaMethod
@staticmethod
def addVirtualZombie(x: int, y: int) -> None: ...

# @LuaMethod
@staticmethod
def addWarningPoint(user: str, reason: str, amount: int) -> None: ...

# @LuaMethod
@staticmethod
@overload
def addZombiesInOutfit(x: int, y: int, z: int, totalZombies: int, outfit: str, femaleChance: Integer) -> ArrayList[IsoZombie]: ...

# @LuaMethod
@staticmethod
@overload
def addZombiesInOutfit(x: int, y: int, z: int, totalZombies: int, outfit: str, femaleChance: Integer, isCrawler: bool, isFallOnFront: bool, isFakeDead: bool, isKnockedDown: bool, health: float) -> ArrayList[IsoZombie]: ...

# @LuaMethod
@staticmethod
def assaultPlayer() -> None: ...

# @LuaMethod
@staticmethod
def attachTrailerToPlayerVehicle(playerIndex: int) -> None: ...

# @LuaMethod
@staticmethod
def backToSinglePlayer() -> None: ...

# @LuaMethod
@staticmethod
def breakpoint() -> None: ...

# @LuaMethod
@staticmethod
def canConnect() -> bool: ...

# @LuaMethod
@staticmethod
def canInviteFriends() -> bool: ...

# @LuaMethod
@staticmethod
def canModifyPlayerScoreboard() -> bool: ...

# @LuaMethod
@staticmethod
def canModifyPlayerStats() -> bool: ...

# @LuaMethod
@staticmethod
def canSeePlayerStats() -> bool: ...

# @LuaMethod
@staticmethod
def checkModsNeedUpdate(arg0: UdpConnection) -> None: ...

# @LuaMethod
@staticmethod
def checkPlayerCanUseChat(chatCommand: str) -> Boolean: ...

# @LuaMethod
@staticmethod
def checkSaveFileExists(f: str) -> bool: ...

# @LuaMethod
@staticmethod
def checkSaveFolderExists(f: str) -> bool: ...

# @LuaMethod
@staticmethod
def checkSavePlayerExists() -> bool: ...

# @LuaMethod
@staticmethod
def checkStringPattern(pattern: str) -> bool: ...

# @LuaMethod
@staticmethod
def cloneItemType(newName: str, oldName: str) -> Item: ...

# @LuaMethod
@staticmethod
def configureLighting(darkStep: float) -> None: ...

# @LuaMethod
@staticmethod
def connectToServerStateCallback(button: str) -> None: ...

# @LuaMethod
@staticmethod
def connectionManagerLog(arg0: str, arg1: str) -> None: ...

# @LuaMethod
@staticmethod
@overload
def copyTable(table: KahluaTable) -> KahluaTable: ...

# @LuaMethod
@staticmethod
@overload
def copyTable(to: KahluaTable, arg1: KahluaTable) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def createHordeFromTo(spawnX: float, spawnY: float, targetX: float, targetY: float, count: int) -> None: ...

# @LuaMethod
@staticmethod
def createHordeInAreaTo(spawnX: int, spawnY: int, spawnW: int, spawnH: int, targetX: int, targetY: int, count: int) -> None: ...

# @LuaMethod
@staticmethod
def createItemTransaction(item: InventoryItem, src: ItemContainer, dst: ItemContainer) -> None: ...

# @LuaMethod
@staticmethod
def createNewScriptItem(base: str, name: str, display: str, type: str, icon: str) -> Item: ...

# @LuaMethod
@staticmethod
def createRandomDeadBody(square: IsoGridSquare, blood: int) -> IsoDeadBody: ...

# @LuaMethod
@staticmethod
def createRegionFile() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def createStory(storyName: str) -> None: ...

# @LuaMethod
@staticmethod
def createTile(tile: str, square: IsoGridSquare) -> None: ...

# @LuaMethod
@staticmethod
def createWorld(worldName: str) -> None: ...

# @LuaMethod
@staticmethod
def createZombie(x: float, y: float, z: float, desc: SurvivorDesc, palette: int, dir: IsoDirections) -> IsoZombie: ...

# @LuaMethod
@staticmethod
def debugFullyStreamedIn(x: int, y: int) -> None: ...

# @LuaMethod
@staticmethod
@overload
def debugLuaTable(param: object) -> None: ...

# @LuaMethod
@staticmethod
@overload
def debugLuaTable(param: object, depth: int) -> None: ...

# @LuaMethod
@staticmethod
def debugSetRoomType(roomType: Double) -> None: ...

# @LuaMethod
@staticmethod
def deleteAllGameModeSaves(gameMode: str) -> None: ...

# @LuaMethod
@staticmethod
def deletePlayerSave(fileName: str) -> None: ...

# @LuaMethod
@staticmethod
def deleteSandboxPreset(name: str) -> None: ...

# @LuaMethod
@staticmethod
def deleteSave(file: str) -> None: ...

# @LuaMethod
@staticmethod
def disconnect() -> None: ...

# @LuaMethod
@staticmethod
def doChallenge(challenge: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
def doKeyPress(doIt: bool) -> None: ...

# @LuaMethod
@staticmethod
def doLuaDebuggerAction(action: str) -> None: ...

# @LuaMethod
@staticmethod
def doTutorial(tutorial: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
def drawOverheadMap(ui: UIElement, zoom: float, xpos: float, ypos: float) -> None: ...

# @LuaMethod
@staticmethod
def endFileInput() -> None: ...

# @LuaMethod
@staticmethod
def endFileOutput() -> None: ...

# @LuaMethod
@staticmethod
def endHelicopter() -> None: ...

# @LuaMethod
@staticmethod
def endTextFileInput() -> None: ...

# @LuaMethod
@staticmethod
def executeQuery(query: str, params: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
def fileExists(filename: str) -> bool: ...

# @LuaMethod
@staticmethod
def focusOnTab(id: Short) -> None: ...

# @LuaMethod
@staticmethod
def forceChangeState(state: GameState) -> None: ...

# @LuaMethod
@staticmethod
def forceDisconnect() -> None: ...

# @LuaMethod
@staticmethod
def forceSnowCheck() -> None: ...

# @LuaMethod
@staticmethod
def getAbsoluteSaveFolderName(f: str) -> str: ...

# @LuaMethod
@staticmethod
def getAccessLevel() -> str: ...

# @LuaMethod
@staticmethod
def getActivatedMods() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAllBeardStyles() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAllDecalNamesForItem(item: InventoryItem) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAllHairStyles(female: bool) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAllItems() -> ArrayList[Item]: ...

# @LuaMethod
@staticmethod
def getAllItemsForBodyLocation(bodyLocation: str) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getAllOutfits(female: bool) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAllRecipes() -> ArrayList[Recipe]: ...

# @LuaMethod
@staticmethod
def getAllSavedPlayers() -> List[BufferedReader]: ...

# @LuaMethod
@staticmethod
def getAllVehicles() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getAmbientStreamManager() -> BaseAmbientStreamManager: ...

# @LuaMethod
@staticmethod
def getAnimationViewerState() -> AnimationViewerState: ...

# @LuaMethod
@staticmethod
def getAttachmentEditorState() -> AttachmentEditorState: ...

# @LuaMethod
@staticmethod
def getBeardStylesInstance() -> BeardStyles: ...

# @LuaMethod
@staticmethod
def getBehaviourDebugPlayer() -> IsoGameCharacter: ...

# @LuaMethod
@staticmethod
def getButtonCount(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getCallframeTop(c: Coroutine) -> int: ...

# @LuaMethod
@staticmethod
def getCameraOffX() -> float: ...

# @LuaMethod
@staticmethod
def getCameraOffY() -> float: ...

# @LuaMethod
@staticmethod
def getCell() -> IsoCell: ...

# @LuaMethod
@staticmethod
def getClassField(o: object, i: int) -> Field: ...

# @LuaMethod
@staticmethod
def getClassFieldVal(o: object, field: Field) -> object: ...

# @LuaMethod
@staticmethod
def getClassFunction(o: object, i: int) -> Method: ...

# @LuaMethod
@staticmethod
def getClientUsername() -> str: ...

# @LuaMethod
@staticmethod
def getClimateManager() -> ClimateManager: ...

# @LuaMethod
@staticmethod
def getClimateMoon() -> ClimateMoon: ...

# @LuaMethod
@staticmethod
def getConnectedPlayers() -> ArrayList[IsoPlayer]: ...

# @LuaMethod
@staticmethod
def getControllerAxisCount(c: int) -> int: ...

# @LuaMethod
@staticmethod
def getControllerAxisValue(c: int, axis: int) -> float: ...

# @LuaMethod
@staticmethod
def getControllerButtonCount(c: int) -> int: ...

# @LuaMethod
@staticmethod
def getControllerCount() -> int: ...

# @LuaMethod
@staticmethod
def getControllerDeadZone(c: int, axis: int) -> float: ...

# @LuaMethod
@staticmethod
def getControllerGUID(joypad: int) -> str: ...

# @LuaMethod
@staticmethod
def getControllerName(joypad: int) -> str: ...

# @LuaMethod
@staticmethod
def getControllerPovX(c: int) -> float: ...

# @LuaMethod
@staticmethod
def getControllerPovY(c: int) -> float: ...

# @LuaMethod
@staticmethod
def getCore() -> Core: ...

# @LuaMethod
@staticmethod
def getCoroutineCallframeStack(c: Coroutine, n: int) -> LuaCallFrame: ...

# @LuaMethod
@staticmethod
def getCoroutineObjStack(c: Coroutine, n: int) -> object: ...

# @LuaMethod
@staticmethod
def getCoroutineObjStackWithBase(c: Coroutine, n: int) -> object: ...

# @LuaMethod
@staticmethod
def getCoroutineTop(c: Coroutine) -> int: ...

# @LuaMethod
@staticmethod
def getCurrentCoroutine() -> Coroutine: ...

# @LuaMethod
@staticmethod
def getCurrentUserProfileName() -> str: ...

# @LuaMethod
@staticmethod
def getCurrentUserSteamID() -> str: ...

# @LuaMethod
@staticmethod
def getDBSchema() -> None: ...

# @LuaMethod
@staticmethod
def getDebug() -> bool: ...

# @LuaMethod
@staticmethod
def getDebugOptions() -> DebugOptions: ...

# @LuaMethod
@staticmethod
def getDirectionTo(chara: IsoGameCharacter, objTarget: IsoObject) -> IsoDirections: ...

# @LuaMethod
@staticmethod
def getEditVehicleState() -> EditVehicleState: ...

# @LuaMethod
@staticmethod
def getErosion() -> ErosionMain: ...

# @LuaMethod
@staticmethod
def getEvolvedRecipes() -> Stack[EvolvedRecipe]: ...

# @LuaMethod
@staticmethod
def getFMODSoundBank() -> BaseSoundBank: ...

# @LuaMethod
@staticmethod
def getFileInput(filename: str) -> DataInputStream: ...

# @LuaMethod
@staticmethod
def getFileOutput(filename: str) -> DataOutputStream: ...

# @LuaMethod
@staticmethod
def getFileReader(filename: str, createIfNull: bool) -> BufferedReader: ...

# @LuaMethod
@staticmethod
def getFileSeparator() -> str: ...

# @LuaMethod
@staticmethod
def getFileWriter(filename: str, createIfNull: bool, append: bool) -> LuaManager.GlobalObject.LuaFileWriter: ...

# @LuaMethod
@staticmethod
def getFilenameOfCallframe(c: LuaCallFrame) -> str: ...

# @LuaMethod
@staticmethod
def getFilenameOfClosure(c: LuaClosure) -> str: ...

# @LuaMethod
@staticmethod
def getFirstLineOfClosure(c: LuaClosure) -> int: ...

# @LuaMethod
@staticmethod
def getFriendsList() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getFullSaveDirectoryTable() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getGameClient() -> GameClient: ...

# @LuaMethod
@staticmethod
def getGameFilesInput(filename: str) -> DataInputStream: ...

# @LuaMethod
@staticmethod
def getGameFilesTextInput(filename: str) -> BufferedReader: ...

# @LuaMethod
@staticmethod
def getGameSpeed() -> int: ...

# @LuaMethod
@staticmethod
def getGameTime() -> GameTime: ...

# @LuaMethod
@staticmethod
def getGameVersion() -> str: ...

# @LuaMethod
@staticmethod
def getGametimeTimestamp() -> int: ...

# @LuaMethod
@staticmethod
def getHairStylesInstance() -> HairStyles: ...

# @LuaMethod
@staticmethod
def getHourMinute() -> str: ...

# @LuaMethod
@staticmethod
def getIsoMarkers() -> IsoMarkers: ...

# @LuaMethod
@staticmethod
def getItemNameFromFullType(fullType: str) -> str: ...

# @LuaMethod
@staticmethod
def getItemText(txt: str) -> str: ...

# @LuaMethod
@staticmethod
def getJoypadAButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadAimingAxisX(joypad: int) -> float: ...

# @LuaMethod
@staticmethod
def getJoypadAimingAxisY(joypad: int) -> float: ...

# @LuaMethod
@staticmethod
def getJoypadBButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadBackButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadLBumper(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadLeftStickButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadMovementAxisX(joypad: int) -> float: ...

# @LuaMethod
@staticmethod
def getJoypadMovementAxisY(joypad: int) -> float: ...

# @LuaMethod
@staticmethod
def getJoypadRBumper(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadRightStickButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadStartButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadXButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getJoypadYButton(joypad: int) -> int: ...

# @LuaMethod
@staticmethod
def getKeyCode(keyName: str) -> int: ...

# @LuaMethod
@staticmethod
def getKeyName(key: int) -> str: ...

# @LuaMethod
@staticmethod
def getLastPlayedDate(filename: str) -> str: ...

# @LuaMethod
@staticmethod
def getLastStandPlayerFileNames() -> List[str]: ...

# @LuaMethod
@staticmethod
def getLastStandPlayersDirectory() -> str: ...

# @LuaMethod
@staticmethod
def getLatestSave() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getLineNumber(c: LuaCallFrame) -> int: ...

# @LuaMethod
@staticmethod
def getLoadedLua(n: int) -> str: ...

# @LuaMethod
@staticmethod
def getLoadedLuaCount() -> int: ...

# @LuaMethod
@staticmethod
def getLocalVarCount(c: Coroutine) -> int: ...

# @LuaMethod
@staticmethod
def getLocalVarName(c: Coroutine, n: int) -> str: ...

# @LuaMethod
@staticmethod
def getLocalVarStack(c: Coroutine, n: int) -> int: ...

# @LuaMethod
@staticmethod
def getLotDirectories() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getLuaDebuggerErrorCount() -> int: ...

# @LuaMethod
@staticmethod
def getLuaDebuggerErrors() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getMPStatistics() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getMPStatus() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getMapDirectoryTable() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getMapFoldersForMod(modID: str) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getMapInfo(mapDir: str) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getMaxActivePlayers() -> int: ...

# @LuaMethod
@staticmethod
def getMaxPlayers() -> Double: ...

# @LuaMethod
@staticmethod
def getMethodParameter(o: Method, i: int) -> str: ...

# @LuaMethod
@staticmethod
def getMethodParameterCount(o: Method) -> int: ...

# @LuaMethod
@staticmethod
def getModDirectoryTable() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getModFileReader(modId: str, filename: str, createIfNull: bool) -> BufferedReader: ...

# @LuaMethod
@staticmethod
def getModFileWriter(modId: str, filename: str, createIfNull: bool, append: bool) -> LuaManager.GlobalObject.LuaFileWriter: ...

# @LuaMethod
@staticmethod
def getModInfo(modDir: str) -> ChooseGameInfo.Mod: ...

# @LuaMethod
@staticmethod
def getModInfoByID(modID: str) -> ChooseGameInfo.Mod: ...

@staticmethod
def getMods() -> List[str]: ...

# @LuaMethod
@staticmethod
def getMouseX() -> int: ...

# @LuaMethod
@staticmethod
def getMouseXScaled() -> int: ...

# @LuaMethod
@staticmethod
def getMouseY() -> int: ...

# @LuaMethod
@staticmethod
def getMouseYScaled() -> int: ...

# @LuaMethod
@staticmethod
def getMyDocumentFolder() -> str: ...

# @LuaMethod
@staticmethod
def getNumActivePlayers() -> int: ...

# @LuaMethod
@staticmethod
def getNumClassFields(o: object) -> int: ...

# @LuaMethod
@staticmethod
def getNumClassFunctions(o: object) -> int: ...

# @LuaMethod
@staticmethod
def getOnlinePlayers() -> ArrayList[IsoPlayer]: ...

# @LuaMethod
@staticmethod
def getOnlineUsername() -> str: ...

# @LuaMethod
@staticmethod
def getPacketCounts(category: int) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getPerformance() -> PerformanceSettings: ...

# @LuaMethod
@staticmethod
def getPlayer() -> IsoPlayer: ...

# @LuaMethod
@staticmethod
def getPlayerByOnlineID(id: int) -> IsoPlayer: ...

# @LuaMethod
@staticmethod
def getPlayerFromUsername(username: str) -> IsoPlayer: ...

# @LuaMethod
@staticmethod
def getPlayerInfo(player: IsoPlayer) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getPlayerScreenHeight(player: int) -> int: ...

# @LuaMethod
@staticmethod
def getPlayerScreenLeft(player: int) -> int: ...

# @LuaMethod
@staticmethod
def getPlayerScreenTop(player: int) -> int: ...

# @LuaMethod
@staticmethod
def getPlayerScreenWidth(player: int) -> int: ...

# @LuaMethod
@staticmethod
def getPublicServersList() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getPuddlesManager() -> IsoPuddles: ...

# @LuaMethod
@staticmethod
def getRadioAPI() -> RadioAPI: ...

# @LuaMethod
@staticmethod
def getRadioText(txt: str) -> str: ...

# @LuaMethod
@staticmethod
def getRadioTranslators(language: Language) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getRandomUUID() -> str: ...

# @LuaMethod
@staticmethod
def getRecipeDisplayName(name: str) -> str: ...

# @LuaMethod
@staticmethod
def getReconnectCountdownTimer() -> str: ...

# @LuaMethod
@staticmethod
def getRenderer() -> SpriteRenderer: ...

# @LuaMethod
@staticmethod
def getSLSoundManager() -> SLSoundManager: ...

# @LuaMethod
@staticmethod
def getSandboxFileWriter(filename: str, createIfNull: bool, append: bool) -> LuaManager.GlobalObject.LuaFileWriter: ...

# @LuaMethod
@staticmethod
def getSandboxOptions() -> SandboxOptions: ...

# @LuaMethod
@staticmethod
def getSandboxPresets() -> List[str]: ...

# @LuaMethod
@staticmethod
def getSaveDirectory(folder: str) -> ArrayList[File]: ...

# @LuaMethod
@staticmethod
def getSaveDirectoryTable() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getSaveInfo(saveDir: str) -> KahluaTable: ...

@staticmethod
def getSaveName(file: File) -> str: ...

# @LuaMethod
@staticmethod
def getScriptManager() -> ScriptManager: ...

# @LuaMethod
@staticmethod
def getSearchMode() -> SearchMode: ...

# @LuaMethod
@staticmethod
def getServerAddressFromArgs() -> str: ...

# @LuaMethod
@staticmethod
def getServerIP() -> str: ...

# @LuaMethod
@staticmethod
def getServerList() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getServerListFile() -> str: ...

# @LuaMethod
@staticmethod
def getServerModData() -> None: ...

# @LuaMethod
@staticmethod
def getServerName() -> str: ...

# @LuaMethod
@staticmethod
def getServerOptions() -> ServerOptions: ...

# @LuaMethod
@staticmethod
def getServerPasswordFromArgs() -> str: ...

# @LuaMethod
@staticmethod
def getServerPort() -> str: ...

# @LuaMethod
@staticmethod
def getServerSavedWorldVersion(saveFolder: str) -> int: ...

# @LuaMethod
@staticmethod
def getServerSettingsManager() -> ServerSettingsManager: ...

# @LuaMethod
@staticmethod
def getServerSpawnRegions() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getServerStatistic() -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getServerStatisticEnable() -> bool: ...

# @LuaMethod
@staticmethod
def getShortenedFilename(str: str) -> str: ...

# @LuaMethod
@staticmethod
def getSleepingEvent() -> SleepingEvent: ...

# @LuaMethod
@staticmethod
def getSoundManager() -> BaseSoundManager: ...

# @LuaMethod
@staticmethod
def getSpecificPlayer(player: int) -> IsoPlayer: ...

# @LuaMethod
@staticmethod
def getSprite(sprite: str) -> IsoSprite: ...

# @LuaMethod
@staticmethod
def getSpriteManager(sprite: str) -> IsoSpriteManager: ...

# @LuaMethod
@staticmethod
def getSquare(x: float, y: float, z: float) -> IsoGridSquare: ...

# @LuaMethod
@staticmethod
def getSteamAvatarFromSteamID(steamID: str) -> Texture: ...

# @LuaMethod
@staticmethod
def getSteamAvatarFromUsername(username: str) -> Texture: ...

# @LuaMethod
@staticmethod
def getSteamIDFromUsername(username: str) -> str: ...

# @LuaMethod
@staticmethod
def getSteamModeActive() -> Boolean: ...

# @LuaMethod
@staticmethod
def getSteamProfileNameFromSteamID(steamID: str) -> str: ...

# @LuaMethod
@staticmethod
def getSteamProfileNameFromUsername(username: str) -> str: ...

# @LuaMethod
@staticmethod
def getSteamScoreboard() -> bool: ...

# @LuaMethod
@staticmethod
def getSteamWorkshopItemIDs() -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getSteamWorkshopItemMods(itemIDStr: str) -> ArrayList[ChooseGameInfo.Mod]: ...

# @LuaMethod
@staticmethod
def getSteamWorkshopStagedItems() -> ArrayList[SteamWorkshopItem]: ...

# @LuaMethod
@staticmethod
def getTableResult(tableName: str, numberPerPages: int) -> None: ...

# @LuaMethod
@staticmethod
@overload
def getText(txt: str) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getText(txt: str, arg1: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getText(txt: str, arg1: object, arg2: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getText(txt: str, arg1: object, arg2: object, arg3: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getText(txt: str, arg1: object, arg2: object, arg3: object, arg4: object) -> str: ...

# @LuaMethod
@staticmethod
def getTextManager() -> TextManager: ...

# @LuaMethod
@staticmethod
def getTextMediaEN(txt: str) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getTextOrNull(txt: str) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getTextOrNull(txt: str, arg1: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getTextOrNull(txt: str, arg1: object, arg2: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getTextOrNull(txt: str, arg1: object, arg2: object, arg3: object) -> str: ...

# @LuaMethod
@staticmethod
@overload
def getTextOrNull(txt: str, arg1: object, arg2: object, arg3: object, arg4: object) -> str: ...

# @LuaMethod
@staticmethod
def getTexture(filename: str) -> Texture: ...

# @LuaMethod
@staticmethod
def getTextureFromSaveDir(filename: str, saveName: str) -> Texture: ...

# @LuaMethod
@staticmethod
def getTickets(author: str) -> None: ...

# @LuaMethod
@staticmethod
def getTimeInMillis() -> int: ...

# @LuaMethod
@staticmethod
def getTimestamp() -> int: ...

# @LuaMethod
@staticmethod
def getTimestampMs() -> int: ...

# @LuaMethod
@staticmethod
def getTranslatorCredits(language: Language) -> ArrayList[str]: ...

# @LuaMethod
@staticmethod
def getUrlInputStream(url: str) -> DataInputStream: ...

# @LuaMethod
@staticmethod
def getVehicleById(id: int) -> BaseVehicle: ...

# @LuaMethod
@staticmethod
def getVehicleInfo(vehicle: BaseVehicle) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getVehicleZoneAt(x: int, y: int, z: int) -> IsoMetaGrid.VehicleZone: ...

# @LuaMethod
@staticmethod
def getWorld() -> IsoWorld: ...

# @LuaMethod
@staticmethod
def getWorldMarkers() -> WorldMarkers: ...

# @LuaMethod
@staticmethod
def getWorldSoundManager() -> WorldSoundManager: ...

# @LuaMethod
@staticmethod
def getZombieInfo(zombie: IsoZombie) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def getZomboidRadio() -> ZomboidRadio: ...

# @LuaMethod
@staticmethod
def getZone(x: int, y: int, z: int) -> IsoMetaGrid.Zone: ...

# @LuaMethod
@staticmethod
def getZones(x: int, y: int, z: int) -> ArrayList[IsoMetaGrid.Zone]: ...

# @LuaMethod
@staticmethod
def hasBreakpoint(file: str, line: int) -> bool: ...

# @LuaMethod
@staticmethod
def hasDataBreakpoint(table: KahluaTable, key: object) -> bool: ...

# @LuaMethod
@staticmethod
def hasDataReadBreakpoint(table: KahluaTable, key: object) -> bool: ...

# @LuaMethod
@staticmethod
def initUISystem() -> None: ...

# @LuaMethod
@staticmethod
@overload
def instanceItem(item: str) -> InventoryItem: ...

# @LuaMethod
@staticmethod
@overload
def instanceItem(item: Item) -> InventoryItem: ...

# @LuaMethod
@staticmethod
def instanceof(obj: object, name: str) -> bool: ...

# @LuaMethod
@staticmethod
def inviteFriend(steamID: str) -> None: ...

# @LuaMethod
@staticmethod
def is64bit() -> bool: ...

# @LuaMethod
@staticmethod
def isAccessLevel(accessLevel: str) -> bool: ...

# @LuaMethod
@staticmethod
def isAdmin() -> bool: ...

# @LuaMethod
@staticmethod
def isAltKeyDown() -> bool: ...

# @LuaMethod
@staticmethod
def isClient() -> bool: ...

# @LuaMethod
@staticmethod
def isControllerConnected(index: int) -> bool: ...

# @LuaMethod
@staticmethod
def isCoopHost() -> bool: ...

# @LuaMethod
@staticmethod
def isCtrlKeyDown() -> bool: ...

# @LuaMethod
@staticmethod
def isCurrentExecutionPoint(file: str, line: int) -> bool: ...

# @LuaMethod
@staticmethod
def isDebugEnabled() -> bool: ...

# @LuaMethod
@staticmethod
def isDemo() -> bool: ...

# @LuaMethod
@staticmethod
def isDesktopOpenSupported() -> bool: ...

# @LuaMethod
@staticmethod
def isFloatingGamepadTextInputVisible() -> bool: ...

# @LuaMethod
@staticmethod
def isGamePaused() -> bool: ...

# @LuaMethod
@staticmethod
def isIngameState() -> bool: ...

# @LuaMethod
@staticmethod
def isItemTransactionConsistent(item: InventoryItem, src: ItemContainer, dst: ItemContainer) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadConnected(index: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadDown(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadLBPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadLTPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadLeft(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadLeftStickButtonPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadPressed(joypad: int, button: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadRBPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadRTPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadRight(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadRightStickButtonPressed(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isJoypadUp(joypad: int) -> bool: ...

# @LuaMethod
@staticmethod
def isKeyDown(key: int) -> bool: ...

# @LuaMethod
@staticmethod
def isKeyPressed(key: int) -> bool: ...

# @LuaMethod
@staticmethod
def isModActive(mod: ChooseGameInfo.Mod) -> bool: ...

# @LuaMethod
@staticmethod
def isMouseButtonDown(number: int) -> bool: ...

# @LuaMethod
@staticmethod
def isPublicServerListAllowed() -> bool: ...

# @LuaMethod
@staticmethod
def isServer() -> bool: ...

# @LuaMethod
@staticmethod
def isServerSoftReset() -> bool: ...

# @LuaMethod
@staticmethod
def isShiftKeyDown() -> bool: ...

# @LuaMethod
@staticmethod
def isShowConnectionInfo() -> bool: ...

# @LuaMethod
@staticmethod
def isShowPingInfo() -> bool: ...

# @LuaMethod
@staticmethod
def isShowServerInfo() -> bool: ...

# @LuaMethod
@staticmethod
def isSoundPlaying(sound: object) -> bool: ...

# @LuaMethod
@staticmethod
def isSteamOverlayEnabled() -> bool: ...

# @LuaMethod
@staticmethod
def isSteamRunningOnSteamDeck() -> bool: ...

# @LuaMethod
@staticmethod
def isSystemLinux() -> bool: ...

# @LuaMethod
@staticmethod
def isSystemMacOS() -> bool: ...

# @LuaMethod
@staticmethod
def isSystemWindows() -> bool: ...

# @LuaMethod
@staticmethod
def isValidSteamID(s: str) -> bool: ...

# @LuaMethod
@staticmethod
def isValidUserName(user: str) -> bool: ...

# @LuaMethod
@staticmethod
def isXBOXController() -> bool: ...

# @LuaMethod
@staticmethod
def isoRegionsRenderer() -> IsoRegionsRenderer: ...

# @LuaMethod
@staticmethod
def isoToScreenX(player: int, x: float, y: float, z: float) -> float: ...

# @LuaMethod
@staticmethod
def isoToScreenY(player: int, x: float, y: float, z: float) -> float: ...

# @LuaMethod
@staticmethod
def istype(obj: object, name: str) -> bool: ...

# @LuaMethod
@staticmethod
def loadSkinnedZomboidModel(name: str, loc: str, tex: str) -> Model: ...

# @LuaMethod
@staticmethod
def loadStaticZomboidModel(name: str, loc: str, tex: str) -> Model: ...

# @LuaMethod
@staticmethod
def loadVehicleModel(name: str, loc: str, tex: str) -> Model: ...

# @LuaMethod
@staticmethod
def loadZomboidModel(name: str, mesh: str, tex: str, shader: str, bStatic: bool) -> Model: ...

# @LuaMethod
@staticmethod
def localVarName(c: Coroutine, n: int) -> str: ...

# @LuaMethod
@staticmethod
def luaDebug() -> None: ...

# @LuaMethod
@staticmethod
def manipulateSavefile(folder: str, action: str) -> None: ...

# @LuaMethod
@staticmethod
def moduleDotType(module: str, type: str) -> str: ...

# @LuaMethod
@staticmethod
def openUrl(url: str) -> None: ...

# @LuaMethod
@staticmethod
def pauseSoundAndMusic() -> None: ...

# @LuaMethod
@staticmethod
def ping(username: str, pwd: str, ip: str, port: str) -> None: ...

# @LuaMethod
@staticmethod
def playServerSound(sound: str, sq: IsoGridSquare) -> None: ...

# @LuaMethod
@staticmethod
def proceedFactionMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def proceedPM(command: str) -> str: ...

# @LuaMethod
@staticmethod
def processAdminChatMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def processGeneralMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def processSafehouseMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def processSayMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def processShoutMessage(message: str) -> None: ...

# @LuaMethod
@staticmethod
def querySteamWorkshopItemDetails(itemIDs: ArrayList[str], functionObj: LuaClosure, arg1: object) -> None: ...

# @LuaMethod
@staticmethod
def queueCharEvent(eventChar: str) -> None: ...

# @LuaMethod
@staticmethod
def queueKeyEvent(lwjglKeyCode: int) -> None: ...

# @LuaMethod
@staticmethod
def rainConfig(cmd: str, arg: int) -> None: ...

# @LuaMethod
@staticmethod
def reactivateJoypadAfterResetLua() -> bool: ...

# @LuaMethod
@staticmethod
def reloadControllerConfigFiles() -> None: ...

# @LuaMethod
@staticmethod
def reloadEngineRPM() -> None: ...

# @LuaMethod
@staticmethod
def reloadLuaFile(filename: str) -> None: ...

# @LuaMethod
@staticmethod
def reloadModelsMatching(meshName: str) -> None: ...

# @LuaMethod
@staticmethod
def reloadServerLuaFile(filename: str) -> None: ...

# @LuaMethod
@staticmethod
def reloadSoundFiles() -> None: ...

# @LuaMethod
@staticmethod
def reloadVehicleTextures(scriptName: str) -> None: ...

# @LuaMethod
@staticmethod
def reloadVehicles() -> None: ...

# @LuaMethod
@staticmethod
def removeItemTransaction(item: InventoryItem, src: ItemContainer, dst: ItemContainer) -> None: ...

# @LuaMethod
@staticmethod
def removeTicket(ticketID: int) -> None: ...

# @LuaMethod
@staticmethod
def removeUserlog(user: str, type: str, text: str) -> None: ...

# @LuaMethod
@staticmethod
def renameSavefile(gameMode: str, oldName: str, newName: str) -> bool: ...

# @LuaMethod
@staticmethod
def renderIsoCircle(x: float, y: float, z: float, radius: float, r: float, g: float, b: float, a: float, thickness: int) -> None: ...

# @LuaMethod
@staticmethod
def replaceWith(toReplace: str, regex: str, by: str) -> str: ...

# @LuaMethod
@staticmethod
def requestPacketCounts() -> None: ...

# @LuaMethod
@staticmethod
def requestTrading(you: IsoPlayer, other: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def requestUserlog(user: str) -> None: ...

# @LuaMethod
@staticmethod
def require(f: str) -> object: ...

# @LuaMethod
@staticmethod
def resetRegionFile() -> None: ...

# @LuaMethod
@staticmethod
def resumeSoundAndMusic() -> None: ...

# @LuaMethod
@staticmethod
def revertToKeyboardAndMouse() -> None: ...

# @LuaMethod
@staticmethod
def sanitizeWorldName(worldName: str) -> str: ...

# @LuaMethod
@staticmethod
def save(doCharacter: bool) -> None: ...

# @LuaMethod
@staticmethod
def saveControllerSettings(c: int) -> None: ...

# @LuaMethod
@staticmethod
def saveGame() -> None: ...

# @LuaMethod
@staticmethod
def saveModsFile() -> None: ...

# @LuaMethod
@staticmethod
def scoreboardUpdate() -> None: ...

# @LuaMethod
@staticmethod
def screenToIsoX(player: int, x: float, y: float, z: float) -> float: ...

# @LuaMethod
@staticmethod
def screenToIsoY(player: int, x: float, y: float, z: float) -> float: ...

# @LuaMethod
@staticmethod
def sendBandage(onlineID: int, i: int, bandaged: bool, bandageLife: float, isAlcoholic: bool, bandageType: str) -> None: ...

# @LuaMethod
@staticmethod
def sendCataplasm(onlineID: int, i: int, plantainFactor: float, comfreyFactor: float, garlicFactor: float) -> None: ...

# @LuaMethod
@staticmethod
def sendCleanBurn(wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, bandage: InventoryItem) -> None: ...

# @LuaMethod
@staticmethod
@overload
def sendClientCommand(module: str, command: str, args: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
@overload
def sendClientCommand(player: IsoPlayer, module: str, command: str, args: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
def sendClothing(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def sendDisinfect(wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, alcohol: InventoryItem) -> None: ...

# @LuaMethod
@staticmethod
def sendFactionInvite(faction: Faction, host: IsoPlayer, invited: str) -> None: ...

# @LuaMethod
@staticmethod
def sendItemListNet(sender: IsoPlayer, items: ArrayList[InventoryItem], receiver: IsoPlayer, transferID: str, custom: str) -> bool: ...

# @LuaMethod
@staticmethod
def sendItemsInContainer(obj: IsoObject, container: ItemContainer) -> None: ...

# @LuaMethod
@staticmethod
def sendPersonalColor(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def sendPing() -> None: ...

# @LuaMethod
@staticmethod
def sendPlayerExtraInfo(p: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def sendPlayerStatsChange(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def sendRemoveBullet(wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart) -> None: ...

# @LuaMethod
@staticmethod
def sendRemoveGlass(wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, handPain: bool) -> None: ...

# @LuaMethod
@staticmethod
def sendRequestInventory(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def sendSafehouseInvite(safehouse: SafeHouse, host: IsoPlayer, invited: str) -> None: ...

# @LuaMethod
@staticmethod
@overload
def sendServerCommand(module: str, command: str, args: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
@overload
def sendServerCommand(player: IsoPlayer, module: str, command: str, args: KahluaTable) -> None: ...

# @LuaMethod
@staticmethod
def sendSplint(onlineID: int, i: int, doIt: bool, factor: float, splintItem: str) -> None: ...

# @LuaMethod
@staticmethod
def sendStitch(wielder: IsoGameCharacter, target: IsoGameCharacter, bodyPart: BodyPart, item: InventoryItem, doIt: bool) -> None: ...

# @LuaMethod
@staticmethod
def sendSwitchSeat(vehicle: BaseVehicle, chr: IsoGameCharacter, seatFrom: int, seatTo: int) -> None: ...

# @LuaMethod
@staticmethod
def sendVisual(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def serverConnect(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, arg7: bool) -> None: ...

# @LuaMethod
@staticmethod
def serverConnectCoop(serverSteamID: str) -> None: ...

# @LuaMethod
@staticmethod
def serverFileExists(filename: str) -> bool: ...

# @LuaMethod
@staticmethod
def setActivePlayer(id: int) -> None: ...

# @LuaMethod
@staticmethod
def setAdmin() -> None: ...

# @LuaMethod
@staticmethod
def setAggroTarget(id: int, x: int, y: int) -> None: ...

# @LuaMethod
@staticmethod
def setBehaviorStep(b: bool) -> None: ...

# @LuaMethod
@staticmethod
def setControllerDeadZone(c: int, axis: int, value: float) -> None: ...

# @LuaMethod
@staticmethod
def setDebugToggleControllerPluggedIn(index: int) -> None: ...

# @LuaMethod
@staticmethod
def setGameSpeed(NewSpeed: int) -> None: ...

# @LuaMethod
@staticmethod
def setModelMetaData(name: str, mesh: str, tex: str, shader: str, bStatic: bool) -> None: ...

# @LuaMethod
@staticmethod
def setMouseXY(x: int, y: int) -> None: ...

# @LuaMethod
@staticmethod
def setPlayerJoypad(player: int, joypad: int, playerObj: IsoPlayer, username: str) -> None: ...

# @LuaMethod
@staticmethod
def setPlayerMouse(playerObj: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def setPlayerMovementActive(id: int, bActive: bool) -> None: ...

# @LuaMethod
@staticmethod
def setProgressBarValue(player: IsoPlayer, value: int) -> None: ...

# @LuaMethod
@staticmethod
def setPuddles(initialPuddles: float) -> None: ...

# @LuaMethod
@staticmethod
def setSavefilePlayer1(gameMode: str, saveDir: str, sqlID: int) -> None: ...

# @LuaMethod
@staticmethod
def setServerStatisticEnable(enable: bool) -> None: ...

# @LuaMethod
@staticmethod
def setShowConnectionInfo(enabled: bool) -> None: ...

# @LuaMethod
@staticmethod
def setShowPausedMessage(b: bool) -> None: ...

# @LuaMethod
@staticmethod
def setShowPingInfo(enabled: bool) -> None: ...

# @LuaMethod
@staticmethod
def setShowServerInfo(enabled: bool) -> None: ...

# @LuaMethod
@staticmethod
def showAnimationViewer() -> None: ...

# @LuaMethod
@staticmethod
def showAttachmentEditor() -> None: ...

# @LuaMethod
@staticmethod
def showChunkDebugger() -> None: ...

# @LuaMethod
@staticmethod
def showFolderInDesktop(folder: str) -> None: ...

# @LuaMethod
@staticmethod
def showGlobalObjectDebugger() -> None: ...

# @LuaMethod
@staticmethod
def showSteamFloatingGamepadTextInput(multiLine: bool, x: int, y: int, width: int, height: int) -> bool: ...

# @LuaMethod
@staticmethod
def showSteamGamepadTextInput(password: bool, multiLine: bool, description: str, maxChars: int, existingText: str) -> bool: ...

# @LuaMethod
@staticmethod
def showVehicleEditor(scriptName: str) -> None: ...

# @LuaMethod
@staticmethod
def showWorldMapEditor(value: str) -> None: ...

# @LuaMethod
@staticmethod
def showWrongChatTabMessage(actualTabID: int, rightTabID: int, chatCommand: str) -> None: ...

# @LuaMethod
@staticmethod
def sledgeDestroy(object: IsoObject) -> None: ...

# @LuaMethod
@staticmethod
def spawnHorde(x: float, y: float, x2: float, y2: float, z: float, count: int) -> None: ...

# @LuaMethod
@staticmethod
def spawnpointsExistsForMod(modID: str, mapFolder: str) -> bool: ...

# @LuaMethod
@staticmethod
def steamGetInternetServerDetails(index: int) -> Server: ...

# @LuaMethod
@staticmethod
def steamGetInternetServersCount() -> int: ...

# @LuaMethod
@staticmethod
def steamReleaseInternetServersRequest() -> None: ...

# @LuaMethod
@staticmethod
def steamRequestInternetServersList() -> None: ...

# @LuaMethod
@staticmethod
def steamRequestServerDetails(host: str, port: int) -> bool: ...

# @LuaMethod
@staticmethod
def steamRequestServerRules(host: str, port: int) -> bool: ...

# @LuaMethod
@staticmethod
def stopPing() -> None: ...

# @LuaMethod
@staticmethod
def stopSound(sound: int) -> None: ...

# @LuaMethod
@staticmethod
def tabToX(a: str, tabX: int) -> str: ...

# @LuaMethod
@staticmethod
@overload
def takeScreenshot() -> None: ...

# @LuaMethod
@staticmethod
@overload
def takeScreenshot(fileName: str) -> None: ...

# @LuaMethod
@staticmethod
def testHelicopter() -> None: ...

# @LuaMethod
@staticmethod
def testSound() -> None: ...

# @LuaMethod
@staticmethod
def timSort(table: KahluaTable, functionObject: object) -> None: ...

# @LuaMethod
@staticmethod
def toInt(val: float) -> int: ...

# @LuaMethod
@staticmethod
def toggleBreakOnChange(table: KahluaTable, key: object) -> None: ...

# @LuaMethod
@staticmethod
def toggleBreakOnRead(table: KahluaTable, key: object) -> None: ...

# @LuaMethod
@staticmethod
def toggleBreakpoint(file: str, line: int) -> None: ...

# @LuaMethod
@staticmethod
def toggleModActive(mod: ChooseGameInfo.Mod, active: bool) -> None: ...

# @LuaMethod
@staticmethod
def toggleSafetyServer(player: IsoPlayer) -> None: ...

# @LuaMethod
@staticmethod
def toggleVehicleRenderToTexture() -> None: ...

# @LuaMethod
@staticmethod
def tradingUISendAddItem(you: IsoPlayer, other: IsoPlayer, i: InventoryItem) -> None: ...

# @LuaMethod
@staticmethod
def tradingUISendRemoveItem(you: IsoPlayer, other: IsoPlayer, index: int) -> None: ...

# @LuaMethod
@staticmethod
def tradingUISendUpdateState(you: IsoPlayer, other: IsoPlayer, state: int) -> None: ...

# @LuaMethod
@staticmethod
def transformIntoKahluaTable(map: HashMap[object, object]) -> KahluaTable: ...

# @LuaMethod
@staticmethod
def translatePointXInOverheadMapToWindow(x: float, ui: UIElement, zoom: float, xpos: float) -> float: ...

# @LuaMethod
@staticmethod
def translatePointXInOverheadMapToWorld(x: float, ui: UIElement, zoom: float, xpos: float) -> float: ...

# @LuaMethod
@staticmethod
def translatePointYInOverheadMapToWindow(y: float, ui: UIElement, zoom: float, ypos: float) -> float: ...

# @LuaMethod
@staticmethod
def translatePointYInOverheadMapToWorld(y: float, ui: UIElement, zoom: float, ypos: float) -> float: ...

# @LuaMethod
@staticmethod
@overload
def triggerEvent(event: str) -> None: ...

# @LuaMethod
@staticmethod
@overload
def triggerEvent(event: str, param: object) -> None: ...

# @LuaMethod
@staticmethod
@overload
def triggerEvent(event: str, param: object, param2: object) -> None: ...

# @LuaMethod
@staticmethod
@overload
def triggerEvent(event: str, param: object, param2: object, param3: object) -> None: ...

# @LuaMethod
@staticmethod
@overload
def triggerEvent(event: str, param: object, param2: object, param3: object, param4: object) -> None: ...

# @LuaMethod
@staticmethod
def updateChatSettings(fontSize: str, showTimestamp: bool, showTitle: bool) -> None: ...

# @LuaMethod
@staticmethod
def updateFire() -> None: ...

# @LuaMethod
@staticmethod
def useStaticErosionRand(use: bool) -> None: ...

# @LuaMethod
@staticmethod
def useTextureFiltering(bUse: bool) -> None: ...

# @LuaMethod
@staticmethod
def wasKeyDown(key: int) -> bool: ...

# @LuaMethod
@staticmethod
def wasMouseActiveMoreRecentlyThanJoypad() -> bool: ...

# @LuaMethod
@staticmethod
def writeLog(loggerName: str, logs: str) -> None: ...

# @LuaMethod
@staticmethod
def zpopClearZombies(cellX: int, cellY: int) -> None: ...

# @LuaMethod
@staticmethod
def zpopNewRenderer() -> ZombiePopulationRenderer: ...

# @LuaMethod
@staticmethod
def zpopSpawnNow(cellX: int, cellY: int) -> None: ...

# @LuaMethod
@staticmethod
def zpopSpawnTimeToZero(cellX: int, cellY: int) -> None: ...

Events: Any
