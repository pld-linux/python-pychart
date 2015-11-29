%define 	fname	PyChart
%define		module	pychart
#
Summary:	PyChart - Python library for creating high quality EPS, PDF, PNG, or SVG charts
Summary(pl.UTF-8):	PyChart - biblioteka Pythona do tworzenia wysokiej jakości wykresów EPS, PDF, PNG i SVG
Name:		python-%{module}
Version:	1.39
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://download.gna.org/pychart/%{fname}-%{version}.tar.gz
# Source0-md5:	f1f509a1c4623056c8e780bb7c9a05c5
URL:		http://home.gna.org/pychart/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1.5
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyChart is a Python library for creating high quality Encapsulated
Postscript, PDF, PNG, or SVG charts. It currently supports line plots,
bar plots, range-fill plots, and pie charts. Because it is based on
Python, you can make full use of Python's scripting power.

%description -l pl.UTF-8
PyChart to biblioteka Pythona do tworzenia wysokiej jakości wykresów w
formacie EPS (Encapsulated Postscript), PDF, PNG i SVG. Aktualnie
obsługuje wykresy liniowe, słupkowe, zakresowe (range-fill) i kołowe.
Ponieważ jest oparta na Pythonie, można wykorzystać w skryptach całą
potęgę tego języka.

%prep
%setup -q -n %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*.egg*
