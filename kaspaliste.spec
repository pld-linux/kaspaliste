Summary:	The literature database
Summary(pl):	Baza danych literatury
Name:		kaspaliste
Version:	0.94
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://kaspaliste.sourceforge.net/%{name}-%{version}.tar.bz2
# Source0-md5:	f969e50c9731db2c2f07342062d5da84
Patch0:		%{name}-c++.patch
URL:		http://kaspaliste.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
Kaspaliste is a literature database. It handles all kinds of books,
articles, journals, webpages etc. But the database goes far beyond
simply storing bibliographical information. There is the possibility
to create annotated links between pieces of information (like the
content of a book chapter) and to group the links in categories.

%description -l pl
Kaspaliste to baza danych literatury. Obs³uguje wszystkie rodzaje
ksi±¿ek, artyku³ów, ¿urnali, stron WWW itp. Ponadto baza danych
wykracza daleko poza proste przechowywanie informacji
bibliograficznych. Umo¿liwia tworzenie opisanych odno¶ników miêdzy
czê¶ciami informacji (typu zawarto¶æ rozdzia³u ksi±¿ki) oraz
grupowanie odno¶ników w kategorie.

%prep
%setup -q
%patch -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-pg-libs=/usr/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO data/create.tables.sql
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Applications/*
%{_datadir}/apps/kaspaliste
%{_datadir}/config/kaspalisterc
%{_pixmapsdir}/[!l]*/*/*/*
