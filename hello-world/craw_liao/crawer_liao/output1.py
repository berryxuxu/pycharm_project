#coding:utf-8

class Output(object):
    def output(self, count, filename, dic):

        f = open('D://liao/'+ str(count) +'. '+ filename + '.html','wb')
        f.write(filename.encode('utf-8'))
        f.write('\n')
        f.write('\n')
        for content in dic[filename]:
            f.write('    ')
            f.write(content.encode('utf-8'))
            f.write('\n')
            f.write('\n')
        f.close()
        #jpg = urlretrieve(image,'D://PIC/'+str(count)+'.html')


