# 查询sql
# encoding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .models import Monitor_Resource

error_dict = {
                'mem_error':'内存可使用资源不足',
                'cpu_error':'cpu使用率超过85%',
                'disk_error':'磁盘可使用资源不足',
                'process_error': '进程已意外关闭',
                'process_error_mem': '单进程使用内存超过85%',
                'process_error_cpu': '单进程使用CPU超过85%',
            }

legend = [
    'auth',
    'path',
    'recovery',
    'thoslide',
    'config',
    'registry',
    'tensorflow_model_server',
    'save_log',
    'celery',
    'redis',
    'nginx',
    'mysql'
]

def get_info(info):
    """定制邮件格式

    :param info:邮件内容
    :return: 格式化的邮件内容
    """  
    email = '<table border="1" cellspacing="0" cellpadding="0"><tr><th>报错的原因</th><th>具体报错的内容</th><th>发生错误的时间</th></tr>'
    for i in info:
        email += '<tr>'
        for j in i:
            email +='<td style="text-align:center;vertical-align:middle;padding:10px;font-size: 18px;">' + str(j) + '</td>'
        email += '</tr>'
    email += '</table>'

    return email

def send_mail(email_content):
    """发送邮件

    :param email_content： 邮件内容
    :return: 无
    """  
    mail_host="smtp.exmail.qq.com"
    mail_user="watchdog@thorough.ai"
    mail_pass="Xueqing1101"

    sender = 'watchdog@thorough.ai'
    receivers = ['wangyuxi@thorough.ai']

    content = email_content

    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = Header("CMDB系统", 'utf-8')
    message['To'] =  Header("系统管理人员", 'utf-8')

    subject = u'报错邮件'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())


def get_error_info(address_ip, start_time):
    """发现错误就发邮件

    :param address_ip：报警的服务器的ip
    :param start_time：判断时间
    :return: 报警结果
    """  
    mem_error = Monitor_Resource.objects.filter(ip=address_ip, mem_free__lte=2000, created_time__gte=start_time).values('mem_free','created_time').last()
    cpu_error = Monitor_Resource.objects.filter(ip=address_ip, cpu_total_use__gte=85, created_time__gte=start_time).values('cpu_total_use','created_time').last()
    
    disk_error = Monitor_Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('volume','created_time').last()
    process_error = Monitor_Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_isalive','created_time').last()
    
    process_error_mem = Monitor_Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_mem_use','created_time').last()
    process_error_cpu = Monitor_Resource.objects.filter(ip=address_ip, created_time__gte=start_time).values('process_cpu_use','created_time').last()

    # 此处适合用class类来解决
    result = []
    if mem_error:
        result.append((error_dict['mem_error'],str(mem_error.get('mem_free',''))+'Mb',mem_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if cpu_error:
        result.append((error_dict['cpu_error'],str(cpu_error.get('cpu_total_use',''))+'%',cpu_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error:
        for idx_process,v_process in enumerate(process_error.get('process_isalive',[]).replace(' ','').split(',')[:-1:]):
            if '0' == v_process:
                result.append((error_dict['process_error'],legend[idx_process],process_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))
            
    if disk_error:
        for idx_disk,v_disk in enumerate(disk_error.get('volume',[]).replace(' ','').split(',')[:-1:]):
            if float(v_disk.split(':')[1][:-2:]) <= 100:
                result.append((error_dict['disk_error'],disk_error.get('volume',[]).replace(' ','').split(',')[:-1:][idx_disk],disk_error['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error_cpu:
        for idx_process_cpu,v_process_cpu in enumerate(process_error_cpu.get('process_cpu_use',[]).replace(' ','').split(',')[:-1:]):
            if float(v_process_cpu) >= 85:
                result.append((error_dict['process_error_cpu'],legend[idx_process_cpu],str(process_error_cpu.get('process_cpu_use',[]).replace(' ','').split(',')[:-1:][idx_process_cpu])+'%',process_error_cpu['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if process_error_mem:
        for idx_process_mem,v_process_mem in enumerate(process_error_mem.get('process_mem_use',[]).replace(' ','').split(',')[:-1:]):
            if float(v_process_mem) >= 85:
                result.append((error_dict['process_error_mem'],legend[idx_process_mem],str(process_error_mem.get('process_mem_use',[]).replace(' ','').split(',')[:-1:][idx_process_mem])+'%',process_error_mem['created_time'].strftime('%Y-%m-%d_%H:%M:%S')))

    if result:
        send_mail(get_info(result))

    return  result