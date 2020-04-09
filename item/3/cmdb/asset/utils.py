# encoding: utf-8
from .models import Host,Host_All,Deploy


def compose(id):

    result = None
    host = Host.objects.get(pk=id)
    host_alls = Host_All.objects.filter(ip=host.ip)

    for host_all in host_alls:
        result  = {
            'id' : id,
            'name' : host.name,
            'ip' : host.ip,
            'user' : host_all.user,
            'mac' : host_all.mac,
            'cpu_number' : host.cpu_number,
            'cpu_core' : host.cpu_core,
            'cpu_vcore' : host.cpu_vcore,
            'cpu_name' : host_all.cpu_name,
            'server_name' : host_all.server_name,
            'server_producter' : host_all.server_producter,
            'serial' : host_all.serial,
            'network' : host_all.network[1:-1],
            'partitions' : host_all.partitions[1:-1],
            'discover_time' : host.discover_time,
            'update_time' : host.update_time,
            'remark' : host.remark,
            'gpu_info' : host.gpu_info

        }

    return result


def compose_up(id):

    result = None
    deploy = Deploy.objects.get(pk=id)

    result  = {
            'hospital_address' : deploy.hospital_address,
            'project_name' : deploy.project_name,
            'deploy_version' : deploy.deploy_version,
            'update_time' : deploy.update_time,
            'remark' : deploy.remark,
        