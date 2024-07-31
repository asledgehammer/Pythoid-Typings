from typing import Any, overload, TypeVar
from java.lang.annotation import Annotation
from java.io import OutputStream, InputStream

class ColorSpace:

  CS_CIEXYZ: int

  CS_GRAY: int

  CS_LINEAR_RGB: int

  CS_PYCC: int

  CS_sRGB: int

  TYPE_2CLR: int

  TYPE_3CLR: int

  TYPE_4CLR: int

  TYPE_5CLR: int

  TYPE_6CLR: int

  TYPE_7CLR: int

  TYPE_8CLR: int

  TYPE_9CLR: int

  TYPE_ACLR: int

  TYPE_BCLR: int

  TYPE_CCLR: int

  TYPE_CMY: int

  TYPE_CMYK: int

  TYPE_DCLR: int

  TYPE_ECLR: int

  TYPE_FCLR: int

  TYPE_GRAY: int

  TYPE_HLS: int

  TYPE_HSV: int

  TYPE_Lab: int

  TYPE_Luv: int

  TYPE_RGB: int

  TYPE_XYZ: int

  TYPE_YCbCr: int

  TYPE_Yxy: int

  def fromCIEXYZ(self, arg0: list[float]) -> list[float]: ...

  def fromRGB(self, arg0: list[float]) -> list[float]: ...

  def getMaxValue(self, arg0: int) -> float: ...

  def getMinValue(self, arg0: int) -> float: ...

  def getName(self, arg0: int) -> str: ...

  def getNumComponents(self) -> int: ...

  def getType(self) -> int: ...

  def isCS_sRGB(self) -> bool: ...

  def toCIEXYZ(self, arg0: list[float]) -> list[float]: ...

  def toRGB(self, arg0: list[float]) -> list[float]: ...

  @staticmethod
  def getInstance(arg0: int) -> ColorSpace: ...

  class BuiltInSpace:

    GRAY: ColorSpace

    LRGB: ColorSpace

    PYCC: ColorSpace

    SRGB: ColorSpace

    XYZ: ColorSpace


class ICC_ColorSpace(ColorSpace):

  def fromCIEXYZ(self, arg0: list[float]) -> list[float]: ...

  def fromRGB(self, arg0: list[float]) -> list[float]: ...

  def getMaxValue(self, arg0: int) -> float: ...

  def getMinValue(self, arg0: int) -> float: ...

  def getProfile(self) -> ICC_Profile: ...

  def toCIEXYZ(self, arg0: list[float]) -> list[float]: ...

  def toRGB(self, arg0: list[float]) -> list[float]: ...

  def __init__(self, arg0: ICC_Profile): ...


class ICC_Profile:

  CLASS_ABSTRACT: int

  CLASS_COLORSPACECONVERSION: int

  CLASS_DEVICELINK: int

  CLASS_DISPLAY: int

  CLASS_INPUT: int

  CLASS_NAMEDCOLOR: int

  CLASS_OUTPUT: int

  icAbsoluteColorimetric: int

  icCurveCount: int

  icCurveData: int

  icHdrAttributes: int

  icHdrCmmId: int

  icHdrColorSpace: int

  icHdrCreator: int

  icHdrDate: int

  icHdrDeviceClass: int

  icHdrFlags: int

  icHdrIlluminant: int

  icHdrMagic: int

  icHdrManufacturer: int

  icHdrModel: int

  icHdrPcs: int

  icHdrPlatform: int

  icHdrProfileID: int

  icHdrRenderingIntent: int

  icHdrSize: int

  icHdrVersion: int

  icICCAbsoluteColorimetric: int

  icMediaRelativeColorimetric: int

  icPerceptual: int

  icRelativeColorimetric: int

  icSaturation: int

  icSigAbstractClass: int

  icSigAToB0Tag: int

  icSigAToB1Tag: int

  icSigAToB2Tag: int

  icSigBlueColorantTag: int

  icSigBlueMatrixColumnTag: int

  icSigBlueTRCTag: int

  icSigBToA0Tag: int

  icSigBToA1Tag: int

  icSigBToA2Tag: int

  icSigCalibrationDateTimeTag: int

  icSigCharTargetTag: int

  icSigChromaticAdaptationTag: int

  icSigChromaticityTag: int

  icSigCmyData: int

  icSigCmykData: int

  icSigColorantOrderTag: int

  icSigColorantTableTag: int

  icSigColorSpaceClass: int

  icSigCopyrightTag: int

  icSigCrdInfoTag: int

  icSigDeviceMfgDescTag: int

  icSigDeviceModelDescTag: int

  icSigDeviceSettingsTag: int

  icSigDisplayClass: int

  icSigGamutTag: int

  icSigGrayData: int

  icSigGrayTRCTag: int

  icSigGreenColorantTag: int

  icSigGreenMatrixColumnTag: int

  icSigGreenTRCTag: int

  icSigHead: int

  icSigHlsData: int

  icSigHsvData: int

  icSigInputClass: int

  icSigLabData: int

  icSigLinkClass: int

  icSigLuminanceTag: int

  icSigLuvData: int

  icSigMeasurementTag: int

  icSigMediaBlackPointTag: int

  icSigMediaWhitePointTag: int

  icSigNamedColor2Tag: int

  icSigNamedColorClass: int

  icSigOutputClass: int

  icSigOutputResponseTag: int

  icSigPreview0Tag: int

  icSigPreview1Tag: int

  icSigPreview2Tag: int

  icSigProfileDescriptionTag: int

  icSigProfileSequenceDescTag: int

  icSigPs2CRD0Tag: int

  icSigPs2CRD1Tag: int

  icSigPs2CRD2Tag: int

  icSigPs2CRD3Tag: int

  icSigPs2CSATag: int

  icSigPs2RenderingIntentTag: int

  icSigRedColorantTag: int

  icSigRedMatrixColumnTag: int

  icSigRedTRCTag: int

  icSigRgbData: int

  icSigScreeningDescTag: int

  icSigScreeningTag: int

  icSigSpace2CLR: int

  icSigSpace3CLR: int

  icSigSpace4CLR: int

  icSigSpace5CLR: int

  icSigSpace6CLR: int

  icSigSpace7CLR: int

  icSigSpace8CLR: int

  icSigSpace9CLR: int

  icSigSpaceACLR: int

  icSigSpaceBCLR: int

  icSigSpaceCCLR: int

  icSigSpaceDCLR: int

  icSigSpaceECLR: int

  icSigSpaceFCLR: int

  icSigTechnologyTag: int

  icSigUcrBgTag: int

  icSigViewingCondDescTag: int

  icSigViewingConditionsTag: int

  icSigXYZData: int

  icSigYCbCrData: int

  icSigYxyData: int

  icTagReserved: int

  icTagType: int

  icXYZNumberX: int

  def getColorSpaceType(self) -> int: ...

  @overload
  def getData(self) -> list[int]: ...

  @overload
  def getData(self, arg0: int) -> list[int]: ...

  def getMajorVersion(self) -> int: ...

  def getMinorVersion(self) -> int: ...

  def getNumComponents(self) -> int: ...

  def getPCSType(self) -> int: ...

  def getProfileClass(self) -> int: ...

  def setData(self, arg0: int, arg1: list[int]) -> None: ...

  @overload
  def write(self, arg0: OutputStream) -> None: ...

  @overload
  def write(self, arg0: str) -> None: ...

  @staticmethod
  @overload
  def getInstance(arg0: list[int]) -> ICC_Profile: ...

  @staticmethod
  @overload
  def getInstance(arg0: int) -> ICC_Profile: ...

  @staticmethod
  @overload
  def getInstance(arg0: InputStream) -> ICC_Profile: ...

  @staticmethod
  @overload
  def getInstance(arg0: str) -> ICC_Profile: ...

  class BuiltInProfile:

    GRAY: ICC_Profile

    LRGB: ICC_Profile

    PYCC: ICC_Profile

    SRGB: ICC_Profile

    XYZ: ICC_Profile

