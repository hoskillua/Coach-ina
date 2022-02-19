<h1 align="center">
  Coach-ina
</h1>
<p align="center">
  <a style="text-decoration:none" >
    <img src="https://img.shields.io/badge/Detection & Logic-Python-blue" alt="Parser Badge" />
  </a>
  <a style="text-decoration:none" >
    <img src="https://img.shields.io/badge/Frontend-Flutter-cyan" alt="Language Badge" />
  </a>
    <a style="text-decoration:none" >
    <img src="https://img.shields.io/badge/Backend-Flask-cyan" alt="Language Badge" />
  </a>
  <a style="text-decoration:none" >
    <img src="https://img.shields.io/badge/Container-Docker-green" alt="Simulation Tool Badge" />
  </a>
</p>
<hr/>

A playing cards cross-platform application that uses taken pictures of the cards by you, detects the cards, and coaches you in your game and suggests the best move!

## Some Examples

https://user-images.githubusercontent.com/56788883/154695744-95fc1fa8-c6bf-4388-b01b-248c7436c32b.mp4

> It currently sypports two games: Kings and Ground Similarity.

### Detecting the Cards

<div >
  <p  align="center">
    <img src="./Screenshots/testCase1.jpg">
    <img src="./Screenshots/testCase2.jpg">
  </p>
  </div>

## Installation of the requirements:

```
pip3 install -r requirements.txt
```

## Running the code:

```
python3 integration.py
```

# Description

## Project Structure

<details><summary> dataSet</summary><blockquote>
<br>image_change.py
    <details><summary>testData</summary><blockquote>
    <br>0.jpeg
    <br>-------
    <br>9.jpeg
    </blockquote></details>
    <details><summary>trainData</summary><blockquote>
        <details><summary>10</summary><blockquote>
        <br>10C0.jpg
        <br>---------
        <br>10S9.jpg
        </blockquote></details>
        <details><summary>2</summary><blockquote>
        <br>2C0.jpg
        <br>---------
        <br>2S9.jpg
        </blockquote></details>
        <details><summary>3</summary><blockquote>
        <br>3C0.jpg
        <br>---------
        <br>3S7.jpg
        </blockquote></details>
        <details><summary>4</summary><blockquote>
        <br>4C11.jpg
        <br>---------
        <br>4S9.jpg
        </blockquote></details>
        <details><summary>5</summary><blockquote>
        <br>5C0.jpg
        <br>---------
        <br>5S9.jpg
        </blockquote></details>
        <details><summary>6</summary><blockquote>
        <br>6C0.jpg
        <br>---------
        <br>7S9.jpg
        </blockquote></details>
        <details><summary>7</summary><blockquote>
|       |   |------------
        </blockquote></details>
        <details><summary>8</summary><blockquote>
        <br>8C0.jpg
        <br>---------
        <br>9S9.jpg
        </blockquote></details>
        <details><summary>A</summary><blockquote>
        <br>AC0.jpg
        <br>---------
        <br>QH7.jpg
        </blockquote></details>
        <details><summary>J</summary><blockquote>
        <br>JC0.jpg
        <br>---------
        <br>JS47.jpg
        </blockquote></details>
        <details><summary>K</summary><blockquote>
        <br>KC0.jpg
        <br>---------
        <br>KS9.jpg
        </blockquote></details>
        <details><summary>Q</summary><blockquote>
        <br>QC0.jpg
        <br>---------
        <br>QS9.jpg
        </blockquote></details>
        <details><summary>spade</summary><blockquote>
        <br>10S0.jpg
        <br>---------
        <br>QS9.jpg
        </blockquote></details>
    </blockquote></details>
</blockquote></details>
<details><summary> find-card.ipynb</summary><blockquote>
</blockquote></details>
<details><summary> frontend</summary><blockquote>
    <details><summary>coachina</summary><blockquote>
        <details><summary>coachina</summary><blockquote>
│           ├── analysis_options.yaml
│           ├── android
│           │   ├── app
│           │   │   ├── build.gradle
│           │   │   └── src
│           │   │       ├── debug
│           │   │       │   └── AndroidManifest.xml
│           │   │       ├── main
│           │   │       │   ├── AndroidManifest.xml
│           │   │       │   ├── kotlin
│           │   │       │   │   └── com
│           │   │       │   │       └── example
│           │   │       │   │           └── coachina
│           │   │       │   │               └── MainActivity.kt
│           │   │       │   └── res
│           │   │       │       ├── drawable
│           │   │       │       │   └── launch_background.xml
│           │   │       │       ├── drawable-v21
│           │   │       │       │   └── launch_background.xml
│           │   │       │       ├── mipmap-hdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-mdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xxhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xxxhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── values
│           │   │       │       │   └── styles.xml
│           │   │       │       └── values-night
│           │   │       │           └── styles.xml
│           │   │       └── profile
│           │   │           └── AndroidManifest.xml
│           │   ├── build.gradle
│           │   ├── gradle
│           │   │   └── wrapper
│           │   │       └── gradle-wrapper.properties
│           │   ├── gradle.properties
│           │   └── settings.gradle
│           ├── ios
│           │   ├── Flutter
│           │   │   ├── AppFrameworkInfo.plist
│           │   │   ├── Debug.xcconfig
│           │   │   └── Release.xcconfig
│           │   ├── Podfile
│           │   ├── Podfile.lock
│           │   ├── Runner
│           │   │   ├── AppDelegate.swift
│           │   │   ├── Assets.xcassets
│           │   │   │   ├── AppIcon.appiconset
│           │   │   │   │   ├── Contents.json
│           │   │   │   │   ├── Icon-App-1024x1024@1x.png
│           │   │   │   │   ├── -------------------------
│           │   │   │   │   ├── Icon-App-76x76@2x.png
│           │   │   │   │   └── Icon-App-83.5x83.5@2x.png
│           │   │   │   └── LaunchImage.imageset
│           │   │   │       ├── Contents.json
│           │   │   │       ├── LaunchImage@2x.png
│           │   │   │       ├── LaunchImage@3x.png
│           │   │   │       ├── LaunchImage.png
│           │   │   │       └── README.md
│           │   │   ├── Base.lproj
│           │   │   │   ├── LaunchScreen.storyboard
│           │   │   │   └── Main.storyboard
│           │   │   ├── Info.plist
│           │   │   └── Runner-Bridging-Header.h
│           │   ├── Runner.xcodeproj
│           │   │   ├── project.pbxproj
│           │   │   ├── project.xcworkspace
│           │   │   │   ├── contents.xcworkspacedata
│           │   │   │   └── xcshareddata
│           │   │   │       ├── IDEWorkspaceChecks.plist
│           │   │   │       └── WorkspaceSettings.xcsettings
│           │   │   └── xcshareddata
│           │   │       └── xcschemes
│           │   │           └── Runner.xcscheme
│           │   └── Runner.xcworkspace
│           │       ├── contents.xcworkspacedata
│           │       └── xcshareddata
│           │           ├── IDEWorkspaceChecks.plist
│           │           └── WorkspaceSettings.xcsettings
│           ├── lib
│           │   ├── generated_plugin_registrant.dart
│           │   ├── main.dart
│           │   └── src
│           │       └── logic
│           │           └── game_controller
│           │               └── game_controller.dart
│           ├── macos
│           │   ├── Flutter
│           │   │   ├── Flutter-Debug.xcconfig
│           │   │   ├── Flutter-Release.xcconfig
│           │   │   └── GeneratedPluginRegistrant.swift
│           │   ├── Podfile
│           │   ├── Runner
│           │   │   ├── AppDelegate.swift
│           │   │   ├── Assets.xcassets
│           │   │   │   └── AppIcon.appiconset
│           │   │   │       ├── app_icon_1024.png
│           │   │   │       ├── ------------------
│           │   │   │       └── Contents.json
│           │   │   ├── Base.lproj
│           │   │   │   └── MainMenu.xib
│           │   │   ├── Configs
│           │   │   │   ├── AppInfo.xcconfig
│           │   │   │   ├── Debug.xcconfig
│           │   │   │   ├── Release.xcconfig
│           │   │   │   └── Warnings.xcconfig
│           │   │   ├── DebugProfile.entitlements
│           │   │   ├── Info.plist
│           │   │   ├── MainFlutterWindow.swift
│           │   │   └── Release.entitlements
│           │   ├── Runner.xcodeproj
│           │   │   ├── project.pbxproj
│           │   │   ├── project.xcworkspace
│           │   │   │   └── xcshareddata
│           │   │   │       └── IDEWorkspaceChecks.plist
│           │   │   └── xcshareddata
│           │   │       └── xcschemes
│           │   │           └── Runner.xcscheme
│           │   └── Runner.xcworkspace
│           │       ├── contents.xcworkspacedata
│           │       └── xcshareddata
│           │           └── IDEWorkspaceChecks.plist
│           ├── pubspec.lock
│           ├── pubspec.yaml
│           ├── README.md
│           ├── test
│           │   └── widget_test.dart
│           └── web
│               ├── favicon.png
│               ├── icons
│               │   ├── Icon-192.png
│               │   ├── Icon-512.png
│               │   ├── Icon-maskable-192.png
│               │   └── Icon-maskable-512.png
│               ├── index.html
│               └── manifest.json
        </blockquote></details>
    </blockquote></details>
</blockquote></details>
<details><summary> Game Logic</summary><blockquote>
<br>HandGroundMatcher.py
<br>Kings.py
</blockquote></details>
<details><summary> Grouping</summary><blockquote>
<br>GroundRemoval.ipynb
    <details><summary>imgs</summary><blockquote>
│   │   ├── 0.jpg
│   |   |-----------
│   │   └── 9.jpg
    </blockquote></details>
    <details><summary>RandomImages</summary><blockquote>
│       ├── 1200px-7_playing_cards.jpg
|       |   --------------------------
│       └── st040.jpg
    </blockquote></details>
</blockquote></details>
<details><summary> integration.py</summary><blockquote>
</blockquote></details>
<details><summary> LICENSE</summary><blockquote>
</blockquote></details>
<details><summary> Model</summary><blockquote>
    <details><summary>dataSet</summary><blockquote>
        <details><summary>trainData</summary><blockquote>
│   │       ├── 10
│   │       │   ├── 10-10C0.jpg
│   |       |   -----------
│   │       │   └── 1.jpg
│   │       ├── 2
│   │       │   ├── 67.jpg
│   |       |   -----------
│   │       │   └── 78.jpg
│   │       ├── 3
│   │       │   ├── 68.jpg
│   │       │   └── 76.jpg
│   │       ├── 4
│   │       │   └── 75.jpg
│   │       ├── 5
│   │       │   ├── 77.jpg
│   |       |   -----------
│   │       │   └── 90.jpg
│   │       ├── 7
│   │       │   ├── 0.jpg
│   |       |   -----------
│   │       │   └── 9.jpg
│   │       ├── 9
│   │       │   ├── 131.jpg
│   |       |   -----------
│   │       │   └── 50.jpg
│   │       ├── A
│   │       │   ├── 109.jpg
│   |       |   -----------
│   │       │   └── 9.jpg
│   │       ├── club
│   │       │   ├── 101.jpg
│   |       |   -----------
│   │       │   └── 89.jpg
│   │       ├── diamond
│   │       │   ├── 106.jpg
│   |       |   -----------
│   │       │   └── 83.jpg
│   │       ├── heart
│   │       │   ├── 103.jpg
│   |       |   -----------
│   │       │   └── 95.jpg
│   │       ├── J
│   │       │   ├── 0.jpg
│   |       |   -----------
│   │       │   └── 96.jpg
│   │       ├── K
│   │       │   ├── 15.jpg
│   |       |   -----------
│   │       │   └── 97.jpg
│   │       ├── Q
│   │       │   ├── 13.jpg
│   |       |   -----------
│   │       │   └── 98.jpg
│   │       └── spade
│   │           ├── 117.jpg
│   |           -----------
│   │           └── 93.jpg
        </blockquote></details>
    </blockquote></details>
<br>dataSet.zip
<br>KNN_model.joblib
    <details><summary>Models</summary><blockquote>
│   │   ├── KNN_model.joblib
│   │   ├── rf_model.joblib
│   │   └── SVC_model.joblib
    </blockquote></details>
<br>modelTrain.py
</blockquote></details>
<details><summary> model.ipynb</summary><blockquote>
</blockquote></details>
<details><summary> __pycache__</summary><blockquote>
<br>integration.cpython-39.pyc
<br>utilities.cpython-39.pyc
</blockquote></details>
<details><summary> README.md</summary><blockquote>
</blockquote></details>
<details><summary> requirments.txt</summary><blockquote>
</blockquote></details>
<details><summary> Screenshots</summary><blockquote>
<br>testCase1.jpg
<br>testCase2.jpg
</blockquote></details>
<details><summary> server</summary><blockquote>
<br>app.py
<br>Dockerfile
<br>model.joblib
<br>model.py
<br>req.txt
<br>requirments.txt
<br>rf_model.joblib
    <details><summary>server_files</summary><blockquote>
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   ├── model.py
│   │   ├── requirments.txt
│   │   └── rf_model.joblib
    </blockquote></details>
<br>SVC_model.joblib
</blockquote></details>
<details><summary> TestCases</summary><blockquote>
    <details><summary>NonOverLapping</summary><blockquote>
│   │   ├── 10.jpeg
│       -----------
│   │   └── 9.jpeg
    </blockquote></details>
    <details><summary>OverLapping</summary><blockquote>
│       ├── 10.jpeg
│       -----------
│       ├── 8.jpeg
│       └── 9.jpeg
    </blockquote></details>
</blockquote></details>
<details><summary> utilities.py</summary><blockquote>
</blockquote></details>

.
├── dataSet
│   ├── image_change.py
│   ├── testData
│   │   ├── 0.jpeg
│   │   ├── -------
│   │   └── 9.jpeg
│   └── trainData
│       ├── 10
│       │   ├── 10C0.jpg
|       |   |------------
│       │   └── 10S9.jpg
│       ├── 2
│       │   ├── 2C0.jpg
|       |   |------------
│       │   └── 2S9.jpg
│       ├── 3
│       │   ├── 3C0.jpg
|       |   |------------
│       │   └── 3S7.jpg
│       ├── 4
│       │   ├── 4C11.jpg
|       |   |------------
│       │   └── 4S9.jpg
│       ├── 5
│       │   ├── 5C0.jpg
|       |   |------------
│       │   └── 5S9.jpg
│       ├── 6
│       │   ├── 6C0.jpg
|       |   |------------
│       │   └── 7S9.jpg
│       ├── 7
|       |   |------------
│       ├── 8
│       │   ├── 8C0.jpg
|       |   |------------
│       │   └── 9S9.jpg
│       ├── A
│       │   ├── AC0.jpg
|       |   |------------
│       │   └── QH7.jpg
│       ├── J
│       │   ├── JC0.jpg
|       |   |------------
│       │   └── JS47.jpg
│       ├── K
│       │   ├── KC0.jpg
|       |   |------------
│       │   └── KS9.jpg
│       ├── Q
│       │   ├── QC0.jpg
|       |   |------------
│       │   └── QS9.jpg
│       └── spade
│           ├── 10S0.jpg
|           |------------
│           └── QS9.jpg
├── find-card.ipynb
├── frontend
│   └── coachina
│       └── coachina
│           ├── analysis_options.yaml
│           ├── android
│           │   ├── app
│           │   │   ├── build.gradle
│           │   │   └── src
│           │   │       ├── debug
│           │   │       │   └── AndroidManifest.xml
│           │   │       ├── main
│           │   │       │   ├── AndroidManifest.xml
│           │   │       │   ├── kotlin
│           │   │       │   │   └── com
│           │   │       │   │       └── example
│           │   │       │   │           └── coachina
│           │   │       │   │               └── MainActivity.kt
│           │   │       │   └── res
│           │   │       │       ├── drawable
│           │   │       │       │   └── launch_background.xml
│           │   │       │       ├── drawable-v21
│           │   │       │       │   └── launch_background.xml
│           │   │       │       ├── mipmap-hdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-mdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xxhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── mipmap-xxxhdpi
│           │   │       │       │   └── ic_launcher.png
│           │   │       │       ├── values
│           │   │       │       │   └── styles.xml
│           │   │       │       └── values-night
│           │   │       │           └── styles.xml
│           │   │       └── profile
│           │   │           └── AndroidManifest.xml
│           │   ├── build.gradle
│           │   ├── gradle
│           │   │   └── wrapper
│           │   │       └── gradle-wrapper.properties
│           │   ├── gradle.properties
│           │   └── settings.gradle
│           ├── ios
│           │   ├── Flutter
│           │   │   ├── AppFrameworkInfo.plist
│           │   │   ├── Debug.xcconfig
│           │   │   └── Release.xcconfig
│           │   ├── Podfile
│           │   ├── Podfile.lock
│           │   ├── Runner
│           │   │   ├── AppDelegate.swift
│           │   │   ├── Assets.xcassets
│           │   │   │   ├── AppIcon.appiconset
│           │   │   │   │   ├── Contents.json
│           │   │   │   │   ├── Icon-App-1024x1024@1x.png
│           │   │   │   │   ├── -------------------------
│           │   │   │   │   ├── Icon-App-76x76@2x.png
│           │   │   │   │   └── Icon-App-83.5x83.5@2x.png
│           │   │   │   └── LaunchImage.imageset
│           │   │   │       ├── Contents.json
│           │   │   │       ├── LaunchImage@2x.png
│           │   │   │       ├── LaunchImage@3x.png
│           │   │   │       ├── LaunchImage.png
│           │   │   │       └── README.md
│           │   │   ├── Base.lproj
│           │   │   │   ├── LaunchScreen.storyboard
│           │   │   │   └── Main.storyboard
│           │   │   ├── Info.plist
│           │   │   └── Runner-Bridging-Header.h
│           │   ├── Runner.xcodeproj
│           │   │   ├── project.pbxproj
│           │   │   ├── project.xcworkspace
│           │   │   │   ├── contents.xcworkspacedata
│           │   │   │   └── xcshareddata
│           │   │   │       ├── IDEWorkspaceChecks.plist
│           │   │   │       └── WorkspaceSettings.xcsettings
│           │   │   └── xcshareddata
│           │   │       └── xcschemes
│           │   │           └── Runner.xcscheme
│           │   └── Runner.xcworkspace
│           │       ├── contents.xcworkspacedata
│           │       └── xcshareddata
│           │           ├── IDEWorkspaceChecks.plist
│           │           └── WorkspaceSettings.xcsettings
│           ├── lib
│           │   ├── generated_plugin_registrant.dart
│           │   ├── main.dart
│           │   └── src
│           │       └── logic
│           │           └── game_controller
│           │               └── game_controller.dart
│           ├── macos
│           │   ├── Flutter
│           │   │   ├── Flutter-Debug.xcconfig
│           │   │   ├── Flutter-Release.xcconfig
│           │   │   └── GeneratedPluginRegistrant.swift
│           │   ├── Podfile
│           │   ├── Runner
│           │   │   ├── AppDelegate.swift
│           │   │   ├── Assets.xcassets
│           │   │   │   └── AppIcon.appiconset
│           │   │   │       ├── app_icon_1024.png
│           │   │   │       ├── ------------------
│           │   │   │       └── Contents.json
│           │   │   ├── Base.lproj
│           │   │   │   └── MainMenu.xib
│           │   │   ├── Configs
│           │   │   │   ├── AppInfo.xcconfig
│           │   │   │   ├── Debug.xcconfig
│           │   │   │   ├── Release.xcconfig
│           │   │   │   └── Warnings.xcconfig
│           │   │   ├── DebugProfile.entitlements
│           │   │   ├── Info.plist
│           │   │   ├── MainFlutterWindow.swift
│           │   │   └── Release.entitlements
│           │   ├── Runner.xcodeproj
│           │   │   ├── project.pbxproj
│           │   │   ├── project.xcworkspace
│           │   │   │   └── xcshareddata
│           │   │   │       └── IDEWorkspaceChecks.plist
│           │   │   └── xcshareddata
│           │   │       └── xcschemes
│           │   │           └── Runner.xcscheme
│           │   └── Runner.xcworkspace
│           │       ├── contents.xcworkspacedata
│           │       └── xcshareddata
│           │           └── IDEWorkspaceChecks.plist
│           ├── pubspec.lock
│           ├── pubspec.yaml
│           ├── README.md
│           ├── test
│           │   └── widget_test.dart
│           └── web
│               ├── favicon.png
│               ├── icons
│               │   ├── Icon-192.png
│               │   ├── Icon-512.png
│               │   ├── Icon-maskable-192.png
│               │   └── Icon-maskable-512.png
│               ├── index.html
│               └── manifest.json
├── Game Logic
│   ├── HandGroundMatcher.py
│   └── Kings.py
├── Grouping
│   ├── GroundRemoval.ipynb
│   ├── imgs
│   │   ├── 0.jpg
│   |   |-----------
│   │   └── 9.jpg
│   └── RandomImages
│       ├── 1200px-7_playing_cards.jpg
|       |   --------------------------
│       └── st040.jpg
├── integration.py
├── LICENSE
├── Model
│   ├── dataSet
│   │   └── trainData
│   │       ├── 10
│   │       │   ├── 10-10C0.jpg
│   |       |   -----------
│   │       │   └── 1.jpg
│   │       ├── 2
│   │       │   ├── 67.jpg
│   |       |   -----------
│   │       │   └── 78.jpg
│   │       ├── 3
│   │       │   ├── 68.jpg
│   │       │   └── 76.jpg
│   │       ├── 4
│   │       │   └── 75.jpg
│   │       ├── 5
│   │       │   ├── 77.jpg
│   |       |   -----------
│   │       │   └── 90.jpg
│   │       ├── 7
│   │       │   ├── 0.jpg
│   |       |   -----------
│   │       │   └── 9.jpg
│   │       ├── 9
│   │       │   ├── 131.jpg
│   |       |   -----------
│   │       │   └── 50.jpg
│   │       ├── A
│   │       │   ├── 109.jpg
│   |       |   -----------
│   │       │   └── 9.jpg
│   │       ├── club
│   │       │   ├── 101.jpg
│   |       |   -----------
│   │       │   └── 89.jpg
│   │       ├── diamond
│   │       │   ├── 106.jpg
│   |       |   -----------
│   │       │   └── 83.jpg
│   │       ├── heart
│   │       │   ├── 103.jpg
│   |       |   -----------
│   │       │   └── 95.jpg
│   │       ├── J
│   │       │   ├── 0.jpg
│   |       |   -----------
│   │       │   └── 96.jpg
│   │       ├── K
│   │       │   ├── 15.jpg
│   |       |   -----------
│   │       │   └── 97.jpg
│   │       ├── Q
│   │       │   ├── 13.jpg
│   |       |   -----------
│   │       │   └── 98.jpg
│   │       └── spade
│   │           ├── 117.jpg
│   |           -----------
│   │           └── 93.jpg
│   ├── dataSet.zip
│   ├── KNN_model.joblib
│   ├── Models
│   │   ├── KNN_model.joblib
│   │   ├── rf_model.joblib
│   │   └── SVC_model.joblib
│   └── modelTrain.py
├── model.ipynb
├── __pycache__
│   ├── integration.cpython-39.pyc
│   └── utilities.cpython-39.pyc
├── README.md
├── requirments.txt
├── Screenshots
│   ├── testCase1.jpg
│   └── testCase2.jpg
├── server
│   ├── app.py
│   ├── Dockerfile
│   ├── model.joblib
│   ├── model.py
│   ├── req.txt
│   ├── requirments.txt
│   ├── rf_model.joblib
│   ├── server_files
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   ├── model.py
│   │   ├── requirments.txt
│   │   └── rf_model.joblib
│   └── SVC_model.joblib
├── TestCases
│   ├── NonOverLapping
│   │   ├── 10.jpeg
│       -----------
│   │   └── 9.jpeg
│   └── OverLapping
│       ├── 10.jpeg
│       -----------
│       ├── 8.jpeg
│       └── 9.jpeg
└── utilities.py

110 directories, 4764 files

## Papers references

1- Hands on Machine Learning with Scikit-learn, keras, and tensorflow textbook, Chapter 5 Support Vector Machines.

2- Single-image Background Removal with Entropy Filtering Paper.

3- G. Kumar and P. K. Bhatia, "A Detailed Review of Feature Extraction in Image Processing Systems," 2014 Fourth International Conference on Advanced Computing & Communication Technologies, 2014, pp. 5-12, doi: 10.1109/ACCT.2014.74.
