%define		major 4
%define		minor 0
%define		micro 1

%define		mver	%{major}%{minor}
%define		ver	%{major}%{minor}%{micro}
%define		v_er	%{major}.%{minor}%{micro}
%define		v__er	4\.01
Summary:	HTML %{v_er}
Summary(pl):	HTML %{v_er}
Name:		html-dtd%{ver}-sgml
Version:	1.0
Release:	4
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Copyright:	W3C
Vendor:		W3C
Source0:	http://www.w3.org/TR/html4/html%{mver}.tgz
URL:		http://www.w3.org/TR/html4/
Requires:	sgml-common >= 0.5
Requires:	sgmlparser
Provides:	html-dtd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
HTML specification (with DTD, needed to parse HTML code).

%description -l pl
Specyfikacja HTML (wraz z DTD, potrzebnym do sprawdzania
poprawności kodu HTML).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}

mv *.ent *.dtd *.decl $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}

grep -v OVERRIDE *.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog
# add alias for 4.0
grep -v OVERRIDE *.cat | grep '%{v__er}' | sed 's/%{v__er}/4.0/g' \
       >> $RPM_BUILD_ROOT%{_datadir}/sgml/html/sgml-dtd-%{v_er}/catalog
rm -f *.cat


%post
/usr/bin/install-catalog --add /etc/sgml/html-%{ver}.cat /usr/share/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%postun
/usr/bin/install-catalog --remove /etc/sgml/html-%{ver}.cat /usr/share/sgml/html/sgml-dtd-%{v_er}/catalog > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
%{_datadir}/sgml/html/*
