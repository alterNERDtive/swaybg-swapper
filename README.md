# swaybg-swapper

A simple Python systemd service for swapping `swaybg` backgrounds on the fly.

## What Does It Do?

It kills the running `swaybg` process and starts a new one with backgrounds 
chosen randomly from the configuration file.

That’s it. Nothing fancy.

## How Does It Work?

1. Copy `backgrounds.example.json` to `~/config/sway/backgrounds.json`.
2. Edit to your heart’s content. The example should be fairly self-explanatory, 
   it’s not exactly rocket science. Nor rockets, nor science :)
3. Run `make` or `make install`. That will copy the script to `~/.local/bin`, 
   set up the systemd user service and enable its timer.
4. By default the service will change your wallpapers every 60 minutes. To 
   customize that, copy `timer.example.conf` to 
   `~/.config/systemd/user/swaybg-swapper.timer.d/timer.conf` and edit the `60m` 
   timer to your desire.

You probably also want a way to start the service when sway starts. There are 
various ways to do that. If you want to keep it simple, `exec` a simple 
`systemctl --user start swaybg-swapper.service` in your sway config. If you want 
to do it “right”, set up some `sway-session.target` and a dropin config for the 
service that binds it to that, then have sway run the target on startup. If you 
want to do it in any other way, go ahead!

## How Do I Get Rid Of It?

You could just disable the timer.

To uninstall it completely, run `make uninstall`. That will remove the script 
from `~/.local/bin` and remove the systemd service/timer.

It will _not_ delete your drop-in configuration files (e.g. see 4. above).
