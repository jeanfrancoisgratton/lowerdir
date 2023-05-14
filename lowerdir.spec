%define debug_package   %{nil}
%define _build_id_links none
%define _name   lowerdir
%define _prefix /opt
%define _version 1.101
%define _rel 1
%define _arch x86_64

Name:       lowerdir
Version:    %{_version}
Release:    %{_rel}
Summary:    lowerdir

Group:      Administration tools
License:    GPL2.0
URL:        https://github.com/jeanfrancoisgratton/lowerdir

Source0:    %{name}-%{_version}.tar.gz
BuildArchitectures: x86_64
#BuildRequires: libvirt-devel,wget,gcc
#Requires: libvirt-devel,libvirt,virt-clone,sudo,postgresql-contrib


%description
Filesystem utilities

%prep
#%setup -q
%autosetup

%build
cd %{_sourcedir}/%{_name}-%{_version}/src
PATH=$PATH:/opt/go/bin go build -o %{_sourcedir}/%{_name} .
strip %{_sourcedir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%install
#%{__mkdir_p} "$RPM_BUILD_ROOT%{_prefix}/bin"
#install -Dpm 0755 %{buildroot}/%{_name} "$RPM_BUILD_ROOT%{_prefix}/bin/"
install -Dpm 0755 %{_sourcedir}/%{name} %{buildroot}%{_bindir}/%{name}

%post
strip %{_prefix}/bin/%{name}

%preun

%postun

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}


%changelog
* Fri Apr 28 2023 builder <builder@famillegratton.net> 1.10.00-2
- Removed useless package (jean-francois@famillegratton.net)
- repackaging (jean-francois@famillegratton.net)
- interim commit to test apkbuilder (jean-francois@famillegratton.net)

* Thu Apr 27 2023 builder <builder@famillegratton.net> 1.01.00-1
- New release, cobra-enabled (jean-francois@famillegratton.net)

* Wed Apr 26 2023 builder <builder@famillegratton.net> 1.000-1
- Release (jean-francois@famillegratton.net)
- final rpmspec fix (builder@famillegratton.net)

* Wed Apr 26 2023 builder <builder@famillegratton.net> 0.100-0
- new package built with tito
