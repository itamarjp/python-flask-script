%global mod_name Flask-Script

%if 0%{?fedora} > 12
%global with_python3 1
%endif

Name:       python-flask-script
Version:    2.0.5
Release:    11%{?dist}
Summary:    Scripting support for Flask

License:    BSD
URL:        http://flask-script.readthedocs.org/en/latest/
Source0:    https://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-flask
BuildRequires:  python2-sphinx
BuildRequires:  python2-pytest
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-flask
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest
%endif

%global _description\
The Flask-Script extension provides support for writing external scripts in\
Flask.This includes running a development server, a customized Python shell,\
scripts to set up your database, cronjobs, and other command-line tasks that\
belong outside the web application itself.

%description %_description

%package -n python2-flask-script
Summary: %summary
Requires:       python2-flask
%{?python_provide:%python_provide python2-flask-script}

%description -n python2-flask-script %_description

%if 0%{?with_python3}
%package -n python3-flask-script
Summary:    Scripting support for flask in python3-flask

Requires:       python3-flask

%description -n python3-flask-script
The Flask-Script extension provides support for writing external scripts in
Flask.This includes running a development server, a customized Python shell,
scripts to set up your database, cronjobs, and other command-line tasks that
belong outside the web application itself.
%endif

%prep
%setup -q -n %{mod_name}-%{version}
# delete the mac's .ds_store file
rm -f docs/.DS_Store

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build
# generate sphinx documentation
cd docs && make html
# deleting unneeded buildinfo, we dont expect users to change html docs
rm -f _build/html/.buildinfo

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
cd docs && make html
rm -f _build/html/.buildinfo
popd
%endif

%check
py.test-%{python2_version} tests.py
%if 0%{?with_python3}
pushd %{py3dir}
py.test-%{python3_version} tests.py
popd
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif


%files -n python2-flask-script
%doc docs/_build/html README.rst LICENSE 
%{python2_sitelib}/*.egg-info/
%{python2_sitelib}/flask_script/*.py*

%if 0%{?with_python3}
%files -n python3-flask-script
%doc docs/_build/html README.rst LICENSE 
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/flask_script
%endif

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.5-9
- Python 2 binary package renamed to python2-flask-script
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Robert Kuska <rkuska@redhat.com> - 2.0.5-1
- Updated to 2.0.5

* Thu Jul 03 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-4
- Move Python 3 Requires into correct place

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 28 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Wed Sep 25 2013 Robert Kuska <rkuska@redhat.com> - 0.6.2-1
- Updated source to latest upstream version and added python3 support

* Tue Aug 06 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-4
- Fix BuildRequires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-2
- Review fixes

* Thu Mar 21 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-1
- Initial package
