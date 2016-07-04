# -*-coding:utf-8 -*-


import MySQLdb
from globe_var import *
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

def get_movie_info(movie_type):
    if movie_type == '全部' or movie_type.encode("utf-8") in movie_types:
        content = query_mysql(movie_type)
        return content
    else:
        content = '请输入："类型",获取电影类型'
        return content


def query_mysql(movie_type):
        conn = MySQLdb.connect(host=mysql_info['host'], user=mysql_info['user'], passwd=mysql_info['passwd'],
                               db=mysql_info['db'], port=int(mysql_info['port']), charset='utf8')
        cur = conn.cursor()
        if movie_type == '全部':
            sql = 'SELECT movie_name,movie_score,people_num,movie_url FROM  movie_info WHERE movie_id >= ((SELECT ' \
                  'MAX(movie_id) FROM movie_info)-(SELECT MIN(movie_id) FROM movie_info)) * RAND() + (SELECT MIN(movie_id) ' \
                  'FROM movie_info)  LIMIT 3'
        else:
            sql = 'SELECT movie_name,movie_score,people_num,movie_url FROM  movie_info WHERE movie_id >= ((SELECT ' \
                  'MAX(movie_id) FROM movie_info)-(SELECT MIN(movie_id) FROM movie_info)) * RAND() + (SELECT MIN(movie_id) ' \
                  'FROM movie_info) AND movie_type LIKE "%%%s%%"  LIMIT 3' % movie_type
        cur.execute(sql)
        result = cur.fetchmany(3)
        conn.cursor().close()
        conn.close()
        movie1 = '电影名:'+result[0][0].encode('utf-8')+' 电影评分:'+result[0][1]+' 评分人数:'+result[0][2]+' 豆瓣电影链接:'\
                 +result[0][3].encode('utf-8')
        movie2 = '电影名:'+result[1][0].encode('utf-8')+' 电影评分:'+result[1][1]+' 评分人数:'+result[1][2]+' 豆瓣电影链接:'\
                 +result[1][3].encode('utf-8')
        movie3 = '电影名:'+result[2][0].encode('utf-8')+' 电影评分:'+result[2][1]+' 评分人数:'+result[2][2]+' 豆瓣电影链接:'\
                 +result[2][3].encode('utf-8')
        content = '1.'+movie1+'\n2.'+movie2+'\n3.'+movie3
        return content

#
# def main():
#     content = get_movie_info('123')
#     print(content)
# if __name__ == '__main__':
#     main()

