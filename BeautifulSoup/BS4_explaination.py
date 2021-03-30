from bs4 import BeautifulSoup

html = '<b id = "xyz" class="abc 123 "> Hello World </b><span></span><span></span>'

soup = BeautifulSoup(html , 'html.parser')

# tag = soup.b

# --------------------- Single Value attribute ---------------------------------

# print(tag['id']) ---------> we get id attribute
# print(tag['class']) ---- > we get class attribute

# print(tag.attrs) -----> here we get the attributes in dictionary format

# tag['id'] = 'hello'
# tag['class'] = 'World'
#
# print(tag)


#----------------------- Multi valued attributes ----------------------

# ----------> class is a multivalued attributes
# -----------> id is a single valued attributes

tag = soup.b

print(tag['class']) # -------- > abc 123 if multivalued attributes = None

print(tag['class']) # ----------> ['abc', '123']