# encoding: utf-8
from .models import Host,Host_All


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
            'os' : host.os,
            'kernel' : host.kernel,
            'arch' : host.arch,
            'cpu_number' : host.cpu_number,
            'cpu_core' : host.cpu_core,
            'cpu_vcore' : host.cpu_vcore,
            'cpu_name' : host_all.cpu_name,
            'mem_size' : host.mem_size,
            'server_name' : host_all.server_name,
            'server_producter' : host_all.server_producter,
            'serial' : host_all.serial,
            'network' : host_all.network,
            'partitons' : host_all.partitons,
            'discover_time' : host.discover_time,
            'update_time' : host.update_time,
            'remark' : host.remark
        }

    return result