import xbmc, xbmcgui, xbmcvfs, zipfile, os
from urllib.request import urlretrieve

ADDON_NAME = "Davey Clan Wizard"

# Build ZIP URL inside repo
BUILD_URL = "https://github.com/DaveyClan/Davey-clan.github.io/releases/download/build/Daveyclan.zip"

TEMP_ZIP = "special://home/temp/daveyclan_build.zip"
KODI_HOME = "special://home/"

dialog = xbmcgui.Dialog()
if not dialog.yesno(ADDON_NAME,
                    "This will install the Davey Clan build.",
                    "Your current Kodi setup will be replaced.",
                    "",
                    "Cancel",
                    "Install"):
    exit()

xbmcgui.Dialog().notification(ADDON_NAME, "Downloading build...", xbmcgui.NOTIFICATION_INFO, 3000)
zip_path = xbmcvfs.translatePath(TEMP_ZIP)
kodi_path = xbmcvfs.translatePath(KODI_HOME)

# Ensure temp folder exists
os.makedirs(os.path.dirname(zip_path), exist_ok=True)

# Download build
urlretrieve(BUILD_URL, zip_path)

# Extract build
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(kodi_path)

# Clean up
os.remove(zip_path)

dialog.ok(ADDON_NAME, "Build installed successfully.", "Kodi will now close.")
xbmc.executebuiltin("Quit")
