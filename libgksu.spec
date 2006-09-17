Summary:	libgksu library
Summary(pl):	Biblioteka libgksu
Name:		libgksu
Version:	1.9.8
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://people.debian.org/~kov/gksu/libgksu2/%{name}-%{version}.tar.gz
# Source0-md5:	5c11e93bfb599a4d6b785f73167f9243
URL:		http://www.nongnu.org/gksu/
BuildRequires:	glib2-devel >= 1:2.11.3
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgksu library.

%description -l pl
Biblioteka libgksu.

%package devel
Summary:	Header files for libgksu library
Summary(pl):	Pliki nag³ówkowe biblioteki libgksu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.11.3

%description devel
Header files for libgksu library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libgksu.

%package static
Summary:	Static libgksu library
Summary(pl):	Statyczna biblioteka libgksu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgksu library.

%description static -l pl
Statyczna biblioteka libgksu.

%prep
%setup -q -n %{name}-%{version}

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

%post -p /sbin/ldconfig
%gconf_schema_install gksu.schema

%postun	-p /sbin/ldconfig
%gconf_schema_uninstall gksu.schema

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%dir %{_datadir}/libgksu
%{_datadir}/libgksu/gksu-properties.glade
%{_desktopdir}/gksu-properties.desktop
%{_pixmapsdir}/gksu.png
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
