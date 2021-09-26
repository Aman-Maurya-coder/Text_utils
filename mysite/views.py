from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,"index.html")
	
def analyze(request):
	txt=request.POST.get("text","default")
	removepunc=request.POST.get("rempunc","off")
	upper=request.POST.get("upcs","off")
	new=request.POST.get("newrem","off")
	sp=request.POST.get("sprem","off")
	if removepunc=="on":
		analy=""
		punc='''.?!,'":;()-@{}[]-|/`_<>#$\\%^&*~'''
		for char in txt :
			if char not in punc :
				analy+=char
		txt=analy
	if upper=="on":
		analy=""
		analy=txt.upper()
		txt=analy
	if new=="on":
		analy=""
		for char in txt :
			if char != "\n" and char !="\r":
				analy+=char
		txt=analy
	if sp=="on":
		analy=""
		for index,char in enumerate(txt) :
			if not (txt[index]==" " and txt[index+1]==" "):
				analy+=char
		txt=analy
	cnt=0
	for char in txt :
		if char.isalnum():
			cnt+=1
	if removepunc !="on" and upper != "on" and new !="on" and sp !="on" or len(txt)==0 :
		return render(request,"eror.html")
	params={"purpose":txt,"analyzed":analy,"count":cnt}
	return render(request,"analyze.html",params)