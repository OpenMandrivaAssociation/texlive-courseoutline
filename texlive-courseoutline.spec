# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/courseoutline
# catalog-date 2008-09-18 22:52:44 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-courseoutline
Version:	1.0
Release:	10
Summary:	Prepare university course outlines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/courseoutline
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750575
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718158
- texlive-courseoutline
- texlive-courseoutline
- texlive-courseoutline
- texlive-courseoutline

