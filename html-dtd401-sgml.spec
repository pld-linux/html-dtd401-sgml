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
Summary(pl):	HTML %{v_er}
Name:		html-dtd%{ver}-sgml
Version:	%{year}%{month}%{day}
Release:	5
Group:		Applications/Publishing/SGML
License:	W3C
Vendor:		W3C
Source0:	http://www.w3.org/TR/%{year}/%{type}-html%{ver}-%{version}/html%{mver}.tgz
# Source0-md5:	1ed76627ba80816079649f67023ec7ab
URL:		http://www.w3.org/TR/html
Requires:	sgml-common >= 0.5
Requires:	sgmlparser
Provides:	html-dtd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
AutoReqProv:	0

%description
HTML specification (with DTD, needed to parse HTML code).

%description -l pl
Specyfikacja HTML (wraz z DTD, potrzebnym do sprawdzania poprawno¶ci
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

rm -f *.cat


%post
/usr/bin/install-catalog --add /etc/sgml/html-%{v_er}.cat /usr/share/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%postun
/usr/bin/install-catalog --remove /etc/sgml/html-%{v_er}.cat /usr/share/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
%{_datadir}/sgml/html/*
