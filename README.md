# Simple University of Manchester WiFi activator.

Tire of manually putting in your username and password every time you want to
connect to the university wifi? Well, this script will ease the pain a bit.

## Install

Clone this repository to somewhere in your filesystem. In my example, it lives in
/home/karl/dev/uom-wifi-activator. You can choose something similar.

```
	$ cd $HOME/dev
	$ git clone https://github.com/karls/uom-wifi-activator.git
	$ cd uom-wifi-activator
```

Have a look around. `main.py` is what does most of the work.
`credentials.example.py` contains information about your username and password.
You should change the values in that file and rename it to `credentials.py`.
In `scripts/` you'll see a file called `10-uom-wifi.sh`. This is the script that
gets called by NetworkManager after it has connected to an access point. In that
file, you'll need to change `$ACTIVATION\_SCRIPT` variable to point to `main.py`
in the project root. But first, you'll need to copy it to
`/etc/NetworkManager/dispatcher.d/`.

```
	$ cd path/to/uom-wifi-activator/
	$ sudo su
	# cp scripts/10-uom-wifi.sh /etc/NetworkManager/dispatcher.d
```

Then open it with your editor of choice:

```
	# cd /etc/NetworkManager/dispatcher.d
	# vim 10-uom-wifi.sh
```

Change the path in `$ACTIVATION_SCRIPT` to point to the main.py in your filesystem.
Once you're done, save and exit. Then

```
	# chmod 700 10-uom-wifi.sh
	# exit
```

This is needed by NetworkManager (see `man 8 NetworkManager`).
