#-e option instructs bash to immediately exit if any command [1] has a non-zero exit status
# We do not want users to end up with a partially working install, so we exit the script
# instead of continuing the installation with something broken
set -e

echo "Watchman Service Installer"
echo "*****RUN THIS SCRIPT AS A ROOT USER*****"
echo "This script will:"
echo "Clone and Install the Watchman Service"
echo "Put the Watchman Service in the startup sequence of the raspberry pi"

######## VARIABLES #########

# Location for final installation log storage
#installLogLoc=/etc/pihole/install.log


echo "Welcome user"
echo $USER
cd $HOME

show_ascii_berry() {
    echo -e "

Watchman Service Installer

    "
}
show_ascii_berry

if [ -d "$HOME/WatchmanService" ]
then
    echo "Directory RPiClient exists."
else
    echo "Error: Directory RPiClient does not exists."
    cd $HOME
    # mkdir ~/RPiClient
    git clone \
    https://github.com/Nauman3S/WatchmanService;
    cd WatchmanService
    sudo cp WatchmanService.conf /boot/
    
fi
if [ -d "$HOME/WatchmanService/logs" ]
then
    echo "Directory WatchmanService/logs exists."
else
    echo "Error: Directory RPiClient does not exists."
    mkdir $HOME/WatchmanService/logs
fi

File="/etc/rc.local"

if [[ $(grep "(sleep 8; sh /home/pi/WatchmanService/starter.sh)&" $File) ]] ; then
    echo "Found startup script. Doing nothing."
else
    echo "Not Found. Adding startup script"
    sed -i -e '$i \(sleep 8; sh /home/pi/WatchmanService/starter.sh)&\n' /etc/rc.local
fi



echo "Installtion Completed. Restart your Raspberry Pi"