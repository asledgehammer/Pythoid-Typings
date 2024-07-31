from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import File, InputStream
from java.net import URL
from javax.sound.sampled import AudioFileFormat, AudioInputStream

class AudioFileReader:

  @overload
  def getAudioFileFormat(self, arg0: File) -> AudioFileFormat: ...

  @overload
  def getAudioFileFormat(self, arg0: InputStream) -> AudioFileFormat: ...

  @overload
  def getAudioFileFormat(self, arg0: URL) -> AudioFileFormat: ...

  @overload
  def getAudioInputStream(self, arg0: File) -> AudioInputStream: ...

  @overload
  def getAudioInputStream(self, arg0: InputStream) -> AudioInputStream: ...

  @overload
  def getAudioInputStream(self, arg0: URL) -> AudioInputStream: ...

