%define real_name File-Modified

Summary:	File::Modified - checks intelligently if files have changed
Name:		perl-%{real_name}
Version:	0.07
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Modified module is intended as a simple method for programs to detect
whether configuration files (or modules they rely on) have changed. There are
currently two methods of change detection implemented, mtime and MD5.
The MD5 method will fall back to use timestamps if the Digest::MD5 module
cannot be loaded.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README example
%{perl_vendorlib}/File/Modified.pm
%{_mandir}/*/*

