Name:           stepmania
Summary:        Advanced cross-platform rhythm game for home and arcade use
Version:        5.0.12
Release:        1%{?dist}
License:        Copyrighted
BuildRequires:  cmake
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  yasm
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libmad-devel
BuildRequires:  bzip2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libva-devel
BuildRequires:  pcre-devel
BuildRequires:  gtk2-devel
BuildRequires:  glew-devel
BuildRequires:  libudev-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-devel
URL:            https://www.stepmania.com/
Source0:        https://github.com/stepmania/stepmania/archive/v5.0.12.zip
Source1:        https://github.com/stepmania/fmt/archive/0b097da31eae1642dd8132f2996e74f7fe354e46.zip
Source2:        https://github.com/stepmania/ffmpeg/archive/eda6effcabcf9c238e4635eb058d72371336e09b.zip
Source3:        https://github.com/stepmania/googletest/archive/0dd5ef8bd4b9e3978955e8cdab2eec7016dda4c2.zip
Source4:        https://github.com/stepmania/ogg/archive/18c401c6bc8814d06f3ae53ebf5d4399f90871cc.zip
Source5:        https://github.com/stepmania/vorbis/archive/d8ffc480787fcd8b5bb7203d6e0acf3bbfb2dd02.zip
Source6:        https://github.com/stepmania/libtomcrypt/archive/e24b01d3925265c4999ad9a63f3d8707af201952.zip
Source7:        https://github.com/stepmania/libtommath/archive/3aba4eacc639dc85b3bc93bf565d2aea91e1ecb7.zip

%description
StepMania is an advanced cross-platform rhythm game for home and arcade use.

%prep
%autosetup -b1 -n stepmania-%{version}
%autosetup -T -D -b2
%autosetup -T -D -b3
%autosetup -T -D -b4
%autosetup -T -D -b5
%autosetup -T -D -b6
%autosetup -T -D -b7
mv ../fmt-0b097da31eae1642dd8132f2996e74f7fe354e46 extern/cppformat
mv ../ffmpeg-eda6effcabcf9c238e4635eb058d72371336e09b extern/ffmpeg-linux-2.1.3
mv ../googletest-0dd5ef8bd4b9e3978955e8cdab2eec7016dda4c2 extern/googletest
mv ../ogg-18c401c6bc8814d06f3ae53ebf5d4399f90871cc extern/libogg-git
mv ../vorbis-d8ffc480787fcd8b5bb7203d6e0acf3bbfb2dd02 extern/libvorbis-git
mv ../libtomcrypt-e24b01d3925265c4999ad9a63f3d8707af201952 extern/tomcrypt
mv ../libtommath-3aba4eacc639dc85b3bc93bf565d2aea91e1ecb7 extern/tommath

%build
cd Build
cmake .. \
  -G 'Unix Makefiles' \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=%{_datadir} \
  -DSM_FFMPEG_SRC_DIR=../extern/ffmpeg-git

cmake ..
%make_build

%install
cd Build
%make_install

# icon to pixmaps
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 644 ../icons/hicolor/scalable/apps/stepmania-ssc.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

# .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Name=%{name}
GenericName=Stepmania
Comment=Advanced cross-platform rhythm game for home and arcade use
Exec=stepmania
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

false

%files
%{_datadir}/stepmania-5.0
%{_datadir}/pixmaps/stepmania.svg
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Sep 5 2017 Jan Kalina <jkalina@redhat.com> - 5.0.12-1
- Initial packaging

