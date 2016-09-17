Summary:	Manage iPhone/iPod Touch SpringBoard icons from the computer
Name:		sbmanager
Version:	0.1.8
Release:	0.3
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/gitsop01/sbmanager/archive/f9ed226b/%{name}-%{version}.tar.gz
# Source0-md5:	c88829b79f434d465aae806392534c93
Patch0:		pkg-config.patch
URL:		https://github.com/libimobiledevice/sbmanager
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	clutter-devel >= 1.0.6
BuildRequires:	clutter-gtk-devel >= 0.10
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gtk+2-devel >= 2:2.16
BuildRequires:	intltool
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libplist-devel >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildConflicts:	Mesa-libGL-devel < 7.8.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBManager is a program which allows to manage the SpringBoard icons on
any iPhone/iPod Touch device running firmware 3.1 or later.

%prep
%setup -qc
mv sbmanager-*/* .
%{__sed} -i -e s/-Werror// configure.ac
%patch0 -p1

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	libbz2_LIBS="-lbz2" libbz2_CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/sbmanager
%{_desktopdir}/sbmanager.desktop
%dir %{_datadir}/sbmanager
%{_datadir}/sbmanager/background.png
%{_datadir}/sbmanager/dot.png
%{_datadir}/sbmanager/folder.png
%{_datadir}/sbmanager/foldermarker.png
%{_datadir}/sbmanager/iconshadow.png
