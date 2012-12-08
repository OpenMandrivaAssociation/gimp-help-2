%define gimp_help_dir %{_datadir}/gimp/2.0/help
%define oname gimp-help
Summary: Help files for Gimp2
Name:    gimp-help-2
Version: 2.6.0
Release: %mkrel 5
Source0: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-de.tar.bz2
Source1: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-en.tar.bz2
Source2: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-es.tar.bz2
Source3: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-fr.tar.bz2
Source4: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-it.tar.bz2
Source5: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-ja.tar.bz2
Source6: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-ko.tar.bz2
Source7: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-nl.tar.bz2
Source8: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-nn.tar.bz2
Source9: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-pl.tar.bz2
Source10: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-ru.tar.bz2
Source11: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-sv.tar.bz2
Source12: ftp://ftp.gimp.org/pub/gimp/help/%oname-%version-html-zh_CN.tar.bz2
License: GFDL
Group: Books/Other
Url: http://docs.gimp.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This is the HTML help for Gimp 2.

%package pl
Summary: Polish translation of Gimp2 help
Group: Books/Other
Requires: locales-pl
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description pl
This package contains the Polish translation of Gimp2 help.

%files pl
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/pl

# -----------------------------------------------------
%package de
Summary: German translation of Gimp2 help
Group: Books/Other
Requires: locales-de
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description de
This package contains the German translation of Gimp2 help.

%files de
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/de

# -----------------------------------------------------
%package en
Summary: English translation of Gimp2 help
Group: Books/Other
Requires: locales-en
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description en
This package contains the English translation of Gimp2 help.

%files en
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/en

# -----------------------------------------------------
%package es
Summary: Spanish translation of Gimp2 help
Group: Books/Other
Requires: locales-es
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description es
This package contains the Spanish translation of Gimp2 help.

%files es
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/es

# -----------------------------------------------------
%package fr
Summary: French translation of Gimp2 help
Group: Books/Other
Requires: locales-fr
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description fr
This package contains the French translation of Gimp2 help.

%files fr
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/fr


%package it
Summary: Italian translation of Gimp2 help
Group: Books/Other
Requires: locales-it
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description it
This package contains the Italian translation of Gimp2 help.

%files it
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/it

%package ja
Summary: Japanese translation of Gimp2 help
Group: Books/Other
Requires: locales-ja
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description ja
This package contains the Japanese translation of Gimp2 help.

%files ja
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/ja

%package ko
Summary: Korean translation of Gimp2 help
Group: Books/Other
Requires: locales-ko
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description ko
This package contains the Korean translation of Gimp2 help.

%files ko
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/ko

# -----------------------------------------------------
%package nl
Summary: Dutch translation of Gimp2 help
Group: Books/Other
Requires: locales-nl
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description nl
This package contains the Dutch translation of Gimp2 help.

%files nl
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/nl

# -----------------------------------------------------
%package nn
Summary: Nynorsk Norwegian translation of Gimp2 help
Group: Books/Other
Requires: locales-no
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2
Obsoletes: %name-no
Provides: %name-no

%description nn
This package contains the Nynorsk Norwegian translation of Gimp2 help.

%files nn
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/nn

# -----------------------------------------------------
%package ru
Summary: Russian translation of Gimp2 help
Group: Books/Other
Requires: locales-ru
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description ru
This package contains the Russian translation of Gimp2 help.

%files ru
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/ru

# -----------------------------------------------------
%package sv
Summary: Swedish translation of Gimp2 help
Group: Books/Other
Requires: locales-sv
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description sv
This package contains the Swedish translation of Gimp2 help.

%files sv
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/sv

# -----------------------------------------------------
%package zh_CN
Summary: Simplified Chinese translation of Gimp2 help
Group: Books/Other
Requires: locales-zh
Provides: %name = %version-%release
Obsoletes: %name < 0.13
Conflicts: %name < 0.13-2

%description zh_CN
This package contains the Simplified Chinese translation of Gimp2 help.

%files zh_CN
%defattr(-,root,root)
%doc %name/AUTHORS %name/MAINTAINERS %name/README %name/HACKING
%gimp_help_dir/zh_CN

# -----------------------------------------------------

%prep
%setup -q -c %oname-%version -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%gimp_help_dir
cp -r %name/html/* %buildroot%gimp_help_dir

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-4mdv2011.0
+ Revision: 664835
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.0-3mdv2011.0
+ Revision: 605457
- rebuild

* Thu Jan 21 2010 Götz Waschk <waschk@mandriva.org> 2.6.0-2mdv2010.1
+ Revision: 494594
- rebuild for lost source package
- new version
- remove common subpackage
- add japanese
- readd chinese
- rename norwegian package to nn

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.4.2-2mdv2010.0
+ Revision: 424989
- rebuild

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 2.4.2-1mdv2009.1
+ Revision: 291773
- update file list
- New version 2.4.2

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 2.4.1-2mdv2009.0
+ Revision: 264543
- rebuild early 2009.0 package (before pixel changes)
- better description

* Thu Apr 10 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2009.0
+ Revision: 192568
- new version
- add Polish translation
- remove Czech, Croatian and Chinese translation

  + Oden Eriksson <oeriksson@mandriva.com>
    - fix funny typo

* Sun Feb 03 2008 Frederik Himpe <fhimpe@mandriva.org> 2.4.0-2mdv2008.1
+ Revision: 161732
- Fix typos and error in package description (bug #37459)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 01 2007 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2008.1
+ Revision: 114271
- new version
- update file list

* Mon Aug 27 2007 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2008.0
+ Revision: 72018
- fix latest upgrade bit

* Mon Aug 27 2007 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2008.0
+ Revision: 71941
- fix upgrade by preventing spreading various sub packages across several transactions (#32731)

* Sat Aug 18 2007 Funda Wang <fwang@mandriva.org> 0.13-1mdv2008.0
+ Revision: 65823
- Split to language packages to reduce the download bandwidth
- New version 0.13


* Thu Mar 08 2007 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2007.1
+ Revision: 138466
- new version
- update file list

* Thu Mar 01 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.11-3mdv2007.1
+ Revision: 130729
- move huge (1Mb!) ChangeLog in devel package

* Thu Dec 21 2006 Götz Waschk <waschk@mandriva.org> 0.11-2mdv2007.1
+ Revision: 101082
- disable ImageMagick usage, it makes convert crash
- add missing files
- fix buildrequires
- update file list
- Import gimp-help-2

* Thu Dec 21 2006 G�tz Waschk <waschk@mandriva.org> 0.11-1mdv2007.1
- update file list
- fix buildrequires
- fix source URL
- new version

* Fri Sep 09 2005 Götz Waschk <waschk@mandriva.org> 0.9-1mdk
- New release 0.9

* Tue May 24 2005 G�tz Waschk <waschk@mandriva.org> 0.8-1mdk
- update file list
- new source URL
- new version

* Wed Feb 23 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.7-1mdk
- new release

* Tue Jan 18 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-1mdk
- new release
- add source's url

* Wed Dec 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5-1mdk
- new release

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.4-1mdk
- new release

* Thu Jul 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-1mdk
- new release

* Thu Apr 15 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.2-2mdk
- buildrequires gimp2-devel

* Fri Mar 26 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-1mdk
- new release

* Thu Mar 25 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-1mdk
- initial package

