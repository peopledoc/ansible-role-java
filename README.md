# Ansible Role: OpenJDK Java

[![Build Status](https://travis-ci.org/peopledoc/ansible-role-java.svg?branch=master)](https://travis-ci.org/peopledoc/ansible-role-java)

Installs OpenJDK Java for Debian linux servers.

## Role Variables

Available variables are listed below, along with default values:

    # The defaults provided by this role are specific to each distribution.
    java_packages:
      - openjdk-11-jdk
    openjdk_version: 11
    java_home: /usr/lib/jvm/java-11-openjdk-amd64


Set the version/development kit of Java to install, along with any other necessary Java packages.
By default, on Debian Buster, Java 11 will be installed. On older Debian, Java 8 will be installed.

CA certificates can be added to the java keystore with the following variables:

```yaml
cacerts_location: ...            # Role default: "jre/lib/security/cacerts", it may be needed to be change according to the installed jdk version
ca_certificates_password: ...    # Role default: "changeit", but you should define your own from vault
devsecops_ca_enabled: True|False # Role default: true, for the local should be false
app_certificates:                # Role default: [], the app can define its own certificates
  - alias: ...
    path: ...
```

```yaml
    keep_oracle_jdk: false
    add_bouncycastle: true
```

This role uninstall OracleJDK by default. You can change the
`keep_oracle_jdk` variable to keep it. This is only available on
Debian distributions. `add_bouncycastle` can be used to add
bouncycastle libs to the JDK.

For bouncycastle you can change the downloaded version and the
artifacts pulled with :

``` yaml
bouncycastle_version: '1.51'
bouncycastle_artifacts:
  - bcpkix
  - bcprov
```


## Dependencies

None.

## Dependencies for tests

The dependencies are `ansible`, `molecule` and `docker` Python packages.

## Tests

Tests can be executed using:

```
$ molecule test --all
```

## License

MIT / BSD

## Author Information

This role was originally created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
