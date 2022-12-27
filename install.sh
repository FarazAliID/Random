clear
echo "\n[+] Updating all installed pkgs"
pkg update -y
echo "[+] Upgrading all installed pkgs"
pkg upgrade -y
echo "[+] Installing Python"
pkg install python -y
echo "[+] Installing pkg zip"
pkg install zip -y
echo "[+] Installing pkg play-audio"
pkg install play-audio -y
echo "[+] Installing python module requests"
python -m pip install requests
echo "[+] Installing Python module gtts"
python -m pip install gtts
echo "\n\n"
echo "Successfully Installed All pkgs & modules"
echo "Thank you Bro For Using My Tool <)<)"
echo "Type: 'python3 run.py' to run script"
