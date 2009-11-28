%define		_rc	rc2
Summary:	Data files for Canta
Name:		canta-media
Version:	0.2
Release:	0.%{_rc}.0.1
License:	GPLv3
Group:		X11/Applications/Games
Source0:	http://cgit.canta-game.org/cgit.cgi/canta-media/snapshot/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	43ecf1772bdae11b0581c05dbdb80841
URL:		http://www.canta-game.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data files for Canta.

%prep
%setup -qn %{name}-%{version}-%{_rc}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/canta/media
cp -a songs themes $RPM_BUILD_ROOT%{_datadir}/canta/media

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/canta/media/songs/*
%{_datadir}/canta/media/themes/*
