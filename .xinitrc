if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

eval "$(ssh-agent)"

export XDG_DATA_DIRS=$HOME/.local/share:/usr/local/share:/usr/share
export EDITOR=nvim
export STARSHIP_CONFIG=$HOME/.config/starship/starship.toml

xset s on
# For dimming the screen
# xset s 60 240
xset s 300
xss-lock dm-tool lock &
