all: install

install:
	mkdir -p ~/.local/bin
	cp swaybg-swapper.py ~/.local/bin
	cp systemd/swaybg-swapper.{service,timer} ~/.config/systemd/user/
	systemctl --user daemon-reload
	systemctl --user enable --now swaybg-swapper.timer

uninstall:
	rm -f ~/.local/bin/swaybg-swapper.py
	rmdir --ignore-fail-on-non-empty ~/.local/bin
	systemctl --user disable --now swaybg-swapper.timer
	rm -f ~/.config/systemd/user/swaybg-swapper.{service,timer}
	systemctl --user daemon-reload
