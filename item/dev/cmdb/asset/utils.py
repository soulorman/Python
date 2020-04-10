# encoding: utf-8
from .models import Host,Host_More,Deploy
from django.utils import timezone

def compose(id):
    """获取更多资源的字典格式

    :param id:信息的id
    :return: 信息的字典格式
    """
    result = None
    host = Host.objects.get(pk=id)
    host_mores = Host_More.objects.filter(ip=host.ip)

    for host_more in host_mores:
        result  = {
            'id' : id,
            'name' : host.name,
            'ip' : host.ip,
            'mac' : host_more.mac,
            'cpu_number' : host.cpu_number,
            'cpu_core' : host.cpu_core,
            'cpu_vcore' : host.cpu_vcore,
            'cpu_name' : host_more.cpu_name,
            'server_name' : host_more.server_name,
            'server_producter' : host_more.server_producter,
            'serial' : host_more.serial,
            'network' : host_more.network[1:-1],
            'partitions' : host_more.partitions[1:-1],
            'discover_time' : host.discover_time,
            'update_time' : host.update_time,
            'user' : host_more.user,
            'remark' : host.remark,
        }

    return result


def compose_up(id):
    """获取部署页面的信息，并作为字典返回

    :param id:信息的id
    :return: 信息的字典格式
    """
    deploy = Deploy.objects.get(pk=id)
    result = {
            'hospital_address' : deploy.hospital_address,
            'project_name' : deploy.project_name,
            'deploy_version' : deploy.deploy_version,
            'update_time' : deploy.update_time,
            'remark' : deploy.remark,
            }

    return result


def save_new_deploy_info(params):
    """存储新的部署信息

    :param params:前端返回的数据
    :return: 保存结果
    """
    deploy = None
    deploy = Deploy()
    deploy.hospital_address = params.get('hospital_address','无')
    deploy.project_name = params.get('project_name', '无')
    deploy.deploy_version = params.get('deploy_version', '无')
    deploy.update_time = params.get('update_time', timezone.now())
    deploy.remark = params.get('remark', '无')
    deploy.save()

    return deploy