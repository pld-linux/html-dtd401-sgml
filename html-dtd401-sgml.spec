# TODO
# - make install re-entrant

%define		major	4
%define		minor	0
%define		micro	1
%define		type	REC
%define		year	1999
%define		month	12
%define		day	24

%define		mver	%{major}%{minor}
%define		ver	%{major}%{minor}%{micro}
%define		v_er	%{major}.%{minor}%{micro}
%define		v__er	%{major}\.%{minor}%{micro}
Summary:	HTML %{v_er}
Summary(pl.UTF-8):	HTML %{v_er}
Name:		html-dtd%{ver}-sgml
Version:	%{year}%{month}%{day}
Release:	7
License:	W3C
Group:		Applications/Publishing/SGML
Source0:	http://www.w3.org/TR/%{year}/%{type}-html%{ver}-%{version}/html%{mver}.tgz
# Source0-md5:	1ed76627ba80816079649f67023ec7ab
URL:		http://www.w3.org/TR/html/
Requires:	sgml-common >= 0.6.3-5
Requires:	sgmlparser
Provides:	html-dtd
AutoReqProv:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML specification (with DTD, needed to parse HTML code).

%description -l pl.UTF-8
Specyfikacja HTML (wraz z DTD, potrzebnym do sprawdzania poprawności
kodu HTML).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}

mv *.ent *.dtd *.decl $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}

grep -v OVERRIDE *.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog
## add alias for 4.0
grep -v OVERRIDE *.cat | grep '%{v__er}' | sed 's/%{v__er}/4.0/g' \
       >> $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog

# used in %doc
rm -f *.cat

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/install-catalog --add %{_sysconfdir}/sgml/html-%{v_er}.cat %{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%postun
%{_bindir}/install-catalog --remove %{_sysconfdir}/sgml/html-%{v_er}.cat %{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%files
%defattr(644,root,root,755)
%doc *
%{_datadir}/sgml/html/*
