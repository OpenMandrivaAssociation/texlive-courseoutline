%global tl_name courseoutline
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Prepare university course outlines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/courseoutline
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/courseoutline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Courseoutline is a class designed to minimise markup in a tedious task
that needs to be repeated often.

