#coding:utf-8

import uuid
from threading import Lock

from speech_synthesis.SpeechSynthsis import SpeechSynthsis


class __SpeechWorker(object):
    GoalFrequency = 16000

    @classmethod
    def __init__(self):
        self.__speech_synthsis = SpeechSynthsis(self.GoalFrequency)
        self.__speech_synthsis.setFile('wav', 'cache')

    @classmethod
    def speechSynthsis(self, content):
        file_name = uuid.uuid1()

        ok, file_name = self.__speech_synthsis.synthesis(content, file_name)

        return ok, file_name

    @classmethod
    def getCachePath(self):
        return self.__speech_synthsis.getCacheFile()


SpeechWorker = __SpeechWorker()