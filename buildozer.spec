[app]

# (str) Title of your application
title = MediCalc

# (str) Package name
package.name = medcalc

# (str) Package domain (needed for android/ios packaging)
package.domain = com.medcalc

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = bin, .buildozer

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# تم تثبيت الإصدارات لضمان نجاح البناء 100%
requirements = python3,kivy==2.3.0,kivymd==1.1.1,plyer,pillow

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = POST_NOTIFICATIONS,VIBRATE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 23b

# (list) Android application meta-data to set (key=value format)
android.meta_data =

# (list) Pattern to whitelist for the android application
android.whitelist =

# (str) Path to a custom whitelist file
android.whitelist_src =

# (str) Path to a custom blacklist file
android.blacklist_src =

# (list) List of Java .jar files to add to the libs
android.add_jars = 

# (list) List of Java files to add to the android project
android.add_src =

# (list) Android AAR archives to add
android.add_aars =

# (list) Put these files or directories in the apk res directory.
android.add_resources =

# (list) Gradle dependencies to add
android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) enables Android auto backup feature (Android 6.0+)
android.allow_backup = True

# (str) launch mode
android.launchMode = singleTask

# (list) All the architectures to build
android.archs = arm64-v8a, armeabi-v7a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate whether to enable the Android Splash Screen
android.private_storage = True

# (str) Android logcat filters
android.logcat_filters =

# (list) Android application meta-data to set (key=value format)
android.presplash_color = #FFFFFF

# (bool) Indicate whether to include the Android SDK license
# هذا السطر هو الذي يحل مشكلة توقف البناء
android.accept_sdk_license = True

#
# iOS specific
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

#
# Buildozer specific
#
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (default))
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
