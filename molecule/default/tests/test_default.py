import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_locales(host):
    f = host.file('/etc/default/locale')

    assert f.exists

    # assert f.contains("LANG=en_US.UTF-8")
    # assert f.contains("LC_ALL=en_US.UTF-8")



