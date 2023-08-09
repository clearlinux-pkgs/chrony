#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : chrony
Version  : 4.4
Release  : 14
URL      : https://chrony-project.org/releases/chrony-4.4.tar.gz
Source0  : https://chrony-project.org/releases/chrony-4.4.tar.gz
Source1  : chrony.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: chrony-bin = %{version}-%{release}
Requires: chrony-config = %{version}-%{release}
Requires: chrony-data = %{version}-%{release}
Requires: chrony-license = %{version}-%{release}
Requires: chrony-man = %{version}-%{release}
Requires: chrony-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(libcap)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(nss)
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Adapting-to-Clear-Linux.patch

%description
What is chrony?
===============
chrony is a versatile implementation of the Network Time Protocol (NTP).
It can synchronise the system clock with NTP servers, reference clocks
(e.g. GPS receiver), and manual input using wristwatch and keyboard.
It can also operate as an NTPv4 (RFC 5905) server and peer to provide
a time service to other computers in the network.

%package bin
Summary: bin components for the chrony package.
Group: Binaries
Requires: chrony-data = %{version}-%{release}
Requires: chrony-config = %{version}-%{release}
Requires: chrony-license = %{version}-%{release}
Requires: chrony-services = %{version}-%{release}

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
Requires: chrony-man = %{version}-%{release}

%description doc
doc components for the chrony package.


%package license
Summary: license components for the chrony package.
Group: Default

%description license
license components for the chrony package.


%package man
Summary: man components for the chrony package.
Group: Default

%description man
man components for the chrony package.


%package services
Summary: services components for the chrony package.
Group: Systemd services
Requires: systemd

%description services
services components for the chrony package.


%prep
%setup -q -n chrony-4.4
cd %{_builddir}/chrony-4.4
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1691619444
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-user=chrony --enable-debug
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1691619444
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/chrony
cp %{_builddir}/chrony-%{version}/COPYING %{buildroot}/usr/share/package-licenses/chrony/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
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
/usr/lib/tmpfiles.d/chrony.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/chrony/chrony.conf

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/chrony/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/chrony/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chronyc.1
/usr/share/man/man5/chrony.conf.5
/usr/share/man/man8/chronyd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/chronyd.service
