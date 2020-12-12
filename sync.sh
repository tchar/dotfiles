mkdir -p .config
mkdir -p .local/share/backgrounds

rsync -v -r ~/.config/alacritty .config
rsync -v -r ~/.config/compton .config
rsync -v -r ~/.config/rofi .config
rsync -v -r ~/.config/neofetch .config
rsync -v -r --exclude '__pycache__' --exclude '*.pyc' ~/.config/qtile .config
rsync -v -r ~/.config/terminator .config

rsync -v -r ~/.local/share/backgrounds/6.png .local/share/backgrounds
rsync -v -r ~/.local/share/fonts .local/share

rsync -v -r ~/.xinitrc .
rsync -v -r ~/.xprofile .

rsync -v -r ~/.p10k.zsh .
rsync -v -r ~/.zshrc .

rsync -v -r ~/.vimrc .
