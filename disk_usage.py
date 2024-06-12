import shutil

du = shutil.disk_usage('C:')
percentage = (du.used/du.total)*100
print('Disk usage: ',"{:.2f}".format(percentage))