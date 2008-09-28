%define name cpufreq
%define version 1.0
%define release %mkrel 29

Summary: An initscript to set CPU frequency settings
Name: %{name}
Version: %{version}
Release: %{release}
Source0: cpufreq.init
Source1: cpufreq.sysconfig
License: GPL
Group: System/Servers
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires(pre): rpm-helper
Requires(postun): rpm-helper
BuildArch: noarch
Url:       http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/SPECS/cpufreq/
Requires:  pciutils, sed, gawk, grep, coreutils

%description
cpufreq is a simple initscript to set CPU frequency settings.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot/%_initrddir %{buildroot}%_sysconfdir/sysconfig
install -D -m755 %{SOURCE0} %{buildroot}%_initrddir/%{name}
install -D -m644 %{SOURCE1} %{buildroot}%_sysconfdir/sysconfig/%{name}

%clean
rm -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service  %{name}

%files
%defattr(-,root,root)
%attr(755,root,root) %_initrddir/%{name}
%config(noreplace) %_sysconfdir/sysconfig/%{name}
