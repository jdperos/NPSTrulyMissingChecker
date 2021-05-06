import requests
import NPSTypes
import csv
from enum import IntEnum

############################################################################
# Constants
############################################################################

pspGamesTSVLink = "https://nopaystation.com/tsv/PSP_GAMES.tsv"
pspDLCTSVLink = "https://nopaystation.com/tsv/PSP_DLCS.tsv"

pendingPSPGamesTSVLink = "https://nopaystation.com/tsv/pending/PSP_GAMES.tsv"
pendingPSPDLCTSVLink = "https://nopaystation.com/tsv/pending/PSP_DLCS.tsv"

############################################################################
# Enums
############################################################################

class EConsoles(IntEnum):
    PSV = 0
    PSM = 1
    PSP = 2
    PS3 = 3
    PSX = 4

class EPSPGamesColumns(IntEnum):
    TITLE_ID = 0
    REGION = 1
    TYPE = 2
    NAME = 3
    PKG_DIRECT_LINK = 4
    CONTENT_ID = 5
    LAST_MOD = 6
    RAP	= 7
    DOWNLOAD_RAP = 8
    FILE_SIZE = 9
    SHA256 = 10

class EPSPDLCColumns(IntEnum):
    TITLE_ID = 0
    REGION = 1
    NAME = 2
    PKG_DIRECT_LINK = 3
    CONTENT_ID = 4
    LAST_MOD = 5
    RAP	= 6
    DOWNLOAD_RAP = 7
    FILE_SIZE = 8
    SHA256 = 9

############################################################################
# Function Definitions
############################################################################

def ConvertContentIDToLink(inContentID):
    # JP0117-NPJH00060_00-0948500100000000
    # UP0177-NPUH10036_00-FOOTBALLMANH2010
    newString = inContentID[0:6] + inContentID[7:16] + '_' + inContentID[17:19] + inContentID[20:36]
    newString = newString.lower()
    newString = f"https://www.jp.playstation.com/software/title/{newString}.html"
    return newString

def FindTrulyMissingPSPGames():
    #realboys
    approvedEntryDB = []
    url = pspGamesTSVLink
    text = requests.get(url).text
    lines = text.splitlines()
    tsv_reader = csv.reader(lines, delimiter='\t')

    line_count = 0
    for row in tsv_reader:
        if line_count == 0:
            line_count += 1
        else:
            newGame = NPSTypes.PSPGame(
                row[EPSPGamesColumns.TITLE_ID],
                row[EPSPGamesColumns.REGION],
                row[EPSPGamesColumns.TYPE],
                row[EPSPGamesColumns.NAME],
                row[EPSPGamesColumns.PKG_DIRECT_LINK],
                row[EPSPGamesColumns.CONTENT_ID],
                row[EPSPGamesColumns.LAST_MOD],
                row[EPSPGamesColumns.RAP],
                row[EPSPGamesColumns.DOWNLOAD_RAP],
                row[EPSPGamesColumns.FILE_SIZE],
                row[EPSPGamesColumns.SHA256]
            )
            approvedEntryDB.append(newGame)
            print(row)
            line_count += 1
    print(f'Processed {line_count} Games.')

    # pending
    pendingEntryDB = []
    url = pendingPSPGamesTSVLink
    text = requests.get(url).text
    lines = text.splitlines()
    tsv_reader = csv.reader(lines, delimiter='\t')

    line_count = 0
    for row in tsv_reader:
        if line_count == 0:
            line_count += 1
        else:
            newGame = NPSTypes.PSPGame(
                row[EPSPGamesColumns.TITLE_ID],
                row[EPSPGamesColumns.REGION],
                row[EPSPGamesColumns.TYPE],
                row[EPSPGamesColumns.NAME],
                row[EPSPGamesColumns.PKG_DIRECT_LINK],
                row[EPSPGamesColumns.CONTENT_ID],
                row[EPSPGamesColumns.LAST_MOD],
                row[EPSPGamesColumns.RAP],
                row[EPSPGamesColumns.DOWNLOAD_RAP],
                row[EPSPGamesColumns.FILE_SIZE],
                row[EPSPGamesColumns.SHA256]
            )
            approvedEntryDB.append(newGame)
            print(row)
            line_count += 1

    # find truly missing
    missingEntryDB = []
    for approveEntry in approvedEntryDB:
        bFound = False
        if approveEntry.pkgDirectLink == "MISSING":
            for pendingEntry in pendingEntryDB:
                if approveEntry == pendingEntry:
                    bFound = True
                    
            if not bFound:
                missingEntryDB.append(approveEntry)

    with open("truly_missing_PSP_GAMES.tsv", "w",encoding="utf-8", newline="") as csvfile:
        tsv_writer = csv.writer(csvfile, delimiter='\t')
        for entry in missingEntryDB:
            tsv_writer.writerow([
                entry.titleID,
                entry.region,
                entry.type,
                entry.name,
                entry.pkgDirectLink,
                entry.contentID,
                entry.lastMod,
                entry.rap,
                entry.downloadRAPfile,
                entry.fileSize,
                entry.sha256,
                ConvertContentIDToLink(entry.contentID)
            ])

def FindTrulyMissingPSPDLC():
    #realboys
    approvedEntryDB = []
    url = pspDLCTSVLink
    text = requests.get(url).text
    lines = text.splitlines()
    tsv_reader = csv.reader(lines, delimiter='\t')

    line_count = 0
    for row in tsv_reader:
        if line_count == 0:
            line_count += 1
        else:
            newGame = NPSTypes.PSPDLC(
                row[EPSPDLCColumns.TITLE_ID],
                row[EPSPDLCColumns.REGION],
                row[EPSPDLCColumns.NAME],
                row[EPSPDLCColumns.PKG_DIRECT_LINK],
                row[EPSPDLCColumns.CONTENT_ID],
                row[EPSPDLCColumns.LAST_MOD],
                row[EPSPDLCColumns.RAP],
                row[EPSPDLCColumns.DOWNLOAD_RAP],
                row[EPSPDLCColumns.FILE_SIZE],
                row[EPSPDLCColumns.SHA256]
            )
            approvedEntryDB.append(newGame)
            print(row)
            line_count += 1
    print(f'Processed {line_count} Games.')

    # pending
    pendingEntryDB = []
    url = pendingPSPDLCTSVLink
    text = requests.get(url).text
    lines = text.splitlines()
    tsv_reader = csv.reader(lines, delimiter='\t')

    line_count = 0
    for row in tsv_reader:
        if line_count == 0:
            line_count += 1
        else:
            newGame = NPSTypes.PSPDLC(
                row[EPSPDLCColumns.TITLE_ID],
                row[EPSPDLCColumns.REGION],
                row[EPSPDLCColumns.NAME],
                row[EPSPDLCColumns.PKG_DIRECT_LINK],
                row[EPSPDLCColumns.CONTENT_ID],
                row[EPSPDLCColumns.LAST_MOD],
                row[EPSPDLCColumns.RAP],
                row[EPSPDLCColumns.DOWNLOAD_RAP],
                row[EPSPDLCColumns.FILE_SIZE],
                row[EPSPDLCColumns.SHA256]
            )
            approvedEntryDB.append(newGame)
            print(row)
            line_count += 1

    # find truly missing
    missingEntryDB = []
    for approveEntry in approvedEntryDB:
        bFound = False
        if approveEntry.pkgDirectLink == "MISSING":
            for pendingEntry in pendingEntryDB:
                if approveEntry == pendingEntry:
                    bFound = True
                    
            if not bFound:
                missingEntryDB.append(approveEntry)

    with open("truly_missing_PSP_DLC.tsv", "w",encoding="utf-8", newline="") as csvfile:
        tsv_writer = csv.writer(csvfile, delimiter='\t')
        for entry in missingEntryDB:
            tsv_writer.writerow([
                entry.titleID,
                entry.region,
                entry.name,
                entry.pkgDirectLink,
                entry.contentID,
                entry.lastMod,
                entry.rap,
                entry.downloadRAPfile,
                entry.fileSize,
                entry.sha256
            ])

############################################################################
# Program entry point
############################################################################

FindTrulyMissingPSPGames()
FindTrulyMissingPSPDLC()