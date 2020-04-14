# encoding: utf-8
from django.db import connection, models


class AccessLogFile(models.Model):
    name = models.CharField(max_length=128, null=False, default='')
    path = models.CharField(max_length=1024, null=False, default='')
    status = models.IntegerField(default=0)

    created_time = models.DateTimeField(auto_now_add=True)


class AccessLog(models.Model):
    file_id = models.IntegerField(null=False, default=0)
    ip = models.CharField(max_length=128, null=False, default='')
    url = models.CharField(max_length=1024, null=False, default='')
    status_code = models.IntegerField(null=False, default=0)

    access_time = models.DateTimeField(null=False)

    @classmethod
    def dist_status_code(cls, file_id):
        """扇形图数据处理

        :param: file_id: 文件的id号
        :return: x，y轴的信息
        """
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT status_code,count(*)
                FROM webanalysis_accesslog
                WHERE file_id = %s
                GROUP BY status_code;
            ''', (file_id))

        rt = cursor.fetchall()

        legend = []
        series = []
        for line in rt:
            legend.append(str(line[0]))
            series.append({"name" : str(line[0]), "value" : line[1]})

        return legend, series

    @classmethod
    def tren_visit(cls, file_id):
        """柱状图数据处理

        :param: file_id: 文件的id号
        :return: x，y轴的信息
        """
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT date_format(access_time, '%%Y-%%m-%%d %%H:00:00') as day, count(*) as cnt
                FROM webanalysis_accesslog
                WHERE file_id = %s and access_time >= %s
                GROUP BY day
                ORDER BY day;
            ''', (file_id, '1900-01-01'))

        rt = cursor.fetchall()
        xAxis = []
        series = []
        for line in rt:
            xAxis.append(line[0])
            series.append(line[1])


        return  xAxis, series