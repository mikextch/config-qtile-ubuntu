
from libqtile import layout
from settings.theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 2,
    'margin': 4
}

layout_monad_conf = {
    'max_ratio': 0.85,
    'min_ratio': 0.15
}
layout_monad_conf.update(layout_conf)

layouts = [
    layout.MonadTall(**layout_monad_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
    ],
    border_focus=colors["color4"][0]
)
