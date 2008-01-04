# TODO:
# - real descriptions for utils package
# - check what the utils does
#
Summary:	libgksu library
Summary(pl.UTF-8):	Biblioteka libgksu
Name:		libgksu
Version:	2.0.5
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/%{name}-%{version}.tar.gz
# Source0-md5:	93f61258751eb7396721281f8f784c46
URL:		http://www.nongnu.org/gksu/
BuildRequires:	GConf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.11.3
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgtop-devel
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
Requires:	glib2-devel >= 1:2.11.3

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

%package utils
Summary:	Gksu properties utility
Summary(pl.UTF-8):	Aplikacja właściwości gksu
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description utils
Gksu properties utility.

%description utils -l pl.UTF-8
Aplikacja właściwości gksu.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post utils
%gconf_schema_install

%postun utils
%gconf_schema_uninstall

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/gksu-run-helper

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}*
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gksu-properties
%{_desktopdir}/gksu-properties.desktop
%dir %{_datadir}/libgksu
%{_datadir}/libgksu/gksu-properties.glade
%{_pixmapsdir}/gksu.png
%{_sysconfdir}/gconf/schemas/gksu.schemas
