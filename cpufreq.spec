Summary:	An initscript to set CPU frequency settings
Name:		cpufreq
Version:	2.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
Url:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/SPECS/cpufreq/
Source0:	%{name}-%{version}.tar.xz
Requires(pre):	rpm-helper
Requires(postun):	rpm-helper
BuildArch:	noarch

Requires:	pciutils, sed, gawk, grep, coreutils

%description
cpufreq is a simple initscript to set CPU frequency settings.

%prep
%setup -q

%build

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m755 %{name}.init %{buildroot}%{_initrddir}/%{name}
install -D -m644 %{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service

%post
%_post_service %{name}

%preun
%_preun_service  %{name}

%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_initrddir}/%{name}
%{_unitdir}/%{name}.service
