
# import sys
# sys.path.insert(1, '/home/furqan/.pyenv/versions/3.8.5/lib/python3.8/site-packages')

from flask import Flask, render_template, url_for, request, jsonify, make_response, flash, redirect, send_file, Response
from flask_restful import Api, Resource
import time
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
import re
import os
import io
from multiprocessing import Process
from selenium import webdriver
from bs4 import BeautifulSoup
import khtube
import glob
import time
import yt_original as yt

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/vbest', methods=['GET', 'POST'])
def Vbest():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        khtube.single_video(link=video_link, quality_in_words="Vbest")

        # Edited here
        files = glob.glob("/home/furqan/Video/*")
        # time.sleep(1)
        print("Length: ", len(files))
        # for i in files:
        #     extension = i.split(".")[-1]
        #     if extension == "mp4":
        #         p = i
        #         return send_file(p, as_attachment=True)
        #     else:
        #         continue
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

@app.route('/best', methods=['GET', 'POST'])
def Best():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        khtube.single_video(link=video_link, quality_in_words="Best")

        files = glob.glob("/home/furqan/Video/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######


        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

@app.route('/low', methods=['GET', 'POST'])
def Low():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        khtube.single_video(link=video_link, quality_in_words="Low")

        files = glob.glob("/home/furqan/Video/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

###########
def background_remove(path):
    task = Process(target=rm(path))
    task.start()

def rm(path):
    os.remove(path)
###########

@app.route('/audio', methods=['GET', 'POST'])
def audio():
    if request.method == 'POST':

        audio_link = request.form["url"]
        
        khtube.only_music(link=audio_link)

        files = glob.glob("/home/furqan/Audio/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)


@app.route('/crop_vid', methods=['GET', 'POST'])
def crop_vid():
    if request.method == 'POST':
        
        video_link = request.form["url"]
        start_time = request.form["initial_time"]
        end_time = request.form["final_time"]

        khtube.crop_video(link=video_link, fromm=start_time, to=end_time)

        files = glob.glob("./*.mp4")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

@app.route('/scrape', methods=['GET', 'POST'])
def call_scrape():
    if request.method == 'POST':
        
        #######
        option = Options()
        option.headless = True
        driver = webdriver.Chrome("/home/furqan/Desktop/python_work/kodershub/Youtube_flask/chromedriver",options=option)
        ######
        
        user_kw = request.form["user_kw"]
        yt.scrape(user_kw, driver)
        files = glob.glob("/home/furqan/Desktop/python_work/kodershub/*.xlsx")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        # ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######
        driver.close()

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

# pip install openpyxl



# @app.route('/download')
# def download_file():
#     # sv_path = "$HOME/Video/%(title)s.%(ext)s"
#     # files = os.listdir()
#     files = glob.glob("/home/furqan/Video/*")

#     p = files[0]
#     return send_file(p, as_attachment=True)

# url = https://www.youtube.com/watch?v=3ps1YL_Bmeo 
# https://www.youtube.com/watch?v=BRAMZwdakTg
# how to get skinny at home by just drinking some herbs # 79
# How to get lean at home without going to gym  # 503 sth
# how to save electricity in multiple garages 50
 
if __name__ == "__main__":
    app.run(debug=True)


