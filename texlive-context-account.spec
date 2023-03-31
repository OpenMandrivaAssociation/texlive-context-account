Name:		texlive-context-account
Version:	47085
Release:	2
Summary:	A simple accounting package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-account
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-account.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-account.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/account
%doc %{_texmfdistdir}/doc/context/third/account

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
