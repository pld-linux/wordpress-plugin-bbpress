%define		plugin	bbpress
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	bbPress is forum software, made the WordPress way
Name:		wordpress-plugin-%{plugin}
Version:	2.4.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/bbpress.%{version}.zip
# Source0-md5:	6657454e11d0f2243b97e9f5092a9c55
URL:		http://wordpress.org/plugins/bbpress/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	webapps
Requires:	webserver(php)
Requires:	wordpress >= 3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wordpress
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/plugins
%define		plugindir	%{pluginsdir}/%{plugin}

%description
bbPress is forum software, made the WordPress way.

%prep
%setup -qc
mv %{plugin}/* .
rmdir %{plugin}

rm languages/bbpress.pot
find -name index.php | xargs rm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/{readme,humans,license}.txt
rm -f $RPM_BUILD_ROOT%{plugindir}/debug*.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt humans.txt
%dir %{plugindir}
%{plugindir}/bbpress.php
%{plugindir}/includes
%{plugindir}/templates
