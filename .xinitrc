if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

export XDG_DATA_DIRS=~/.local/share:/usr/local/share:/usr/share
export EDITOR=vim

xset s on
# For dimming the screen
# xset s 60 240
xset s 300
xss-lock dm-tool lock &
