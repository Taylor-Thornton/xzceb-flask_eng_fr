'''Module used to translate text from English to French or French to English'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2023-05-24',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''Translate text from English to French'''
    response = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    french_text = response["translations"][0]
    frenchText = french_text["translation"]
    return frenchText

def frenchToEnglish(french_text):
    '''Translate text from French to English'''
    response = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    english_text = response["translations"][0]
    englishText = english_text["translation"]
    return englishText
