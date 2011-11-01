Name:		texlive-courseoutline
Version:	1.0
Release:	1
Summary:	Prepare university course outlines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/courseoutline
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Courseoutline is a class designed to minimise markup in a
tedious task that needs to be repeated often.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/courseoutline/courseoutline.cls
%doc %{_texmfdistdir}/doc/latex/courseoutline/Outline.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
