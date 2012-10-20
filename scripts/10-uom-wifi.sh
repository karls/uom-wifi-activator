#!/bin/sh -e

# Activation script for UoM_WIFI
# Put this in /etc/NetworkManager/dispatcher.d/

SSID='UoM_WIFI'

# You should change the ACTIVATION_SCRIPT variable to point to the activate.sh
# script that does the actual activation

# Change me
ACTIVATION_SCRIPT="/home/karl/dev/uom-wifi-activator/scripts/activate.sh"

case $2 in
	"up" )	if [ $CONNECTION_ID = $SSID ]; then
			$ACTIVATION_SCRIPT
		fi
		;;
esac
exit 0
