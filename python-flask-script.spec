%global mod_name Flask-Script

Name:       python-flask-script
Version:    0.5.3
Release:    3%{?dist}
Summary:    Scripting support for Flask

License:    BSD
URL:        http://flask-script.readthedocs.org/en/latest/
Source0:    https://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# for check purpose nose is needed
BuildRequires:  python-nose
BuildRequires:  python-flask
Requires:       python-flask

%description
The Flask-Script extension provides support for writing external scripts in
Flask.This includes running a development server, a customized Python shell,
scripts to set up your database, cronjobs, and other command-line tasks that
belong outside the web application itself.


%prep
%setup -q -n %{mod_name}-%{version}
# delete the mac's .ds_store file
rm -f docs/.DS_Store

%build
%{__python} setup.py build
# generate sphinx documentation
cd docs && make html
# deleting unneeded buildinfo, we dont expect users to change html docs
rm -f _build/html/.buildinfo

%check
%{__python} setup.py test

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc docs/_build/html README.rst LICENSE 
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flask_script/*.py*

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Robert Kuska <rkuska@redhat.com> 0.5.3-2
- Review fixes

* Thu Mar 21 2013 Robert Kuska <rkuska@redhat.com> 0.5.3-1
- Initial package
