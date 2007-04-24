%define 	fname	PyChart
%define		module	pychart
#
Summary:	PyChart is a Python library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts.
Name:		python-%{module}
Version:	1.26.1
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://home.gna.org/pychart/old/%{fname}-%{version}.tar.gz
URL:		http://home.gna.org/pychart
BuildRequires:	python >= 1.5
Requires:   python >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyChart is a Python library for creating high quality Encapsulated Postscript, PDF, PNG, or SVG charts. It currently
supports line plots, bar plots, range-fill plots, and pie charts. Because it is based on Python, you can make full use
of Python's scripting power.

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

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/ -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
