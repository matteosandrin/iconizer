#!/usr/local/bin/python

import os
import click
import json

contentsTemplate = json.loads("""{
	"images":[
		{
			"idiom":"iphone",
			"size":"29x29",
			"scale":"1x",
			"filename":"Icon-App-29x29@1x.png"
		},
		{
			"idiom":"iphone",
			"size":"29x29",
			"scale":"2x",
			"filename":"Icon-App-29x29@2x.png"
		},
		{
			"idiom":"iphone",
			"size":"29x29",
			"scale":"3x",
			"filename":"Icon-App-29x29@3x.png"
		},
		{
			"idiom":"iphone",
			"size":"40x40",
			"scale":"1x",
			"filename":"Icon-App-40x40@1x.png"
		},
		{
			"idiom":"iphone",
			"size":"40x40",
			"scale":"2x",
			"filename":"Icon-App-40x40@2x.png"
		},
		{
			"idiom":"iphone",
			"size":"40x40",
			"scale":"3x",
			"filename":"Icon-App-40x40@3x.png"
		},
		{
			"idiom":"iphone",
			"size":"60x60",
			"scale":"1x",
			"filename":"Icon-App-60x60@1x.png"
		},
		{
			"idiom":"iphone",
			"size":"60x60",
			"scale":"2x",
			"filename":"Icon-App-60x60@2x.png"
		},
		{
			"idiom":"iphone",
			"size":"60x60",
			"scale":"3x",
			"filename":"Icon-App-60x60@3x.png"
		},
		{
			"idiom":"ipad",
			"size":"29x29",
			"scale":"1x",
			"filename":"Icon-App-29x29@1x.png"
		},
		{
			"idiom":"ipad",
			"size":"29x29",
			"scale":"2x",
			"filename":"Icon-App-29x29@2x.png"
		},
		{
			"idiom":"ipad",
			"size":"40x40",
			"scale":"1x",
			"filename":"Icon-App-40x40@1x.png"
		},
		{
			"idiom":"ipad",
			"size":"40x40",
			"scale":"2x",
			"filename":"Icon-App-40x40@2x.png"
		},
		{
			"idiom":"ipad",
			"size":"76x76",
			"scale":"1x",
			"filename":"Icon-App-76x76@1x.png"
		},
		{
			"idiom":"ipad",
			"size":"76x76",
			"scale":"2x",
			"filename":"Icon-App-76x76@2x.png"
		},
		{
			"idiom":"ipad",
			"size":"76x76",
			"scale":"3x",
			"filename":"Icon-App-76x76@3x.png"
		},
		{
			"idiom":"ipad",
			"size":"83.5x83.5",
			"scale":"2x",
			"filename":"Icon-App-83.5x83.5@2x.png"
		}
	],
	"info":{
		"version":1,
		"author":"matteo"
	}
}""")

@click.command()
@click.argument('path')

def make(path):
	"""Simple program that resizes an iOS icon to all the required sizes."""
	if os.path.isfile(path):
		os.mkdir('AppIcon.appiconset')
		content = open('./AppIcon.appiconset/Contents.json','w')
		content.write(json.dumps(contentsTemplate))
		content.close()

		temp = "convert {} -resize {size} ./AppIcon.appiconset/{filename}"
		for image in contentsTemplate["images"]:
			image["size"] = "x".join([str(i * int(image["scale"][:-1])) for i in [float(s) for s in image["size"].split("x")]])
			click.echo('Resizing for {idiom} to {size}...'.format(**image))
			os.system(temp.format(path,**image))
		click.echo('Done.')
	else:
		click.echo('Invalid path.')

if __name__ == '__main__':
	make()