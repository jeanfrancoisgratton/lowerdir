all: 
	cd ../src
	CGO_ENABLED=0 go build . -o ./lowerdir.exe

prepare:
	sudo /opt/bin/install_golang.sh 1.20.4 amd64
	sudo apk update

install:
	test -d $(DESTDIR)$(PREFIX)/bin || mkdir -p $(DESTDIR)$(PREFIX)/bin
	install -pm 755 $(BUILDDIR)/lowerdir.exe $(DESTDIR)$(PREFIX)/bin/lowerdir
	strip $(DESTDIR)$(PREFIX)/bin/lowerdir
