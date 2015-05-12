%define gimp_help_dir %{_datadir}/gimp/2.0/help
%define oname gimp-help

Summary:	Help files for Gimp2
Name:		gimp-help-2
Version:	2.8.2
Release:	1
License:	GFDL
Group:		Books/Other
Url:		http://docs.gimp.org/
Source0:        http://download.gimp.org/pub/gimp/help/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:  xsltproc
BuildRequires:  python2-libxml2
BuildRequires:  docbook-style-xsl

%description
This is the HTML help for Gimp 2.

%if 0
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
%endif

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
%package el
Summary:        Greek translation of Gimp2 help
Group:          Books/Other
Requires:       locales-el
Provides:       %{name} = %{version}-%{release}

%description el
This package contains the Greek translation of Gimp2 help.

%files el
%{gimp_help_dir}/el

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
%package fi
Summary:        Finnish translation of Gimp2 help
Group:          Books/Other
Requires:       locales-fi
Provides:       %{name} = %{version}-%{release}

%description fi
This package contains the Finnish translation of Gimp2 help.

%files fi
%{gimp_help_dir}/fi

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

%if 0
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
%endif

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
%if 0
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
%endif

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
%package sl
Summary:        Slovenian translation of Gimp2 help
Group:          Books/Other
Requires:       locales-sl
Provides:       %{name} = %{version}-%{release}

%description sl
This package contains the Slovenian translation of Gimp2 help.

%files sl
%{gimp_help_dir}/sl

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
%setup -qn %{oname}-%{version}

sed -i 's#/usr/bin/env python#/usr/bin/env python2#' tools/xml2po.py

%build
export ALL_LINGUAS="de el en es fi fr ja ko nn ru sl sv zh_CN"
%configure2_5x --build=%{_host} --without-gimp
%make

%install
%makeinstall_std
