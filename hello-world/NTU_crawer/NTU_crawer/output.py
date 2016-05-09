#coding:utf-8
class Output(object):
    def __init__(self):
        self.lis = []

    def add(self, data):
        if data == None :
            return
        else:
            self.lis.append(data)
            #print data


    def out_html(self):
        fh = open('ntu.html','w')
        fh.write('<html>')
        fh.write('<body>')
        fh.write('<table>')
        for data in self.lis:
            fh.write('<tr>')
            fh.write('<td>%s<td>'%data['title'].encode('utf-8'))
            fh.write('</tr>')
        fh.write('</table>')
        fh.write('</body>')
        fh.write('</html>')
        fh.close()