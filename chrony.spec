#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5FF06F29BA1E013B (mlichvar@redhat.com)
#
Name     : chrony
Version  : 3.2
Release  : 2
URL      : https://download.tuxfamily.org/chrony/chrony-3.2.tar.gz
Source0  : https://download.tuxfamily.org/chrony/chrony-3.2.tar.gz
Source1  : chrony.tmpfiles
Source99 : https://download.tuxfamily.org/chrony/chrony-3.2.tar.gz.asc
Summary  : An NTP client/server
Group    : Development/Tools
License  : GPL-2.0
Requires: chrony-bin
Requires: chrony-config
Requires: chrony-data
Requires: chrony-doc
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(nss)
BuildRequires : readline-dev
Patch1: 0001-Adapting-to-Clear-Linux.patch

%description
chrony is a client and server for the Network Time Protocol (NTP).
This program keeps your computer's clock accurate. It was specially
designed to support systems with intermittent Internet connections,
but it also works well in permanently connected environments. It can
also use hardware reference clocks, the system real-time clock, or
manual input as time references.

%package bin
Summary: bin components for the chrony package.
Group: Binaries
Requires: chrony-data
Requires: chrony-config

%description bin
bin components for the chrony package.


%package config
Summary: config components for the chrony package.
Group: Default

%description config
config components for the chrony package.


%package data
Summary: data components for the chrony package.
Group: Data

%description data
data components for the chrony package.


%package doc
Summary: doc components for the chrony package.
Group: Documentation

%description doc
doc components for the chrony package.


%prep
%setup -q -n chrony-3.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518124725
%configure --disable-static --with-user=chrony --enable-debug
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1518124725
rm -rf %{buildroot}
%make_install install-service install-conf install-examples
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/chrony.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chronyc
/usr/bin/chronyd

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/chronyd.service
/usr/lib/tmpfiles.d/chrony.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/chrony/chrony.conf

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/chrony/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
