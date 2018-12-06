# skip tests by default because they require a running xmlrpc server
%bcond_with check
%global goipath     github.com/kolo/xmlrpc
%global commit      0826b98aaa29c0766956cb40d45cf7482a597671

Version:            0

%global common_description %{expand:
Implementation of XMLRPC protocol in Go language.}

%gometa

Name:    %{goname}
Release: 0.2%{?dist}
Summary: Implementation of XMLRPC protocol in Go language
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/transform)


%description
%{common_description}

%package   devel
Summary:   %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE
%doc *\.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git0826b98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180513git0826b9
- First package for Fedora
