#!/usr/bin/python


class WiFiHelper(object):
    import tkinter as tk
    import string
    import os
    import _thread
    import socket
    from os import system as system_call       # Execute a shell command
    import time
    import sys

    VERSION = "v1.2.0"
    COMPANY = "SunFounder     www.sunfounder.com"

    BACKGROUND_COLOR = '#EEEEEE'
    FOREGROUND_COLOR = '#202020'
    ERROR_COLOR = '#FA0F0F'

    _alphabets = list(string.ascii_lowercase)

    def __init__(self):
        # Get avalible disks
        disks = self.get_all_disk()
        self.top = self.tk.Tk()
        self.top.title('SunFounder Wi-Fi Helper')
        self.top.iconbitmap('./SunFounder_LOGO_small.ico')
        main_frame = self.tk.Frame(self.top, width=800)
        info_frame = self.tk.Frame(self.top)
        control_frame = self.tk.Frame(main_frame, width=360)
        debug_frame = self.tk.Frame(main_frame, width=360)
        frame_1_1 = self.tk.Frame(control_frame)
        self.frame_1_2 = self.tk.Frame(control_frame)
        frame_1_3 = self.tk.Frame(control_frame)
        frame_1_4 = self.tk.Frame(control_frame)
        frame_1_5 = self.tk.Frame(control_frame)
        frame_1_6 = self.tk.Frame(control_frame)
        frame_1_7 = self.tk.Frame(control_frame)
        frame_1_8 = self.tk.Frame(control_frame)
        frame_1_9 = self.tk.Frame(control_frame)
        frame_2_1 = self.tk.Frame(debug_frame)
        frame_2_2 = self.tk.Frame(debug_frame)
        self.enabled_ssh = self.tk.IntVar()
        self.disk = self.tk.StringVar(self.frame_1_2)
        self.message = self.tk.StringVar(frame_1_7)
        self.message.set('')
        self.disk.set('')

        main_lable         = self.tk.Label(frame_1_1, text="Raspbian Wi-Fi Helper", fg=self.FOREGROUND_COLOR)
        disk_label         = self.tk.Label(self.frame_1_2, text="Select the disk of your Rasbian", fg=self.FOREGROUND_COLOR)
        self.disk_menu     = self.tk.OptionMenu(self.frame_1_2, self.disk, *disks)
        disk_reflash       = self.tk.Button(self.frame_1_2, width=7, text='Reflash')
        ssid_label         = self.tk.Label(frame_1_3, text="SSID: ", fg=self.FOREGROUND_COLOR)
        self.ssid_input    = self.tk.Entry(frame_1_3, bg=self.BACKGROUND_COLOR, fg=self.FOREGROUND_COLOR)
        passwd_label       = self.tk.Label(frame_1_4, text="PASSWORD: ", fg=self.FOREGROUND_COLOR)
        self.passwd_input  = self.tk.Entry(frame_1_4, bg=self.BACKGROUND_COLOR, fg=self.FOREGROUND_COLOR)
        ssh_check          = self.tk.Checkbutton(frame_1_5, text="Enable SSH", variable=self.enabled_ssh)
        message_lable      = self.tk.Label(frame_1_6, textvariable=self.message, fg=self.ERROR_COLOR)
        confirm_button     = self.tk.Button(frame_1_7, width=10, text='Confirm')
        self.keyword_input = self.tk.Entry(frame_1_8, bg=self.BACKGROUND_COLOR, fg=self.FOREGROUND_COLOR)
        search_button      = self.tk.Button(frame_1_8, width=20, text='Search Raspberry Pi')
        self.ip_listbox    = self.tk.Listbox(frame_1_9, width=50, height=200)
        debug_label        = self.tk.Label(frame_2_1, text="Debug:", fg=self.FOREGROUND_COLOR)
        self.debug_listbox = self.tk.Listbox(frame_2_2, width=100, height=200)
        info_version       = self.tk.Label(info_frame,text=self.VERSION, fg=self.FOREGROUND_COLOR)
        info_company       = self.tk.Label(info_frame,text=self.COMPANY, fg=self.FOREGROUND_COLOR)


        # Pack 
        main_frame.pack(fill="both")
        info_frame.pack(side=self.tk.BOTTOM,fill="both")

        control_frame.pack(side=self.tk.LEFT, padx=20, pady=20, fill="both")
        debug_frame.pack(side=self.tk.RIGHT, padx=20, pady=20, fill="both")

        frame_1_1.pack(pady=10, side=self.tk.TOP,fill="both")
        self.frame_1_2.pack(side=self.tk.TOP,fill="both")
        frame_1_3.pack(padx=30, side=self.tk.TOP,fill="both")
        frame_1_4.pack(padx=30, side=self.tk.TOP,fill="both")
        frame_1_5.pack(side=self.tk.TOP,fill="both")
        frame_1_6.pack(side=self.tk.TOP,fill="both")
        frame_1_7.pack(side=self.tk.TOP,fill="both")
        frame_1_8.pack(side=self.tk.TOP,fill="both")
        frame_1_9.pack(side=self.tk.TOP,fill="both")

        frame_2_1.pack(side=self.tk.TOP,fill="x")
        frame_2_2.pack(side=self.tk.TOP,fill="both")

        main_lable.pack(side=self.tk.LEFT)
        disk_label.pack(side=self.tk.LEFT)
        disk_reflash.pack(side=self.tk.RIGHT)
        self.disk_menu.pack(side=self.tk.RIGHT)
        ssid_label.pack(side=self.tk.LEFT)
        self.ssid_input.pack(side=self.tk.RIGHT)
        passwd_label.pack(side=self.tk.LEFT)
        self.passwd_input.pack(side=self.tk.RIGHT)
        ssh_check.pack()
        message_lable.pack(side=self.tk.LEFT)
        confirm_button.pack(side=self.tk.RIGHT)
        self.keyword_input.pack(side=self.tk.LEFT)
        search_button.pack(side=self.tk.RIGHT)
        self.ip_listbox.pack(fill="x")

        debug_label.pack(side=self.tk.LEFT)
        self.debug_listbox.pack(fill="both")

        info_version.pack(side=self.tk.LEFT)
        info_company.pack(side=self.tk.RIGHT)

        # Setup
        self.top.resizable(width=False, height=False)
        self.top.geometry('{}x{}'.format(1000, 480))
        confirm_button.bind('<ButtonRelease-1>', self.confirm)
        search_button.bind('<ButtonRelease-1>', self.search)
        disk_reflash.bind('<ButtonRelease-1>', self.reflash)
        self.keyword_input.insert(0, 'raspberrypi')
        ssh_check.select()
        #self.ip_listbox.config(state=self.tk.DISABLED)
        #self.debug_listbox.config(state=self.tk.DISABLED)

    def start(self):
        self.debug("Ready.")
        self.top.mainloop()

    def get_all_disk(self):
        disks = []
        for disk in self._alphabets:
            disk = '%s:'%disk
            try:
                self.os.listdir(disk)
                disks.append(disk)
            except:
                continue
        return disks

    def reflash(self, event):
        self.debug("Reflashing avalible disks...")
        self.disk_menu.pack_forget()
        disks = self.get_all_disk()
        self.disk_menu = self.tk.OptionMenu(self.frame_1_2, self.disk, *disks)
        self.disk_menu.pack(side=self.tk.RIGHT)
        self.debug("Done!")

    def confirm(self, event):
        if self.disk.get() == "":
            self.message.set("Error! You must select a disk!")
            self.debug("Error! You must select a disk!")
        elif self.ssid_input.get() == "":
            self.message.set("Error! SSID must not be empty!")
            self.debug("Error! SSID must not be empty!")
        elif self.passwd_input.get() == "":
            self.message.set("Error! PASSWARD must not be empty!")
            self.debug("Error! PASSWARD must not be empty!")
        else:
            wpa = 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev,update_config=1,,network={,    ssid="%s",    psk="%s",    key_mgmt=WPA-PSK,}' % (self.ssid_input.get(),self.passwd_input.get())
            wpa = wpa.replace(',', '\n')
            self.debug("wpa_file:\n%s"%wpa)
            if self.apply_settings(wpa):
                self.message.set("Done!")
                self.debug("Done!")
                self.debug("You can now unmount your TF Card.")
                self.debug("And turn on your Pi.")


    def apply_settings(self, wpa):
        wpa_file = "%s/wpa_supplicant.conf" % self.disk.get()
        ssh_file = "%s/ssh" % self.disk.get()
        self.debug("wpa file will be at: %s" % wpa_file)
        self.debug("ssh file will be at: %s" % ssh_file)
        
        f = open(wpa_file, 'w')
        f.write(wpa)
        f.close()
        if self.enabled_ssh.get():
            f = open(ssh_file, 'w')
            f.write('')
            f.close
        return 1

    def search(self, event):
        self.debug("Searching...")
        keyword = self.keyword_input.get()
        self.ip_listbox.delete(0, self.tk.END)
        my_name = self.socket.getfqdn(self.socket.gethostname())
        my_address = self.socket.gethostbyname(my_name)
        gateway = my_address.split('.')
        gateway = gateway[0]+'.'+gateway[1]+'.'+gateway[2]+'.'
        self.debug('My Name: %s' % my_name)
        self.debug('My Address: %s' % my_address)
        self.debug('Gateway: %s' % gateway+'0')
        ip_from = 1
        ip_to   = 255
        ip_to += 1
        for i in range(ip_from, ip_to):
            ip = gateway+'%d'%i
            self._thread.start_new_thread(self.search_ip, (keyword,ip,))
            #self.search_ip(keyword,ip)

    def search_ip(self, keyword, ip):
        try:
            host = self.socket.gethostbyaddr(ip)
            host = host[0].split('.')[0]
            #self.debug('  host: "%s"'%host)
            if keyword in '%s'%host:
                self.debug('Found host: "%s"'%host)
                status = self.ping(ip)
                if status:
                    #self.debug('host: %s@%s' % (host,ip))
                    self.ip_listbox.insert(self.tk.END, '%s@%s' % (host,ip))
                else:
                    self.debug('%s@%s ping failed'%(host,ip))
        except:
            pass

    def ping(self, host):
        return self.system_call("ping -n 1 " + host) == 0

    def debug(self, messages):
        localtime = self.time.asctime(self.time.localtime(self.time.time()))
        messages = "%s" % messages
        messages = messages.split('\n')
        for m in messages:
            m = str(localtime) + "    " + m
            print(m)
            self.debug_listbox.insert(self.tk.END, "%s"%m)
            self.debug_listbox.yview(self.tk.END)

if __name__ == '__main__':
    w = WiFiHelper()
    w.start()


