Name:      DVDStyler
Version:   1.4
Release:   1
Summary:	DVDStyler is a cross-platform DVD authoring System
Summary(pl):   Wieloplatformowy program do auhoringu DVD
License:   GPL
Group:     Applications/Multimedia
Packager:  <pld@vp.pl>
Source:   http://mesh.dl.sourceforge.net/sourceforge/dvdstyler/%{name}-%{version}.tar.gz
URL:      http://dvdstyler.sourceforge.net

BuildRequires: dvdauthor >= 0.6.10
BuildRequires: gtk+2-devel >= 2.2.0
BuildRequires: wxGTK2-devel >= 2.4.2
BuildRequires: mjpegtools
BuildRequires: mpgtx
BuildRequires: dvd+rw-tools

BuildRoot: %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVDStyler is a crossplatform dvd authoring system.
The main DVDStyler features are:
* you can drag and drop MPEG files directly
* you can import image file for background
* you can create NTSC/PAL menu
* you can place text and images anywhere on the menu screen
* you can change font/color
* you can put basic text buttons, change font/color and background color
* you can set chapters for each movie
* you can change post command for each movie

%prep
%setup

%build
%configure --with-wx-config=/usr/bin/wx-gtk2-ansi-config 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/dvdstyler
/usr/share/doc/dvdstyler/*
/usr/share/dvdstyler/*
/usr/share/locale/*
%{_pixmapsdir}/*
