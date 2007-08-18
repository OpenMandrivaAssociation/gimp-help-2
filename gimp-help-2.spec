Summary: Help files for Gimp2
Name:    gimp-help-2
Version: 0.13
Release: %mkrel 1
Source0: ftp://ftp.gimp.org/pub/gimp/help/%name-%version.tar.bz2
License: GFDL
Group:   Development/Other
Url: http://docs.gimp.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gimp2-devel
BuildRequires: libxslt-proc
BuildRequires: libxml2-utils
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd43-xml
BuildArch: noarch

%description
This is the new HTML help for Gimp 2.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README HACKING TERMINOLOGY
%dir %_datadir/gimp/2.0/help/images
%_datadir/gimp/2.0/help/images/*.png
%_datadir/gimp/2.0/help/images/callouts/
%dir %_datadir/gimp/2.0/help/images/dialogs/
%_datadir/gimp/2.0/help/images/dialogs/*.png
%lang(cs) %_datadir/gimp/2.0/help/images/dialogs/cs/
%lang(de) %_datadir/gimp/2.0/help/images/dialogs/de/
%lang(es) %_datadir/gimp/2.0/help/images/dialogs/es/
%lang(fr) %_datadir/gimp/2.0/help/images/dialogs/fr/
%lang(it) %_datadir/gimp/2.0/help/images/dialogs/it/
%lang(ko) %_datadir/gimp/2.0/help/images/dialogs/ko/
%lang(nl) %_datadir/gimp/2.0/help/images/dialogs/nl/
%lang(no) %_datadir/gimp/2.0/help/images/dialogs/no/
%lang(ru) %_datadir/gimp/2.0/help/images/dialogs/ru/
%lang(zh) %_datadir/gimp/2.0/help/images/dialogs/zh_CN/
%_datadir/gimp/2.0/help/images/dialogs/examples/
%dir %_datadir/gimp/2.0/help/images/filters/
%_datadir/gimp/2.0/help/images/filters/*.png
%lang(cs) %_datadir/gimp/2.0/help/images/filters/cs/
%lang(de) %_datadir/gimp/2.0/help/images/filters/de/
%lang(es) %_datadir/gimp/2.0/help/images/filters/es/
%lang(fr) %_datadir/gimp/2.0/help/images/filters/fr/
%lang(it) %_datadir/gimp/2.0/help/images/filters/it/
%lang(zh) %_datadir/gimp/2.0/help/images/filters/zh_CN/
%_datadir/gimp/2.0/help/images/filters/examples/
%_datadir/gimp/2.0/help/images/glossary/
%_datadir/gimp/2.0/help/images/math/
%dir %_datadir/gimp/2.0/help/images/menus/
%_datadir/gimp/2.0/help/images/menus/*.png
%lang(cs) %_datadir/gimp/2.0/help/images/menus/cs/
%lang(de) %_datadir/gimp/2.0/help/images/menus/de/
%lang(fr) %_datadir/gimp/2.0/help/images/menus/fr/
%lang(it) %_datadir/gimp/2.0/help/images/menus/it/
%lang(no) %_datadir/gimp/2.0/help/images/menus/no/
%lang(zh) %_datadir/gimp/2.0/help/images/menus/zh_CN/
%dir %_datadir/gimp/2.0/help/images/preferences/
%_datadir/gimp/2.0/help/images/preferences/*.png
%lang(de) %_datadir/gimp/2.0/help/images/preferences/de/
%lang(fr) %_datadir/gimp/2.0/help/images/preferences/fr/
%lang(it) %_datadir/gimp/2.0/help/images/preferences/it/
%lang(nl) %_datadir/gimp/2.0/help/images/preferences/nl/
%lang(ru) %_datadir/gimp/2.0/help/images/preferences/ru/
%lang(zh) %_datadir/gimp/2.0/help/images/preferences/zh_CN/
%dir %_datadir/gimp/2.0/help/images/tool-options/
%_datadir/gimp/2.0/help/images/tool-options/*.png
%lang(es) %_datadir/gimp/2.0/help/images/tool-options/es/
%lang(it) %_datadir/gimp/2.0/help/images/tool-options/it/
%dir %_datadir/gimp/2.0/help/images/toolbox
%_datadir/gimp/2.0/help/images/toolbox/*.png
%lang(cs) %_datadir/gimp/2.0/help/images/toolbox/cs/
%lang(de) %_datadir/gimp/2.0/help/images/toolbox/de/
%lang(es) %_datadir/gimp/2.0/help/images/toolbox/es/
%lang(fr) %_datadir/gimp/2.0/help/images/toolbox/fr/
%lang(it) %_datadir/gimp/2.0/help/images/toolbox/it/
%lang(ko) %_datadir/gimp/2.0/help/images/toolbox/ko/
%lang(nl) %_datadir/gimp/2.0/help/images/toolbox/nl/
%lang(no) %_datadir/gimp/2.0/help/images/toolbox/no/
%lang(zh) %_datadir/gimp/2.0/help/images/toolbox/zh_CN/
%dir %_datadir/gimp/2.0/help/images/using/*.*
%lang(cs) %_datadir/gimp/2.0/help/images/using/cs/
%lang(de) %_datadir/gimp/2.0/help/images/using/de/
%lang(es) %_datadir/gimp/2.0/help/images/using/es/
%lang(fr) %_datadir/gimp/2.0/help/images/using/fr/
%lang(hr) %_datadir/gimp/2.0/help/images/using/hr/
%lang(it) %_datadir/gimp/2.0/help/images/using/it/
%lang(ko) %_datadir/gimp/2.0/help/images/using/ko/
%lang(nl) %_datadir/gimp/2.0/help/images/using/nl/
%lang(no) %_datadir/gimp/2.0/help/images/using/no/
%lang(ru) %_datadir/gimp/2.0/help/images/using/ru/
%lang(zh) %_datadir/gimp/2.0/help/images/using/zh_CN/

%lang(cs) %_datadir/gimp/2.0/help/cs
%lang(de) %_datadir/gimp/2.0/help/de
%lang(es) %_datadir/gimp/2.0/help/es
%lang(it) %_datadir/gimp/2.0/help/it
%_datadir/gimp/2.0/help/en
%lang(fr) %_datadir/gimp/2.0/help/fr
%lang(hr) %_datadir/gimp/2.0/help/hr
%lang(ko) %_datadir/gimp/2.0/help/ko
%lang(nl) %_datadir/gimp/2.0/help/nl
%lang(no) %_datadir/gimp/2.0/help/no
%lang(ru) %_datadir/gimp/2.0/help/ru
%lang(sv) %_datadir/gimp/2.0/help/sv
%lang(zh) %_datadir/gimp/2.0/help/zh_CN


