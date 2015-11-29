# TODO: missing dir (see files)
%define		pname	testoob
Summary:	An advanced unit testing framework for Python
Summary(pl.UTF-8):	Zaawansowany framework testów jednostkowych dla Pythona
Name:		python-testoob
Version:	1.13
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/testoob/%{pname}-%{version}.tar.gz
# Source0-md5:	92cbf328647488ed21a55cfe0f74b2cf
Patch0:		%{pname}-pyo.patch
URL:		http://testoob.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:  rpm-pythonprov
%pyrequires_eq  python-modules
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Testoob is an advanced unit testing framework for Python. It
integrates effortlessly with existing PyUnit (module "unittest") test
suites.

%description -l pl.UTF-8
Testoob jest zaawansowanym frameworkiem testów jednostkowych
dla Pythona. Integruje się bezproblemowo z istniejącym środowiskiem
do testów PyUnit (moduł "unittest").

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib=%{py_sitedir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/CHANGELOG README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/testoob
%{py_sitedir}/testoob/*.py[co]
# XXX: missing dir(s)
%{py_sitedir}/testoob/*/*.py[co]
