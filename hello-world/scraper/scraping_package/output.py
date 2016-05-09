# -*- coding: UTF-8 -*-
class Output(object):
    def __init__(self):
        self.data = []

    def collect_data(self, new_datas):
        if new_datas == None :
            return
        else :
            self.data.append(new_datas)

    def output_html(self):
        fhand = open('baiduwiki.html','w')
        fhand.write('<html>')
        fhand.write('<body>')
        fhand.write('<table>')

        for data in self.data:
            fhand.write('<tr>')
            fhand.write('<td>%s<td>'%data['url' ])
            fhand.write('<td>%s<td>'%data['title'].encode('utf-8'))
            fhand.write('<td>%s<td>'%data['summary'].encode('utf-8'))
            fhand.write('</tr>')

        fhand.write('</table>')
        fhand.write('</body>')
        fhand.write('</html>')
        fhand.close()