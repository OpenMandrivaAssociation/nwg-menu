%define _empty_manifest_terminate_build 0

Name:       nwg-menu
Version:    0.1.1
Release:    1
Summary:    MenuStart plugin to nwg-panel, also capable of working standalone
Group:      System/X11/Utilities/NWG 
License:    MIT
URL:        https://github.com/nwg-piotr/nwg-menu
Source:     https://github.com/nwg-piotr/nwg-menu/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: go
BuildRequires: pkgconfig(gtk-layer-shell-0)

Requires: typelib(GtkLayerShell)
Requires: gtk+3.0

Recommends: alacritty
Recommends: thunar

%description
This code provides the MenuStart plugin to nwg-panel. It also may be used standalone, however, with a little help from command line arguments.
This program is being developed with sway in mind. 
It should work with other wlroots-based Wayland compositors, but for now it's only been tested briefly on Wayfire.
The nwg-menu command displays the system menu with simplified freedesktop main categories (8 instead of 13). 
It also provides the search entry, to look for installed application on the basis of .desktop files, and for files in XDG user directories.
You may pin applications by right-clicking them. Pinned items will appear above the categories list. 
Right-click a pinned item to unpin it. The pinned items cache is shared with the nwggrid command, which is a part of nwg-launchers.
In the bottom-right corner of the window you'll also see a set of buttons: logout, lock screen, restart and shutdown. 
The commands attached to them may be defined in the nwg-panel settings or given as the arguments.
    
%prep
%autosetup -p1
  
%build
go build -o bin/nwg-menu *.go
  
%install
  
%files
