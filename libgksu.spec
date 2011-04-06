Summary:	libgksu library
Summary(pl.UTF-8):	Biblioteka libgksu
Name:		libgksu
Version:	2.0.12
Release:	4
License:	LGPL v2
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/%{name}-%{version}.tar.gz
# Source0-md5:	c7154c8806f791c10e7626ff123049d3
Patch0:		%{name}-configure.patch
Patch1:		%{name}-helper.patch
Patch2:		am.patch
URL:		http://www.nongnu.org/gksu/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool
BuildRequires:	libgtop-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgksu library.

%description -l pl.UTF-8
Biblioteka libgksu.

%package devel
Summary:	Header files for libgksu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgksu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel
Requires:	glib2-devel >= 1:2.12.0
Requires:	gnome-keyring-devel
Requires:	startup-notification-devel

%description devel
Header files for libgksu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgksu.

%package static
Summary:	Static libgksu library
Summary(pl.UTF-8):	Statyczna biblioteka libgksu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgksu library.

%description static -l pl.UTF-8
Statyczna biblioteka libgksu.

%package apidocs
Summary:	libgksu library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgksu
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgksu library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgksu.

%package utils
Summary:	GKSu properties utility
Summary(pl.UTF-8):	Aplikacja właściwości GKSu
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}

%description utils
This program allows you to define how GKSu grants the privileges and
locks input devices.

%description utils -l pl.UTF-8
Ten program pozwala zdefiniować jak GKSu przyznaje uprawnienia i
blokuje urządzenia wejściowe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gtkdocize} --docdir docs/
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgksu2.la

%find_lang libgksu

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post utils
%gconf_schema_install gksu.schemas

%preun utils
%gconf_schema_uninstall gksu.schemas

%files -f libgksu.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libgksu2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgksu2.so.0
%dir %{_libdir}/libgksu
%attr(755,root,root) %{_libdir}/libgksu/gksu-run-helper

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgksu2.so
%{_includedir}/libgksu
%{_pkgconfigdir}/libgksu2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgksu2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgksu

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gksu-properties
%{_desktopdir}/gksu-properties.desktop
%dir %{_datadir}/libgksu
%{_datadir}/libgksu/gksu-properties.ui
%{_mandir}/man1/gksu-properties.1*
%{_pixmapsdir}/gksu.png
%{_sysconfdir}/gconf/schemas/gksu.schemas
