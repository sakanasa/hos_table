from kivy.app import App  # 從 kivy.app 模組導入 App 類別
from kivy.uix.boxlayout import BoxLayout  # 從 kivy.uix.boxlayout 模組導入 BoxLayout 類別
from kivy.uix.button import Button  # 從 kivy.uix.button 模組導入 Button 類別

class MyApp(App):  # 定義一個類別 MyApp，繼承自 App 類別
    def build(self):  # 定義建構子方法 build
        layout = BoxLayout(orientation='vertical')  # 建立一個 BoxLayout 物件，設定方向為垂直 (vertical)
        btn = Button(text='點擊我',font_name= 'C:/Windows/Fonts/微軟正黑體.ttf')  # 建立一個 Button 物件，設定文字為「點擊我」
        
        layout.add_widget(btn)  # 將按鈕加入到 BoxLayout 中
        return layout  # 回傳該 BoxLayout 物件

if __name__ == '__main__':
    MyApp().run()  # 執行 MyApp 的程式，啟動應用程式