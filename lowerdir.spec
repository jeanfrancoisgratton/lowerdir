%define debug_package   %{nil}
%define _build_id_links none
%define _name   lowerdir
%define _prefix /opt
%define _version 0.100
%define _rel 0
%define _arch x86_64
%define _binaryname lowerdir

Name:       lowerdir
Version:    %{_version}
Release:    %{_rel}
Summary:    lowerdir

Group:      Utils
License:    GPL2.0
URL:        https://github.com/jeanfrancoisgratton/lowerdir

Source0:    %{name}-%{_version}.tar.gz
BuildArchitectures: x86_64
#BuildRequires: gcc
#Requires: sudo
#Obsoletes: vmman1 > 1.140

%description
Batch file rename tool

%prep
#%setup -q
%autosetup

%build
cd %{_sourcedir}/%{_name}-%{_version}/src
#PATH=$PATH:/opt/go/bin go build -o %{_sourcedir}/%{_name} .
PATH=$PATH:/opt/go/bin go build -o %{_sourcedir}/%{_binaryname} .
#strip %{_sourcedir}/%{_name}
strip %{_sourcedir}/%{_binaryname}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
exit 0

%install
#%{__mkdir_p} "$RPM_BUILD_ROOT%{_prefix}/bin"
#install -Dpm 0755 %{_sourcedir}/%{name} %{buildroot}%{_bindir}/%{name}
#install -Dpm 0755 %{_sourcedir}/%{name} %{buildroot}%{_bindir}/%{binaryname}

%post

%preun

%postun

%files
%defattr(-,root,root,-)
#%{_bindir}/%{name}
%{_bindir}/%{binaryname}


%changelog
* Wed Apr 26 2023 builder <builder@famillegratton.net> 0.100-0
- new package built with tito

