%define gimp_help_dir %{_datadir}/gimp/2.0/help
%define oname gimp-help

Summary:	Help files for Gimp2
Name:		gimp-help-2
Version:	2.6.0
Release:	10
License:	GFDL
Group:		Books/Other
Url:		http://docs.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-de.tar.bz2
Source1:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-en.tar.bz2
Source2:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-es.tar.bz2
Source3:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-fr.tar.bz2
Source4:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-it.tar.bz2
Source5:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-ja.tar.bz2
Source6:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-ko.tar.bz2
Source7:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-nl.tar.bz2
Source8:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-nn.tar.bz2
Source9:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-pl.tar.bz2
Source10:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-ru.tar.bz2
Source11:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-sv.tar.bz2
Source12:	ftp://ftp.gimp.org/pub/gimp/help/%{oname}-%{version}-html-zh_CN.tar.bz2
BuildArch:	noarch

%description
This is the HTML help for Gimp 2.

%package pl
Summary:	Polish translation of Gimp2 help
Group:		Books/Other
Requires:	locales-pl
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description pl
This package contains the Polish translation of Gimp2 help.

%files pl
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/pl

# -----------------------------------------------------
%package de
Summary:	German translation of Gimp2 help
Group:		Books/Other
Requires:	locales-de
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description de
This package contains the German translation of Gimp2 help.

%files de
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/de

# -----------------------------------------------------
%package en
Summary:	English translation of Gimp2 help
Group:		Books/Other
Requires:	locales-en
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description en
This package contains the English translation of Gimp2 help.

%files en
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/en

# -----------------------------------------------------
%package es
Summary:	Spanish translation of Gimp2 help
Group:		Books/Other
Requires:	locales-es
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description es
This package contains the Spanish translation of Gimp2 help.

%files es
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/es

# -----------------------------------------------------
%package fr
Summary:	French translation of Gimp2 help
Group:		Books/Other
Requires:	locales-fr
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description fr
This package contains the French translation of Gimp2 help.

%files fr
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/fr


%package it
Summary:	Italian translation of Gimp2 help
Group:		Books/Other
Requires:	locales-it
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description it
This package contains the Italian translation of Gimp2 help.

%files it
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/it

%package ja
Summary:	Japanese translation of Gimp2 help
Group:		Books/Other
Requires:	locales-ja
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description ja
This package contains the Japanese translation of Gimp2 help.

%files ja
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/ja

%package ko
Summary:	Korean translation of Gimp2 help
Group:		Books/Other
Requires:	locales-ko
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description ko
This package contains the Korean translation of Gimp2 help.

%files ko
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/ko

# -----------------------------------------------------
%package nl
Summary:	Dutch translation of Gimp2 help
Group:		Books/Other
Requires:	locales-nl
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description nl
This package contains the Dutch translation of Gimp2 help.

%files nl
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/nl

# -----------------------------------------------------
%package nn
Summary:	Nynorsk Norwegian translation of Gimp2 help
Group:		Books/Other
Requires:	locales-no
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2
Obsoletes:	%{name}-no
Provides:	%{name}-no

%description nn
This package contains the Nynorsk Norwegian translation of Gimp2 help.

%files nn
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/nn

# -----------------------------------------------------
%package ru
Summary:	Russian translation of Gimp2 help
Group:		Books/Other
Requires:	locales-ru
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description ru
This package contains the Russian translation of Gimp2 help.

%files ru
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/ru

# -----------------------------------------------------
%package sv
Summary:	Swedish translation of Gimp2 help
Group:			Books/Other
Requires:	locales-sv
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description sv
This package contains the Swedish translation of Gimp2 help.

%files sv
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/sv

# -----------------------------------------------------
%package zh_CN
Summary:	Simplified Chinese translation of Gimp2 help
Group:		Books/Other
Requires:	locales-zh
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < 0.13
Conflicts:	%{name} < 0.13-2

%description zh_CN
This package contains the Simplified Chinese translation of Gimp2 help.

%files zh_CN
%doc %{name}/AUTHORS %{name}/MAINTAINERS %{name}/README %{name}/HACKING
%{gimp_help_dir}/zh_CN

# -----------------------------------------------------

%prep
%setup -q -c %{oname}-%{version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12

%install
mkdir -p %{buildroot}%{gimp_help_dir}
cp -r %{name}/html/* %{buildroot}%{gimp_help_dir}


