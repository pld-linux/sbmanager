Summary:	Manage iPhone/iPod Touch SpringBoard icons from the computer
Name:		sbmanager
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}.tar.bz2
# Source0-md5:	21a2b982075b3dc6afc0b32c706950ce
URL:		http://www.libimobiledevice.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBManager is a program which allows to manage the SpringBoard icons on
any iPhone/iPod Touch device running firmware 3.1 or later.

%prep
%setup -q -n %{name}
%{__sed} -i -e s/-Werror// configure.ac

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
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
