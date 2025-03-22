Name:           filotimo-fonts
Version:        1.0
Release:        1%{?dist}
Summary:        Fontface for Filotimo Linux

License:        OFL-1.1
URL:            https://github.com/filotimo-project/fonts
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint
BuildRequires:  python3-devel

%description
Customised fonts from Filotimo - taken from https://gitlab.gnome.org/GNOME/adwaita-fonts.

%define debug_package %{nil}

%prep
%setup -q

%build
python3 -m pip install --user --upgrade opentype-feature-freezer
export PATH=$HOME/.local/bin:$PATH
./build.sh

%install
mkdir -p %{buildroot}%{_datadir}/fonts/Filotimo
install -p {mono,sans}/*.ttf %{buildroot}%{_datadir}/fonts/Filotimo/

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/fonts/Filotimo
%{_datadir}/fonts/Filotimo/FilotimoMono-Bold.ttf
%{_datadir}/fonts/Filotimo/FilotimoMono-BoldItalic.ttf
%{_datadir}/fonts/Filotimo/FilotimoMono-Italic.ttf
%{_datadir}/fonts/Filotimo/FilotimoMono-Regular.ttf
%{_datadir}/fonts/Filotimo/FilotimoSans-Italic.ttf
%{_datadir}/fonts/Filotimo/FilotimoSans-Regular.ttf

%changelog
* Sat Mar 22 2025 Thomas Duckworth <tduck@filotimoproject.org> 1.0-1
- new package built with tito

* Sat Mar 22 2025 Thomas Duckworth <tduck@filotimoproject.org> 1.0-1
- new package built with tito

