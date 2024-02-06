import favicon
import requests
import sys
import getopt
import os
import re

def main():
   argv = sys.argv[1:]
   url = ''
   fi = 0
   try:
     opts, args = getopt.getopt(argv,"u:",["url="])
   except getopt.GetoptError:
      print (__file__,'-u url')
      sys.exit(2)
   if not opts:
      print ('Usage: ',__file__,' -u url')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ('-u', '--url'):
         url = arg
         print ('Url is ', url)
      else:
         print ('Usage: ',__file__,' -u url')
         sys.exit(0)
   
   icons = favicon.get(url)
   for icon in icons:
     if 'favicon.ico' in icon.url:
       print (icon.url)
       fi += 1 
       site_name = re.sub(r"https?://(www\.)?",'',url)
       response = requests.get(icon.url, allow_redirects=True)
       icon_file = '/tmp/icons/'+site_name+'.'+format(icon.format)
       print (icon_file)
       os.makedirs(os.path.dirname(icon_file), exist_ok=True)
       open(icon_file,"wb").write(response.content)
   if fi == 0:
       print ('There is no favicon.ico on this site')
       sys.exit(0)

if __name__ == "__main__":
   main()
