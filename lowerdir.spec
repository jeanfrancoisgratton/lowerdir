%define debug_package   %{nil}
%define _build_id_links none
%define _name   lowerdir
%define _prefix /opt
%define _version 1.000
%define _rel 1
%define _arch x86_64

Name:       lowerdir
Version:    %{_version}
Release:    %{_rel}
Summary:    lowerdir

Group:      virtualMachines/orchestration
License:    GPL2.0
URL:        https://github.com/jeanfrancoisgratton/lowerdir

Source0:    %{name}-%{_version}.tar.gz
BuildArchitectures: x86_64
#BuildRequires: libvirt-devel,wget,gcc
#Requires: libvirt-devel,libvirt,virt-clone,sudo,postgresql-contrib


%description
GoLang-based libvirt client

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
/usr/sbin/groupadd kvm 2> /dev/null
/usr/sbin/groupadd -g 2500 devops 2> /dev/null
exit 0

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
* Wed Apr 26 2023 builder <builder@famillegratton.net> 1.000-1
- Release (jean-francois@famillegratton.net)
- final rpmspec fix (builder@famillegratton.net)

* Wed Apr 26 2023 builder <builder@famillegratton.net> 0.100-0
- new package built with tito
