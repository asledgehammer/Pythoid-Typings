from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.nio import FloatBuffer

class BestCandidateSampling:

  def __init__(self): ...

  class Cube:

    @overload
    def generate(self, arg0: list[float]) -> BestCandidateSampling.Cube: ...

    @overload
    def generate(self, arg0: FloatBuffer) -> BestCandidateSampling.Cube: ...

    @overload
    def generate(self, arg0: Callback3d) -> BestCandidateSampling.Cube: ...

    def numCandidates(self, arg0: int) -> BestCandidateSampling.Cube: ...

    def numSamples(self, arg0: int) -> BestCandidateSampling.Cube: ...

    def seed(self, arg0: int) -> BestCandidateSampling.Cube: ...

    def __init__(self): ...

  class Octree: ...

  class Quad:

    @overload
    def generate(self, arg0: list[float]) -> BestCandidateSampling.Quad: ...

    @overload
    def generate(self, arg0: FloatBuffer) -> BestCandidateSampling.Quad: ...

    @overload
    def generate(self, arg0: Callback2d) -> BestCandidateSampling.Quad: ...

    def numCandidates(self, arg0: int) -> BestCandidateSampling.Quad: ...

    def numSamples(self, arg0: int) -> BestCandidateSampling.Quad: ...

    def seed(self, arg0: int) -> BestCandidateSampling.Quad: ...

    def __init__(self): ...

  class Disk:

    @overload
    def generate(self, arg0: list[float]) -> BestCandidateSampling.Disk: ...

    @overload
    def generate(self, arg0: FloatBuffer) -> BestCandidateSampling.Disk: ...

    @overload
    def generate(self, arg0: Callback2d) -> BestCandidateSampling.Disk: ...

    def numCandidates(self, arg0: int) -> BestCandidateSampling.Disk: ...

    def numSamples(self, arg0: int) -> BestCandidateSampling.Disk: ...

    def seed(self, arg0: int) -> BestCandidateSampling.Disk: ...

    def __init__(self): ...

  class QuadTree: ...

  class Sphere:

    @overload
    def generate(self, arg0: list[float]) -> BestCandidateSampling.Sphere: ...

    @overload
    def generate(self, arg0: FloatBuffer) -> BestCandidateSampling.Sphere: ...

    @overload
    def generate(self, arg0: Callback3d) -> BestCandidateSampling.Sphere: ...

    def numCandidates(self, arg0: int) -> BestCandidateSampling.Sphere: ...

    def numSamples(self, arg0: int) -> BestCandidateSampling.Sphere: ...

    def onHemisphere(self, arg0: bool) -> BestCandidateSampling.Sphere: ...

    def seed(self, arg0: int) -> BestCandidateSampling.Sphere: ...

    def __init__(self): ...

    class Node: ...

  class IntHolder: ...


class Callback2d:

  def onNewSample(self, arg0: float, arg1: float) -> None: ...


class Callback3d:

  def onNewSample(self, arg0: float, arg1: float, arg2: float) -> None: ...


class Convolution:

  @staticmethod
  @overload
  def gaussianKernel(arg0: int, arg1: int, arg2: float, arg3: list[float]) -> None: ...

  @staticmethod
  @overload
  def gaussianKernel(arg0: int, arg1: int, arg2: float, arg3: FloatBuffer) -> None: ...

  def __init__(self): ...


class PoissonSampling:

  def __init__(self): ...

  class Disk:

    def __init__(self, arg0: int, arg1: float, arg2: float, arg3: int, arg4: Callback2d): ...


class SpiralSampling:

  @overload
  def createEquiAngle(self, arg0: float, arg1: int, arg2: int, arg3: Callback2d) -> None: ...

  @overload
  def createEquiAngle(self, arg0: float, arg1: int, arg2: int, arg3: float, arg4: Callback2d) -> None: ...

  def __init__(self, arg0: int): ...


class StratifiedSampling:

  def generateCentered(self, arg0: int, arg1: float, arg2: Callback2d) -> None: ...

  def generateRandom(self, arg0: int, arg1: Callback2d) -> None: ...

  def __init__(self, arg0: int): ...


class UniformSampling:

  def __init__(self): ...

  class Sphere:

    def generate(self, arg0: int, arg1: Callback3d) -> None: ...

    def __init__(self, arg0: int, arg1: int, arg2: Callback3d): ...

  class Disk:

    def __init__(self, arg0: int, arg1: int, arg2: Callback2d): ...
