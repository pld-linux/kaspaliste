Summary:	The literature database
Summary(pl.UTF-8):   Baza danych literatury
Name:		kaspaliste
Version:	0.96
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kaspaliste/%{name}-%{version}.tar.gz
# Source0-md5:	6256575740bb4bc5aa542f10e749bc01
Patch0:		%{name}-c++.patch
URL:		http://kaspaliste.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	postgresql-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kaspaliste is a literature database. It handles all kinds of books,
articles, journals, webpages etc. But the database goes far beyond
simply storing bibliographical information. There is the possibility
to create annotated links between pieces of information (like the
content of a book chapter) and to group the links in categories.

%description -l pl.UTF-8
Kaspaliste to baza danych literatury. Obsługuje wszystkie rodzaje
książek, artykułów, żurnali, stron WWW itp. Ponadto baza danych
wykracza daleko poza proste przechowywanie informacji
bibliograficznych. Umożliwia tworzenie opisanych odnośników między
częściami informacji (typu zawartość rozdziału książki) oraz
grupowanie odnośników w kategorie.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure2_13 \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--with-pg-libs=/usr/lib

%{__make} \
	CXX="%{__cxx}"

echo 'Categories=Office' >> $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/%{name}.desktop \
   $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO data/create.tables.sql
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/kaspaliste
%{_datadir}/config/kaspalisterc
%{_iconsdir}/hicolor/*/apps/*.png
