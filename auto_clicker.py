#libraries
import win32api
import win32con
from time import sleep
from libs.which_key_is_pressed import check_key_pressed, give_vk_id
from libs.work_with_files import file_check, file_write, file_read, file_create



#clicker
def clicker(settings):

	#loading settings
	start_first_key=give_vk_id(settings[0])
	start_second_key=give_vk_id(settings[1])
	end_first_key=give_vk_id(settings[2])
	end_second_key=give_vk_id(settings[3])
	speed=1/int(settings[4])
	mouse_click=settings[5]



	while True:
		#Check if start keys is pressed

		if win32api.GetAsyncKeyState(start_first_key) != 0 and win32api.GetAsyncKeyState(start_second_key) != 0:

			while True:

				#Get the current position of the cursor
				(x,y) = win32api.GetCursorPos()

				#Click
				if mouse_click=="left":
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
				else:
					win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
					win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)					

				#Wait sometime
				sleep(speed)

				#Check if end keys is pressed
				if win32api.GetAsyncKeyState(end_first_key) != 0 and win32api.GetAsyncKeyState(end_second_key) != 0:
				
					break

#settings
def settings():
	#set settings
	def set():
		
		settings=["start_first_key=","start_second_key=","end_first_key=","end_second_key=","speed=","mouse_click="]
		
		print("Settings setup")
		print("####################################")
		print("Key combination to start autoclicker")
		print("You will need to press a key combination (two keys, each key separately)")
		sleep(0.5)
		
		#first start key
		print("Please press first key")
		start_first_key=check_key_pressed()
		settings[0]=settings[0]+start_first_key
		print("You pressed: "+ start_first_key)
		sleep(1)
		
		#second start key
		print("Please press second key")
		start_second_key=check_key_pressed()
		settings[1]=settings[1]+start_second_key
		print("You pressed: "+ start_second_key)
		sleep(1)

		print("####################################")
		print("Key combination to stop autoclicker")
		print("You will need to press a key combination (two keys, each key separately)")
		sleep(1)

		#first end key
		print("Please press first key")
		end_first_key=check_key_pressed()
		settings[2]=settings[2]+end_first_key
		print("You pressed: "+ end_first_key)
		sleep(1)

		#second end key
		print("Please press second key")
		end_second_key=check_key_pressed()
		settings[3]=settings[3]+end_second_key
		print("You pressed: "+ end_second_key)
		sleep(1)

		#speed
		print("####################################")
		print("Please enter speed autocliker (amount of clicks per second)")
		speed=input()
		for x in range(len(speed)):
			if speed[x]=="0" or speed[x]=="1" or speed[x]=="2" or speed[x]=="3" or speed[x]=="4" or speed[x]=="5" or speed[x]=="6" or speed[x]=="7" or speed[x]=="8" or speed[x]=="9":
				speed=speed[x:]
				break
		settings[4]=settings[4]+speed
		print("You entered speed: "+ speed)
		sleep(0.5)

		#mouse click
		print("####################################")
		print("Please chose mouse click:")
		print("1) right")
		print("2) left")
		mouse_click=input()
		if mouse_click=="1":
			mouse_click="right"
		else:
			mouse_click="left"
		settings[5]=settings[5]+mouse_click
		print("You entered: "+ mouse_click)
		sleep(0.5)
		
		#saving settings in file
		print("####################################")
		print("Saving settings in settings.ini")
		file_write("settings.ini",settings)
		print("Saved")
		print("####################################")


	#checking and creating file with settings
	def create_and_check():
		if file_check("settings.ini")==False:
			file_create("settings.ini")
		
		settings=file_read("settings.ini")
		if settings==[] or len(settings)!=6:
			set()

	#loading settings
	def load():
		settings=file_read("settings.ini")
		loading=[]
		for x in range(len(settings)):
			loading.append(settings[x].split("=")[1])
		return loading


	create_and_check()
	return load()

#information about programm
def print_logo():
	print("╔══╦╗╔╦════╦══╦══╦╗─╔══╦══╦╗╔══╦═══╦═══╗")
	print("║╔╗║║║╠═╗╔═╣╔╗║╔═╣║─╚╗╔╣╔═╣║║╔═╣╔══╣╔═╗║")
	print("║╚╝║║║║─║║─║║║║║─║║──║║║║─║╚╝║─║╚══╣╚═╝║")
	print("║╔╗║║║║─║║─║║║║║─║║──║║║║─║╔╗║─║╔══╣╔╗╔╝")
	print("║║║║╚╝║─║║─║╚╝║╚═╣╚═╦╝╚╣╚═╣║║╚═╣╚══╣║║║ ")
	print("╚╝╚╩══╝─╚╝─╚══╩══╩══╩══╩══╩╝╚══╩═══╩╝╚╝ ")
	print("Created by Gick)")
	print("If you want to change the settings, you just need to delete settings.ini)")
	print("To close the program click on the cross symbol")


def main():

	#print some information
	print_logo()

	#load settings
	load_settings=settings()

	#start autocliker
	clicker(load_settings)


if __name__== "__main__":
	main()