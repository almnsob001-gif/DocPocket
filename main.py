import os
import json
from datetime import datetime
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import StringProperty, ColorProperty, NumericProperty
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDCheckbox

try:
    from kivymd.uix.picker import MDTimePicker
except ImportError:
    try:
        from kivymd.uix.pickers import MDTimePicker
    except ImportError:
        MDTimePicker = None

try:
    from plyer import notification
    PLYER_OK = True
except ImportError:
    PLYER_OK = False

KV = r"""
#:import dp kivy.metrics.dp

<GetStartedScreen>:
    name: "get_started"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(24)
        spacing: dp(8)
        Widget: size_hint_y: 0.1
        AnchorLayout:
            anchor_x: "center"
            size_hint_y: 0.2
            MDIcon:
                icon: "medical-bag"
                font_size: dp(90)
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                halign: "center"
        MDLabel:
            text: "MediCalc"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Primary"
            size_hint_y: None
            height: dp(50)
        MDLabel:
            text: "Your personal medical companion"
            halign: "center"
            font_style: "Subtitle1"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: dp(30)
        Widget: size_hint_y: 0.3
        MDRaisedButton:
            text: "GET STARTED"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
            height: dp(50)
            font_size: dp(16)
            on_release: root.go_next()
        Widget: size_hint_y: 0.05

<DisclaimerScreen>:
    name: "disclaimer"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Disclaimer"
            elevation: 8
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                MDIcon:
                    icon: "alert-circle"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.accent_color
                    font_size: dp(60)
                    halign: "center"
                    size_hint_y: None
                    height: dp(60)
                MDLabel:
                    id: disclaimer_text
                    halign: "left"
                    valign: "top"
                    text_size: self.width - dp(40), None
                    size_hint_y: None
                    height: self.texture_size[1]
                    font_style: "Body1"
                    theme_text_color: "Secondary"
        MDBoxLayout:
            padding: dp(20)
            size_hint_y: None
            height: dp(70)
            MDRaisedButton:
                text: "I AGREE AND CONTINUE"
                size_hint_x: 1
                on_release: root.go_next()

<HomeScreen>:
    name: "home"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "MediCalc"
            elevation: 8
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(16)
                spacing: dp(12)
                size_hint_y: None
                height: self.minimum_height
                FeatureCard:
                    route: "bmi"
                    icon: "calculator-variant"
                    title: "BMI Calculator"
                    subtitle: "Calculate your Body Mass Index"
                    color: [0.36, 0.21, 0.69, 1]
                    on_release: app.go_screen(self.route)
                FeatureCard:
                    route: "bp"
                    icon: "heart-pulse"
                    title: "Blood Pressure Log"
                    subtitle: "Record and track readings"
                    color: [0.90, 0.22, 0.21, 1]
                    on_release: app.go_screen(self.route)
                FeatureCard:
                    route: "sugar"
                    icon: "water"
                    title: "Blood Sugar Log"
                    subtitle: "Track glucose readings"
                    color: [0.13, 0.59, 0.95, 1]
                    on_release: app.go_screen(self.route)
                FeatureCard:
                    route: "meds"
                    icon: "pill"
                    title: "Medication Reminder"
                    subtitle: "Never miss a dose again"
                    color: [0.26, 0.63, 0.28, 1]
                    on_release: app.go_screen(self.route)
                FeatureCard:
                    route: "calories"
                    icon: "fire"
                    title: "Calorie Calculator"
                    subtitle: "Track daily caloric needs"
                    color: [0.98, 0.55, 0.0, 1]
                    on_release: app.go_screen(self.route)

<FeatureCard>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(85)
    padding: dp(10)
    spacing: dp(10)
    radius: [dp(15)]
    elevation: 2
    ripple_behavior: True
    AnchorLayout:
        size_hint: None, None
        size: dp(55), dp(55)
        anchor_x: "center"
        anchor_y: "center"
        canvas.before:
            Color:
                rgba: root.color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(15)]
        MDIcon:
            icon: root.icon
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_size: dp(26)
    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"center_y": 0.5}
        MDLabel:
            text: root.title
            font_style: "Subtitle1"
            bold: True
            theme_text_color: "Primary"
            size_hint_y: None
            height: dp(24)
        MDLabel:
            text: root.subtitle
            font_style: "Caption"
            theme_text_color: "Secondary"
            size_hint_y: None
            height: dp(20)
    MDIcon:
        icon: "chevron-right"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.5}

<BMIScreen>:
    name: "bmi"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "BMI Calculator"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            elevation: 8
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                MDTextField:
                    id: height_field
                    hint_text: "Height (cm)"
                    input_filter: "float"
                    mode: "rectangle"
                MDTextField:
                    id: weight_field
                    hint_text: "Weight (kg)"
                    input_filter: "float"
                    mode: "rectangle"
                MDRaisedButton:
                    text: "CALCULATE"
                    size_hint_x: 1
                    on_release: root.calculate()
                MDCard:
                    id: result_card
                    orientation: "vertical"
                    padding: dp(15)
                    spacing: dp(5)
                    size_hint_y: None
                    height: dp(170)
                    radius: [dp(15)]
                    elevation: 2
                    opacity: 0
                    MDLabel:
                        id: bmi_value
                        text: "--"
                        halign: "center"
                        font_style: "H2"
                    MDLabel:
                        id: bmi_category
                        text: ""
                        halign: "center"
                        font_style: "H6"
                    MDLabel:
                        id: bmi_advice
                        text: ""
                        halign: "center"
                        font_style: "Body2"
                        text_size: self.width - dp(20), None

<BPScreen>:
    name: "bp"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Blood Pressure"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            elevation: 8
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(10)
            MDBoxLayout:
                spacing: dp(10)
                MDTextField:
                    id: sys_field
                    hint_text: "Systolic"
                    input_filter: "int"
                    mode: "rectangle"
                MDTextField:
                    id: dia_field
                    hint_text: "Diastolic"
                    input_filter: "int"
                    mode: "rectangle"
            MDRaisedButton:
                text: "SAVE READING"
                size_hint_x: 1
                on_release: root.save_reading()
        ScrollView:
            MDBoxLayout:
                id: readings_list
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

<BPReadingItem>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(70)
    padding: dp(10)
    radius: [dp(10)]
    elevation: 1
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: root.reading_text
            font_style: "Subtitle1"
            theme_text_color: "Custom"
            text_color: root.cat_color
        MDLabel:
            text: root.date_text
            font_style: "Caption"
    MDIconButton:
        icon: "trash-can-outline"
        on_release: root.delete_me()

<SugarScreen>:
    name: "sugar"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Blood Sugar"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            elevation: 8
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(10)
            MDBoxLayout:
                spacing: dp(10)
                MDTextField:
                    id: glucose_field
                    hint_text: "Glucose (mg/dL)"
                    input_filter: "float"
                    mode: "rectangle"
                MDRaisedButton:
                    text: root.selected_type
                    on_release: root.open_type_menu(self)
            MDRaisedButton:
                text: "SAVE READING"
                size_hint_x: 1
                on_release: root.save_reading()
        ScrollView:
            MDBoxLayout:
                id: sugar_list
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

<SugarItem>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(70)
    padding: dp(10)
    radius: [dp(10)]
    elevation: 1
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: root.reading_text
            font_style: "Subtitle1"
            theme_text_color: "Custom"
            text_color: root.cat_color
        MDLabel:
            text: root.date_text
            font_style: "Caption"
    MDIconButton:
        icon: "trash-can-outline"
        on_release: root.delete_me()

<MedsScreen>:
    name: "meds"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Medications"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            elevation: 8
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(15)
            spacing: dp(10)
            MDTextField:
                id: med_name
                hint_text: "Medication Name"
                mode: "rectangle"
            MDBoxLayout:
                spacing: dp(10)
                MDTextField:
                    id: med_dose
                    hint_text: "Dose (e.g. 500mg)"
                    mode: "rectangle"
                MDRaisedButton:
                    text: "TIME"
                    on_release: root.open_time_picker()
            MDLabel:
                id: time_label
                text: "Selected time: --:--"
                halign: "center"
            MDRaisedButton:
                text: "ADD REMINDER"
                size_hint_x: 1
                on_release: root.add_medication()
        ScrollView:
            MDBoxLayout:
                id: meds_list
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

<MedItem>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(70)
    padding: dp(10)
    radius: [dp(10)]
    elevation: 1
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: root.med_name
            font_style: "Subtitle1"
        MDLabel:
            text: root.med_dose + " • " + root.med_time
            font_style: "Caption"
    MDIconButton:
        icon: "trash-can-outline"
        on_release: root.delete_me()

<CalorieScreen>:
    name: "calories"
    md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Calories"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            elevation: 8
        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                MDTextField:
                    id: age_field
                    hint_text: "Age"
                    input_filter: "int"
                    mode: "rectangle"
                MDBoxLayout:
                    spacing: dp(10)
                    MDTextField:
                        id: height_field
                        hint_text: "Height (cm)"
                        input_filter: "float"
                        mode: "rectangle"
                    MDTextField:
                        id: weight_field
                        hint_text: "Weight (kg)"
                        input_filter: "float"
                        mode: "rectangle"
                MDBoxLayout:
                    spacing: dp(10)
                    MDCheckbox:
                        id: male_cb
                        group: "gender"
                        active: True
                    MDLabel:
                        text: "Male"
                    MDCheckbox:
                        id: female_cb
                        group: "gender"
                    MDLabel:
                        text: "Female"
                MDRaisedButton:
                    id: activity_btn
                    text: "Select Activity"
                    size_hint_x: 1
                    on_release: root.open_activity_menu(self)
                MDRaisedButton:
                    text: "CALCULATE"
                    size_hint_x: 1
                    on_release: root.calculate()
                MDCard:
                    id: result_card
                    orientation: "vertical"
                    padding: dp(15)
                    size_hint_y: None
                    height: dp(150)
                    radius: [dp(15)]
                    elevation: 2
                    opacity: 0
                    MDLabel:
                        id: cal_result
                        text: "--"
                        halign: "center"
                        font_style: "H3"
                    MDLabel:
                        id: cal_detail
                        text: ""
                        halign: "center"
"""

class GetStartedScreen(MDScreen):
    def go_next(self):
        self.manager.current = "disclaimer"

class DisclaimerScreen(MDScreen):
    def on_pre_enter(self):
        self.ids.disclaimer_text.text = (
            "This application (MediCalc) is an educational tool and NOT a substitute "
            "for professional medical advice, diagnosis, or treatment.\n\n"
            "Always seek the advice of a qualified healthcare provider with any questions "
            "you may have regarding a medical condition.\n\n"
            "In case of emergency, call your local emergency number immediately.\n\n"
            "By continuing, you agree to use this application at your own risk."
        )
    def go_next(self):
        App.get_running_app().mark_first_run_complete()
        self.manager.current = "home"

class HomeScreen(MDScreen): pass

class BMIScreen(MDScreen):
    def go_back(self): App.get_running_app().go_back()
    def calculate(self):
        try:
            h, w = float(self.ids.height_field.text), float(self.ids.weight_field.text)
            bmi = w / ((h / 100) ** 2)
            if bmi < 18.5: cat, color = "Underweight", [0.29, 0.56, 0.85, 1]
            elif bmi < 25: cat, color = "Normal", [0.30, 0.69, 0.31, 1]
            elif bmi < 30: cat, color = "Overweight", [1.0, 0.60, 0.0, 1]
            else: cat, color = "Obese", [0.90, 0.22, 0.21, 1]
            self.ids.bmi_value.text = f"{bmi:.1f}"
            self.ids.bmi_value.text_color = color
            self.ids.bmi_category.text = cat
            self.ids.bmi_category.text_color = color
            self.ids.result_card.opacity = 1
        except:
            Snackbar(text="Enter valid numbers").show()

class BPScreen(MDScreen):
    def go_back(self): App.get_running_app().go_back()
    def on_enter(self): self.refresh_list()
    def save_reading(self):
        try:
            sys, dia = int(self.ids.sys_field.text), int(self.ids.dia_field.text)
            app = App.get_running_app()
            app.bp_readings.append({"sys": sys, "dia": dia, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
            app.save_json("bp.json", app.bp_readings)
            self.ids.sys_field.text, self.ids.dia_field.text = "", ""
            self.refresh_list()
        except:
            Snackbar(text="Invalid input").show()
    def refresh_list(self):
        self.ids.readings_list.clear_widgets()
        for r in reversed(App.get_running_app().bp_readings):
            col = [0.90, 0.22, 0.21, 1] if r["sys"] >= 140 else [0.30, 0.69, 0.31, 1]
            self.ids.readings_list.add_widget(BPReadingItem(reading_text=f"{r['sys']}/{r['dia']} mmHg", date_text=r["date"], cat_color=col, reading=r))

class BPReadingItem(MDCard):
    reading_text, date_text = StringProperty(), StringProperty()
    cat_color, reading = ColorProperty([0,0,0,1]), None
    def delete_me(self):
        app = App.get_running_app()
        app.bp_readings.remove(self.reading)
        app.save_json("bp.json", app.bp_readings)
        app.sm.get_screen("bp").refresh_list()

class SugarScreen(MDScreen):
    selected_type = StringProperty("Fasting")
    def go_back(self): App.get_running_app().go_back()
    def on_enter(self): self.refresh_list()
    def open_type_menu(self, btn):
        types = ["Fasting", "Post-meal", "Random"]
        menu = MDDropdownMenu(caller=btn, items=[{"viewclass": "OneLineListItem", "text": t, "on_release": lambda x=t: self.set_type(x)} for t in types], width_mult=3)
        menu.open()
    def set_type(self, t):
        self.selected_type = t
        self.ids.sugar_list.parent.parent.parent.children[0].children[1].children[0].children[1].text = t
    def save_reading(self):
        try:
            g = float(self.ids.glucose_field.text)
            app = App.get_running_app()
            app.sugar_readings.append({"glucose": g, "type": self.selected_type, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
            app.save_json("sugar.json", app.sugar_readings)
            self.ids.glucose_field.text = ""
            self.refresh_list()
        except:
            Snackbar(text="Invalid input").show()
    def refresh_list(self):
        self.ids.sugar_list.clear_widgets()
        for r in reversed(App.get_running_app().sugar_readings):
            col = [0.13, 0.59, 0.95, 1] if r["glucose"] < 70 else ([0.30, 0.69, 0.31, 1] if r["glucose"] < 140 else [0.90, 0.22, 0.21, 1])
            self.ids.sugar_list.add_widget(SugarItem(reading_text=f"{r['glucose']:.0f} mg/dL ({r['type']})", date_text=r["date"], cat_color=col, reading=r))

class SugarItem(MDCard):
    reading_text, date_text = StringProperty(), StringProperty()
    cat_color, reading = ColorProperty([0,0,0,1]), None
    def delete_me(self):
        app = App.get_running_app()
        app.sugar_readings.remove(self.reading)
        app.save_json("sugar.json", app.sugar_readings)
        app.sm.get_screen("sugar").refresh_list()

class MedsScreen(MDScreen):
    selected_time = StringProperty("")
    def go_back(self): App.get_running_app().go_back()
    def on_enter(self): self.refresh_list()
    def open_time_picker(self):
        if MDTimePicker:
            picker = MDTimePicker()
            picker.bind(on_save=lambda inst, val: self.set_time(val))
            picker.open()
    def set_time(self, val):
        self.selected_time = val.strftime("%H:%M")
        self.ids.time_label.text = f"Selected: {self.selected_time}"
    def add_medication(self):
        name, dose = self.ids.med_name.text.strip(), self.ids.med_dose.text.strip()
        if name and dose and self.selected_time:
            app = App.get_running_app()
            app.medications.append({"name": name, "dose": dose, "time": self.selected_time, "last_notified": ""})
            app.save_json("meds.json", app.medications)
            self.ids.med_name.text, self.ids.med_dose.text = "", ""
            self.refresh_list()
    def refresh_list(self):
        self.ids.meds_list.clear_widgets()
        for m in App.get_running_app().medications:
            self.ids.meds_list.add_widget(MedItem(med_name=m["name"], med_dose=m["dose"], med_time=m["time"], med=m))

class MedItem(MDCard):
    med_name, med_dose, med_time = StringProperty(), StringProperty(), StringProperty()
    med = None
    def delete_me(self):
        app = App.get_running_app()
        app.medications.remove(self.med)
        app.save_json("meds.json", app.medications)
        app.sm.get_screen("meds").refresh_list()

class CalorieScreen(MDScreen):
    mult, _menu = NumericProperty(1.2), None
    ACT = [("Sedentary", 1.2), ("Light", 1.375), ("Moderate", 1.55), ("Active", 1.725)]
    def go_back(self): App.get_running_app().go_back()
    def open_activity_menu(self, btn):
        self._menu = MDDropdownMenu(caller=btn, items=[{"viewclass": "OneLineListItem", "text": n, "on_release": lambda x=n, y=m: self.set_act(x, y)} for n, m in self.ACT], width_mult=3)
        self._menu.open()
    def set_act(self, name, val):
        self.mult = val
        self.ids.activity_btn.text = name
        self._menu.dismiss()
    def calculate(self):
        try:
            age, h, w = int(self.ids.age_field.text), float(self.ids.height_field.text), float(self.ids.weight_field.text)
            bmr = (10*w + 6.25*h - 5*age + 5) if self.ids.male_cb.active else (10*w + 6.25*h - 5*age - 161)
            self.ids.cal_result.text = f"{int(bmr*self.mult)} kcal"
            self.ids.result_card.opacity = 1
        except:
            Snackbar(text="Invalid numbers").show()

class MediCalcApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.first_run = not os.path.exists(os.path.join(self.user_data_dir, "seen.txt"))
        self.bp_readings = self._load("bp.json")
        self.sugar_readings = self._load("sugar.json")
        self.medications = self._load("meds.json")
        
        Builder.load_string(KV)
        self.sm = ScreenManager()
        self.sm.add_widget(GetStartedScreen(name="get_started"))
        self.sm.add_widget(DisclaimerScreen(name="disclaimer"))
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(BMIScreen(name="bmi"))
        self.sm.add_widget(BPScreen(name="bp"))
        self.sm.add_widget(SugarScreen(name="sugar"))
        self.sm.add_widget(MedsScreen(name="meds"))
        self.sm.add_widget(CalorieScreen(name="calories"))
        
        self.sm.current = "get_started" if self.first_run else "home"
        Window.bind(on_keyboard=self._on_keyboard)
        Clock.schedule_interval(self._check_meds, 30)
        return self.sm
        
    def go_screen(self, name): self.sm.current = name
    def go_back(self): self.sm.current = "home"
    
    def mark_first_run_complete(self):
        self.first_run = False
        with open(os.path.join(self.user_data_dir, "seen.txt"), "w") as f: f.write("1")
        
    def _load(self, fn):
        p = os.path.join(self.user_data_dir, fn)
        return json.load(open(p)) if os.path.exists(p) else []
        
    def save_json(self, fn, data):
        with open(os.path.join(self.user_data_dir, fn), "w") as f: json.dump(data, f)
        
    def _on_keyboard(self, window, key, *args):
        if key == 27:
            if self.sm.current in ("home", "disclaimer", "get_started"): self.stop()
            else: self.go_back()
            return True
            
    def _check_meds(self, dt):
        if not PLYER_OK: return
        now = datetime.now()
        for m in self.medications:
            if m.get("time") == now.strftime("%H:%M"):
                key = now.strftime("%Y-%m-%d ") + m["time"]
                if m.get("last_notified") != key:
                    notification.notify(title="Med Reminder", message=f"{m['name']} - {m['dose']}")
                    m["last_notified"] = key
                    self.save_json("meds.json", self.medications)

if __name__ == "__main__":
    MediCalcApp().run()
