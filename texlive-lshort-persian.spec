%global tl_name lshort-persian
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.01
Release:	%{tl_revision}.1
Summary:	Persian (Farsi) introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/persian
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-persian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-persian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Persian (Farsi) translation of Oetiker's (not so) short introduction.

