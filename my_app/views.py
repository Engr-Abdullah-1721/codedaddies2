from django.shortcuts import render
from django.views import generic
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
# Create your views here.
#Base_craiglist_url='https://pakistan.craigslist.org/search/jjj?query={}'

Base_craiglist_url='https://losangeles.craigslist.org/search/bbb?query={}'
Base_image_url='https://images.craigslist.org/{}_300x300.jpg'
class SearchView(generic.TemplateView):
	template_name='my_app/search.html'
# def HomeView(request):
# 	return render(request,'my_app/home.html')

def SearchView1(request):
	search=request.POST.get('search')
	print(quote_plus(search))
	full_url=Base_craiglist_url.format(quote_plus(search))
	response=requests.get(full_url)
	data=response.text
	#print(data)
	soup=BeautifulSoup(data,features='html.parser')

	post_listings=soup.find_all('li',{'class':'result-row'})
	# post_title=post_listings[0].find(class_='result-title').text
	# post_url=post_listings[0].find('a').get('href')
	# print(post_title)
	# print(post_url)
	final_listings=[]
	for post in post_listings:
		post_title=post.find(class_='result-title').text
		post_url=post.find('a').get('href')
		if post.find(class_='result-price'):
			post_price=post.find(class_='result-price')
		else:
			post_price='N/A'

		if post.find(class_='result-image').get('data-ids'):
			post_image_id=post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
			#print(post_image_id)
			post_image_url=Base_image_url.format(post_image_id)
		else:
			post_image_url='https://images.craigslist.org/00e0e_fxBLmewJ5w1_300x300.jpg'
		final_listings.append((post_title,post_url,post_price,post_image_url))
	#response=requests.get()
	#print(response.text)
	show_content_to_front_end={'search':search,'final_listings':final_listings}
	return render(request,'my_app/search.html',show_content_to_front_end)

