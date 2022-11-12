Name:		texlive-courseoutline
Version:	15878
Release:	1
Summary:	Prepare university course outlines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/courseoutline
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Courseoutline is a class designed to minimise markup in a
tedious task that needs to be repeated often.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/courseoutline/courseoutline.cls
%doc %{_texmfdistdir}/doc/latex/courseoutline/Outline.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
