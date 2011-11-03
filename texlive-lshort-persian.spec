# revision 15878
# category Package
# catalog-ctan /info/lshort/persian
# catalog-date 2009-11-09 23:05:00 +0100
# catalog-license pd
# catalog-version 4.26:2009-08-04
Name:		texlive-lshort-persian
Version:	4.26:2009-08-04
Release:	1
Summary:	Persian (Farsi) introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/persian
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-persian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-persian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A Persian (Farsi) translation of Oetiker's (not so) short
introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-persian/README
%doc %{_texmfdistdir}/doc/latex/lshort-persian/appendix.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lshort-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lshort-base.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lshort.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lshort.sty
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lshort.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-persian/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/preface.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/transpreface.tex
%doc %{_texmfdistdir}/doc/latex/lshort-persian/typeset.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
