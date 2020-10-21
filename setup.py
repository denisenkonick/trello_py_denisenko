trello_client-basics-api-denisenkonick

import setuptools  
  
with open("README.md", "r") as fh:  
	long_description = fh.read()  
	setuptools.setup(  
		name="trello_client-basics-api-denisenkonick",
		version="0.0.1", 
		author="Nick DENISENKO", 
		author_email="info.deniseno@gmail.com", 
		description="trello console client", 
		long_description=long_description, 
		long_description_content_type="text/markdown", 
		url="[https://github.com/denisenkonick/trello_py_denisenko](https://github.com/denisenkonick/trello_py_denisenko)",  
		# Адрес сайта вашего пакета, можно указать ссылку на репозиторий GitHub. 
		packages=setuptools.find_packages(), 
		classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], 
		python_requires='>=3.6',) 