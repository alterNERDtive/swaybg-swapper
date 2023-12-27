# swaybg-swapper

A simple Python systemd service for swapping `swaybg` backgrounds on the fly.

## What Does It Do?

It kills the running `swaybg` process and starts a new one with backgrounds 
chosen randomly from the configuration file.

That’s it. Nothing fancy.

## Why Should I Use This?

Eh, you don’t have to. I was looking for a way to change my wallpaper at set 
intervals that

* supported multi-monitor setups properly,
* didn’t reinvent the wallpaper wheel, instead used `swaybg` in the background,
* integrated nicely with systemd (which I use to run _all_ my desktop related 
  things) and
* just worked.

That didn’t seem to exist, so I made it. And since I’m _probably_ not the only 
one looking for it, here it is. Have fun!

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

You probably also want to start the service when sway starts. There are various 
ways to do that. If you want to keep it simple, `exec` a simple `systemctl
--user start swaybg-swapper.timer` in your sway config. If you want to do it 
“right”, set up some `sway-session.target` and a drop-in config for the service 
that binds it to that, then have sway run the target on startup.

If you want to do it in any other way, go ahead! I’m not your dad. At least I’m 
fairly confident that I’m not.

## Known Issues

Since I have hacked this in a couple hours from concept to “eh, works well 
enough”, it is not very resilient. You mess up the timer/service, you have 
syntax errors in your configuration file … it will just die instead of spawning 
a `swaybg` process.

On the plus side, you’ll notice when it doesn’t work. Since, you know, you don’t 
get your wallpapers.

## How Do I Get Rid Of It?

You could just disable the timer.

To uninstall it completely, run `make uninstall`. That will remove the script 
from `~/.local/bin` and remove the systemd service/timer.

It will _not_ delete your drop-in configuration files (e.g. see 4. above).
