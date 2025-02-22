from libqtile.layout.floating   import Floating
from libqtile.config            import Click, Drag, Match
from libqtile.lazy              import lazy
from colours                    import colours 

colours = colours

mod = "mod4"

    # Drag floating layouts.
mouse = [
         Drag( [mod], "Button1",  lazy.window.set_position_floating(),    start=lazy.window.get_position()),
         Drag( [mod], "Button3",  lazy.window.set_size_floating(),        start=lazy.window.get_size()),
         Click([mod], "Button2",  lazy.window.bring_to_front()),
        ]

floating_layout = Floating(
    float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client. #
            #          I've never used these but I don't want to delete them!         #
        *Floating.default_float_rules,
        Match(wm_class  = "confirmreset"),  # gitk
        Match(wm_class  = "makebranch"),    # gitk
        Match(wm_class  = "maketag"),       # gitk
        Match(wm_class  = "ssh-askpass"),   # ssh-askpass
        Match(title     = "branchdialog"),  # gitk
        Match(title     = "pinentry"),      # GPG key password entry
                ],
        border_focus   = colours[1], 
        border_normal  = colours[4],
                          )
