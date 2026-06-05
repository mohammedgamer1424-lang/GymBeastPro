from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from database import initialize_schema
from services import WorkoutService

Window.clearcolor = (0.12, 0.12, 0.12, 1)

class GymApp(App):
    def build(self):
        initialize_schema()
        self.title = "Gym Beast Pro"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        title_label = Label(text="Gym Beast Pro 🔥", font_size='28sp', bold=True, color=(0.1, 0.6, 0.9, 1))
        layout.add_widget(title_label)
        
        self.exercise_input = TextInput(hint_text="اسم التمرين", multiline=False, size_hint_y=None, height=50)
        self.weight_input = TextInput(hint_text="الوزن بالـ kg", multiline=False, input_filter='float', size_hint_y=None, height=50)
        self.reps_input = TextInput(hint_text="عدد التكرارات", multiline=False, input_filter='int', size_hint_y=None, height=50)
        
        layout.add_widget(self.exercise_input)
        layout.add_widget(self.weight_input)
        layout.add_widget(self.reps_input)
        
        self.status_label = Label(text="مستعد لتسجيل الرفعة يا لورد..", font_size='14sp')
        layout.add_widget(self.status_label)
        
        save_btn = Button(text="حفظ الرفعة", font_size='20sp', bold=True, background_color=(0.1, 0.8, 0.3, 1), size_hint_y=None, height=60)
        save_btn.bind(on_press=self.save_data)
        layout.add_widget(save_btn)
        return layout

    def save_data(self, instance):
        exercise = self.exercise_input.text
        weight_txt = self.weight_input.text
        reps_txt = self.reps_input.text
        if not exercise or not weight_txt or not reps_txt:
            self.status_label.text = "⚠️ أكتب البيانات كاملة الأول!"
            return
        try:
            WorkoutService.log_workout(exercise, 4, int(reps_txt), float(weight_txt))
            self.status_label.text = f"✅ تم تسجيل {exercise} بنجاح!"
            self.exercise_input.text = ""
            self.weight_input.text = ""
            self.reps_input.text = ""
        except Exception as e:
            self.status_label.text = f"❌ خطأ: {str(e)}"

if __name__ == '__main__':
    GymApp().run()
