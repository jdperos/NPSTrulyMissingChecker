#NPSTypes.py
class NPSEntry:
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256):
        self.titleID = inTitleID
        self.region = inRegion
        self.name = inName
        self.pkgDirectLink = inPKGDirectLink
        self.contentID = inContentID
        self.lastMod = inLastModification
        self.fileSize = inFileSize
        self.sha256 = inSHA256

    def PrintName(self):
        print(self.name)

    def GetRegionCode(self):
        if self.region == "ASIA":
            return "AS"
        else:
            return self.region

class PSVGame(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inzRIF, inContentID, inLastModification, inOriginalName, inFileSize, inSHA256, inReqFW, inAppVersion):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.zRIF = inzRIF
        self.originalName = inOriginalName
        self.reqFW = inReqFW
        self.appVersion = inAppVersion


class PSMGame(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inzRIF, inContentID, inLastModification, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.zRIF = inzRIF

class PSXGame(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inOriginalName, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.originalName = inOriginalName

class PS3Game(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inRAP, inContentID, inLastModification, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

class PSPGame(NPSEntry):
    def __init__(self, inTitleID, inRegion, inType, inName, inPKGDirectLink, inContentID, inLastModification, inRAP, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.type = inType
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

#################################################################################################

class PSVDemo(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inzRIF, inContentID, inLastModification, inOriginalName, inFileSize, inSHA256, inReqFW, inAppVersion):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.zRIF = inzRIF
        self.originalName = inOriginalName
        self.reqFW = inReqFW
        self.appVersion = inAppVersion

class PS3Demo(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inRAP, inContentID, inLastModification, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

#################################################################################################

class PSVDLC(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inzRIF, inContentID, inLastModification, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.zRIF = inzRIF
        
class PS3DLC(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inRAP, inContentID, inLastModification, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

class PSPDLC(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inRAP, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)    
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

#################################################################################################

class PSVUpdate(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inUpdateVersion, inReqFW, inPKGDirectLink, inLastModification, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, 0, inLastModification, inFileSize, inSHA256)
        self.updateVersion = inUpdateVersion
        self.reqFW = inReqFW


class PSPUpdate(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inRAP, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)    
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

#################################################################################################

class PSVTheme(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inzRIF, inContentID, inLastModification, inFileSize, inSHA256, inReqFW):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.zRIF = inzRIF
        self.reqFW = inReqFW

class PS3Theme(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inRAP, inContentID, inLastModification, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

class PS3Avatar(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inRAP, inContentID, inLastModification, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile

class PSPTheme(NPSEntry):
    def __init__(self, inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inRAP, inDownloadRAPFile, inFileSize, inSHA256):
        super().__init__(inTitleID, inRegion, inName, inPKGDirectLink, inContentID, inLastModification, inFileSize, inSHA256)    
        self.rap = inRAP
        self.downloadRAPfile = inDownloadRAPFile