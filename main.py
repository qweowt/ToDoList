import tkinter
import customtkinter
import datetime
import json

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
class task:

	def __init__(self, frame, text, index, cb, date):
		self.frame = frame
		self.text = text
		self.index = index
		self.date = date
		self.cb = cb
		self.label = customtkinter.CTkLabel(frame, text=f"{text}",
																				 fg_color="transparent",
																				 font=("Gilroy", 20, "bold"))
		self.button = customtkinter.CTkButton(frame, text="Delete", 
																	command=lambda: DeleteTask(self),
																	fg_color="transparent", 
																	hover_color="#cccccc", 
																	border_width=2, 
																	border_color="#666666",
																	font=("Gilroy", 20, "bold"))
		self.dateLabel = customtkinter.CTkLabel(frame, text=f"{date}",
																				 fg_color="transparent",
																				 font=("Gilroy", 14, "bold"))
		self.checkBox = customtkinter.CTkCheckBox(frame, text="")
		clr = color(self.cb)
		self.comboBox = customtkinter.CTkLabel(frame, text=f"{cb}", fg_color="transparent", font=("Gilroy", 20, "bold"), text_color=clr)
	
def color(cb):
	if(cb == "low"):
		return "green"
	elif(cb == "medium"):
		return "yellow"
	else:
		return "red"

tempText = ""
tempIndex = 0
cb = ""

tasks = list()
app = customtkinter.CTk()
app.title("ToDo List")

mainFrame = customtkinter.CTkFrame(app)
mainFrame.pack(side=customtkinter.TOP, fill=customtkinter.X, expand=False)

textBox = customtkinter.CTkTextbox(mainFrame, width=300, height=20,
																		 font=("Gilroy", 20, "bold"))
comboBox = customtkinter.CTkComboBox(mainFrame, values=["low", "medium", "high"], font=("Gilroy", 20, "bold"))
textBox.pack(side=customtkinter.LEFT, padx=4, pady=4)
comboBox.pack(side=customtkinter.LEFT, padx=4, pady=4)

def Exit ():
	app.destroy()

def AddTask ():	
	GetText()
	global tempText
	global tempIndex

	tasks.append(task(customtkinter.CTkFrame(app), tempText, tempIndex, cb,
																f"{datetime.datetime.today():%Y-%m-%d}"))
	Updatetask()
	tempIndex += 1

def Updatetask():
	for i in range(len(tasks)):
		tasks[i].frame.pack(side=customtkinter.TOP, fill=customtkinter.X, expand=False, padx=4, pady=4)
		tasks[i].label.pack(side=customtkinter.LEFT, fill=customtkinter.Y, expand=False)
		tasks[i].button.pack(side=customtkinter.RIGHT, expand=False, padx=4, pady=4)
		tasks[i].dateLabel.pack(side=customtkinter.RIGHT, fill=customtkinter.Y, expand=False)
		tasks[i].checkBox.pack(side=customtkinter.RIGHT, fill=customtkinter.Y, expand=False)
		tasks[i].comboBox.pack(side=customtkinter.RIGHT, fill=customtkinter.Y, expand=False, padx=10, pady=4)

def DeleteTask(index):
	trueIndex = tasks.index(index)
	tasks[trueIndex].frame.destroy()
	tasks.pop(trueIndex)

def GetText():
	global cb
	global tempText
	cb = comboBox.get()
	tempText = customtkinter.CTkTextbox.get(textBox, "1.0", "end")
	textBox.delete("1.0", "end")

def importData():
	file_path = tkinter.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
	with open(file_path, "r") as file:
		for line in file:
			data = json.loads(line)
			print(data)


def exportData():
	dict = {task.index:task.text[[str(task.date), str(task.cb)]] for task in tasks}

	with open('data.json', 'w') as file:
		json.dump(dict, file, indent=4)
		file.write('\n')

def main ():
	bottomPanel = customtkinter.CTkFrame(app)
	bottomPanel.pack(side=customtkinter.BOTTOM, fill=customtkinter.X, expand=False)

	importButton = customtkinter.CTkButton(bottomPanel, text="Import", 
																				 command=importData,
																				 fg_color="transparent", 
																				 hover_color="#cccccc", 
																				 border_width=2, 
																				 border_color="#666666",
																				 font=("Gilroy", 20, "bold"))
	exportButton = customtkinter.CTkButton(bottomPanel, text="Export",
																				 command=exportData,
																				 fg_color="transparent", 
																				 hover_color="#cccccc", 
																				 border_width=2, 
																				 border_color="#666666",
																				 font=("Gilroy", 20, "bold"))

	button = customtkinter.CTkButton(mainFrame, text="Exit", 
																	command=Exit,
																	fg_color="transparent", 
																	hover_color="#cccccc", 
																	border_width=2, 
																	border_color="#666666",
																	font=("Gilroy", 20, "bold"))
	button2 = customtkinter.CTkButton(mainFrame, text="Add", 
																	command = AddTask,
																	fg_color="transparent", 
																	hover_color="#cccccc", 
																	border_width=2, 
																	border_color="#666666",
																	font=("Gilroy", 20, "bold"))

	button.pack(side=customtkinter.RIGHT, padx=4, pady=4)
	button2.pack(side=customtkinter.RIGHT, padx=4, pady=4)
	importButton.pack(side=customtkinter.RIGHT, padx=4, pady=4)
	exportButton.pack(side=customtkinter.RIGHT, padx=4, pady=4)
	
	app.minsize(800, 400)
	app.maxsize(800, 400)
	app.mainloop()

if __name__ == "__main__":
	main()