import webbrowser
#https://www.facebook.com/
#https://www.google.com/gmail/
#https://www.google.com/
#https://www.youtube.com/
def test(welcome):
	if welcome[0:len("youtube")]=="youtube":
		webbrowser.open("https://www.youtube.com/")
    #webbrowser.open("https://www.youtube.com/results?search_query="+welcome[8:])         
    elif welcome =="facebook":
    	webbrowser.open("https://www.facebook.com/")
    elif welcome=="gmail":
    	webbrowser.open("https://www.google.com/gmail/")
    elif welcome=="google":
    	webbrowser.open("https://www.google.com/")			