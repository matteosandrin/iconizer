#!/usr/local/bin/python

import os
import click
import json
import shutil

contentsTemplate = json.loads("""{"images":[{"idiom":"iphone","size":"29x29","scale":"1x","filename":"Icon-App-29x29@1x.png"},{"idiom":"iphone","size":"29x29","scale":"2x","filename":"Icon-App-29x29@2x.png"},{"idiom":"iphone","size":"29x29","scale":"3x","filename":"Icon-App-29x29@3x.png"},{"idiom":"iphone","size":"40x40","scale":"1x","filename":"Icon-App-40x40@1x.png"},{"idiom":"iphone","size":"40x40","scale":"2x","filename":"Icon-App-40x40@2x.png"},{"idiom":"iphone","size":"40x40","scale":"3x","filename":"Icon-App-40x40@3x.png"},{"idiom":"iphone","size":"60x60","scale":"1x","filename":"Icon-App-60x60@1x.png"},{"idiom":"iphone","size":"60x60","scale":"2x","filename":"Icon-App-60x60@2x.png"},{"idiom":"iphone","size":"60x60","scale":"3x","filename":"Icon-App-60x60@3x.png"},{"idiom":"ipad","size":"29x29","scale":"1x","filename":"Icon-App-29x29@1x.png"},{"idiom":"ipad","size":"29x29","scale":"2x","filename":"Icon-App-29x29@2x.png"},{"idiom":"ipad","size":"40x40","scale":"1x","filename":"Icon-App-40x40@1x.png"},{"idiom":"ipad","size":"40x40","scale":"2x","filename":"Icon-App-40x40@2x.png"},{"idiom":"ipad","size":"76x76","scale":"1x","filename":"Icon-App-76x76@1x.png"},{"idiom":"ipad","size":"76x76","scale":"2x","filename":"Icon-App-76x76@2x.png"},{"idiom":"ipad","size":"76x76","scale":"3x","filename":"Icon-App-76x76@3x.png"},{"idiom":"ipad","size":"83.5x83.5","scale":"2x","filename":"Icon-App-83.5x83.5@2x.png"}],"info":{"version":1,"author":"iconizer"}}""")
iconFolder = 'AppIcon.appiconset'

@click.command()
@click.argument('path')
@click.option('-o','--out',default='./',help='Path where to output icon files.')

def cli(path,out):

	"""Simple program that resizes an iOS icon to all the required sizes."""

	if out[-1] != '/': out += '/'

	if os.path.isfile(path):

		if os.path.isdir(out):

			if os.path.isdir(out+iconFolder):
				shutil.rmtree(out+iconFolder)
			os.mkdir(out+iconFolder)

			contentsFile = open(out+iconFolder+'/Contents.json','w')
			contentsFile.write(json.dumps(contentsTemplate,indent=4,sort_keys=True))
			contentsFile.close()

			temp = "convert {} -resize {size} {}/{}/{filename}"
			for image in contentsTemplate["images"]:
				image["size"] = "x".join([str(i * int(image["scale"][:-1])) for i in [float(s) for s in image["size"].split("x")]]) # multiplying the dimenions by the correct factor (1x, 2x, 3x)
				click.echo('Resizing for {idiom} to {size}...'.format(**image))
				os.system(temp.format(path,out,iconFolder,**image))
			click.echo('Done.')
		else:
			click.echo('Invalid output path.')
	else:
		click.echo('Invalid input path.')

if __name__ == '__main__':
	cli()