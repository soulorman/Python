#encoding: utf-8

import subprocess

#[1,2,3,4,5,7,8]
#['舒克','贝塔','萨达姆']

def get_gpu_user():
    return subprocess.getoutput("for i in `seq 0 8`;do bash /etc/zabbix/zabbix_agentd.d/gpu_user_1.sh $i;done").split('\n')

def get_gpu_use():
    return subprocess.getoutput("for i in `seq 0 8`;do bash /etc/zabbix/zabbix_agentd.d/gpu_use.sh $i;done").split('\n')

#def get_gpu_program():
#    return subprocess.getoutput("cat /proc/cpuinfo | grep 'processor' | sort | uniq | wc -l")

if __name__ == '__main__':
    print(get_gpu_user())
    print(get_gpu_use())



function reload_resource_chart(ip){
    jQuery.get("{% url 'asset:resource_ajax' %}", {'ip' : ip, '_':(new Date()).getTime()}, function(result) {
        if(result['code'] == 200) {
            option.xAxis.data = result['result']['xAxis'];
            option.series[0].data = result['result']['CPU_datas'];
            option.series[1].data = result['result']['MEM_datas'];

            chart_resource.setOption(option);
            } else if(result['code'] == 400){
                var errors = []
                jQuery.each(result['errors'], function(k, v){
                  errors.push(v)
            });
                swal("获取数据失败:", errors.join('\n'), "error");
            } else if(result['code'] == 403){
            swal({
                title: "未登录",
                text: "",
                timer: 2000,
                showConfirmButton: false
            });
        }
        }, 'json');
    }


        reload_resource_chart(ip);
        setInterval(function(){
            reload_resource_chart(ip);
        }, 300000);