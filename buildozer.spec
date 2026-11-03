[app]
title = MedCalc Hub
package.name = medcalchub
package.domain = org.medcalchub
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy==2.1.0,kivymd==1.1.1,plyer,pillow
orientation = portrait
fullscreen = 0
android.permissions = POST_NOTIFICATIONS,VIBRATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.build_tools = 30.0.3
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
