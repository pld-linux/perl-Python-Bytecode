#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Python
%define	pnam	Bytecode
Summary:	Python::Bytecode - Disassemble and investigate Python bytecode
Name:		perl-Python-Bytecode
Version:	2.7
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Python/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e357351a3bf32c54ac1aa8910b4c53f7
URL:		http://search.cpan.org/dist/Python-Bytecode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python::Bytecode accepts a string or filehandle contain Python
bytecode and puts it into a format you can manipulate.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Python/*.pm
%{perl_vendorlib}/Python/Bytecode
%{_mandir}/man3/*
