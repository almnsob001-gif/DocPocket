[app]
title = MedCalc Hub
package.name = medcalchub
package.domain = org.medcalchub
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,plyer
orientation = portrait
fullscreen = 0
android.permissions = POST_NOTIFICATIONS,VIBRATE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
