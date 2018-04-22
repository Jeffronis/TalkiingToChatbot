from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
import os
import speech_recognition as sr
r = sr.Recognizer()

bot = ChatBot(
    "Math & Time Bot",
    logic_adapters=[
        #allows the chat bot to do basic math and give the user the current time
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    # training data for converstations humor and greetings
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor"
)

while True:
    #user input
    choiceText = input("1 for type response|| 2 for microphone response")
    #text response section
    if(choiceText == '1'):
        inputText = input("Talk to the bot...")
        #Get response to the input text
        response = bot.get_response(inputText)
        gTTSresponse = response.text
        tts = gTTS(text=gTTSresponse, lang='en')
        tts.save("Botresponse.mp3")
        #Uses the defalt media player to play audio file
        os.startfile("Botresponse.mp3")
        print(response)
    #microphone respnes section
    if(choiceText == '2'):
        with sr.Microphone() as source:
            print("Say someting!")
            #save audio from microphone
            audio = r.listen(source)

        print("You said: " + r.recognize_google(audio))
        #give response to chatbot
        response = bot.get_response(r.recognize_google(audio))
        gTTSresponse = response.text
        tts = gTTS(text=gTTSresponse, lang='en')
        tts.save("Botresponse.mp3")
        # Uses the defalt media player to play audio file
        os.startfile("Botresponse.mp3")
        print(response)













