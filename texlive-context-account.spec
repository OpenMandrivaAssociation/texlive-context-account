# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-account
# catalog-date 2009-02-07 09:38:09 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-account
Version:	20090207
Release:	6
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

%description
TeXLive context-account package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090207-2
+ Revision: 750484
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090207-1
+ Revision: 718122
- texlive-context-account
- texlive-context-account
- texlive-context-account
- texlive-context-account

