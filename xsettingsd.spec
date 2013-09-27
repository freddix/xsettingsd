%define		gitver	474f18a687010d04e81820a4afa5e06a79bc3ebe

Summary:	Daemon that implements the XSETTINGS specification
Name:		xsettingsd
Version:	20121210
Release:	1
License:	BSD
Group:		X11/Applications
# git clone git://github.com/derat/xsettingsd.git
# git archive --format=tar --prefix=xsettingsd/ HEAD | xz -c > xsettingsd-gitver.tar.xz
Source0:	%{name}-%{gitver}.tar.xz
# Source0-md5:	773392ac2e044f66fab2e913e265a5e9
URL:		http://code.google.com/p/xsettingsd
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRequires:	scons
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsettingsd is a daemon that implements the XSETTINGS specification.
It is intended to be small, fast, and minimally dependent on other
libraries. It can serve as an alternative to gnome-settings-daemon
for users who are not using the GNOME desktop environment but who
still run GTK+ applications and want to configure things such as
themes, font antialiasing/hinting, and UI sound effects.

%prep
%setup -qn %{name}

%build
export CC='%{__cc}'
export CPPFLAGS='%{rpmcflags}'
export CXX='%{__cxx}'
export CXXFLAGS='%{rpmcxxflags}'
export LDFLAGS='%{rpmldflags}'
%{__scons}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install xsettingsd dump_xsettings $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/dump_xsettings
%attr(755,root,root) %{_bindir}/xsettingsd
%{_mandir}/man1/*.1*

