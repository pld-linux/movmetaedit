# TODO: system libzen
Summary:	Embed and edit MOV files metadata
Summary(pl.UTF-8):	Osadzanie i modyfikowanie metadanych w plikach MOV
Name:		movmetaedit
Version:	17.10.1
Release:	1
License:	MIT
Group:		Applications/Multimedia
Source0:	https://mediaarea.net/download/source/movmetaedit/%{version}/%{name}_%{version}.tar.xz
# Source0-md5:	f18e979052a8e52bc8e350cedf5db4b3
URL:		https://mediaarea.net/MOVMetaEdit
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MOV MetaEdit is a tool that supports the embedding and editing of
metadata in MOV (Apple QuickTime) or MP4 (ISO/IEC 14496-14 a.k.a.
MPEG-4 Part 14) files. It is currently focused on Universal Ad ID
metadata but could be expanded on request.

%description -l pl.UTF-8
MOV MetaEdit to narzędzie obsługujące osadzanie i modyfikowanie
metadanych w plikach MOV (Apple QuickTime) lub MP4 (ISO/IEC 14496-14,
znanych także jako MPEG-4 Part 14). Obecnie skupia się na metadanych
Universal Ad ID, ale w razie potrzeby może być rozszerzone.

%package gui
Summary:	GUI to embed and edit MOV files metadata
Summary(pl.UTF-8):	Graficzny interfejs do osadzania i modyfikowania metadanych w plikach MOV
Group:		X11/Applications/Multimedia

%description gui
MOV MetaEdit is a tool that supports the embedding and editing of
metadata in MOV (Apple QuickTime) or MP4 (ISO/IEC 14496-14 a.k.a.
MPEG-4 Part 14) files. It is currently focused on Universal Ad ID
metadata but could be expanded on request.

%description gui -l pl.UTF-8
MOV MetaEdit to narzędzie obsługujące osadzanie i modyfikowanie
metadanych w plikach MOV (Apple QuickTime) lub MP4 (ISO/IEC 14496-14,
znanych także jako MPEG-4 Part 14). Obecnie skupia się na metadanych
Universal Ad ID, ale w razie potrzeby może być rozszerzone.

%prep
%setup -q -n movmetaedit
%undos *.html *.txt
chmod 644 *.html *.txt

%build
# build CLI
cd Project/GNU/CLI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

# now build GUI
cd ../../../Project/Qt
qmake-qt5 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Project/GNU/CLI install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_iconsdir}/hicolor/128x128/apps}
install Project/Qt/movmetaedit-gui $RPM_BUILD_ROOT%{_bindir}
cp -p Project/Qt/movmetaedit-gui.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p Source/Resource/Image/Icon.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps/movmetaedit.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.html History_CLI.txt LICENSE License.html README.md
%attr(755,root,root) %{_bindir}/movmetaedit

%files gui
%defattr(644,root,root,755)
%doc License.html History_GUI.txt LICENSE License.html README.md
%attr(755,root,root) %{_bindir}/movmetaedit-gui
%{_desktopdir}/movmetaedit-gui.desktop
%{_iconsdir}/hicolor/128x128/apps/movmetaedit.png
