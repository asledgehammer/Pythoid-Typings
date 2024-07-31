from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from com.jcraft.jogg import Packet
from java.io import InputStream
from java.lang import Exception

class Block:

  def clear(self) -> int: ...

  def init(self, arg0: DspState) -> None: ...

  def synthesis(self, arg0: Packet) -> int: ...

  @staticmethod
  def asdsadsa(arg0: str, arg1: list[int], arg2: int) -> str: ...

  def __init__(self, arg0: DspState): ...


class CodeBook:

  class DecodeAux: ...


class Comment:

  def add(self, arg0: str) -> None: ...

  def add_tag(self, arg0: str, arg1: str) -> None: ...

  def getComment(self, arg0: int) -> str: ...

  def getVendor(self) -> str: ...

  def header_out(self, arg0: Packet) -> int: ...

  def init(self) -> None: ...

  @overload
  def query(self, arg0: str) -> str: ...

  @overload
  def query(self, arg0: str, arg1: int) -> str: ...

  def toString(self) -> str: ...

  def __init__(self):
    self.comment_lengths: list[int]
    self.comments: int
    self.user_comments: list[list[int]]
    self.vendor: list[int]


class DspState:

  def clear(self) -> None: ...

  def synthesis_blockin(self, arg0: Block) -> int: ...

  def synthesis_init(self, arg0: Info) -> int: ...

  def synthesis_pcmout(self, arg0: list[list[list[float]]], arg1: list[int]) -> int: ...

  def synthesis_read(self, arg0: int) -> int: ...

  def __init__(self): ...


class FuncFloor:

  floor_P: list[FuncFloor]


class FuncMapping:

  mapping_P: list[FuncMapping]


class FuncResidue:

  residue_P: list[FuncResidue]


class FuncTime:

  time_P: list[FuncTime]


class Info:

  def blocksize(self, arg0: Packet) -> int: ...

  def clear(self) -> None: ...

  def init(self) -> None: ...

  def synthesis_headerin(self, arg0: Comment, arg1: Packet) -> int: ...

  def toString(self) -> str: ...

  def __init__(self):
    self.channels: int
    self.rate: int
    self.version: int


class InfoMode: ...


class JOrbisException(Exception):

  @overload
  def __init__(self): ...
  @overload
  def __init__(self, arg0: str): ...


class Mapping0(FuncMapping):

  ThiggleA: str

  ThiggleAQ: str

  ThiggleAQ2: str

  ThiggleAQQ2: str

  ThiggleB: str

  ThiggleBB: str

  ThiggleC: str

  ThiggleCC: str

  ThiggleD: str

  ThiggleDA: str

  ThiggleDB: str

  ThiggleE: str

  ThiggleEA: str

  ThiggleF: str

  ThiggleFA: str

  ThiggleG: str

  ThiggleGA: str

  ThiggleGB: str

  ThiggleGC: str

  def __init__(self): ...

  class LookMapping0: ...

  class InfoMapping0: ...


class PsyInfo: ...


class PsyLook: ...


class StaticCodeBook: ...


class VorbisFile:

  def bitrate(self, arg0: int) -> int: ...

  def bitrate_instant(self) -> int: ...

  def close(self) -> None: ...

  @overload
  def getComment(self) -> list[Comment]: ...

  @overload
  def getComment(self, arg0: int) -> Comment: ...

  @overload
  def getInfo(self) -> list[Info]: ...

  @overload
  def getInfo(self, arg0: int) -> Info: ...

  def pcm_seek(self, arg0: int) -> int: ...

  def pcm_tell(self) -> int: ...

  def pcm_total(self, arg0: int) -> int: ...

  def raw_seek(self, arg0: int) -> int: ...

  def raw_tell(self) -> int: ...

  def raw_total(self, arg0: int) -> int: ...

  def seekable(self) -> bool: ...

  def serialnumber(self, arg0: int) -> int: ...

  def streams(self) -> int: ...

  def time_tell(self) -> float: ...

  def time_total(self, arg0: int) -> float: ...

  @overload
  def __init__(self, arg0: str): ...
  @overload
  def __init__(self, arg0: InputStream, arg1: list[int], arg2: int): ...

  class SeekableInputStream(InputStream):

    def available(self) -> int: ...

    def close(self) -> None: ...

    def getLength(self) -> int: ...

    def mark(self, arg0: int) -> None: ...

    def markSupported(self) -> bool: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, arg0: list[int]) -> int: ...

    @overload
    def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...

    def reset(self) -> None: ...

    def seek(self, arg0: int) -> None: ...

    def skip(self, arg0: int) -> int: ...

    def tell(self) -> int: ...

