Name:		texlive-knowledge
Version:	70594
Release:	1
Summary:	Displaying, hyperlinking, and indexing notions in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/knowledge
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knowledge.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knowledge.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knowledge.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a systematic way to handle
notions/concepts/terms throughout a document. It helps building
an index. In combination with hyperref it makes it easy to have
every reference of a concept linked to its introduction. It
also offers simple notations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/knowledge
%{_texmfdistdir}/tex/latex/knowledge
%doc %{_texmfdistdir}/doc/latex/knowledge

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
