#!/usr/bin/env python
#
# Splunk Diet Tracker
# Splunk Bioelectrical Tracking Experiment
# This application was made for use with a Makey Makey kit http://makeymakey.com
# https://github.com/splunkzilla/dietsplunk
#
# Released under the GNU General Public License

import sys
import pygame
from pygame.locals import *
import pygame.mixer

# CONSTANTS
VERSION = "0.1"
ENCODE = "utf-8"				# Splunk uses UTF-8 encoding. Setting log to only write in UTF-8
WRITE_TYPE = "a"				# Appends to file. Use w for Writing.
F_SPACE=sys.argv[1]			# Set mapping for Food Keys using makey makey defaults
F_UP=sys.argv[2]
F_DOWN=sys.argv[3]
F_LEFT=sys.argv[4]
F_RIGHT=sys.argv[5]

# GENERAL Variables
running = True
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
score = 0
white = (255,255,255)
black = (0,0,0)

# MODIFIABLE CONFIGS
logfile = "dietlog.log"

def writelog(type):
	data = 'food_type=' + type + '\n'
	file(logfile, WRITE_TYPE).write(data)


if __name__ == "__main__":

	# Initialize Window
	pygame.init()
	pygame.display.set_caption('Splunk BioElectrical Experiment - Diet Tracker')
	window.fill(white)

	pygame.display.update()

	try:
		foods = sys.argv[5]

		try:
			open(logfile, WRITE_TYPE)
			data = file(logfile).read()
			data = data.encode(ENCODE)
			
		except:
			pass

		# Loop through Keys
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						writelog(F_SPACE)
					elif event.key == pygame.K_UP:
						writelog(F_UP)
					elif event.key == pygame.K_DOWN:
						writelog(F_DOWN)
					elif event.key == pygame.K_LEFT:
						writelog(F_LEFT)
					elif event.key == pygame.K_RIGHT:
						writelog(F_RIGHT)

				# Increase score only if proper key is pressed
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_SPACE:
						score += 1
					elif event.key == pygame.K_UP:
						score += 1
					elif event.key == pygame.K_DOWN:
						score += 1
					elif event.key == pygame.K_LEFT:
						score += 1
					elif event.key == pygame.K_RIGHT:
						score += 1

				# Fill Background
				background = pygame.Surface(window.get_size())
				background = background.convert()
				background.fill(white)

				# Display score
				font = pygame.font.Font(None, 60)
				text = font.render("Total Servings {0}".format(score), 1, black)
				textpos = text.get_rect()
				textpos.centerx = background.get_rect().centerx
				textpos.centery = background.get_rect().centery
				background.blit(text, textpos)

				# Blit to screen
				window.blit(background, (0,0))
				pygame.display.flip()

		file.closed

	except IndexError:
		print 'Input not recognized!\n'
		print 'Usage: python diettracker.py <list_of_foods>'
		print 'Example: python diettracker.py banana apple grapefruit broccoli carrot'