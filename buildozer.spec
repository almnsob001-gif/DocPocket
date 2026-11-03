[app]
title = MediCalc
package.name = medcalc
package.domain = com.medcalc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0
requirements = python3,kivy==2.1.0,kivymd==1.1.1,plyer,pillow
orientation = portrait
fullscreen = 0
android.permissions = POST_NOTIFICATIONS,VIBRATE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
