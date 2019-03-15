Name:      simengine-database
Version:   3.14
Release:   1%{?dist}
Summary:   SimEngine - Databases
URL:       https://github.com/Seneca-CDOT/simengine
License:   GPLv3+

%global gittag %{version}

Source0: https://github.com/Seneca-CDOT/simengine/archive/%{gittag}/simengine-%{version}.tar.gz
BuildArch: noarch

Requires:  neo4j, cypher-shell, redis, python-neo4j-driver, python-redis

%description
Installs the SimEngine database configuration for Neo4j.

%pre
systemctl stop neo4j

%prep
%autosetup -c %{name}

%build

%install
mkdir -p %{buildroot}%{_sharedstatedir}/neo4j/data/dbms/
cp -fp simengine-%{version}/database/auth %{buildroot}%{_sharedstatedir}/neo4j/data/dbms/

%files
%attr(0644, neo4j, neo4j) %{_sharedstatedir}/neo4j/data/dbms/auth

%post
systemctl enable neo4j --now
systemctl enable redis --now
sleep 10
echo "CREATE CONSTRAINT ON (n:Asset) ASSERT (n.key) IS UNIQUE;" | cypher-shell -u simengine -p simengine

%changelog
* Fri Mar 15 2019 Chris Tyler <ctyler.fedora@gmail.com> - 3.14-1
- new version

* Fri Mar 15 2019 Chris Tyler <ctyler.fedora@gmail.com> - 3.13-1
- new version

* Fri Mar 15 2019 Chris Tyler <ctyler.fedora@gmail.com> - 3.12-1
- new version

* Mon Mar 11 2019 Chris Tyler - 3.11-1
- new version

* Mon Mar 11 2019 Chris Tyler <ctyler.fedora@gmail.com> - 3.10-1
- new version

* Mon Mar 11 2019 Chris Tyler <ctyler.fedora@gmail.com> - 3.8-1
- new version

* Fri Mar 01 2019 Chris Tyler <chris.tyler@senecacollege.ca> - 3.7-3
- Updated for simengine 3.7

* Thu Aug 16 2018 Chris Johnson <chris.johnson@senecacollege.ca>
- Updated package dependencies, converted SPEC file to encompass all database work (previously simegine-neo4jdb)

* Mon Jul 23 2018 Chris Johnson <chris.johnson@senecacollege.ca>
- First alpha flight
