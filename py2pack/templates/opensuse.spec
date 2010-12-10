#
# spec file for package python-{{ name|lower }}
#
# Copyright (c) {{ year }} SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           python-{{ name|lower }}
Version:        {{ version }}
Release:        0
Url:            {{ home_page }}
Summary:        {{ summary }}
License:        {{ license }}
Group:          Development/Languages/Python
%define mod_name {{ name }}
Source:         %{mod_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
{%- for req in requires %}
BuildRequires:  python-{{ req|lower }}
Requires:       pyhton-{{ req|lower }}
{%- endfor %}
%if 0%{?suse_version}
%py_requires
%if 0%{suse_version} > 1110}
BuildArch:      noarch
%endif
%endif

%description
{{ description }}

Authors:
--------
    {{ author}} <{{ author_email }}>

%prep
export CFLAGS="%{optflags}"
%setup -n %{mod_name}-%{version}

%build
%{__python} setup.py build

%install
%if 0%{?suse_version}
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot} --record-rpm=INSTALLED_FILES
%else
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif

%clean
%{__rm} -rf %{buildroot}

%if 0%{?suse_version}
%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%else
%files
%defattr(-,root,root,-)
# You may have to add additional files here!
/usr/lib/python2.6/site-packages/%{mod_name}*
%endif

%changelog
