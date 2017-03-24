## SunFounder_Wi-Fi_Helper
SunFounder Wi-Fi Helper

Quick Links:

 * [About SunFounder Wi-Fi Helper](#about_this_software)
 * [Update](#update)
 * [About SunFounder](#about_sunfounder)
 * [Build Guide](#build_guide)
 * [License](#license)
 * [Contact us](#contact_us)

<a id="about_this_software"></a>
### About SunFounder Wi-Fi Helper:
SunFounder Wi-Fi Helper is a simple Windows software to set Raspbian's Wi-Fi open ssh by adding `wpa-supplicant` and `ssh` file to `/boot`. Also search the Raspberry Pi's IP Address by the name "raspberrypi".

Feel free to fork and pull.

<a id="build_guide"></a>
### Build Guide:
1. Install Python 3.4 (not the lastest):
    Download the Python 3.4 from [Python.org](python.org). Sinces py2exe only work on Python 3.4 (by far as we tested), you should not download the lastest one. Also, remember to check tkinter and pip while installing the Python 3.4.
2. Install py2exe
    In CMD(as Administraion), use pip3 to install py2exe:

        pip3 install py2exe
3. Test if the script works ok:
    
        python wifi_helper.py
4. Package the software:

        python setup.py py2exe
5. Move the icon file:
    The packaged files will all be in `dist`, copy the `.ico` file to `dist`.
6. Done!
    Then, everything is done, the excutable files is in `dist`


<a id="update"></a>
### Update:
2017-03-24:
 - V1.0.0 New Release

----------------------------------------------
<a id="about_sunfounder"></a>
### About SunFounder
SunFounder is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, SunFounder also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

----------------------------------------------
<a id="license"></a>
### License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

SunFounder_Wi-Fi_Helper comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'SunFounder_Wi-Fi_Helper' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Email: service@sunfounder.com, support@sunfounder.com

----------------------------------------------
<a id="contact_us"></a>
### Contact us:
website:
	www.sunfounder.com

E-mail:
	service@sunfounder.com, support@sunfounder.com
