all: install

install:
	mkdir -p ~/.local/bin
	cp swaybg-swapper.py ~/.local/bin
	cp systemd/swaybg-swapper.{service,timer} ~/.config/systemd/user/
	systemctl --user daemon-reload
	systemctl --user enable --now swaybg-swapper.timer
