from typing import Any, overload
from zombie.Lua import LuaManager

class Pythoid:

    @staticmethod
    def expose(clazz: Any) -> None: ...

    @staticmethod
    def invoke(instance: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def invokeStatic(clazz: object, methodName: str, *args) -> Any: ...

    @staticmethod
    def getField(instance: object, fieldName: str) -> Any: ...

    @staticmethod
    def getStaticField(clazz: object, fieldName: str) -> Any: ... 


def getDebug():
  return LuaManager.GlobalObject.getDebug()

def save(var0):
  return LuaManager.GlobalObject.save(var0)

def istype(var0, var1):
  return LuaManager.GlobalObject.istype(var0, var1)

def getLineNumber(var0):
  return LuaManager.GlobalObject.getLineNumber(var0)

def replaceWith(var0, var1, var2):
  return LuaManager.GlobalObject.replaceWith(var0, var1, var2)

def getTimestamp():
  return LuaManager.GlobalObject.getTimestamp()

def getZone(var0, var1, var2):
  return LuaManager.GlobalObject.getZone(var0, var1, var2)

@overload
def getText(var0):
  return LuaManager.GlobalObject.getText(var0)

@overload
def getText(var0, var1):
  return LuaManager.GlobalObject.getText(var0, var1)

@overload
def getText(var0, var1, var2):
  return LuaManager.GlobalObject.getText(var0, var1, var2)

@overload
def getText(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.getText(var0, var1, var2, var3, var4)

@overload
def getText(var0, var1, var2, var3):
  return LuaManager.GlobalObject.getText(var0, var1, var2, var3)

def getTimeInMillis():
  return LuaManager.GlobalObject.getTimeInMillis()

@overload
def triggerEvent(var0, var1, var2):
  return LuaManager.GlobalObject.triggerEvent(var0, var1, var2)

@overload
def triggerEvent(var0, var1):
  return LuaManager.GlobalObject.triggerEvent(var0, var1)

@overload
def triggerEvent(var0):
  return LuaManager.GlobalObject.triggerEvent(var0)

@overload
def triggerEvent(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.triggerEvent(var0, var1, var2, var3, var4)

@overload
def triggerEvent(var0, var1, var2, var3):
  return LuaManager.GlobalObject.triggerEvent(var0, var1, var2, var3)

def createWorld(var0):
  return LuaManager.GlobalObject.createWorld(var0)

def forceDisconnect():
  return LuaManager.GlobalObject.forceDisconnect()

def isCoopHost():
  return LuaManager.GlobalObject.isCoopHost()

def disconnect():
  return LuaManager.GlobalObject.disconnect()

def getTexture(var0):
  return LuaManager.GlobalObject.getTexture(var0)

def saveModsFile():
  return LuaManager.GlobalObject.saveModsFile()

def getMyDocumentFolder():
  return LuaManager.GlobalObject.getMyDocumentFolder()

def writeLog(var0, var1):
  return LuaManager.GlobalObject.writeLog(var0, var1)

def isValidUserName(var0):
  return LuaManager.GlobalObject.isValidUserName(var0)

def getMaxPlayers():
  return LuaManager.GlobalObject.getMaxPlayers()

def isValidSteamID(var0):
  return LuaManager.GlobalObject.isValidSteamID(var0)

def InvMngRemoveItem(var0, var2):
  return LuaManager.GlobalObject.InvMngRemoveItem(var0, var2)

def InvMngGetItem(var0, var2, var3):
  return LuaManager.GlobalObject.InvMngGetItem(var0, var2, var3)

def getCell():
  return LuaManager.GlobalObject.getCell()

def getSprite(var0):
  return LuaManager.GlobalObject.getSprite(var0)

def getSquare(var0, var2, var4):
  return LuaManager.GlobalObject.getSquare(var0, var2, var4)

def addUserlog(var0, var1, var2):
  return LuaManager.GlobalObject.addUserlog(var0, var1, var2)

def sendClothing(var0):
  return LuaManager.GlobalObject.sendClothing(var0)

def addBloodSplat(var1, var2):
  return LuaManager.GlobalObject.addBloodSplat(var1, var2)

def resumeSoundAndMusic():
  return LuaManager.GlobalObject.resumeSoundAndMusic()

def canModifyPlayerStats():
  return LuaManager.GlobalObject.canModifyPlayerStats()

def sendPlayerExtraInfo(var0):
  return LuaManager.GlobalObject.sendPlayerExtraInfo(var0)

def sendItemsInContainer(var0, var1):
  return LuaManager.GlobalObject.sendItemsInContainer(var0, var1)

def isKeyDown(var0):
  return LuaManager.GlobalObject.isKeyDown(var0)

def wasKeyDown(var0):
  return LuaManager.GlobalObject.wasKeyDown(var0)

def isAccessLevel(var0):
  return LuaManager.GlobalObject.isAccessLevel(var0)

def getAllSavedPlayers():
  return LuaManager.GlobalObject.getAllSavedPlayers()

def sendVisual(var0):
  return LuaManager.GlobalObject.sendVisual(var0)

def SendCommandToServer(var0):
  return LuaManager.GlobalObject.SendCommandToServer(var0)

@overload
def copyTable(var0, var1):
  return LuaManager.GlobalObject.copyTable(var0, var1)

@overload
def copyTable(var0):
  return LuaManager.GlobalObject.copyTable(var0)

def moduleDotType(var0, var1):
  return LuaManager.GlobalObject.moduleDotType(var0, var1)

def addVehicle(var0):
  return LuaManager.GlobalObject.addVehicle(var0)

def getPlayerFromUsername(var0):
  return LuaManager.GlobalObject.getPlayerFromUsername(var0)

def setServerStatisticEnable(var0):
  return LuaManager.GlobalObject.setServerStatisticEnable(var0)

def getReconnectCountdownTimer():
  return LuaManager.GlobalObject.getReconnectCountdownTimer()

def sendSafehouseInvite(var0, var1, var2):
  return LuaManager.GlobalObject.sendSafehouseInvite(var0, var1, var2)

def requestPacketCounts():
  return LuaManager.GlobalObject.requestPacketCounts()

def tradingUISendAddItem(var0, var1, var2):
  return LuaManager.GlobalObject.tradingUISendAddItem(var0, var1, var2)

def getServerSpawnRegions():
  return LuaManager.GlobalObject.getServerSpawnRegions()

def tradingUISendUpdateState(var0, var1, var2):
  return LuaManager.GlobalObject.tradingUISendUpdateState(var0, var1, var2)

def getPlayerByOnlineID(var0):
  return LuaManager.GlobalObject.getPlayerByOnlineID(var0)

def tradingUISendRemoveItem(var0, var1, var2):
  return LuaManager.GlobalObject.tradingUISendRemoveItem(var0, var1, var2)

def getServerStatisticEnable():
  return LuaManager.GlobalObject.getServerStatisticEnable()

def getConnectedPlayers():
  return LuaManager.GlobalObject.getConnectedPlayers()

def acceptFactionInvite(var0, var1):
  return LuaManager.GlobalObject.acceptFactionInvite(var0, var1)

def sendRequestInventory(var0):
  return LuaManager.GlobalObject.sendRequestInventory(var0)

def acceptSafehouseInvite(var0, var1):
  return LuaManager.GlobalObject.acceptSafehouseInvite(var0, var1)

def playServerSound(var0, var1):
  return LuaManager.GlobalObject.playServerSound(var0, var1)

@overload
def sendClientCommand(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendClientCommand(var0, var1, var2, var3)

@overload
def sendClientCommand(var0, var1, var2):
  return LuaManager.GlobalObject.sendClientCommand(var0, var1, var2)

def getPlayer():
  return LuaManager.GlobalObject.getPlayer()

def addSound(var1, var2, var3, var4, var5, var6):
  return LuaManager.GlobalObject.addSound(var1, var2, var3, var4, var5, var6)

def getAccessLevel():
  return LuaManager.GlobalObject.getAccessLevel()

def ping(var0, var1, var2, var3):
  return LuaManager.GlobalObject.ping(var0, var1, var2, var3)

@overload
def sendServerCommand(var0, var1, var2):
  return LuaManager.GlobalObject.sendServerCommand(var0, var1, var2)

@overload
def sendServerCommand(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendServerCommand(var0, var1, var2, var3)

def canSeePlayerStats():
  return LuaManager.GlobalObject.canSeePlayerStats()

def getDBSchema():
  return LuaManager.GlobalObject.getDBSchema()

def getTableResult(var0, var1):
  return LuaManager.GlobalObject.getTableResult(var0, var1)

def addWarningPoint(var0, var1, var2):
  return LuaManager.GlobalObject.addWarningPoint(var0, var1, var2)

def executeQuery(var0, var1):
  return LuaManager.GlobalObject.executeQuery(var0, var1)

def addTicket(var0, var1, var2):
  return LuaManager.GlobalObject.addTicket(var0, var1, var2)

def sendItemListNet(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.sendItemListNet(var0, var1, var2, var3, var4)

def removeTicket(var0):
  return LuaManager.GlobalObject.removeTicket(var0)

def getTickets(var0):
  return LuaManager.GlobalObject.getTickets(var0)

def pauseSoundAndMusic():
  return LuaManager.GlobalObject.pauseSoundAndMusic()

def stopSound(var0):
  return LuaManager.GlobalObject.stopSound(var0)

def isKeyPressed(var0):
  return LuaManager.GlobalObject.isKeyPressed(var0)

def getServerIP():
  return LuaManager.GlobalObject.getServerIP()

def getMPStatistics():
  return LuaManager.GlobalObject.getMPStatistics()

def getServerPort():
  return LuaManager.GlobalObject.getServerPort()

def getControllerCount():
  return LuaManager.GlobalObject.getControllerCount()

def getAllItems():
  return LuaManager.GlobalObject.getAllItems()

def getGameVersion():
  return LuaManager.GlobalObject.getGameVersion()

def deleteSave(var0):
  return LuaManager.GlobalObject.deleteSave(var0)

def getServerName():
  return LuaManager.GlobalObject.getServerName()

def sendAddXp(var1, var2, var3):
  return LuaManager.GlobalObject.sendAddXp(var1, var2, var3)

def sendStitch(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.sendStitch(var0, var1, var2, var3, var4)

def sendSplint(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.sendSplint(var0, var1, var2, var3, var4)

def sendRemoveGlass(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendRemoveGlass(var0, var1, var2, var3)

def sendBandage(var0, var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.sendBandage(var0, var1, var2, var3, var4, var5)

def sendRemoveBullet(var0, var1, var2):
  return LuaManager.GlobalObject.sendRemoveBullet(var0, var1, var2)

def sendCleanBurn(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendCleanBurn(var0, var1, var2, var3)

def canConnect():
  return LuaManager.GlobalObject.canConnect()

def scoreboardUpdate():
  return LuaManager.GlobalObject.scoreboardUpdate()

def sendPersonalColor(var0):
  return LuaManager.GlobalObject.sendPersonalColor(var0)

def sendDisinfect(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendDisinfect(var0, var1, var2, var3)

def requestUserlog(var0):
  return LuaManager.GlobalObject.requestUserlog(var0)

def sendPing():
  return LuaManager.GlobalObject.sendPing()

def requestTrading(var0, var1):
  return LuaManager.GlobalObject.requestTrading(var0, var1)

def sendFactionInvite(var0, var1, var2):
  return LuaManager.GlobalObject.sendFactionInvite(var0, var1, var2)

def acceptTrading(var0, var1, var2):
  return LuaManager.GlobalObject.acceptTrading(var0, var1, var2)

def sendCataplasm(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.sendCataplasm(var0, var1, var2, var3, var4)

def removeUserlog(var0, var1, var2):
  return LuaManager.GlobalObject.removeUserlog(var0, var1, var2)

def resetRegionFile():
  return LuaManager.GlobalObject.resetRegionFile()

@overload
def getTextOrNull(var0):
  return LuaManager.GlobalObject.getTextOrNull(var0)

@overload
def getTextOrNull(var0, var1, var2, var3):
  return LuaManager.GlobalObject.getTextOrNull(var0, var1, var2, var3)

@overload
def getTextOrNull(var0, var1, var2):
  return LuaManager.GlobalObject.getTextOrNull(var0, var1, var2)

@overload
def getTextOrNull(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.getTextOrNull(var0, var1, var2, var3, var4)

def getTextOrNull(var0, var1):
  return LuaManager.GlobalObject.getTextOrNull(var0, var1)

def getKeyCode(var0):
  return LuaManager.GlobalObject.getKeyCode(var0)

def getKeyName(var0):
  return LuaManager.GlobalObject.getKeyName(var0)

def getButtonCount(var0):
  return LuaManager.GlobalObject.getButtonCount(var0)

def isGamePaused():
  return LuaManager.GlobalObject.isGamePaused()

def revertToKeyboardAndMouse():
  return LuaManager.GlobalObject.revertToKeyboardAndMouse()

def saveControllerSettings(var0):
  return LuaManager.GlobalObject.saveControllerSettings(var0)

def isJoypadConnected(var0):
  return LuaManager.GlobalObject.isJoypadConnected(var0)

def setDebugToggleControllerPluggedIn(var0):
  return LuaManager.GlobalObject.setDebugToggleControllerPluggedIn(var0)

def setShowPausedMessage(var0):
  return LuaManager.GlobalObject.setShowPausedMessage(var0)

def isServer():
  return LuaManager.GlobalObject.isServer()

def getItemNameFromFullType(var0):
  return LuaManager.GlobalObject.getItemNameFromFullType(var0)

def getTextMediaEN(var0):
  return LuaManager.GlobalObject.getTextMediaEN(var0)

def getRadioText(var0):
  return LuaManager.GlobalObject.getRadioText(var0)

def getCurrentCoroutine():
  return LuaManager.GlobalObject.getCurrentCoroutine()

def toggleBreakOnChange(var0, var1):
  return LuaManager.GlobalObject.toggleBreakOnChange(var0, var1)

def isFloatingGamepadTextInputVisible():
  return LuaManager.GlobalObject.isFloatingGamepadTextInputVisible()

def getAllRecipes():
  return LuaManager.GlobalObject.getAllRecipes()

def createHordeInAreaTo(var0, var1, var2, var3, var4, var5, var6):
  return LuaManager.GlobalObject.createHordeInAreaTo(var0, var1, var2, var3, var4, var5, var6)

def spawnHorde(var0, var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.spawnHorde(var0, var1, var2, var3, var4, var5)

def createHordeFromTo(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.createHordeFromTo(var0, var1, var2, var3, var4)

def setAggroTarget(var0, var1, var2):
  return LuaManager.GlobalObject.setAggroTarget(var0, var1, var2)

def addPhysicsObject():
  return LuaManager.GlobalObject.addPhysicsObject()

def getCallframeTop(var0):
  return LuaManager.GlobalObject.getCallframeTop(var0)

def hasDataBreakpoint(var0, var1):
  return LuaManager.GlobalObject.hasDataBreakpoint(var0, var1)

def toggleBreakOnRead(var0, var1):
  return LuaManager.GlobalObject.toggleBreakOnRead(var0, var1)

def hasBreakpoint(var0, var1):
  return LuaManager.GlobalObject.hasBreakpoint(var0, var1)

def isModActive(var0):
  return LuaManager.GlobalObject.isModActive(var0)

def require(var0):
  return LuaManager.GlobalObject.require(var0)

def sanitizeWorldName(var0):
  return LuaManager.GlobalObject.sanitizeWorldName(var0)

def getServerListFile():
  return LuaManager.GlobalObject.getServerListFile()

@overload
def debugLuaTable(var0):
  return LuaManager.GlobalObject.debugLuaTable(var0)

@overload
def debugLuaTable(var0, var1):
  return LuaManager.GlobalObject.debugLuaTable(var0, var1)

def loadZomboidModel(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.loadZomboidModel(var0, var1, var2, var3, var4)

def serverConnect(var0, var1, var2, var3, var4, var5, var6, var7):
  return LuaManager.GlobalObject.serverConnect(var0, var1, var2, var3, var4, var5, var6, var7)

def getSaveDirectory(var0):
  return LuaManager.GlobalObject.getSaveDirectory(var0)

def getRandomUUID():
  return LuaManager.GlobalObject.getRandomUUID()

def getPacketCounts(var0):
  return LuaManager.GlobalObject.getPacketCounts(var0)

def isSystemWindows():
  return LuaManager.GlobalObject.isSystemWindows()

def isSystemMacOS():
  return LuaManager.GlobalObject.isSystemMacOS()

def getSteamModeActive():
  return LuaManager.GlobalObject.getSteamModeActive()

def addAllVehicles():
  return LuaManager.GlobalObject.addAllVehicles()

def focusOnTab(var0):
  return LuaManager.GlobalObject.focusOnTab(var0)

def sendSwitchSeat(var0, var1, var2, var3):
  return LuaManager.GlobalObject.sendSwitchSeat(var0, var1, var2, var3)

def addVehicleDebug(var0, var1, var2, var3):
  return LuaManager.GlobalObject.addVehicleDebug(var0, var1, var2, var3)

@overload
def addZombiesInOutfit(var0, var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.addZombiesInOutfit(var0, var1, var2, var3, var4, var5)

@overload
def addZombiesInOutfit(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10):
  return LuaManager.GlobalObject.addZombiesInOutfit(var0, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10)

def updateChatSettings(var0, var1, var2):
  return LuaManager.GlobalObject.updateChatSettings(var0, var1, var2)

def setPuddles(var0):
  return LuaManager.GlobalObject.setPuddles(var0)

def setBehaviorStep(var0):
  return LuaManager.GlobalObject.setBehaviorStep(var0)

def getZomboidRadio():
  return LuaManager.GlobalObject.getZomboidRadio()

def instanceof(var0, var1):
  return LuaManager.GlobalObject.instanceof(var0, var1)

def serverConnectCoop(var0):
  return LuaManager.GlobalObject.serverConnectCoop(var0)

def backToSinglePlayer():
  return LuaManager.GlobalObject.backToSinglePlayer()

def isIngameState():
  return LuaManager.GlobalObject.isIngameState()

def saveGame():
  return LuaManager.GlobalObject.saveGame()

def tabToX(var0, var1):
  return LuaManager.GlobalObject.tabToX(var0, var1)

def loadVehicleModel(var0, var1, var2):
  return LuaManager.GlobalObject.loadVehicleModel(var0, var1, var2)

def getSLSoundManager():
  return LuaManager.GlobalObject.getSLSoundManager()

def getRadioAPI():
  return LuaManager.GlobalObject.getRadioAPI()

def getLatestSave():
  return LuaManager.GlobalObject.getLatestSave()

def screenToIsoY(var0, var1, var2, var3):
  return LuaManager.GlobalObject.screenToIsoY(var0, var1, var2, var3)

def AddWorldSound(var0, var1, var2):
  return LuaManager.GlobalObject.AddWorldSound(var0, var1, var2)

def getLoadedLua(var0):
  return LuaManager.GlobalObject.getLoadedLua(var0)

def isServerSoftReset():
  return LuaManager.GlobalObject.isServerSoftReset()

def setActivePlayer(var0):
  return LuaManager.GlobalObject.setActivePlayer(var0)

def getOnlinePlayers():
  return LuaManager.GlobalObject.getOnlinePlayers()

def isoToScreenY(var0, var1, var2, var3):
  return LuaManager.GlobalObject.isoToScreenY(var0, var1, var2, var3)

def getPlayerScreenTop(var0):
  return LuaManager.GlobalObject.getPlayerScreenTop(var0)

def initUISystem():
  return LuaManager.GlobalObject.initUISystem()

def isDebugEnabled():
  return LuaManager.GlobalObject.isDebugEnabled()

def getSpecificPlayer(var0):
  return LuaManager.GlobalObject.getSpecificPlayer(var0)

def toggleBreakpoint(var0, var1):
  return LuaManager.GlobalObject.toggleBreakpoint(var0, var1)

def getCameraOffX():
  return LuaManager.GlobalObject.getCameraOffX()

def isoToScreenX(var0, var1, var2, var3):
  return LuaManager.GlobalObject.isoToScreenX(var0, var1, var2, var3)

def getLoadedLuaCount():
  return LuaManager.GlobalObject.getLoadedLuaCount()

def getPerformance():
  return LuaManager.GlobalObject.getPerformance()

def isDemo():
  return LuaManager.GlobalObject.isDemo()

def screenToIsoX(var0, var1, var2, var3):
  return LuaManager.GlobalObject.screenToIsoX(var0, var1, var2, var3)

def reloadLuaFile(var0):
  return LuaManager.GlobalObject.reloadLuaFile(var0)

def AddNoiseToken(var0, var1):
  return LuaManager.GlobalObject.AddNoiseToken(var0, var1)

def getSleepingEvent():
  return LuaManager.GlobalObject.getSleepingEvent()

def getFileSeparator():
  return LuaManager.GlobalObject.getFileSeparator()

def fileExists(var0):
  return LuaManager.GlobalObject.fileExists(var0)

def sledgeDestroy(var0):
  return LuaManager.GlobalObject.sledgeDestroy(var0)

@overload
def takeScreenshot():
  return LuaManager.GlobalObject.takeScreenshot()

@overload
def takeScreenshot(var0):
  return LuaManager.GlobalObject.takeScreenshot(var0)

def doTutorial(var0):
  return LuaManager.GlobalObject.doTutorial(var0)

def serverFileExists(var0):
  return LuaManager.GlobalObject.serverFileExists(var0)

def checkStringPattern(var0):
  return LuaManager.GlobalObject.checkStringPattern(var0)

def getModInfoByID(var0):
  return LuaManager.GlobalObject.getModInfoByID(var0)

def cloneItemType(var0, var1):
  return LuaManager.GlobalObject.cloneItemType(var0, var1)

def getCameraOffY():
  return LuaManager.GlobalObject.getCameraOffY()

def getServerList():
  return LuaManager.GlobalObject.getServerList()

def createZombie(var0, var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.createZombie(var0, var1, var2, var3, var4, var5)

def getModInfo(var0):
  return LuaManager.GlobalObject.getModInfo(var0)

def doChallenge(var0):
  return LuaManager.GlobalObject.doChallenge(var0)

@overload
def instanceItem(var0):
  return LuaManager.GlobalObject.instanceItem(var0)

@overload
def instanceItem(var0):
  return LuaManager.GlobalObject.instanceItem(var0)

def createRegionFile():
  return LuaManager.GlobalObject.createRegionFile()

def stopPing():
  return LuaManager.GlobalObject.stopPing()

def getFileOutput(var0):
  return LuaManager.GlobalObject.getFileOutput(var0)

def getControllerPovY(var0):
  return LuaManager.GlobalObject.getControllerPovY(var0)

def getModFileReader(var0, var1, var2):
  return LuaManager.GlobalObject.getModFileReader(var0, var1, var2)

def updateFire():
  return LuaManager.GlobalObject.updateFire()

def isJoypadPressed(var0, var1):
  return LuaManager.GlobalObject.isJoypadPressed(var0, var1)

def getJoypadBButton(var0):
  return LuaManager.GlobalObject.getJoypadBButton(var0)

def getJoypadAButton(var0):
  return LuaManager.GlobalObject.getJoypadAButton(var0)

def isJoypadLTPressed(var0):
  return LuaManager.GlobalObject.isJoypadLTPressed(var0)

def getJoypadXButton(var0):
  return LuaManager.GlobalObject.getJoypadXButton(var0)

def getSandboxPresets():
  return LuaManager.GlobalObject.getSandboxPresets()

def getModFileWriter(var0, var1, var2, var3):
  return LuaManager.GlobalObject.getModFileWriter(var0, var1, var2, var3)

def getFileReader(var0, var1):
  return LuaManager.GlobalObject.getFileReader(var0, var1)

def getControllerName(var0):
  return LuaManager.GlobalObject.getControllerName(var0)

def deletePlayerSave(var0):
  return LuaManager.GlobalObject.deletePlayerSave(var0)

def getControllerPovX(var0):
  return LuaManager.GlobalObject.getControllerPovX(var0)

def getGameTime():
  return LuaManager.GlobalObject.getGameTime()

def isJoypadDown(var0):
  return LuaManager.GlobalObject.isJoypadDown(var0)

def isJoypadRTPressed(var0):
  return LuaManager.GlobalObject.isJoypadRTPressed(var0)

def getMPStatus():
  return LuaManager.GlobalObject.getMPStatus()

def getControllerGUID(var0):
  return LuaManager.GlobalObject.getControllerGUID(var0)

def createStory(var0):
  return LuaManager.GlobalObject.createStory(var0)

def ZombRandBetween(var0, var2):
  return LuaManager.GlobalObject.ZombRandBetween(var0, var2)

def endTextFileInput():
  return LuaManager.GlobalObject.endTextFileInput()

def ZombRandFloat(var0, var1):
  return LuaManager.GlobalObject.ZombRandFloat(var0, var1)

def getGameFilesInput(var0):
  return LuaManager.GlobalObject.getGameFilesInput(var0)

@overload
def ZombRand(var0):
  return LuaManager.GlobalObject.ZombRand(var0)

@overload
def ZombRand(var0, var2):
  return LuaManager.GlobalObject.ZombRand(var0, var2)

def isJoypadRight(var0):
  return LuaManager.GlobalObject.isJoypadRight(var0)

def isJoypadRBPressed(var0):
  return LuaManager.GlobalObject.isJoypadRBPressed(var0)

def endFileOutput():
  return LuaManager.GlobalObject.endFileOutput()

def setPlayerMouse(var0):
  return LuaManager.GlobalObject.setPlayerMouse(var0)

def isJoypadLeft(var0):
  return LuaManager.GlobalObject.isJoypadLeft(var0)

def isSoundPlaying(var0):
  return LuaManager.GlobalObject.isSoundPlaying(var0)

def getFMODSoundBank():
  return LuaManager.GlobalObject.getFMODSoundBank()

def getFileWriter(var0, var1, var2):
  return LuaManager.GlobalObject.getFileWriter(var0, var1, var2)

def getJoypadRBumper(var0):
  return LuaManager.GlobalObject.getJoypadRBumper(var0)

def getClientUsername():
  return LuaManager.GlobalObject.getClientUsername()

def setPlayerJoypad(var0, var1, var2, var3):
  return LuaManager.GlobalObject.setPlayerJoypad(var0, var1, var2, var3)

def getJoypadLBumper(var0):
  return LuaManager.GlobalObject.getJoypadLBumper(var0)

def endFileInput():
  return LuaManager.GlobalObject.endFileInput()

def getJoypadYButton(var0):
  return LuaManager.GlobalObject.getJoypadYButton(var0)

def isJoypadUp(var0):
  return LuaManager.GlobalObject.isJoypadUp(var0)

def isJoypadLBPressed(var0):
  return LuaManager.GlobalObject.isJoypadLBPressed(var0)

def getFileInput(var0):
  return LuaManager.GlobalObject.getFileInput(var0)

def forceChangeState(var0):
  return LuaManager.GlobalObject.forceChangeState(var0)

def getDebugOptions():
  return LuaManager.GlobalObject.getDebugOptions()

def manipulateSavefile(var0, var1):
  return LuaManager.GlobalObject.manipulateSavefile(var0, var1)

def getCore():
  return LuaManager.GlobalObject.getCore()

def getLocalVarCount(var0):
  return LuaManager.GlobalObject.getLocalVarCount(var0)

def localVarName(var0, var1):
  return LuaManager.GlobalObject.localVarName(var0, var1)

def getLocalVarStack(var0, var1):
  return LuaManager.GlobalObject.getLocalVarStack(var0, var1)

def isSystemLinux():
  return LuaManager.GlobalObject.isSystemLinux()

def createTile(var0, var1):
  return LuaManager.GlobalObject.createTile(var0, var1)

def getNumClassFields(var0):
  return LuaManager.GlobalObject.getNumClassFields(var0)

def toggleModActive(var0, var1):
  return LuaManager.GlobalObject.toggleModActive(var0, var1)

def isShiftKeyDown():
  return LuaManager.GlobalObject.isShiftKeyDown()

def getClassField(var0, var1):
  return LuaManager.GlobalObject.getClassField(var0, var1)

def getCoroutineTop(var0):
  return LuaManager.GlobalObject.getCoroutineTop(var0)

def getClassFunction(var0, var1):
  return LuaManager.GlobalObject.getClassFunction(var0, var1)

def isCtrlKeyDown():
  return LuaManager.GlobalObject.isCtrlKeyDown()

def openUrl(var0):
  return LuaManager.GlobalObject.openUrl(var0)

def getActivatedMods():
  return LuaManager.GlobalObject.getActivatedMods()

def getLocalVarName(var0, var1):
  return LuaManager.GlobalObject.getLocalVarName(var0, var1)

def isAltKeyDown():
  return LuaManager.GlobalObject.isAltKeyDown()

def addVirtualZombie(var0, var1):
  return LuaManager.GlobalObject.addVirtualZombie(var0, var1)

def getMouseXScaled():
  return LuaManager.GlobalObject.getMouseXScaled()

def drawOverheadMap(var0, var1, var2, var3):
  return LuaManager.GlobalObject.drawOverheadMap(var0, var1, var2, var3)

def luaDebug():
  return LuaManager.GlobalObject.luaDebug()

def getGameSpeed():
  return LuaManager.GlobalObject.getGameSpeed()

def getLastPlayedDate(var0):
  return LuaManager.GlobalObject.getLastPlayedDate(var0)

def isoRegionsRenderer():
  return LuaManager.GlobalObject.isoRegionsRenderer()

def zpopSpawnNow(var0, var1):
  return LuaManager.GlobalObject.zpopSpawnNow(var0, var1)

def assaultPlayer():
  return LuaManager.GlobalObject.assaultPlayer()

def getClassFieldVal(var0, var1):
  return LuaManager.GlobalObject.getClassFieldVal(var0, var1)

def setMouseXY(var0, var1):
  return LuaManager.GlobalObject.setMouseXY(var0, var1)

def zpopNewRenderer():
  return LuaManager.GlobalObject.zpopNewRenderer()

def getSaveInfo(var0):
  return LuaManager.GlobalObject.getSaveInfo(var0)

def getDirectionTo(var0, var1):
  return LuaManager.GlobalObject.getDirectionTo(var0, var1)

def isMouseButtonDown(var0):
  return LuaManager.GlobalObject.isMouseButtonDown(var0)

def getMouseX():
  return LuaManager.GlobalObject.getMouseX()

def setGameSpeed(var0):
  return LuaManager.GlobalObject.setGameSpeed(var0)

def getMouseYScaled():
  return LuaManager.GlobalObject.getMouseYScaled()

def zpopClearZombies(var0, var1):
  return LuaManager.GlobalObject.zpopClearZombies(var0, var1)

def getMouseY():
  return LuaManager.GlobalObject.getMouseY()

def getSoundManager():
  return LuaManager.GlobalObject.getSoundManager()

def getMethodParameter(var0, var1):
  return LuaManager.GlobalObject.getMethodParameter(var0, var1)

def isAdmin():
  return LuaManager.GlobalObject.isAdmin()

def getGameClient():
  return LuaManager.GlobalObject.getGameClient()

def renameSavefile(var0, var1, var2):
  return LuaManager.GlobalObject.renameSavefile(var0, var1, var2)

def getZombieInfo(var0):
  return LuaManager.GlobalObject.getZombieInfo(var0)

def isXBOXController():
  return LuaManager.GlobalObject.isXBOXController()

def getTextManager():
  return LuaManager.GlobalObject.getTextManager()

def getServerModData():
  return LuaManager.GlobalObject.getServerModData()

def setAdmin():
  return LuaManager.GlobalObject.setAdmin()

def doKeyPress(var0):
  return LuaManager.GlobalObject.doKeyPress(var0)

def toggleSafetyServer(var0):
  return LuaManager.GlobalObject.toggleSafetyServer(var0)

def getHourMinute():
  return LuaManager.GlobalObject.getHourMinute()

def getEvolvedRecipes():
  return LuaManager.GlobalObject.getEvolvedRecipes()

def setSavefilePlayer1(var0, var1, var2):
  return LuaManager.GlobalObject.setSavefilePlayer1(var0, var1, var2)

def getPlayerInfo(var0):
  return LuaManager.GlobalObject.getPlayerInfo(var0)

def getVehicleInfo(var0):
  return LuaManager.GlobalObject.getVehicleInfo(var0)

def getItemText(var0):
  return LuaManager.GlobalObject.getItemText(var0)

def getOnlineUsername():
  return LuaManager.GlobalObject.getOnlineUsername()

def getMapInfo(var0):
  return LuaManager.GlobalObject.getMapInfo(var0)

def debugSetRoomType(var0):
  return LuaManager.GlobalObject.debugSetRoomType(var0)

def inviteFriend(var0):
  return LuaManager.GlobalObject.inviteFriend(var0)

def getUrlInputStream(var0):
  return LuaManager.GlobalObject.getUrlInputStream(var0)

def getSteamScoreboard():
  return LuaManager.GlobalObject.getSteamScoreboard()

def renderIsoCircle(var0, var1, var2, var3, var4, var5, var6, var7, var8):
  return LuaManager.GlobalObject.renderIsoCircle(var0, var1, var2, var3, var4, var5, var6, var7, var8)

def configureLighting(var0):
  return LuaManager.GlobalObject.configureLighting(var0)

def is64bit():
  return LuaManager.GlobalObject.is64bit()

def testHelicopter():
  return LuaManager.GlobalObject.testHelicopter()

def forceSnowCheck():
  return LuaManager.GlobalObject.forceSnowCheck()

def getTimestampMs():
  return LuaManager.GlobalObject.getTimestampMs()

def getFriendsList():
  return LuaManager.GlobalObject.getFriendsList()

def getZones(var0, var1, var2):
  return LuaManager.GlobalObject.getZones(var0, var1, var2)

def canInviteFriends():
  return LuaManager.GlobalObject.canInviteFriends()

def testSound():
  return LuaManager.GlobalObject.testSound()

def reloadEngineRPM():
  return LuaManager.GlobalObject.reloadEngineRPM()

def processSayMessage(var0):
  return LuaManager.GlobalObject.processSayMessage(var0)

def getVehicleById(var0):
  return LuaManager.GlobalObject.getVehicleById(var0)

def addCarCrash():
  return LuaManager.GlobalObject.addCarCrash()

def proceedPM(var0):
  return LuaManager.GlobalObject.proceedPM(var0)

def getClimateMoon():
  return LuaManager.GlobalObject.getClimateMoon()

def endHelicopter():
  return LuaManager.GlobalObject.endHelicopter()

def reloadVehicles():
  return LuaManager.GlobalObject.reloadVehicles()

def rainConfig(var0, var1):
  return LuaManager.GlobalObject.rainConfig(var0, var1)

def addZombiesEating(var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.addZombiesEating(var1, var2, var3, var4, var5)

def reloadSoundFiles():
  return LuaManager.GlobalObject.reloadSoundFiles()

def queueCharEvent(var0):
  return LuaManager.GlobalObject.queueCharEvent(var0)

def queueKeyEvent(var0):
  return LuaManager.GlobalObject.queueKeyEvent(var0)

def addZombieSitting(var1, var2, var3):
  return LuaManager.GlobalObject.addZombieSitting(var1, var2, var3)

def getTileOverlays():
  return LuaManager.GlobalObject.getTileOverlays()

def screenZoomIn():
  return LuaManager.GlobalObject.screenZoomIn()

def timSort(var0, var1):
  return LuaManager.GlobalObject.timSort(var0, var1)

def getAllBeardStyles():
  return LuaManager.GlobalObject.getAllBeardStyles()

def getAllOutfits(var0):
  return LuaManager.GlobalObject.getAllOutfits(var0)

def getIsoMarkers():
  return LuaManager.GlobalObject.getIsoMarkers()

def getAllVehicles():
  return LuaManager.GlobalObject.getAllVehicles()

def screenZoomOut():
  return LuaManager.GlobalObject.screenZoomOut()

def getAverageFPS():
  return LuaManager.GlobalObject.getAverageFPS()

def getSearchMode():
  return LuaManager.GlobalObject.getSearchMode()

def checkServerName(var1):
  return LuaManager.GlobalObject.checkServerName(var1)

def getErosion():
  return LuaManager.GlobalObject.getErosion()

def getWorldMarkers():
  return LuaManager.GlobalObject.getWorldMarkers()

def Render3DItem(var1, var2, var3, var4, var5, var6):
  return LuaManager.GlobalObject.Render3DItem(var1, var2, var3, var4, var5, var6)

def getAllHairStyles(var0):
  return LuaManager.GlobalObject.getAllHairStyles(var0)

def SyncXp(var1):
  return LuaManager.GlobalObject.SyncXp(var1)

def getServerStatistic():
  return LuaManager.GlobalObject.getServerStatistic()

def isClient():
  return LuaManager.GlobalObject.isClient()

def createRandomDeadBody(var0, var1):
  return LuaManager.GlobalObject.createRandomDeadBody(var0, var1)

def setShowPingInfo(var0):
  return LuaManager.GlobalObject.setShowPingInfo(var0)

def isShowServerInfo():
  return LuaManager.GlobalObject.isShowServerInfo()

def isShowPingInfo():
  return LuaManager.GlobalObject.isShowPingInfo()

def setShowServerInfo(var0):
  return LuaManager.GlobalObject.setShowServerInfo(var0)

def getSpriteManager(var0):
  return LuaManager.GlobalObject.getSpriteManager(var0)

def getVehicleZoneAt(var0, var1, var2):
  return LuaManager.GlobalObject.getVehicleZoneAt(var0, var1, var2)

def getLotDirectories():
  return LuaManager.GlobalObject.getLotDirectories()

def getPuddlesManager():
  return LuaManager.GlobalObject.getPuddlesManager()

def getClimateManager():
  return LuaManager.GlobalObject.getClimateManager()

def getServerOptions():
  return LuaManager.GlobalObject.getServerOptions()

def getSandboxOptions():
  return LuaManager.GlobalObject.getSandboxOptions()

def getScriptManager():
  return LuaManager.GlobalObject.getScriptManager()

def breakpoint():
  return LuaManager.GlobalObject.breakpoint()

def toInt(var0):
  return LuaManager.GlobalObject.toInt(var0)

def getWorld():
  return LuaManager.GlobalObject.getWorld()

def reloadModelsMatching(var0):
  return LuaManager.GlobalObject.reloadModelsMatching(var0)

def showAnimationViewer():
  return LuaManager.GlobalObject.showAnimationViewer()

def debugFullyStreamedIn(var0, var1):
  return LuaManager.GlobalObject.debugFullyStreamedIn(var0, var1)

def showAttachmentEditor():
  return LuaManager.GlobalObject.showAttachmentEditor()
def showGlobalObjectDebugger():
  return LuaManager.GlobalObject.showGlobalObjectDebugger()

def setModelMetaData(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.setModelMetaData(var0, var1, var2, var3, var4)

def getLastStandPlayersDirectory():
  return LuaManager.GlobalObject.getLastStandPlayersDirectory()

def getMapFoldersForMod(var0):
  return LuaManager.GlobalObject.getMapFoldersForMod(var0)

def getSteamWorkshopItemIDs():
  return LuaManager.GlobalObject.getSteamWorkshopItemIDs()

def getPlayerScreenWidth(var0):
  return LuaManager.GlobalObject.getPlayerScreenWidth(var0)

def getServerPasswordFromArgs():
  return LuaManager.GlobalObject.getServerPasswordFromArgs()

def spawnpointsExistsForMod(var0, var1):
  return LuaManager.GlobalObject.spawnpointsExistsForMod(var0, var1)

def getTranslatorCredits(var0):
  return LuaManager.GlobalObject.getTranslatorCredits(var0)

def getControllerAxisCount(var0):
  return LuaManager.GlobalObject.getControllerAxisCount(var0)

def getBehaviourDebugPlayer():
  return LuaManager.GlobalObject.getBehaviourDebugPlayer()

def hasDataReadBreakpoint(var0, var1):
  return LuaManager.GlobalObject.hasDataReadBreakpoint(var0, var1)

def isJoypadRightStickButtonPressed(var0):
  return LuaManager.GlobalObject.isJoypadRightStickButtonPressed(var0)

def getRadioTranslators(var0):
  return LuaManager.GlobalObject.getRadioTranslators(var0)

def getControllerDeadZone(var0, var1):
  return LuaManager.GlobalObject.getControllerDeadZone(var0, var1)

def getControllerAxisValue(var0, var1):
  return LuaManager.GlobalObject.getControllerAxisValue(var0, var1)

def getFullSaveDirectoryTable():
  return LuaManager.GlobalObject.getFullSaveDirectoryTable()

def getSaveDirectoryTable():
  return LuaManager.GlobalObject.getSaveDirectoryTable()

def isControllerConnected(var0):
  return LuaManager.GlobalObject.isControllerConnected(var0)

def reloadControllerConfigFiles():
  return LuaManager.GlobalObject.reloadControllerConfigFiles()

def getJoypadAimingAxisX(var0):
  return LuaManager.GlobalObject.getJoypadAimingAxisX(var0)

def getJoypadAimingAxisY(var0):
  return LuaManager.GlobalObject.getJoypadAimingAxisY(var0)

def getPlayerScreenHeight(var0):
  return LuaManager.GlobalObject.getPlayerScreenHeight(var0)

def checkSavePlayerExists():
  return LuaManager.GlobalObject.checkSavePlayerExists()

def loadStaticZomboidModel(var0, var1, var2):
  return LuaManager.GlobalObject.loadStaticZomboidModel(var0, var1, var2)

def createItemTransaction(var0, var1, var2):
  return LuaManager.GlobalObject.createItemTransaction(var0, var1, var2)

def transformIntoKahluaTable(var0):
  return LuaManager.GlobalObject.transformIntoKahluaTable(var0)

def checkSaveFolderExists(var0):
  return LuaManager.GlobalObject.checkSaveFolderExists(var0)

def getModDirectoryTable():
  return LuaManager.GlobalObject.getModDirectoryTable()

def createNewScriptItem(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.createNewScriptItem(var0, var1, var2, var3, var4)

def getLastStandPlayerFileNames():
  return LuaManager.GlobalObject.getLastStandPlayerFileNames()

def getJoypadMovementAxisX(var0):
  return LuaManager.GlobalObject.getJoypadMovementAxisX(var0)

def getPlayerScreenLeft(var0):
  return LuaManager.GlobalObject.getPlayerScreenLeft(var0)

def getNumActivePlayers():
  return LuaManager.GlobalObject.getNumActivePlayers()

def removeItemTransaction(var0, var1, var2):
  return LuaManager.GlobalObject.removeItemTransaction(var0, var1, var2)

def setPlayerMovementActive(var0, var1):
  return LuaManager.GlobalObject.setPlayerMovementActive(var0, var1)

def getMapDirectoryTable():
  return LuaManager.GlobalObject.getMapDirectoryTable()

def getWorldSoundManager():
  return LuaManager.GlobalObject.getWorldSoundManager()

def getMaxActivePlayers():
  return LuaManager.GlobalObject.getMaxActivePlayers()

def isCurrentExecutionPoint(var0, var1):
  return LuaManager.GlobalObject.isCurrentExecutionPoint(var0, var1)

def getAmbientStreamManager():
  return LuaManager.GlobalObject.getAmbientStreamManager()

def reloadServerLuaFile(var0):
  return LuaManager.GlobalObject.reloadServerLuaFile(var0)

def getServerAddressFromArgs():
  return LuaManager.GlobalObject.getServerAddressFromArgs()

def connectionManagerLog(var0, var1):
  return LuaManager.GlobalObject.connectionManagerLog(var0, var1)

def deleteSandboxPreset(var0):
  return LuaManager.GlobalObject.deleteSandboxPreset(var0)

def deleteAllGameModeSaves(var0):
  return LuaManager.GlobalObject.deleteAllGameModeSaves(var0)

def loadSkinnedZomboidModel(var0, var1, var2):
  return LuaManager.GlobalObject.loadSkinnedZomboidModel(var0, var1, var2)

def getAbsoluteSaveFolderName(var0):
  return LuaManager.GlobalObject.getAbsoluteSaveFolderName(var0)

def checkSaveFileExists(var0):
  return LuaManager.GlobalObject.checkSaveFileExists(var0)

def setControllerDeadZone(var0, var1, var2):
  return LuaManager.GlobalObject.setControllerDeadZone(var0, var1, var2)

def getControllerButtonCount(var0):
  return LuaManager.GlobalObject.getControllerButtonCount(var0)

def isJoypadLeftStickButtonPressed(var0):
  return LuaManager.GlobalObject.isJoypadLeftStickButtonPressed(var0)

def getSteamAvatarFromUsername(var0):
  return LuaManager.GlobalObject.getSteamAvatarFromUsername(var0)

def activateSteamOverlayToWebPage(var0):
  return LuaManager.GlobalObject.activateSteamOverlayToWebPage(var0)

def getSteamWorkshopStagedItems():
  return LuaManager.GlobalObject.getSteamWorkshopStagedItems()

def isSteamRunningOnSteamDeck():
  return LuaManager.GlobalObject.isSteamRunningOnSteamDeck()

def showSteamGamepadTextInput(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.showSteamGamepadTextInput(var0, var1, var2, var3, var4)

def getCoroutineObjStackWithBase(var0, var1):
  return LuaManager.GlobalObject.getCoroutineObjStackWithBase(var0, var1)

def useTextureFiltering(var0):
  return LuaManager.GlobalObject.useTextureFiltering(var0)

def showSteamFloatingGamepadTextInput(var0, var1, var2, var3, var4):
  return LuaManager.GlobalObject.showSteamFloatingGamepadTextInput(var0, var1, var2, var3, var4)

def sendPlayerStatsChange(var0):
  return LuaManager.GlobalObject.sendPlayerStatsChange(var0)

def querySteamWorkshopItemDetails(var0, var1, var2):
  return LuaManager.GlobalObject.querySteamWorkshopItemDetails(var0, var1, var2)

def connectToServerStateCallback(var0):
  return LuaManager.GlobalObject.connectToServerStateCallback(var0)

def getNumClassFunctions(var0):
  return LuaManager.GlobalObject.getNumClassFunctions(var0)

def getSteamWorkshopItemMods(var0):
  return LuaManager.GlobalObject.getSteamWorkshopItemMods(var0)

def getPublicServersList():
  return LuaManager.GlobalObject.getPublicServersList()

def getJoypadMovementAxisY(var0):
  return LuaManager.GlobalObject.getJoypadMovementAxisY(var0)

def getLuaDebuggerErrors():
  return LuaManager.GlobalObject.getLuaDebuggerErrors()

def getFirstLineOfClosure(var0):
  return LuaManager.GlobalObject.getFirstLineOfClosure(var0)

def isDesktopOpenSupported():
  return LuaManager.GlobalObject.isDesktopOpenSupported()

def getTextureFromSaveDir(var0, var1):
  return LuaManager.GlobalObject.getTextureFromSaveDir(var0, var1)

def getJoypadRightStickButton(var0):
  return LuaManager.GlobalObject.getJoypadRightStickButton(var0)

def activateJoypadOnSteamDeck():
  return LuaManager.GlobalObject.activateJoypadOnSteamDeck()

def getFilenameOfCallframe(var0):
  return LuaManager.GlobalObject.getFilenameOfCallframe(var0)

def showFolderInDesktop(var0):
  return LuaManager.GlobalObject.showFolderInDesktop(var0)

def getJoypadBackButton(var0):
  return LuaManager.GlobalObject.getJoypadBackButton(var0)

def getCoroutineCallframeStack(var0, var1):
  return LuaManager.GlobalObject.getCoroutineCallframeStack(var0, var1)

def getServerSavedWorldVersion(var0):
  return LuaManager.GlobalObject.getServerSavedWorldVersion(var0)

def getGametimeTimestamp():
  return LuaManager.GlobalObject.getGametimeTimestamp()

def activateSteamOverlayToWorkshopItem(var0):
  return LuaManager.GlobalObject.activateSteamOverlayToWorkshopItem(var0)

def activateSteamOverlayToWorkshopUser():
  return LuaManager.GlobalObject.activateSteamOverlayToWorkshopUser()

def reactivateJoypadAfterResetLua():
  return LuaManager.GlobalObject.reactivateJoypadAfterResetLua()

def getCurrentUserProfileName():
  return LuaManager.GlobalObject.getCurrentUserProfileName()

def getJoypadStartButton(var0):
  return LuaManager.GlobalObject.getJoypadStartButton(var0)

def getCoroutineObjStack(var0, var1):
  return LuaManager.GlobalObject.getCoroutineObjStack(var0, var1)

def getSandboxFileWriter(var0, var1, var2):
  return LuaManager.GlobalObject.getSandboxFileWriter(var0, var1, var2)

def getLuaDebuggerErrorCount():
  return LuaManager.GlobalObject.getLuaDebuggerErrorCount()

def getGameFilesTextInput(var0):
  return LuaManager.GlobalObject.getGameFilesTextInput(var0)

def isSteamOverlayEnabled():
  return LuaManager.GlobalObject.isSteamOverlayEnabled()

def activateSteamOverlayToWorkshop():
  return LuaManager.GlobalObject.activateSteamOverlayToWorkshop()

def getMethodParameterCount(var0):
  return LuaManager.GlobalObject.getMethodParameterCount(var0)

def getCurrentUserSteamID():
  return LuaManager.GlobalObject.getCurrentUserSteamID()

def getJoypadLeftStickButton(var0):
  return LuaManager.GlobalObject.getJoypadLeftStickButton(var0)

def setProgressBarValue(var0, var1):
  return LuaManager.GlobalObject.setProgressBarValue(var0, var1)

def getRecipeDisplayName(var0):
  return LuaManager.GlobalObject.getRecipeDisplayName(var0)

def getFilenameOfClosure(var0):
  return LuaManager.GlobalObject.getFilenameOfClosure(var0)

def zpopSpawnTimeToZero(var0, var1):
  return LuaManager.GlobalObject.zpopSpawnTimeToZero(var0, var1)

def canModifyPlayerScoreboard():
  return LuaManager.GlobalObject.canModifyPlayerScoreboard()

def getSteamProfileNameFromSteamID(var0):
  return LuaManager.GlobalObject.getSteamProfileNameFromSteamID(var0)

def getShortenedFilename(var0):
  return LuaManager.GlobalObject.getShortenedFilename(var0)

def doLuaDebuggerAction(var0):
  return LuaManager.GlobalObject.doLuaDebuggerAction(var0)

def getSteamAvatarFromSteamID(var0):
  return LuaManager.GlobalObject.getSteamAvatarFromSteamID(var0)

def getSteamIDFromUsername(var0):
  return LuaManager.GlobalObject.getSteamIDFromUsername(var0)

def getSteamProfileNameFromUsername(var0):
  return LuaManager.GlobalObject.getSteamProfileNameFromUsername(var0)

def isItemTransactionConsistent(var0, var1, var2):
  return LuaManager.GlobalObject.isItemTransactionConsistent(var0, var1, var2)

def proceedFactionMessage(var0):
  return LuaManager.GlobalObject.proceedFactionMessage(var0)

def addZombiesInBuilding(var1, var2, var3, var4, var5):
  return LuaManager.GlobalObject.addZombiesInBuilding(var1, var2, var3, var4, var5)

def processAdminChatMessage(var0):
  return LuaManager.GlobalObject.processAdminChatMessage(var0)

def addAllSmashedVehicles():
  return LuaManager.GlobalObject.addAllSmashedVehicles()

def steamReleaseInternetServersRequest():
  return LuaManager.GlobalObject.steamReleaseInternetServersRequest()

def getAllItemsForBodyLocation(var0):
  return LuaManager.GlobalObject.getAllItemsForBodyLocation(var0)

def toggleVehicleRenderToTexture():
  return LuaManager.GlobalObject.toggleVehicleRenderToTexture()

def checkPlayerCanUseChat(var0):
  return LuaManager.GlobalObject.checkPlayerCanUseChat(var0)

def getEditVehicleState():
  return LuaManager.GlobalObject.getEditVehicleState()

def addAllBurntVehicles():
  return LuaManager.GlobalObject.addAllBurntVehicles()

def processGeneralMessage(var0):
  return LuaManager.GlobalObject.processGeneralMessage(var0)

def attachTrailerToPlayerVehicle(var0):
  return LuaManager.GlobalObject.attachTrailerToPlayerVehicle(var0)

def getAttachmentEditorState():
  return LuaManager.GlobalObject.getAttachmentEditorState()

def processSafehouseMessage(var0):
  return LuaManager.GlobalObject.processSafehouseMessage(var0)

def showWrongChatTabMessage(var0, var1, var2):
  return LuaManager.GlobalObject.showWrongChatTabMessage(var0, var1, var2)

def useStaticErosionRand(var0):
  return LuaManager.GlobalObject.useStaticErosionRand(var0)

def getBeardStylesInstance():
  return LuaManager.GlobalObject.getBeardStylesInstance()

def steamRequestServerRules(var0, var1):
  return LuaManager.GlobalObject.steamRequestServerRules(var0, var1)

def steamRequestInternetServersList():
  return LuaManager.GlobalObject.steamRequestInternetServersList()

def isPublicServerListAllowed():
  return LuaManager.GlobalObject.isPublicServerListAllowed()

def steamGetInternetServersCount():
  return LuaManager.GlobalObject.steamGetInternetServersCount()

def getAnimationViewerState():
  return LuaManager.GlobalObject.getAnimationViewerState()

def checkModsNeedUpdate(var0):
  return LuaManager.GlobalObject.checkModsNeedUpdate(var0)

def addZombiesInOutfitArea(var1, var2, var3, var4, var5, var6, var7, var8):
  return LuaManager.GlobalObject.addZombiesInOutfitArea(var1, var2, var3, var4, var5, var6, var7, var8)

def steamGetInternetServerDetails(var0):
  return LuaManager.GlobalObject.steamGetInternetServerDetails(var0)

def reloadVehicleTextures(var0):
  return LuaManager.GlobalObject.reloadVehicleTextures(var0)

def getAllDecalNamesForItem(var0):
  return LuaManager.GlobalObject.getAllDecalNamesForItem(var0)

def getContainerOverlays():
  return LuaManager.GlobalObject.getContainerOverlays()

def steamRequestServerDetails(var0, var1):
  return LuaManager.GlobalObject.steamRequestServerDetails(var0, var1)

def getServerSettingsManager():
  return LuaManager.GlobalObject.getServerSettingsManager()

def processShoutMessage(var0):
  return LuaManager.GlobalObject.processShoutMessage(var0)

def getHairStylesInstance():
  return LuaManager.GlobalObject.getHairStylesInstance()

def isShowConnectionInfo():
  return LuaManager.GlobalObject.isShowConnectionInfo()

def setShowConnectionInfo(var0):
  return LuaManager.GlobalObject.setShowConnectionInfo(var0)

def wasMouseActiveMoreRecentlyThanJoypad():
  return LuaManager.GlobalObject.wasMouseActiveMoreRecentlyThanJoypad()

def translatePointXInOverheadMapToWindow(var0, var1, var2, var3):
  return LuaManager.GlobalObject.translatePointXInOverheadMapToWindow(var0, var1, var2, var3)

def translatePointYInOverheadMapToWindow(var0, var1, var2, var3):
  return LuaManager.GlobalObject.translatePointYInOverheadMapToWindow(var0, var1, var2, var3)

def translatePointXInOverheadMapToWorld(var0, var1, var2, var3):
  return LuaManager.GlobalObject.translatePointXInOverheadMapToWorld(var0, var1, var2, var3)

def translatePointYInOverheadMapToWorld(var0, var1, var2, var3):
  return LuaManager.GlobalObject.translatePointYInOverheadMapToWorld(var0, var1, var2, var3)

def getRenderer():
  return LuaManager.GlobalObject.getRenderer()

def showWorldMapEditor(var0):
  return LuaManager.GlobalObject.showWorldMapEditor(var0)

def showChunkDebugger():
  return LuaManager.GlobalObject.showChunkDebugger()

def showVehicleEditor(var0):
  return LuaManager.GlobalObject.showVehicleEditor(var0)

Events: Any
