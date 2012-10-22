# Simple University of Manchester WiFi activator.

Tired of manually putting in your username and password every time you want to
connect to the university wifi? Well, this script will ease the pain a bit.

## Requirements

* Python 2.7.3
* NetworkManager 0.9.6.0
* Logbook 0.4 (optional)
* libnotify 0.7.5-1 (optional)
* python2-gobject 3.2.2-2 (optional)

I've only tested it with Python 2.7.3 on Arch Linux, but it probably works with
lower versions as well. Same goes for NetworkManager.
If it doesn't, feel free to file a ticket or patch it and submit a pull request.

Logbook can be installed with a simple `pip2 install Logbook`. Logbook is optional
and is only really needed for debugging. If you decide to install Logbook, it will
create a file named `USERNAME.log` in the project root that contains some
information about what happens during authentication.

For more info, see [Logbook's repo](https://github.com/mitsuhiko/logbook).

`libnotify` and `python2-gobject` are needed if you want to have notifications.

**Note:** the version numbers are what are installed on my system. You might find
that it works perfectly well with other (lower) versions of the same software.

## Install

Clone this repository to somewhere in your filesystem. In my example, it lives in
`/home/karl/dev/uom-wifi-activator`. You can choose something similar.

```
	$ cd $HOME/dev/
	$ git clone https://github.com/karls/uom-wifi-activator.git
	$ cd uom-wifi-activator/
```

Have a look around. `main.py` is what does most of the work.
`credentials.example.py` contains information about your username and password.
You should change the values in that file and rename it to `credentials.py`.

```
	$ vim credentials.example.py
```

Update the values to match your username and password. Then

```
	$ mv credentials.example.py credentials.py
```

In `scripts/` you'll see a file called `10-uom-wifi.sh`. This is the script that
gets called by NetworkManager after it has connected to an access point. In that
file, you'll need to change `$ACTIVATION_SCRIPT` variable to point to `activate.sh`
in the `scripts/` directory. But first, you'll need to copy it to
`/etc/NetworkManager/dispatcher.d/`.

```
	$ sudo su
	# cp scripts/10-uom-wifi.sh /etc/NetworkManager/dispatcher.d/
```

Then open it with your editor of choice:

```
	# cd /etc/NetworkManager/dispatcher.d/
	# vim 10-uom-wifi.sh
```

Change the path in `$ACTIVATION_SCRIPT` to point to the activate.sh in your filesystem.
Once you're done, save and exit. Then

```
	# chmod 700 10-uom-wifi.sh
	# exit
```

This is needed by NetworkManager (see `man 8 NetworkManager`).

### Note

This is quickly hacked together, so if it doesn't work, please let me know and
I'll see what I can do. Ofcourse, you're welcome to patch it and send me a pull
request.
