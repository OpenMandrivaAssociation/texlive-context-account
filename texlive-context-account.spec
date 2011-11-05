# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-account
# catalog-date 2009-02-07 09:38:09 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-account
Version:	20090207
Release:	1
Summary:	A simple accounting package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-account
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-account.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-account.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive context-account package.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-account.xml
%{_texmfdistdir}/tex/context/third/account/t-account.mkii
%{_texmfdistdir}/tex/context/third/account/t-account.mkiv
%{_texmfdistdir}/tex/context/third/account/t-account.tex
%{_texmfdistdir}/tex/context/third/account/t-floatnumber.mkii
%{_texmfdistdir}/tex/context/third/account/t-floatnumber.mkiv
%{_texmfdistdir}/tex/context/third/account/t-floatnumber.tex
%doc %{_texmfdistdir}/doc/context/third/account/README
%doc %{_texmfdistdir}/doc/context/third/account/account-doc.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
