%define module py-cpuinfo
%define oname py_cpuinfo

%bcond tests 1

Name:		python-py-cpuinfo
Version:	9.0.0
Release:	2
Summary:	A module for getting CPU info with pure Python
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/py-cpuinfo/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Py-cpuinfo gets CPU info with pure Python.

Py-cpuinfo should work without any extra programs or libraries,
beyond what your OS provides.

It does not require any compilation(C/C++, assembly, et cetera) to use.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%if %{with tests}
%check
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
%{__python} test_suite.py
%endif

%files
%{_bindir}/cpuinfo
%{py_sitedir}/cpuinfo
%{py_sitedir}/%{oname}-%{version}.dist-info
