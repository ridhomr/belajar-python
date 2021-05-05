import tkinter

main_window = tkinter.Tk()

def event_tekan():
	label2 = tkinter.Label(main_window, text="i love u")
	label2.pack()

label = tkinter.Label(main_window, text="hello, saya adalah \n GUI sederhana dengan \n menggunakan python3")
tombol = tkinter.Button(main_window, text="click here", command = event_tekan)


label.pack()
tombol.pack()



main_window.mainloop()