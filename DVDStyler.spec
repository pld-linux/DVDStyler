Summary:	DVDStyler is a cross-platform DVD authoring System
Summary(pl.UTF-8):	Wieloplatformowy program do authoringu DVD
Name:		DVDStyler
Version:	1.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/dvdstyler/%{name}-%{version}.tar.gz
# Source0-md5:	2e8ee561c56cf968516bc3e7cf20e96f
URL:		http://dvdstyler.sourceforge.net
BuildRequires:	dvd+rw-tools
BuildRequires:	dvdauthor >= 0.6.10
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	mjpegtools
BuildRequires:	mpgtx
BuildRequires:	wxGTK2-devel >= 2.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVDStyler is a crossplatform dvd authoring system. The main DVDStyler
features are:
- you can drag and drop MPEG files directly
- you can import image file for background
- you can create NTSC/PAL menu
- you can place text and images anywhere on the menu screen
- you can change font/color
- you can put basic text buttons, change font/color and background
  color
- you can set chapters for each movie
- you can change post command for each movie

%description -l pl.UTF-8
DVDStyler to wieloplatformowy system do tworzenia DVD. Główne cechy
DVDStylera to:
- można bezpośrednio przeciągać i upuszczać pliki MPEG
- można importować pliki obrazów jako tło
- można tworzyć menu NTSC/PAL
- można umieszczać tekst i obrazki w dowolnym miejscu ekranu menu
- można zmieniać font/kolor
- można umieszczać podstawowe przyciski tekstowe, zmieniać font/kolor
  oraz kolor tła
- można ustawiać rozdziały dla każdego filmu
- można zmieniać polecenie do wykonania po odtworzeniu każdego filmu

%prep
%setup -q

%build
%configure \
	--with-wx-config=%{_bindir}/wx-gtk2-ansi-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# name needs check
%find_lang dvdstyler

%clean
rm -rf $RPM_BUILD_ROOT

%files -f dvdstyler.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/dvdstyler
%{_datadir}/dvdstyler
%{_pixmapsdir}/*
