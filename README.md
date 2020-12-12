## Display manager
[`LightDM`](https://www.archlinux.org/packages/extra/x86_64/lightdm/)

For locking use [`xss-lock`](https://www.archlinux.org/packages/community/x86_64/xss-lock/) (see setup in `~/.xinitrc`)

## Window Manager
[`qtile`](https://www.archlinux.org/packages/community/x86_64/qtile/)

Uses [`feh`](https://www.archlinux.org/packages/extra/x86_64/feh/) to setup wallpapers

Uses [`terminator`](# Terminal Emulators) as the main terminal

## Compositor
[`compton-tryone-git`](https://aur.archlinux.org/packages/compton-tryone-git/)

## Terminal Emulators
[`terminator`](https://www.archlinux.org/packages/community/any/terminator/)

[`alacritty`](https://www.archlinux.org/packages/community/x86_64/alacritty/)

## Shells
[`zsh`](https://www.archlinux.org/packages/extra/x86_64/zsh/)

`~/.zshrc` is already preconfigured to use the following plugins/themes (it uses the ~/.p10k.zsh` file as theme so that file is also needed along with the theme (see [Powerlevel10k](# Powelevel10k))

### Themes and Plugins
Zsh Manager

Install [`oh-my-zsh`](https://github.com/ohmyzsh/ohmyzsh) with
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

#### Powerlevel10k
Nice theme that speeds up zsh loading when lots of plugins are loaded

Install the fonts in `~/.local/share/fonts` with `fc-cache -fv` and then install [`powerlevel10k`](https://github.com/romkatv/powerlevel10k) with
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```
The configuration file for `powerlevel10k` is `~/.p10k.zsh` and already exists. You can reconfigure the theme with the command `p10k configure` (this will replace the `~/.p10k.zsh` with a new configuration


#### Zsh Autosuggestions

Install [`auto-suggestions`](https://github.com/zsh-users/zsh-autosuggestions) with
```
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

#### Zsh Syntax Highlighting

Install [`syntax-highlight`](https://github.com/zsh-users/zsh-syntax-highlighting) with 
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

## Text Editors
[`vim`](https://www.archlinux.org/packages/extra/x86_64/vim/)

[`sublime-text-3`](https://aur.archlinux.org/packages/sublime-text-3/)

## File Managers
[`nnn`](https://www.archlinux.org/packages/community/x86_64/nnn/)

## System Monitor
[`htop`](https://www.archlinux.org/packages/extra/x86_64/htop/)

## Calendar
[`calcurse`](https://www.archlinux.org/packages/community/x86_64/calcurse/)

## Misc
[`neofetch`](https://www.archlinux.org/packages/community/any/neofetch/)

To display images install [`w3m`](https://www.archlinux.org/packages/extra/x86_64/w3m/) and use with `neofetch --w3m /path/to/image` (see example `~/.zshrc`)
