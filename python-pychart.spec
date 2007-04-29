%define 	fname	PyChart
%define		module	pychart
#
Summary:	PyChart - Python library for creating high quality EPS, PDF, PNG, or SVG charts
Summary(pl.UTF-8):	PyChart - biblioteka Pythona do tworzenia wysokiej jakości wykresów EPS, PDF, PNG i SVG
Name:		python-%{module}
Version:	1.26.1
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://home.gna.org/pychart/old/%{fname}-%{version}.tar.gz
# Source0-md5:	4a1299542c24ab22852353b97c94265e
URL:		http://home.gna.org/pychart/
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
