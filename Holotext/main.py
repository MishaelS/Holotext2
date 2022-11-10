from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from random import choice
from pygame import mixer
from gtts import gTTS

import speech_recognition
import desing_2
import sys, os

# ----------------------------------------------------------------------------------------

class Window(QMainWindow, desing_2.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.__pathFolderSave = ''
		self.__folder = 'voice_folder'
		self.__audio = 'vocalize.mp3'
		
		self.__sr = speech_recognition.Recognizer()
		self.__clipboard = QApplication.clipboard()
		
		self.plainTextEdit.setPlaceholderText('Введите текст для озвучивания: ')
		
		self.btnVoiceInput.clicked.connect(self.connect_voiceInput)
		self.btnVocalize.clicked.connect(self.connect_vocalize)
		self.btnClear.clicked.connect(self.connect_clear)
		self.btnCopy.clicked.connect(self.connect_copy)
		
		self.actionOpen.triggered.connect(self.connect_openFile)
		self.actionSave.triggered.connect(self.connect_saveAudio)
		self.actionSaveAs.triggered.connect(self.connect_saveAudioAs)
		self.actionExit.triggered.connect(self.closeEvent)
		
		self.actionVoiceInput.triggered.connect(self.connect_voiceInput)
		self.actionVocalize.triggered.connect(self.connect_vocalize)
		self.actionClear.triggered.connect(self.connect_clear)
		self.actionCopy.triggered.connect(self.connect_copy)
		
		
	def connect_voiceInput(self) -> None:
		''' Function - voice recording '''
	
		self.plainTextEdit.setPlainText(self.listen_command())
	
	
	def connect_vocalize(self) -> None:
		''' Text-to-speech function '''
	
		self.create_audio(self.__folder, self.__audio)
			
		mixer.music.load('{0}/{1}'.format(self.__folder, self.__audio))
		mixer.music.play()
	
	
	def connect_clear(self) -> None:
		''' Function - clearing the text field '''
	
		self.plainTextEdit.clear()
	
	
	def connect_copy(self) -> None:
		''' Function - copying a text field '''
	
		self.__clipboard.setText(self.plainTextEdit.toPlainText())


	def connect_openFile(self) -> None:
		''' Function - file opening '''
	
		filePath = QFileDialog.getOpenFileName(self, 'Open file')
		with open(filePath[0]) as file:
			text = file.read()
			self.plainTextEdit.setText(text)
		

	def connect_saveAudio(self) -> None:
		''' Function - file saving '''
	
		if self.__pathFolderSave == '':
			self.connect_saveAudioAs()
		else:
			audio = '{0}.mp3'.format(self.name_choice())
			self.create_audio(self.__pathFolderSave, audio)
	
	
	def connect_saveAudioAs(self) -> None:
		''' Function - save the file as '''
		
		audio = '{0}.mp3'.format(self.name_choice())
		filePath = QFileDialog.getSaveFileName(self, 'Save As', audio)
		if filePath == ('', ''):
			return 0
		
		self.__pathFolderSave = str(filePath[0][:len(filePath[0]) - (len(filePath[0].split('/')[-1]) + 1)])
		self.create_audio(self.__pathFolderSave, audio)

		
	def listen_command(self) -> str:
		''' Function - word return after wiretapping '''
		
		try:
			with speech_recognition.Microphone() as mic:
				self.__sr.adjust_for_ambient_noise(source=mic, duration=0.5)
				audio = self.__sr.listen(source=mic)
				query = self.__sr.recognize_google(audio_data=audio, language='ru-RU')
			return query
		except speech_recognition.UnknownValueError:
			return 'Мда... Я вас не понимаю! :|'


	def create_audio(self, folder: str, audio: str) -> None:
		''' Function - create audio file '''
		
		if folder != '':
			if not os.path.isdir(folder):
				 os.makedirs(folder)
			
		self.__output = gTTS(self.plainTextEdit.toPlainText(), lang='ru')
		self.__output.save('{0}/{1}'.format(folder, audio))
	
		
	def name_choice(self) -> str:
		''' Function - random name for the file '''
		
		symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
		name = ''
		for i in range(7):
			name += choice(symbols)
		return name
		
		
	def remove_folder(self, folder, audio) -> None:
		''' Function - File deletion '''
		
		os.remove('{0}/{1}'.format(folder, audio))
		
	def closeEvent(self, event) -> None:
		''' Function - closing the program '''
	
		if os.path.exists('{0}/{1}'.format(self.__folder, self.__audio)):
			self.remove_folder(self.__folder, self.__audio)
		sys.exit(0)
		
# ----------------------------------------------------------------------------------------

def main():
	mixer.init()
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())
	
# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()
