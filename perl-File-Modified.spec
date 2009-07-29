%define upstream_name    File-Modified
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	File::Modified - checks intelligently if files have changed
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Modified module is intended as a simple method for programs to detect
whether configuration files (or modules they rely on) have changed. There are
currently two methods of change detection implemented, mtime and MD5.
The MD5 method will fall back to use timestamps if the Digest::MD5 module
cannot be loaded.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
