import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

mod = 'mod4'
terminal = 'terminator'
terminal_class = 'Terminator'
browser = 'brave'
file_browser = terminal + ' -T nnn -x nnn -de'
sys_monitor = terminal + ' -T htop -x htop'
sys_monitor_floating = terminal + ' -T htop-floating -x htop'
editor = terminal + ' -T neovim -x nvim'
code = 'subl'
drun = 'rofi -modi drun -show drun'
sound_floating = terminal + ' -T alsamixer-floating -x alsamixer'
calendar = terminal + ' -T calcurse -x calcurse'
calendar_floating = terminal + ' -T calcurse-floating -x calcurse'

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus down in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "Left", lazy.layout.left(),
        desc="Move focus down in stack pane"),
    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus up in stack pane"),
    
    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn(browser), desc="Spawn browser"),
    Key([mod], "e", lazy.spawn(editor), desc="Spawn editor"),
    Key([mod], "m", lazy.spawn(sys_monitor),
        desc="Spawn system monitor"),
    Key([mod], "d", lazy.spawn(code),
        desc="Spawn code"),
    Key([mod], "c", lazy.spawn(calendar),
        desc="Spawn calendar"),
    Key([mod], 'f', lazy.spawn(file_browser),
        desc='Spawn file browser'),
    Key([mod, 'shift'], 'Return', lazy.spawn(drun),
        desc='Spawn drun'),
    Key([mod], "s", lazy.spawn(sound_floating),
        desc="Spawn sound"),

    Key([], 'XF86AudioLowerVolume',
        lazy.spawn('amixer -q sset Master 10%-'),
        desc='Decrease volume'),
    Key([], 'XF86AudioRaiseVolume',
            lazy.spawn('amixer -q sset Master 10%+'),
        desc='Increase volume'),
    Key([], 'XF86ScreenSaver',
            lazy.spawn('dm-tool lock'),
        desc='Lock screen'),
]

groups = ['dev', 'sys', 'www', 'msg', 'etc', '6', '7']
groups = list(map(Group, groups))


for i, g in enumerate(groups):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i + 1), lazy.group[g.name].toscreen(),
            desc="Switch to group {}".format(g.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i + 1), lazy.window.togroup(g.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(g.name)),
    ])

# colors = ['#2a2d38', '#ffffff', '#b566ff', '#8c8c8c', '#fa4175']
colors = dict(
    bg = '#2a2d38',
    fg = '#ffffff',
    main_bg = '#d026b6',
    inactive_fg = '#8c8c8c',
    urgent_bg = '#ff0000',
    urgent_fg = '#ff3344',
)

layout_defaults = dict(
    margin = 5,
    border_width = 1,
    border_focus = colors['main_bg'],
    border_normal = colors['bg']
)

layouts = [
    layout.Bsp(**layout_defaults),
    layout.Max(**layout_defaults),
    #layout.Stack(num_stacks=2, **layout_defaults),
    #layout.Columns(**layout_defaults),
    #layout.Matrix(**layout_defaults),
    #layout.MonadTall(**layout_defaults),
    #layout.MonadWide(**layout_defaults),
    #layout.RatioTile(**layout_defaults),
    #layout.Tile(**layout_defaults),
    #layout.TreeTab(**layout_defaults),
    #layout.VerticalTile(**layout_defaults),
    #layout.Zoomy(**layout_defaults),
]

widget_defaults = dict(
    font='MesloLGS NF',
    fontsize=12,
    padding=0,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    ' ',
                    foreground = colors['main_bg'],
                    background = colors['main_bg'],
                ),
                widget.CurrentLayoutIcon(
                    foreground =colors['fg'],
                    background =colors['main_bg'],
                    scale = 0.7
                ),
                widget.TextBox(
                    ' ',
                    fontsize = 20,
                    foreground = colors['bg'],
                    background = colors['main_bg'],
                ),
                widget.TextBox(
                    ' ',
                    fontsize = 20,
                    foreground = colors['bg'],
                    background = colors['bg'],
                ),
                widget.GroupBox(
                    block_highlight_text_color = colors['fg'],
                    this_current_screen_border = colors['main_bg'],
                    highlight_method = 'block',
                    disable_drag = True,
                    padding = 4,
                    background = colors['bg'],
                    inactive = colors['inactive_fg'],
                    urgent_border = colors['urgent_bg'],
                    urgent_text = colors['urgent_fg']
                ),
                widget.Prompt(
                    prompt = '  ',
                    foreground = colors['fg'],
                    background = colors['bg']
                ),
                widget.TextBox(
                    ' 类 ',
                    fontsize = 17,
                    foreground = colors['fg'],
                    background = colors['bg'],
                ),
                widget.WindowName(
                    foreground = colors['fg'],
                    background = colors['bg']
                ),
                widget.Chord(
                    chords_colors = {
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform = lambda name: name.upper(),
                ),
                widget.TextBox(
                    ' ',
                    fontsize = 20,
                    foreground = colors['main_bg'],
                    background = colors['bg'],
                ),
                widget.TextBox(
                    '  ',
                    fontsize = 17,
                    foreground = colors['fg'],
                    background = colors['main_bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(sys_monitor_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(sys_monitor_floating)
                    }
                ),
                widget.Memory(
                    fmt = '{:^6}',
                    format = '{MemPercent:4.1f}%',
                    foreground = colors['fg'],
                    background = colors['main_bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(sys_monitor_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(sys_monitor_floating)
                    }
                ),
                widget.TextBox(
                    ' ',
                    fontsize = 20,
                    foreground = colors['bg'],
                    background = colors['main_bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(sys_monitor_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(sys_monitor_floating)
                    }
                ),
                widget.TextBox(
                    '  ',
                    fontsize = 17,
                    foreground = colors['fg'],
                    background = colors['bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(sys_monitor_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(sys_monitor_floating)
                    }
                ),
                widget.CPU(
                    fmt = '{:^7}',
                    format = '{load_percent:4.1f}% ',
                    padding = 0,
                    foreground = colors['fg'],
                    background = colors['bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(sys_monitor_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(sys_monitor_floating)
                    }
                ),
                widget.TextBox(
                    '',
                    fontsize = 20,
                    foreground = colors['main_bg'],
                    background = colors['bg'],
                ),
                widget.Volume(
                    emoji = True,
                    fmt = ' {} ',
                    fontsize = 15,
                    foreground = colors['fg'],
                    background = colors['main_bg'],
                    update_interval = 1,
                ),
                widget.TextBox(
                    '',
                    fontsize = 20,
                    foreground = colors['bg'],
                    background = colors['main_bg'],
                ),
                widget.Battery(
                    battery = 'BAT1',
                    format = ' {char} {percent:2.0%}',
                    background = colors['bg'],
                    foreground = colors['fg'],
                    charge_char = '',
                    discharge_char = '',
                    empty_char = '',
                    full_char = '',
                    unknown_char = '',
                    low_foreground = colors['urgent_fg'],
                    update_interval = 30
                    ),
                widget.TextBox(
                    ' ',
                    fontsize = 20,
                    foreground = colors['main_bg'],
                    background = colors['bg'],
                ),
                widget.TextBox(
                    '  ',
                    fontsize = 17,
                    foreground = colors['fg'],
                    background = colors['main_bg'],
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(calendar_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(calendar_floating)
                    }
                ),
                widget.Clock(
                    format = '%a %d %b %H:%M',
                    foreground = colors['fg'],
                    background = colors['main_bg'],
                    padding = 4,
                    mouse_callbacks = {
                        'Button1': lambda qtile: qtile.cmd_spawn(calendar_floating),
                        'Button3': lambda qtile: qtile.cmd_spawn(calendar_floating)
                    }
                ),
                widget.Systray(padding = 4),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating( 
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ],
    **layout_defaults
)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    w_name = window.window.get_name()
    w_class = set(window.window.get_wm_class())
    
    if dialog or transient:
        window.floating = True
    elif 'Terminator Preferences' == w_name and 'terminator' in w_class:
        window.floating = True
    elif 'htop-floating' == w_name and terminal_class in w_class:
        window.floating = True
    elif 'calendar-floating' == w_name and terminal_class in w_class:
        window.floating = True
    elif 'alsamixer-floating' == w_name and terminal_class in w_class:
        window.floating = True
    elif 'htop' == w_name and terminal_class in w_class:
        window.togroup('sys', switch_group=True)
    elif 'brave-browser' in w_class:
        window.togroup('www', switch_group=True)
    elif 'subl' in w_class:
        window.togroup('dev', switch_group=True)

@hook.subscribe.startup
def setup_wallpaper():
    wallpaper_path = '~/.local/share/backgrounds/6.png'
    wallpaper_path = os.path.expanduser(wallpaper_path)
    qtile.cmd_spawn([
        'feh', '--bg-scale', '--randomize', wallpaper_path
    ])

@hook.subscribe.startup
def setup_compositor():
    config_path = '~/.config/compton/compton.conf'
    config_path = os.path.expanduser(config_path)
    qtile.cmd_spawn([
        'compton', '--config', config_path
    ])
