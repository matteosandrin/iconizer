from setuptools import setup

setup(
	name='iconizer',
	version='0.1',
	py_modules=['iconizer'],
	install_requires=['click'],
	entry_points='''
		[console_scripts]
		iconizer=iconizer:cli
	'''
)