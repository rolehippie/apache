import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_apache_running_and_enabled(host):
    svc = host.service("apache2")
    assert svc.is_running
    assert svc.is_enabled

def test_apache_listener(host):
    assert host.socket("tcp://127.0.0.1:80").is_listening

def test_exporter_running_and_enabled(host):
    svc = host.service("apache-exporter")
    assert svc.is_running
    assert svc.is_enabled

def test_exporter_listener(host):
    assert host.socket("tcp://127.0.0.1:9117").is_listening
