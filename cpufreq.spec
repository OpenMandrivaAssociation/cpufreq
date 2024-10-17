Summary:	An initscript to set CPU frequency settings
Name:		cpufreq
Version:	2.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
Url:		https://cvs.mandriva.com/cgi-bin/cvsweb.cgi/SPECS/cpufreq/
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


%changelog
* Sun May 27 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0-1mdv2012.0
+ Revision: 800793
- update to new version 2.0 (sync with mageia)

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-35
+ Revision: 663414
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-34mdv2011.0
+ Revision: 603853
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-33mdv2010.1
+ Revision: 520038
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-32mdv2010.0
+ Revision: 413270
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-31mdv2009.1
+ Revision: 321089
- rebuild

* Mon Sep 29 2008 Olivier Blin <blino@mandriva.org> 1.0-30mdv2009.0
+ Revision: 289167
- implement service status (to be fastinit compatible)

* Tue Aug 05 2008 Olivier Blin <blino@mandriva.org> 1.0-29mdv2009.0
+ Revision: 264028
- use ondemand governor by default (#42310)

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0-28mdv2009.0
+ Revision: 220512
- rebuild

* Tue Feb 12 2008 Olivier Blin <blino@mandriva.org> 1.0-27mdv2008.1
+ Revision: 166314
- do not require obsolete acpi service in initscript

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0-26mdv2008.1
+ Revision: 149131
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-25mdv2008.0
+ Revision: 42542
- rebuild for 2008
- Import cpufreq




* Mon Jul 10 2006 Olivier Blin <oblin@mandriva.com> 1.0-24mdv2007.0
- drop modules probing, this is done by harddrake now
- drop chkconfig comments in initscript

* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 1.0-23mdk
- from Andrey Borzenkov (#20523): fix startup order and add comments

* Mon Jan  9 2006 Olivier Blin <oblin@mandriva.com> 1.0-22mdk
- convert parallel init to LSB
- acpi-cpufreq support (Andrey Borzenkov, #20519)

* Mon Jan  2 2006 Olivier Blin <oblin@mandriva.com> 1.0-21mdk
- parallel init support

* Tue Dec 20 2005 Olivier Blin <oblin@mandriva.com> 1.0-20mdk
- adapt to new "lspci -n" format  (Michael Reinsch, #20275)

* Mon Oct  3 2005 Olivier Blin <oblin@mandriva.com> 1.0-19mdk
- fix typo in service description (#18961)

* Mon Sep 19 2005 Olivier Blin <oblin@mandriva.com> 1.0-18mdk
- don't unload module on stop, but try to reload it on restart (#18460)

* Mon Aug 29 2005 Austin Acton <austin@mandriva.org> 1.0-17mdk
- add conservative governor module

* Mon Aug 08 2005 Frederic Crozat <fcrozat@mandriva.com> 1.0-16mdk 
- Update source0 and add source1 : add support for setting
  governor, max and min frequencies after loading modules
- Fix url

* Mon Jun 13 2005 Erwan Velu <velu@seanodes.com> 1.0-15mdk
- Fixing rights

* Thu Mar 17 2005 Olivier Blin <oblin@mandrakesoft.com> 1.0-14mdk
- AMD 64 support (#14687)

* Mon Mar 14 2005 Olivier Blin <oblin@mandrakesoft.com> 1.0-13mdk
- do not look for cpufreq entry in /proc (obsolete)
  or in /sysfs (dynamically created by cpufreq modules) (#13289)

* Sat Feb 12 2005 Olivier Blin <oblin@mandrakesoft.com> 1.0-12mdk
- probe speedstep-smi module (#13015)

* Wed Feb  2 2005 Olivier Blin <oblin@mandrakesoft.com> 1.0-11mdk
- PPC support and misc fixes (from Danny Tholen)

* Tue Feb  1 2005 Olivier Blin <blino@mandrake.org> 1.0-10mdk
- load all cpufreq governors (#13290)
  (performance, ondemand, userspace, powersave)

* Wed Jan  5 2005 Olivier Blin <blino@mandrake.org> 1.0-9mdk
- handle one more centrino CPU (Dothan, model 13)
- merge patch0

* Fri Oct 22 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-8.1mdk
- handle powernow-k8

* Wed Sep  8 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.0-8mdk
- applied patch from Jan Ciger (bug #11309)

* Sat Sep  4 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-7mdk
- Oups, fixing stupid friday syntax

* Fri Sep  3 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-6mdk
- Probing the chipset drivers first
- 2.4 kernel support was missing
- Adding requires

* Fri Sep  3 2004 Juan Quintela <quintela@n5.mandrakesoft.com> 1.0-5mdk
- we need to ask for ich before P4, otherwise, P4 wins always.

* Sat Aug 28 2004 Michael Scherer <misc@mandrake.org> 1.0-4mdk 
- add a Requires on pci-utils ( fix #11049 )
- add Url

* Thu Aug 26 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-3mdk
- Fixing stupid parsing in /proc : ht & smp systems were buggy #10976

* Wed Aug 25 2004 Robert Vojta <robert.vojta@mandrake.org> 1.0-2mdk
- next ICH added (8086:244c) (#10940)
- probe_P4() function fixed (#10940)
- it's a simple script -> i586 moved to noarch

* Mon Aug 23 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-1mdk
- Initial release
# end of file
