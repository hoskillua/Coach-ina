# Coach-ina
A playing cards cross-platform application that coach you in your game and suggests the best move!

https://user-images.githubusercontent.com/56788883/154695744-95fc1fa8-c6bf-4388-b01b-248c7436c32b.mp4
> It currently sypports two games: Kings and Ground Similarity.


Detecting the Cards
---

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

mostafa@mostafawael:/media/mostafa/CUFE/CMP3/Image Processing/Project/Coach-ina$ 
> tree
```
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
│       ├── 1.jpeg
│       ├── 2.jpg
│       ├── 3.jpg
│       ├── 4.jpg
│       ├── AcetoFive.jpeg
│       ├── atef.jpg
│       ├── cards2.png
│       ├── cards3.jpeg
│       ├── cards4.jpg
│       ├── cards5.jpg
│       ├── cards6.jpg
│       ├── Cars46.png
│       ├── depositphotos_21549311-stock-photo-playing-cards-in-hand.jpg
│       ├── hand-cards-trump-spades.jpg
│       ├── istockphoto-496913440-170667a.jpg
│       ├── Skatblatt_02.jpg
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
```


