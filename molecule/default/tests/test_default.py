import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    assert (host.package('openjdk-8-jre-headless').is_installed
            or host.package('java-1.8.0-openjdk-headless').is_installed)


def test_java_binary(host):
    # Check java availability
    run1 = host.run('java -version')
    assert run1.rc == 0


def test_jce(host):
    cmd = "java -cp /tmp Main"
    run = host.run(cmd)
    assert 'true' in run.stdout


def test_bouncycastle(host):
    lib_path = '/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/'
    jar1 = lib_path + 'bcpkix-jdk15on-1.51.jar'
    assert host.file(jar1).exists
    jar2 = lib_path + 'bcprov-jdk15on-1.51.jar'
    assert host.file(jar2).exists
