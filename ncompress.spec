#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ncompress
Version  : 4.2.4.4
Release  : 11
URL      : http://downloads.sourceforge.net/ncompress/ncompress-4.2.4.4.tar.gz
Source0  : http://downloads.sourceforge.net/ncompress/ncompress-4.2.4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain

%description
This is version 4.2 of (N)compress (an improved version of compress 4.1).
Compress is a fast, simple LZW file compressor.  Compress does not have
the highest compression rate, but it is one of the fastest programs to
compress data.  Compress is the defacto standard in the UNIX community
for compressing files.

%prep
%setup -q -n ncompress-4.2.4.4

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%exclude /usr/local/bin/compress
%exclude /usr/local/bin/zcat
%exclude /usr/local/bin/zcmp
%exclude /usr/local/bin/zdiff
%exclude /usr/local/bin/zmore
%exclude /usr/local/man/man1/compress.1
%exclude /usr/local/man/man1/zcmp.1
%exclude /usr/local/man/man1/zmore.1
/usr/local/bin/uncompress
