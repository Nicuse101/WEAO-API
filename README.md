# WEAO-API
User-friendly library for handling WEAO (whatexpsare.online) API in Python

Installation (requires git & pip):
```
pip install git+https://github.com/Nicuse101/WEAO-API.git
```
Example Usage:
```py
from weao_api import WEAO
from weao_api import Platform

android_version = WEAO.fetch_roblox_version(Platform.ANDROID)
windows_version = WEAO.fetch_roblox_version(Platform.WINDOWS)

print(f"Windows version: {windows_version}\nReleased at: {windows_version.date}")
print(f"Android version: {android_version}\nReleased at: {android_version.date}")

executor = WEAO.fetch_exploit_status("Wave")
print(f"Executor: {executor.title}\nVersion: {executor.version}\nLast Updated: {executor.updatedDate}")
```
Output:
```
Windows version: version-bef193a8f3d14d3c
Released at: 3/19/2025, 4:46:38 PM UTC
Android version: 2.637.730
Released at: 8/12/2024, 4:19:54 PM
Executor: Wave
Version: v2.9.1a
Last Updated: 03/19/2025 at 6:59 PM UTC
```
