#!/usr/bin/python

from tkinter import *
import string
import os
import _thread
import socket
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

VERSION = "v1.0.0"
COMPANY = "SunFounder     www.sunfounder.com"

bg = '#EEEEEE'
fg = '#202020'
ErrorColor = '#FA0F0F'

alphabet = list(string.ascii_lowercase)

def setup():
    global top, message, ip_listbox, disk_menu, frame_2
    global ssid_input, passwd_input, enabled_ssh, disk, disks

    # Get avalible disks
    disks = get_all_disk()

    top = Tk()
    top.title('SunFounder Wi-Fi Helper')
    top.iconbitmap('./SunFounder_LOGO_small.ico')
    main_frame = Frame(top)
    info_frame = Frame(top)
    control_frame = Frame(main_frame)
    debug_frame = Frame(main_frame)
    frame_1 = Frame(control_frame)
    frame_2 = Frame(control_frame)
    frame_3 = Frame(control_frame)
    frame_4 = Frame(control_frame)
    frame_5 = Frame(control_frame)
    frame_6 = Frame(control_frame)
    frame_7 = Frame(control_frame)
    frame_8 = Frame(control_frame)
    frame_9 = Frame(control_frame)
    enabled_ssh = IntVar()
    disk = StringVar(frame_2)
    message = StringVar(frame_7)
    message.set('')
    disk.set('')

    main_lable     = Label(frame_1, text="Raspbian Wi-Fi Helper", fg=fg)
    disk_label     = Label(frame_2, text="Select the disk of your Rasbian", fg=fg)
    disk_menu      = OptionMenu(frame_2, disk, *disks)
    disk_reflash   = Button(frame_2, width=7, text='Reflash')
    ssid_label     = Label(frame_3, text="SSID: ", fg=fg)
    ssid_input     = Entry(frame_3, bg=bg, fg=fg)
    passwd_label   = Label(frame_4, text="PASSWORD: ", fg=fg)
    passwd_input   = Entry(frame_4, bg=bg, fg=fg)
    ssh_check      = Checkbutton(frame_5, text="Enable SSH", variable=enabled_ssh)
    message_lable  = Label(frame_6, textvariable=message, fg=ErrorColor)
    confirm_button = Button(frame_7, width=10, text='Confirm')
    search_button  = Button(frame_8, width=20, text='Search Raspberry Pi')
    ip_listbox     = Listbox(frame_9, fg=fg)
    debug_lable    = Listbox(debug_frame, fg=fg)
    info_version   = Label(info_frame,text=VERSION, fg=fg)
    info_company   = Label(info_frame,text=COMPANY, fg=fg)


    # Pack 
    main_frame.pack(padx=20, pady=20, fill="both")
    info_frame.pack(side=BOTTOM,fill="both")
    control_frame.pack(side=LEFT, fill="both")
    debug_frame.pack(side=RIGHT, fill="both")
    frame_1.pack(pady=10, side=TOP,fill="both")
    frame_2.pack(pady=10, side=TOP,fill="both")
    frame_3.pack(padx=30, side=TOP,fill="both")
    frame_4.pack(padx=30, side=TOP,fill="both")
    frame_5.pack(side=TOP,fill="both")
    frame_6.pack(side=TOP,fill="both")
    frame_7.pack(side=TOP,fill="both")
    frame_8.pack(side=TOP,fill="both")
    frame_9.pack(side=TOP,fill="both")
    main_lable.pack(side=LEFT)
    disk_label.pack(side=LEFT)
    disk_reflash.pack(side=RIGHT)
    disk_menu.pack(side=RIGHT)
    ssid_label.pack(side=LEFT)
    ssid_input.pack(side=RIGHT)
    passwd_label.pack(side=LEFT)
    passwd_input.pack(side=RIGHT)
    ssh_check.pack()
    message_lable.pack(side=LEFT)
    confirm_button.pack(side=RIGHT)
    search_button.pack(side=LEFT)
    ip_listbox.pack(fill="both")
    info_version.pack(side=LEFT)
    info_company.pack(side=RIGHT)

    # Setup
    top.resizable(width=False, height=False)
    top.geometry('{}x{}'.format(800, 480))
    confirm_button.bind('<ButtonRelease-1>', confirm)
    search_button.bind('<ButtonRelease-1>', search)
    disk_reflash.bind('<ButtonRelease-1>', reflash)
    ssh_check.select()
    ip_listBox_.config(state=DISABLED)

def main():
    top.mainloop()

def quit_fun(event):
    top.quit()

def reflash(event):
    global disk_menu
    disk_menu.pack_forget()
    disks = get_all_disk()
    disk_menu = OptionMenu(frame_2, disk, *disks)
    disk_menu.pack(side=RIGHT)

def confirm(event):
    if ssid_input.get() == "":
        message.set("Error! SSID must not be empty!")
    elif passwd_input.get() == "":
        message.set("Error! PASSWARD must not be empty!")
    else:
        wpa = 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev,update_config=1,,network={,    ssid="%s",    psk="%s",    key_mgmt=WPA-PSK,}' % (ssid_input.get(),passwd_input.get())
        wpa = wpa.replace(',', '\n')
        print("wpa_file:\n%s"%wpa)
        if apply_settings(wpa):
            message.set("Done!")

def get_all_disk():
    disks = []
    for disk in alphabet:
        disk = '%s:'%disk
        try:
            os.listdir(disk)
            disks.append(disk)
        except:
            continue
    return disks

def apply_settings(wpa):
    wpa_file = "%s/wpa_supplicant.conf" % disk.get()
    ssh_file = "%s/ssh" % disk.get()
    print("wpa file will be at: %s" % wpa_file)
    print("ssh file will be at: %s" % ssh_file)
    
    f = open(wpa_file, 'w')
    f.write(wpa)
    f.close()
    if enabled_ssh.get():
        f = open(ssh_file, 'w')
        f.write('')
        f.close
    return 1

def search(event):
    ip_listbox.delete(0, END)
    my_name = socket.getfqdn(socket.gethostname())
    my_address = socket.gethostbyname(my_name)
    gateway = my_address.split('.')
    gateway = gateway[0]+'.'+gateway[1]+'.'+gateway[2]+'.'
    print('My Name: %s' % my_name)
    print('My Address: %s' % my_address)
    print('Gateway: %s' % gateway+'0')
    for i in range(1,255):
        ip = gateway+'%d'%i
        _thread.start_new_thread(search_ip, (ip,))
        #search_ip(ip)

def search_ip(ip):
    try:
        host = socket.gethostbyaddr(ip)
        host = host[0].split('.')[0]
        if host == 'raspberrypi':
            status = ping(ip)
            print(status)
            if status:
                print('host: %s@%s' % (host,ip))
                ip_listbox.insert(END, '%s@%s' % (host,ip))
    except:
        pass
        #print("Unexpected error: %s" % sys.exc_info()[0])


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1" if system_name().lower()=="windows" else "-c 1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0

if __name__ == '__main__':
    setup()
    main()


