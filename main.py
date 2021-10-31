import tkinter as tk
import recognizer
import recorder


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.minsize(1200, 600)

        # FRAMES
        self.left_frame = tk.Frame(
            master=self.root, bg='red', width=600, height=600)
        self.right_frame = tk.Frame(
            master=self.root, bg='blue', width=600, height=600)
        self.rec_frame = tk.Frame(
            master=self.left_frame, bg='red', width=600, height=300)
        self.settings_frame = tk.Frame(
            master=self.left_frame, bg='green', width=600, height=300)

        # TITLES
        self.rec_title = tk.Label(
            master=self.rec_frame, text='Recorder', font=('Arial', 20))
        self.reco_title = tk.Label(
            master=self.right_frame, text='Recognizer', font=('Arial', 20))
        self.settings_title = tk.Label(
            master=self.settings_frame, text='Settings', font=('Arial', 20))

        # BUTTONS
        self.btn_record = tk.Button(
            master=self.rec_frame, text='Record', width=20, height=10, command=self.record_voice)
        self.btn_reco = tk.Button(
            master=self.rec_frame, text='Recognize', width=20, height=10, command=self.recognize_voice)
        self.lbl_sec = tk.Label(
            master=self.settings_frame, text='Seconds', width=20, height=10)
        self.btn_sec_increase = tk.Button(
            master=self.settings_frame, text='+', width=20, height=10, command=self.increase_sec)
        self.btn_sec_decrease = tk.Button(
            master=self.settings_frame, text='-', width=20, height=10, command=self.decrease_sec)
        self.lbl_sec_value = tk.Label(
            master=self.settings_frame, text='3', width=20, height=10)
        self.btn_quit = tk.Button(
            master=self.right_frame, text='Quit', command=self.close_window)

        self.lbl_text = tk.Label(
            master=self.right_frame, text='Your text here.....', font=('Arial', 15))

        # PACK
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.rec_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.settings_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.rec_title.pack(side=tk.TOP)
        self.reco_title.pack(side=tk.TOP)
        self.settings_title.pack(side=tk.TOP)

        self.btn_record.pack(side=tk.LEFT)
        self.btn_reco.pack(side=tk.RIGHT)
        self.lbl_sec.pack(side=tk.TOP)
        self.btn_sec_increase.pack(side=tk.RIGHT)
        self.btn_sec_decrease.pack(side=tk.LEFT)
        self.lbl_sec_value.pack()
        self.btn_quit.pack(side=tk.BOTTOM)

        self.lbl_text.pack()

    def close_window(self):
        self.root.destroy()

    def increase_sec(self):
        value = int(self.lbl_sec_value['text'])
        self.lbl_sec_value['text'] = value + 1

    def decrease_sec(self):
        value = int(self.lbl_sec_value['text'])
        if value > 1:
            self.lbl_sec_value['text'] = value - 1

    def record_voice(self):
        recorder.record(int(self.lbl_sec_value['text']))

    def recognize_voice(self):
        self.lbl_text['text'] = recognizer.recognize()


def main():
    root = tk.Tk(className='voice recognizer')
    root.iconbitmap(default='icon.ico')

    app = MainApplication(root)

    root.mainloop()


if __name__ == '__main__':
    main()
