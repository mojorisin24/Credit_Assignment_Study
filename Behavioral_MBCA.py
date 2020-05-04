#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 03, 2020, at 20:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'Behavioral_MBCA'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Carlos\\Documents\\Credit_Assignment_Study\\Behavioral_MBCA.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Prac_Instructions"
Prac_InstructionsClock = core.Clock()
key_resp = keyboard.Keyboard()
Ins = visual.TextStim(win=win, name='Ins',
    text="Hello, in this task you will be presented with two separate images of a face and a house. You will see points overlayed on these images that you can gamble for. Each image will have an independent probability of leading to that amount of reward. Once you see the choose screen, you will indicate which image you'd like to gamble for with the left and right arrow key. Press left for the first image and right for the second. Based on the number of points you get in a given block, you will receive a cash payout! To start we will first be performing a few practice rounds. \nPlease note that loss does not mean that you will lose that amount of points for your gamble, it just means that you earned zero points. \nWhen you're ready press the spacebar to continue. ",
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "iti2"
iti2Clock = core.Clock()
fix4 = visual.ImageStim(
    win=win,
    name='fix4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim_presentation1"
stim_presentation1Clock = core.Clock()
stim1 = visual.ImageStim(
    win=win,
    name='stim1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fix = visual.ImageStim(
    win=win,
    name='fix', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prob1 = visual.TextStim(win=win, name='prob1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
jitter1 = visual.ImageStim(
    win=win,
    name='jitter1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim_presentation2"
stim_presentation2Clock = core.Clock()
stim2 = visual.ImageStim(
    win=win,
    name='stim2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fix2 = visual.ImageStim(
    win=win,
    name='fix2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prob2 = visual.TextStim(win=win, name='prob2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
jitter1 = visual.ImageStim(
    win=win,
    name='jitter1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
Choice = visual.TextStim(win=win, name='Choice',
    text='Choose',
    font='Arial',
    pos=(0, 0.01), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
choice_fix = visual.ImageStim(
    win=win,
    name='choice_fix', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "timeout_msg"
timeout_msgClock = core.Clock()
timeout_text = visual.TextStim(win=win, name='timeout_text',
    text='You did not respond in time! This trial will not count. Please make sure that you are paying attention. Press the spacebar when ready to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "long_delay"
long_delayClock = core.Clock()
fix3 = visual.ImageStim(
    win=win,
    name='fix3', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Outcome"
OutcomeClock = core.Clock()
reveal = visual.TextStim(win=win, name='reveal',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix5 = visual.ImageStim(
    win=win,
    name='fix5', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
outcome_circle = visual.ImageStim(
    win=win,
    name='outcome_circle', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
points_this_round = 0 
points_total = 0 
feedbacktext = visual.TextStim(win=win, name='feedbacktext',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "iti2"
iti2Clock = core.Clock()
fix4 = visual.ImageStim(
    win=win,
    name='fix4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "counterfactual"
counterfactualClock = core.Clock()
reveal2 = visual.TextStim(win=win, name='reveal2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix6 = visual.ImageStim(
    win=win,
    name='fix6', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
counter_square = visual.ImageStim(
    win=win,
    name='counter_square', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
feedbacktext_2 = visual.TextStim(win=win, name='feedbacktext_2',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "practice_end"
practice_endClock = core.Clock()
practice_finish = visual.TextStim(win=win, name='practice_finish',
    text='This concludes the practice. Press the spacebar when ready to continue to the actual trials. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
total_points_earned = visual.TextStim(win=win, name='total_points_earned',
    text='default text',
    font='Arial',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
points_earned = visual.TextStim(win=win, name='points_earned',
    text='Total Points Earned During Practice:  ',
    font='Arial',
    pos=(0, .35), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Exp_Instructions"
Exp_InstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='We will now start the actual experiment. You will no longer be seeing text with your result, just the colored shapes associated with each outcome. You will be performing N blocks of this task, at the end of the experiment we will select the points you earned on one block and that will be converted to a dollar amount which we will send to you via email. Press the spacebar when ready to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "iti2"
iti2Clock = core.Clock()
fix4 = visual.ImageStim(
    win=win,
    name='fix4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim_presentation1"
stim_presentation1Clock = core.Clock()
stim1 = visual.ImageStim(
    win=win,
    name='stim1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fix = visual.ImageStim(
    win=win,
    name='fix', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prob1 = visual.TextStim(win=win, name='prob1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
jitter1 = visual.ImageStim(
    win=win,
    name='jitter1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim_presentation2"
stim_presentation2Clock = core.Clock()
stim2 = visual.ImageStim(
    win=win,
    name='stim2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(400, 400),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fix2 = visual.ImageStim(
    win=win,
    name='fix2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prob2 = visual.TextStim(win=win, name='prob2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "iti"
itiClock = core.Clock()
jitter1 = visual.ImageStim(
    win=win,
    name='jitter1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
Choice = visual.TextStim(win=win, name='Choice',
    text='Choose',
    font='Arial',
    pos=(0, 0.01), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
choice_fix = visual.ImageStim(
    win=win,
    name='choice_fix', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "timeout_msg"
timeout_msgClock = core.Clock()
timeout_text = visual.TextStim(win=win, name='timeout_text',
    text='You did not respond in time! This trial will not count. Please make sure that you are paying attention. Press the spacebar when ready to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "long_delay"
long_delayClock = core.Clock()
fix3 = visual.ImageStim(
    win=win,
    name='fix3', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Outcome"
OutcomeClock = core.Clock()
reveal = visual.TextStim(win=win, name='reveal',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix5 = visual.ImageStim(
    win=win,
    name='fix5', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
outcome_circle = visual.ImageStim(
    win=win,
    name='outcome_circle', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
points_this_round = 0 
points_total = 0 
feedbacktext = visual.TextStim(win=win, name='feedbacktext',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "iti2"
iti2Clock = core.Clock()
fix4 = visual.ImageStim(
    win=win,
    name='fix4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "counterfactual"
counterfactualClock = core.Clock()
reveal2 = visual.TextStim(win=win, name='reveal2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix6 = visual.ImageStim(
    win=win,
    name='fix6', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(25, 25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
counter_square = visual.ImageStim(
    win=win,
    name='counter_square', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
feedbacktext_2 = visual.TextStim(win=win, name='feedbacktext_2',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Finish"
FinishClock = core.Clock()
Block_Finish = visual.TextStim(win=win, name='Block_Finish',
    text='This concludes the first block. Please feel free to take a break and press the spacebar whenever you are ready to continue. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
block1_wait = keyboard.Keyboard()
block1_points = visual.TextStim(win=win, name='block1_points',
    text=points_total
,
    font='Arial',
    pos=(0, .3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
block1_points_earned = visual.TextStim(win=win, name='block1_points_earned',
    text='Total Points Earned During Block 1:  ',
    font='Arial',
    pos=(0, .35), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Prac_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Prac_InstructionsComponents = [key_resp, Ins]
for thisComponent in Prac_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Prac_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Prac_Instructions"-------
while continueRoutine:
    # get current time
    t = Prac_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Prac_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Ins* updates
    if Ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ins.frameNStart = frameN  # exact frame index
        Ins.tStart = t  # local t and not account for scr refresh
        Ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ins, 'tStartRefresh')  # time at next scr refresh
        Ins.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prac_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Prac_Instructions"-------
for thisComponent in Prac_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Ins.started', Ins.tStartRefresh)
thisExp.addData('Ins.stopped', Ins.tStopRefresh)
# the Routine "Prac_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.csv'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "iti2"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    fix4.setImage(imageFix)
    # keep track of which components have finished
    iti2Components = [fix4]
    for thisComponent in iti2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    iti2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = iti2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=iti2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix4* updates
        if fix4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix4.frameNStart = frameN  # exact frame index
            fix4.tStart = t  # local t and not account for scr refresh
            fix4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix4, 'tStartRefresh')  # time at next scr refresh
            fix4.setAutoDraw(True)
        if fix4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix4.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix4.tStop = t  # not accounting for scr refresh
                fix4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix4, 'tStopRefresh')  # time at next scr refresh
                fix4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in iti2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti2"-------
    for thisComponent in iti2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('fix4.started', fix4.tStartRefresh)
    practice.addData('fix4.stopped', fix4.tStopRefresh)
    
    # ------Prepare to start Routine "stim_presentation1"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stim1.setImage(imageFile)
    fix.setImage(imageFix)
    prob1.setText(option1)
    # keep track of which components have finished
    stim_presentation1Components = [stim1, fix, prob1]
    for thisComponent in stim_presentation1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_presentation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_presentation1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_presentation1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_presentation1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim1* updates
        if stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim1.frameNStart = frameN  # exact frame index
            stim1.tStart = t  # local t and not account for scr refresh
            stim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
            stim1.setAutoDraw(True)
        if stim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim1.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                stim1.tStop = t  # not accounting for scr refresh
                stim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim1, 'tStopRefresh')  # time at next scr refresh
                stim1.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *prob1* updates
        if prob1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prob1.frameNStart = frameN  # exact frame index
            prob1.tStart = t  # local t and not account for scr refresh
            prob1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prob1, 'tStartRefresh')  # time at next scr refresh
            prob1.setAutoDraw(True)
        if prob1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prob1.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                prob1.tStop = t  # not accounting for scr refresh
                prob1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prob1, 'tStopRefresh')  # time at next scr refresh
                prob1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_presentation1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_presentation1"-------
    for thisComponent in stim_presentation1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('stim1.started', stim1.tStartRefresh)
    practice.addData('stim1.stopped', stim1.tStopRefresh)
    practice.addData('fix.started', fix.tStartRefresh)
    practice.addData('fix.stopped', fix.tStopRefresh)
    practice.addData('prob1.started', prob1.tStartRefresh)
    practice.addData('prob1.stopped', prob1.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    jitter1.setPos((0, 0))
    jitter1.setImage(imageFix)
    # keep track of which components have finished
    itiComponents = [jitter1]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter1* updates
        if jitter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jitter1.frameNStart = frameN  # exact frame index
            jitter1.tStart = t  # local t and not account for scr refresh
            jitter1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jitter1, 'tStartRefresh')  # time at next scr refresh
            jitter1.setAutoDraw(True)
        if jitter1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.-frameTolerance:
                # keep track of stop time/frame for later
                jitter1.tStop = t  # not accounting for scr refresh
                jitter1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jitter1, 'tStopRefresh')  # time at next scr refresh
                jitter1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('jitter1.started', jitter1.tStartRefresh)
    practice.addData('jitter1.stopped', jitter1.tStopRefresh)
    
    # ------Prepare to start Routine "stim_presentation2"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stim2.setImage(imageFile2)
    fix2.setImage(imageFix)
    prob2.setText(option2)
    # keep track of which components have finished
    stim_presentation2Components = [stim2, fix2, prob2]
    for thisComponent in stim_presentation2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_presentation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_presentation2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_presentation2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_presentation2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim2* updates
        if stim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim2.frameNStart = frameN  # exact frame index
            stim2.tStart = t  # local t and not account for scr refresh
            stim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
            stim2.setAutoDraw(True)
        if stim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                stim2.tStop = t  # not accounting for scr refresh
                stim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim2, 'tStopRefresh')  # time at next scr refresh
                stim2.setAutoDraw(False)
        
        # *fix2* updates
        if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            fix2.setAutoDraw(True)
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
                fix2.setAutoDraw(False)
        
        # *prob2* updates
        if prob2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prob2.frameNStart = frameN  # exact frame index
            prob2.tStart = t  # local t and not account for scr refresh
            prob2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prob2, 'tStartRefresh')  # time at next scr refresh
            prob2.setAutoDraw(True)
        if prob2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prob2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                prob2.tStop = t  # not accounting for scr refresh
                prob2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prob2, 'tStopRefresh')  # time at next scr refresh
                prob2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_presentation2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_presentation2"-------
    for thisComponent in stim_presentation2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('stim2.started', stim2.tStartRefresh)
    practice.addData('stim2.stopped', stim2.tStopRefresh)
    practice.addData('fix2.started', fix2.tStartRefresh)
    practice.addData('fix2.stopped', fix2.tStopRefresh)
    practice.addData('prob2.started', prob2.tStartRefresh)
    practice.addData('prob2.stopped', prob2.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    jitter1.setPos((0, 0))
    jitter1.setImage(imageFix)
    # keep track of which components have finished
    itiComponents = [jitter1]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter1* updates
        if jitter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jitter1.frameNStart = frameN  # exact frame index
            jitter1.tStart = t  # local t and not account for scr refresh
            jitter1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jitter1, 'tStartRefresh')  # time at next scr refresh
            jitter1.setAutoDraw(True)
        if jitter1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.-frameTolerance:
                # keep track of stop time/frame for later
                jitter1.tStop = t  # not accounting for scr refresh
                jitter1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jitter1, 'tStopRefresh')  # time at next scr refresh
                jitter1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('jitter1.started', jitter1.tStartRefresh)
    practice.addData('jitter1.stopped', jitter1.tStopRefresh)
    
    # ------Prepare to start Routine "choice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    choice_fix.setImage(imageFix)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    nReps = 0 
    nReps2 = 1
    # keep track of which components have finished
    choiceComponents = [Choice, choice_fix, key_resp_2]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice* updates
        if Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice.frameNStart = frameN  # exact frame index
            Choice.tStart = t  # local t and not account for scr refresh
            Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice, 'tStartRefresh')  # time at next scr refresh
            Choice.setAutoDraw(True)
        if Choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Choice.tStop = t  # not accounting for scr refresh
                Choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice, 'tStopRefresh')  # time at next scr refresh
                Choice.setAutoDraw(False)
        
        # *choice_fix* updates
        if choice_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_fix.frameNStart = frameN  # exact frame index
            choice_fix.tStart = t  # local t and not account for scr refresh
            choice_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_fix, 'tStartRefresh')  # time at next scr refresh
            choice_fix.setAutoDraw(True)
        if choice_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice_fix.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                choice_fix.tStop = t  # not accounting for scr refresh
                choice_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice_fix, 'tStopRefresh')  # time at next scr refresh
                choice_fix.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(corr)) or (key_resp_2.keys == corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('Choice.started', Choice.tStartRefresh)
    practice.addData('Choice.stopped', Choice.tStopRefresh)
    practice.addData('choice_fix.started', choice_fix.tStartRefresh)
    practice.addData('choice_fix.stopped', choice_fix.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('key_resp_2.keys',key_resp_2.keys)
    practice.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        practice.addData('key_resp_2.rt', key_resp_2.rt)
    practice.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    practice.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    if not key_resp_2.keys:
        nReps = 1 
        nReps2 = 0
    
    # set up handler to look after randomisation of conditions etc
    message_loop = data.TrialHandler(nReps=nReps, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='message_loop')
    thisExp.addLoop(message_loop)  # add the loop to the experiment
    thisMessage_loop = message_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMessage_loop.rgb)
    if thisMessage_loop != None:
        for paramName in thisMessage_loop:
            exec('{} = thisMessage_loop[paramName]'.format(paramName))
    
    for thisMessage_loop in message_loop:
        currentLoop = message_loop
        # abbreviate parameter names if possible (e.g. rgb = thisMessage_loop.rgb)
        if thisMessage_loop != None:
            for paramName in thisMessage_loop:
                exec('{} = thisMessage_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "timeout_msg"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        timeout_msgComponents = [timeout_text, key_resp_4]
        for thisComponent in timeout_msgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        timeout_msgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "timeout_msg"-------
        while continueRoutine:
            # get current time
            t = timeout_msgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=timeout_msgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *timeout_text* updates
            if timeout_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timeout_text.frameNStart = frameN  # exact frame index
                timeout_text.tStart = t  # local t and not account for scr refresh
                timeout_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timeout_text, 'tStartRefresh')  # time at next scr refresh
                timeout_text.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in timeout_msgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "timeout_msg"-------
        for thisComponent in timeout_msgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        message_loop.addData('timeout_text.started', timeout_text.tStartRefresh)
        message_loop.addData('timeout_text.stopped', timeout_text.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        message_loop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            message_loop.addData('key_resp_4.rt', key_resp_4.rt)
        message_loop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        message_loop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "timeout_msg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nReps repeats of 'message_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    practice_timeout = data.TrialHandler(nReps=nReps2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_timeout')
    thisExp.addLoop(practice_timeout)  # add the loop to the experiment
    thisPractice_timeout = practice_timeout.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_timeout.rgb)
    if thisPractice_timeout != None:
        for paramName in thisPractice_timeout:
            exec('{} = thisPractice_timeout[paramName]'.format(paramName))
    
    for thisPractice_timeout in practice_timeout:
        currentLoop = practice_timeout
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_timeout.rgb)
        if thisPractice_timeout != None:
            for paramName in thisPractice_timeout:
                exec('{} = thisPractice_timeout[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "long_delay"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        fix3.setImage(imageFix)
        # keep track of which components have finished
        long_delayComponents = [fix3]
        for thisComponent in long_delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        long_delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "long_delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = long_delayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=long_delayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix3* updates
            if fix3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix3.frameNStart = frameN  # exact frame index
                fix3.tStart = t  # local t and not account for scr refresh
                fix3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix3, 'tStartRefresh')  # time at next scr refresh
                fix3.setAutoDraw(True)
            if fix3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix3.tStop = t  # not accounting for scr refresh
                    fix3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix3, 'tStopRefresh')  # time at next scr refresh
                    fix3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in long_delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "long_delay"-------
        for thisComponent in long_delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_timeout.addData('fix3.started', fix3.tStartRefresh)
        practice_timeout.addData('fix3.stopped', fix3.tStopRefresh)
        
        # ------Prepare to start Routine "Outcome"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        reveal.setText(option1)
        fix5.setImage(imageFix)
        outcome_circle.setImage(outcome)
        if key_resp_2.corr:
            msg= outcome_msg_optimal
            msgColor='black'
            points_this_round=points_this_round + point_earned_optimal
        else:
            msg= outcome_msg_alt
            msgColor='black'
            points_this_round=points_this_round + point_earned_alt
        feedbacktext.setColor(msgColor, colorSpace='rgb')
        feedbacktext.setText(msg)
        # keep track of which components have finished
        OutcomeComponents = [reveal, fix5, outcome_circle, feedbacktext]
        for thisComponent in OutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        OutcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Outcome"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = OutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=OutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *reveal* updates
            if reveal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reveal.frameNStart = frameN  # exact frame index
                reveal.tStart = t  # local t and not account for scr refresh
                reveal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reveal, 'tStartRefresh')  # time at next scr refresh
                reveal.setAutoDraw(True)
            if reveal.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reveal.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    reveal.tStop = t  # not accounting for scr refresh
                    reveal.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reveal, 'tStopRefresh')  # time at next scr refresh
                    reveal.setAutoDraw(False)
            
            # *fix5* updates
            if fix5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix5.frameNStart = frameN  # exact frame index
                fix5.tStart = t  # local t and not account for scr refresh
                fix5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix5, 'tStartRefresh')  # time at next scr refresh
                fix5.setAutoDraw(True)
            if fix5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix5.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix5.tStop = t  # not accounting for scr refresh
                    fix5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix5, 'tStopRefresh')  # time at next scr refresh
                    fix5.setAutoDraw(False)
            
            # *outcome_circle* updates
            if outcome_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                outcome_circle.frameNStart = frameN  # exact frame index
                outcome_circle.tStart = t  # local t and not account for scr refresh
                outcome_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(outcome_circle, 'tStartRefresh')  # time at next scr refresh
                outcome_circle.setAutoDraw(True)
            if outcome_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > outcome_circle.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    outcome_circle.tStop = t  # not accounting for scr refresh
                    outcome_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(outcome_circle, 'tStopRefresh')  # time at next scr refresh
                    outcome_circle.setAutoDraw(False)
            
            # *feedbacktext* updates
            if feedbacktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbacktext.frameNStart = frameN  # exact frame index
                feedbacktext.tStart = t  # local t and not account for scr refresh
                feedbacktext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbacktext, 'tStartRefresh')  # time at next scr refresh
                feedbacktext.setAutoDraw(True)
            if feedbacktext.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbacktext.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbacktext.tStop = t  # not accounting for scr refresh
                    feedbacktext.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbacktext, 'tStopRefresh')  # time at next scr refresh
                    feedbacktext.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Outcome"-------
        for thisComponent in OutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_timeout.addData('reveal.started', reveal.tStartRefresh)
        practice_timeout.addData('reveal.stopped', reveal.tStopRefresh)
        practice_timeout.addData('fix5.started', fix5.tStartRefresh)
        practice_timeout.addData('fix5.stopped', fix5.tStopRefresh)
        practice_timeout.addData('outcome_circle.started', outcome_circle.tStartRefresh)
        practice_timeout.addData('outcome_circle.stopped', outcome_circle.tStopRefresh)
        if not key_resp_2.keys:
            points_total=0 + points_total
            thisExp.addData('points_total',points_total)
        else:
            points_total=points_this_round + points_total
            thisExp.addData('points_total',points_total)
        
        practice_timeout.addData('feedbacktext.started', feedbacktext.tStartRefresh)
        practice_timeout.addData('feedbacktext.stopped', feedbacktext.tStopRefresh)
        
        # ------Prepare to start Routine "iti2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        fix4.setImage(imageFix)
        # keep track of which components have finished
        iti2Components = [fix4]
        for thisComponent in iti2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        iti2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "iti2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = iti2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=iti2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix4* updates
            if fix4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix4.frameNStart = frameN  # exact frame index
                fix4.tStart = t  # local t and not account for scr refresh
                fix4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix4, 'tStartRefresh')  # time at next scr refresh
                fix4.setAutoDraw(True)
            if fix4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix4.tStop = t  # not accounting for scr refresh
                    fix4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix4, 'tStopRefresh')  # time at next scr refresh
                    fix4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iti2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti2"-------
        for thisComponent in iti2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_timeout.addData('fix4.started', fix4.tStartRefresh)
        practice_timeout.addData('fix4.stopped', fix4.tStopRefresh)
        
        # ------Prepare to start Routine "counterfactual"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        reveal2.setText(option2)
        fix6.setImage(imageFix)
        counter_square.setImage(counterfactual)
        if key_resp_2.corr:
            msg= counterfactual_msg_optimal
            msgColor='black'
        else:
            msg= counterfactual_msg_alt
            msgColor='black'
        
        feedbacktext_2.setColor(msgColor, colorSpace='rgb')
        feedbacktext_2.setText(msg)
        # keep track of which components have finished
        counterfactualComponents = [reveal2, fix6, counter_square, feedbacktext_2]
        for thisComponent in counterfactualComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        counterfactualClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "counterfactual"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = counterfactualClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=counterfactualClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *reveal2* updates
            if reveal2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reveal2.frameNStart = frameN  # exact frame index
                reveal2.tStart = t  # local t and not account for scr refresh
                reveal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reveal2, 'tStartRefresh')  # time at next scr refresh
                reveal2.setAutoDraw(True)
            if reveal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reveal2.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    reveal2.tStop = t  # not accounting for scr refresh
                    reveal2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reveal2, 'tStopRefresh')  # time at next scr refresh
                    reveal2.setAutoDraw(False)
            
            # *fix6* updates
            if fix6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix6.frameNStart = frameN  # exact frame index
                fix6.tStart = t  # local t and not account for scr refresh
                fix6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix6, 'tStartRefresh')  # time at next scr refresh
                fix6.setAutoDraw(True)
            if fix6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix6.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix6.tStop = t  # not accounting for scr refresh
                    fix6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix6, 'tStopRefresh')  # time at next scr refresh
                    fix6.setAutoDraw(False)
            
            # *counter_square* updates
            if counter_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                counter_square.frameNStart = frameN  # exact frame index
                counter_square.tStart = t  # local t and not account for scr refresh
                counter_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(counter_square, 'tStartRefresh')  # time at next scr refresh
                counter_square.setAutoDraw(True)
            if counter_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > counter_square.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    counter_square.tStop = t  # not accounting for scr refresh
                    counter_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(counter_square, 'tStopRefresh')  # time at next scr refresh
                    counter_square.setAutoDraw(False)
            
            # *feedbacktext_2* updates
            if feedbacktext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbacktext_2.frameNStart = frameN  # exact frame index
                feedbacktext_2.tStart = t  # local t and not account for scr refresh
                feedbacktext_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbacktext_2, 'tStartRefresh')  # time at next scr refresh
                feedbacktext_2.setAutoDraw(True)
            if feedbacktext_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbacktext_2.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbacktext_2.tStop = t  # not accounting for scr refresh
                    feedbacktext_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbacktext_2, 'tStopRefresh')  # time at next scr refresh
                    feedbacktext_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in counterfactualComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "counterfactual"-------
        for thisComponent in counterfactualComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_timeout.addData('reveal2.started', reveal2.tStartRefresh)
        practice_timeout.addData('reveal2.stopped', reveal2.tStopRefresh)
        practice_timeout.addData('fix6.started', fix6.tStartRefresh)
        practice_timeout.addData('fix6.stopped', fix6.tStopRefresh)
        practice_timeout.addData('counter_square.started', counter_square.tStartRefresh)
        practice_timeout.addData('counter_square.stopped', counter_square.tStopRefresh)
        practice_timeout.addData('feedbacktext_2.started', feedbacktext_2.tStartRefresh)
        practice_timeout.addData('feedbacktext_2.stopped', feedbacktext_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps2 repeats of 'practice_timeout'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice'


# ------Prepare to start Routine "practice_end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
total_points_earned.setText(points_total)
# keep track of which components have finished
practice_endComponents = [practice_finish, key_resp_3, total_points_earned, points_earned]
for thisComponent in practice_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_end"-------
while continueRoutine:
    # get current time
    t = practice_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_finish* updates
    if practice_finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_finish.frameNStart = frameN  # exact frame index
        practice_finish.tStart = t  # local t and not account for scr refresh
        practice_finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_finish, 'tStartRefresh')  # time at next scr refresh
        practice_finish.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *total_points_earned* updates
    if total_points_earned.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        total_points_earned.frameNStart = frameN  # exact frame index
        total_points_earned.tStart = t  # local t and not account for scr refresh
        total_points_earned.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(total_points_earned, 'tStartRefresh')  # time at next scr refresh
        total_points_earned.setAutoDraw(True)
    
    # *points_earned* updates
    if points_earned.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        points_earned.frameNStart = frameN  # exact frame index
        points_earned.tStart = t  # local t and not account for scr refresh
        points_earned.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(points_earned, 'tStartRefresh')  # time at next scr refresh
        points_earned.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_end"-------
for thisComponent in practice_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_finish.started', practice_finish.tStartRefresh)
thisExp.addData('practice_finish.stopped', practice_finish.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('total_points_earned.started', total_points_earned.tStartRefresh)
thisExp.addData('total_points_earned.stopped', total_points_earned.tStopRefresh)
thisExp.addData('points_earned.started', points_earned.tStartRefresh)
thisExp.addData('points_earned.stopped', points_earned.tStopRefresh)
# the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Exp_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Exp_InstructionsComponents = [text_2, key_resp_5]
for thisComponent in Exp_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Exp_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Exp_Instructions"-------
while continueRoutine:
    # get current time
    t = Exp_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Exp_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Exp_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Exp_Instructions"-------
for thisComponent in Exp_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "Exp_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block1.csv'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

for thisBlock1 in block1:
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "iti2"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    fix4.setImage(imageFix)
    # keep track of which components have finished
    iti2Components = [fix4]
    for thisComponent in iti2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    iti2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = iti2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=iti2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix4* updates
        if fix4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix4.frameNStart = frameN  # exact frame index
            fix4.tStart = t  # local t and not account for scr refresh
            fix4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix4, 'tStartRefresh')  # time at next scr refresh
            fix4.setAutoDraw(True)
        if fix4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix4.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                fix4.tStop = t  # not accounting for scr refresh
                fix4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix4, 'tStopRefresh')  # time at next scr refresh
                fix4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in iti2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti2"-------
    for thisComponent in iti2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('fix4.started', fix4.tStartRefresh)
    block1.addData('fix4.stopped', fix4.tStopRefresh)
    
    # ------Prepare to start Routine "stim_presentation1"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stim1.setImage(imageFile)
    fix.setImage(imageFix)
    prob1.setText(option1)
    # keep track of which components have finished
    stim_presentation1Components = [stim1, fix, prob1]
    for thisComponent in stim_presentation1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_presentation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_presentation1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_presentation1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_presentation1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim1* updates
        if stim1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim1.frameNStart = frameN  # exact frame index
            stim1.tStart = t  # local t and not account for scr refresh
            stim1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
            stim1.setAutoDraw(True)
        if stim1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim1.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                stim1.tStop = t  # not accounting for scr refresh
                stim1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim1, 'tStopRefresh')  # time at next scr refresh
                stim1.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *prob1* updates
        if prob1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prob1.frameNStart = frameN  # exact frame index
            prob1.tStart = t  # local t and not account for scr refresh
            prob1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prob1, 'tStartRefresh')  # time at next scr refresh
            prob1.setAutoDraw(True)
        if prob1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prob1.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                prob1.tStop = t  # not accounting for scr refresh
                prob1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prob1, 'tStopRefresh')  # time at next scr refresh
                prob1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_presentation1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_presentation1"-------
    for thisComponent in stim_presentation1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('stim1.started', stim1.tStartRefresh)
    block1.addData('stim1.stopped', stim1.tStopRefresh)
    block1.addData('fix.started', fix.tStartRefresh)
    block1.addData('fix.stopped', fix.tStopRefresh)
    block1.addData('prob1.started', prob1.tStartRefresh)
    block1.addData('prob1.stopped', prob1.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    jitter1.setPos((0, 0))
    jitter1.setImage(imageFix)
    # keep track of which components have finished
    itiComponents = [jitter1]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter1* updates
        if jitter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jitter1.frameNStart = frameN  # exact frame index
            jitter1.tStart = t  # local t and not account for scr refresh
            jitter1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jitter1, 'tStartRefresh')  # time at next scr refresh
            jitter1.setAutoDraw(True)
        if jitter1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.-frameTolerance:
                # keep track of stop time/frame for later
                jitter1.tStop = t  # not accounting for scr refresh
                jitter1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jitter1, 'tStopRefresh')  # time at next scr refresh
                jitter1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('jitter1.started', jitter1.tStartRefresh)
    block1.addData('jitter1.stopped', jitter1.tStopRefresh)
    
    # ------Prepare to start Routine "stim_presentation2"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    stim2.setImage(imageFile2)
    fix2.setImage(imageFix)
    prob2.setText(option2)
    # keep track of which components have finished
    stim_presentation2Components = [stim2, fix2, prob2]
    for thisComponent in stim_presentation2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stim_presentation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stim_presentation2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stim_presentation2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stim_presentation2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim2* updates
        if stim2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim2.frameNStart = frameN  # exact frame index
            stim2.tStart = t  # local t and not account for scr refresh
            stim2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
            stim2.setAutoDraw(True)
        if stim2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                stim2.tStop = t  # not accounting for scr refresh
                stim2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim2, 'tStopRefresh')  # time at next scr refresh
                stim2.setAutoDraw(False)
        
        # *fix2* updates
        if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            fix2.setAutoDraw(True)
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
                fix2.setAutoDraw(False)
        
        # *prob2* updates
        if prob2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prob2.frameNStart = frameN  # exact frame index
            prob2.tStart = t  # local t and not account for scr refresh
            prob2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prob2, 'tStartRefresh')  # time at next scr refresh
            prob2.setAutoDraw(True)
        if prob2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prob2.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                prob2.tStop = t  # not accounting for scr refresh
                prob2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prob2, 'tStopRefresh')  # time at next scr refresh
                prob2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_presentation2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim_presentation2"-------
    for thisComponent in stim_presentation2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('stim2.started', stim2.tStartRefresh)
    block1.addData('stim2.stopped', stim2.tStopRefresh)
    block1.addData('fix2.started', fix2.tStartRefresh)
    block1.addData('fix2.stopped', fix2.tStopRefresh)
    block1.addData('prob2.started', prob2.tStartRefresh)
    block1.addData('prob2.stopped', prob2.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    jitter1.setPos((0, 0))
    jitter1.setImage(imageFix)
    # keep track of which components have finished
    itiComponents = [jitter1]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter1* updates
        if jitter1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            jitter1.frameNStart = frameN  # exact frame index
            jitter1.tStart = t  # local t and not account for scr refresh
            jitter1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(jitter1, 'tStartRefresh')  # time at next scr refresh
            jitter1.setAutoDraw(True)
        if jitter1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.-frameTolerance:
                # keep track of stop time/frame for later
                jitter1.tStop = t  # not accounting for scr refresh
                jitter1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(jitter1, 'tStopRefresh')  # time at next scr refresh
                jitter1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('jitter1.started', jitter1.tStartRefresh)
    block1.addData('jitter1.stopped', jitter1.tStopRefresh)
    
    # ------Prepare to start Routine "choice"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    choice_fix.setImage(imageFix)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    nReps = 0 
    nReps2 = 1
    # keep track of which components have finished
    choiceComponents = [Choice, choice_fix, key_resp_2]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Choice* updates
        if Choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Choice.frameNStart = frameN  # exact frame index
            Choice.tStart = t  # local t and not account for scr refresh
            Choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Choice, 'tStartRefresh')  # time at next scr refresh
            Choice.setAutoDraw(True)
        if Choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Choice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Choice.tStop = t  # not accounting for scr refresh
                Choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Choice, 'tStopRefresh')  # time at next scr refresh
                Choice.setAutoDraw(False)
        
        # *choice_fix* updates
        if choice_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_fix.frameNStart = frameN  # exact frame index
            choice_fix.tStart = t  # local t and not account for scr refresh
            choice_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_fix, 'tStartRefresh')  # time at next scr refresh
            choice_fix.setAutoDraw(True)
        if choice_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice_fix.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                choice_fix.tStop = t  # not accounting for scr refresh
                choice_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice_fix, 'tStopRefresh')  # time at next scr refresh
                choice_fix.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(corr)) or (key_resp_2.keys == corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1.addData('Choice.started', Choice.tStartRefresh)
    block1.addData('Choice.stopped', Choice.tStopRefresh)
    block1.addData('choice_fix.started', choice_fix.tStartRefresh)
    block1.addData('choice_fix.stopped', choice_fix.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for block1 (TrialHandler)
    block1.addData('key_resp_2.keys',key_resp_2.keys)
    block1.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        block1.addData('key_resp_2.rt', key_resp_2.rt)
    block1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    block1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    if not key_resp_2.keys:
        nReps = 1 
        nReps2 = 0
    
    # set up handler to look after randomisation of conditions etc
    timeout_msg_loop = data.TrialHandler(nReps=nReps, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='timeout_msg_loop')
    thisExp.addLoop(timeout_msg_loop)  # add the loop to the experiment
    thisTimeout_msg_loop = timeout_msg_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTimeout_msg_loop.rgb)
    if thisTimeout_msg_loop != None:
        for paramName in thisTimeout_msg_loop:
            exec('{} = thisTimeout_msg_loop[paramName]'.format(paramName))
    
    for thisTimeout_msg_loop in timeout_msg_loop:
        currentLoop = timeout_msg_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTimeout_msg_loop.rgb)
        if thisTimeout_msg_loop != None:
            for paramName in thisTimeout_msg_loop:
                exec('{} = thisTimeout_msg_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "timeout_msg"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        timeout_msgComponents = [timeout_text, key_resp_4]
        for thisComponent in timeout_msgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        timeout_msgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "timeout_msg"-------
        while continueRoutine:
            # get current time
            t = timeout_msgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=timeout_msgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *timeout_text* updates
            if timeout_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timeout_text.frameNStart = frameN  # exact frame index
                timeout_text.tStart = t  # local t and not account for scr refresh
                timeout_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timeout_text, 'tStartRefresh')  # time at next scr refresh
                timeout_text.setAutoDraw(True)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in timeout_msgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "timeout_msg"-------
        for thisComponent in timeout_msgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timeout_msg_loop.addData('timeout_text.started', timeout_text.tStartRefresh)
        timeout_msg_loop.addData('timeout_text.stopped', timeout_text.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        timeout_msg_loop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            timeout_msg_loop.addData('key_resp_4.rt', key_resp_4.rt)
        timeout_msg_loop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        timeout_msg_loop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "timeout_msg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nReps repeats of 'timeout_msg_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    timeout = data.TrialHandler(nReps=nReps2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='timeout')
    thisExp.addLoop(timeout)  # add the loop to the experiment
    thisTimeout = timeout.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTimeout.rgb)
    if thisTimeout != None:
        for paramName in thisTimeout:
            exec('{} = thisTimeout[paramName]'.format(paramName))
    
    for thisTimeout in timeout:
        currentLoop = timeout
        # abbreviate parameter names if possible (e.g. rgb = thisTimeout.rgb)
        if thisTimeout != None:
            for paramName in thisTimeout:
                exec('{} = thisTimeout[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "long_delay"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        fix3.setImage(imageFix)
        # keep track of which components have finished
        long_delayComponents = [fix3]
        for thisComponent in long_delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        long_delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "long_delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = long_delayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=long_delayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix3* updates
            if fix3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix3.frameNStart = frameN  # exact frame index
                fix3.tStart = t  # local t and not account for scr refresh
                fix3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix3, 'tStartRefresh')  # time at next scr refresh
                fix3.setAutoDraw(True)
            if fix3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix3.tStop = t  # not accounting for scr refresh
                    fix3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix3, 'tStopRefresh')  # time at next scr refresh
                    fix3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in long_delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "long_delay"-------
        for thisComponent in long_delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timeout.addData('fix3.started', fix3.tStartRefresh)
        timeout.addData('fix3.stopped', fix3.tStopRefresh)
        
        # ------Prepare to start Routine "Outcome"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        reveal.setText(option1)
        fix5.setImage(imageFix)
        outcome_circle.setImage(outcome)
        if key_resp_2.corr:
            msg= outcome_msg_optimal
            msgColor='black'
            points_this_round=points_this_round + point_earned_optimal
        else:
            msg= outcome_msg_alt
            msgColor='black'
            points_this_round=points_this_round + point_earned_alt
        feedbacktext.setColor(msgColor, colorSpace='rgb')
        feedbacktext.setText(msg)
        # keep track of which components have finished
        OutcomeComponents = [reveal, fix5, outcome_circle, feedbacktext]
        for thisComponent in OutcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        OutcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Outcome"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = OutcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=OutcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *reveal* updates
            if reveal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reveal.frameNStart = frameN  # exact frame index
                reveal.tStart = t  # local t and not account for scr refresh
                reveal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reveal, 'tStartRefresh')  # time at next scr refresh
                reveal.setAutoDraw(True)
            if reveal.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reveal.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    reveal.tStop = t  # not accounting for scr refresh
                    reveal.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reveal, 'tStopRefresh')  # time at next scr refresh
                    reveal.setAutoDraw(False)
            
            # *fix5* updates
            if fix5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix5.frameNStart = frameN  # exact frame index
                fix5.tStart = t  # local t and not account for scr refresh
                fix5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix5, 'tStartRefresh')  # time at next scr refresh
                fix5.setAutoDraw(True)
            if fix5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix5.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix5.tStop = t  # not accounting for scr refresh
                    fix5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix5, 'tStopRefresh')  # time at next scr refresh
                    fix5.setAutoDraw(False)
            
            # *outcome_circle* updates
            if outcome_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                outcome_circle.frameNStart = frameN  # exact frame index
                outcome_circle.tStart = t  # local t and not account for scr refresh
                outcome_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(outcome_circle, 'tStartRefresh')  # time at next scr refresh
                outcome_circle.setAutoDraw(True)
            if outcome_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > outcome_circle.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    outcome_circle.tStop = t  # not accounting for scr refresh
                    outcome_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(outcome_circle, 'tStopRefresh')  # time at next scr refresh
                    outcome_circle.setAutoDraw(False)
            
            # *feedbacktext* updates
            if feedbacktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbacktext.frameNStart = frameN  # exact frame index
                feedbacktext.tStart = t  # local t and not account for scr refresh
                feedbacktext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbacktext, 'tStartRefresh')  # time at next scr refresh
                feedbacktext.setAutoDraw(True)
            if feedbacktext.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbacktext.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbacktext.tStop = t  # not accounting for scr refresh
                    feedbacktext.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbacktext, 'tStopRefresh')  # time at next scr refresh
                    feedbacktext.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Outcome"-------
        for thisComponent in OutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timeout.addData('reveal.started', reveal.tStartRefresh)
        timeout.addData('reveal.stopped', reveal.tStopRefresh)
        timeout.addData('fix5.started', fix5.tStartRefresh)
        timeout.addData('fix5.stopped', fix5.tStopRefresh)
        timeout.addData('outcome_circle.started', outcome_circle.tStartRefresh)
        timeout.addData('outcome_circle.stopped', outcome_circle.tStopRefresh)
        if not key_resp_2.keys:
            points_total=0 + points_total
            thisExp.addData('points_total',points_total)
        else:
            points_total=points_this_round + points_total
            thisExp.addData('points_total',points_total)
        
        timeout.addData('feedbacktext.started', feedbacktext.tStartRefresh)
        timeout.addData('feedbacktext.stopped', feedbacktext.tStopRefresh)
        
        # ------Prepare to start Routine "iti2"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        fix4.setImage(imageFix)
        # keep track of which components have finished
        iti2Components = [fix4]
        for thisComponent in iti2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        iti2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "iti2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = iti2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=iti2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix4* updates
            if fix4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix4.frameNStart = frameN  # exact frame index
                fix4.tStart = t  # local t and not account for scr refresh
                fix4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix4, 'tStartRefresh')  # time at next scr refresh
                fix4.setAutoDraw(True)
            if fix4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix4.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix4.tStop = t  # not accounting for scr refresh
                    fix4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix4, 'tStopRefresh')  # time at next scr refresh
                    fix4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iti2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti2"-------
        for thisComponent in iti2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timeout.addData('fix4.started', fix4.tStartRefresh)
        timeout.addData('fix4.stopped', fix4.tStopRefresh)
        
        # ------Prepare to start Routine "counterfactual"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        reveal2.setText(option2)
        fix6.setImage(imageFix)
        counter_square.setImage(counterfactual)
        if key_resp_2.corr:
            msg= counterfactual_msg_optimal
            msgColor='black'
        else:
            msg= counterfactual_msg_alt
            msgColor='black'
        
        feedbacktext_2.setColor(msgColor, colorSpace='rgb')
        feedbacktext_2.setText(msg)
        # keep track of which components have finished
        counterfactualComponents = [reveal2, fix6, counter_square, feedbacktext_2]
        for thisComponent in counterfactualComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        counterfactualClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "counterfactual"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = counterfactualClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=counterfactualClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *reveal2* updates
            if reveal2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                reveal2.frameNStart = frameN  # exact frame index
                reveal2.tStart = t  # local t and not account for scr refresh
                reveal2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reveal2, 'tStartRefresh')  # time at next scr refresh
                reveal2.setAutoDraw(True)
            if reveal2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reveal2.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    reveal2.tStop = t  # not accounting for scr refresh
                    reveal2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reveal2, 'tStopRefresh')  # time at next scr refresh
                    reveal2.setAutoDraw(False)
            
            # *fix6* updates
            if fix6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix6.frameNStart = frameN  # exact frame index
                fix6.tStart = t  # local t and not account for scr refresh
                fix6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix6, 'tStartRefresh')  # time at next scr refresh
                fix6.setAutoDraw(True)
            if fix6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix6.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix6.tStop = t  # not accounting for scr refresh
                    fix6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix6, 'tStopRefresh')  # time at next scr refresh
                    fix6.setAutoDraw(False)
            
            # *counter_square* updates
            if counter_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                counter_square.frameNStart = frameN  # exact frame index
                counter_square.tStart = t  # local t and not account for scr refresh
                counter_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(counter_square, 'tStartRefresh')  # time at next scr refresh
                counter_square.setAutoDraw(True)
            if counter_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > counter_square.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    counter_square.tStop = t  # not accounting for scr refresh
                    counter_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(counter_square, 'tStopRefresh')  # time at next scr refresh
                    counter_square.setAutoDraw(False)
            
            # *feedbacktext_2* updates
            if feedbacktext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbacktext_2.frameNStart = frameN  # exact frame index
                feedbacktext_2.tStart = t  # local t and not account for scr refresh
                feedbacktext_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbacktext_2, 'tStartRefresh')  # time at next scr refresh
                feedbacktext_2.setAutoDraw(True)
            if feedbacktext_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbacktext_2.tStartRefresh + .3-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbacktext_2.tStop = t  # not accounting for scr refresh
                    feedbacktext_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbacktext_2, 'tStopRefresh')  # time at next scr refresh
                    feedbacktext_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in counterfactualComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "counterfactual"-------
        for thisComponent in counterfactualComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        timeout.addData('reveal2.started', reveal2.tStartRefresh)
        timeout.addData('reveal2.stopped', reveal2.tStopRefresh)
        timeout.addData('fix6.started', fix6.tStartRefresh)
        timeout.addData('fix6.stopped', fix6.tStopRefresh)
        timeout.addData('counter_square.started', counter_square.tStartRefresh)
        timeout.addData('counter_square.stopped', counter_square.tStopRefresh)
        timeout.addData('feedbacktext_2.started', feedbacktext_2.tStartRefresh)
        timeout.addData('feedbacktext_2.stopped', feedbacktext_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nReps2 repeats of 'timeout'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'block1'


# ------Prepare to start Routine "Finish"-------
continueRoutine = True
# update component parameters for each repeat
block1_wait.keys = []
block1_wait.rt = []
_block1_wait_allKeys = []
# keep track of which components have finished
FinishComponents = [Block_Finish, block1_wait, block1_points, block1_points_earned]
for thisComponent in FinishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Finish"-------
while continueRoutine:
    # get current time
    t = FinishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Block_Finish* updates
    if Block_Finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Block_Finish.frameNStart = frameN  # exact frame index
        Block_Finish.tStart = t  # local t and not account for scr refresh
        Block_Finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Block_Finish, 'tStartRefresh')  # time at next scr refresh
        Block_Finish.setAutoDraw(True)
    
    # *block1_wait* updates
    waitOnFlip = False
    if block1_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block1_wait.frameNStart = frameN  # exact frame index
        block1_wait.tStart = t  # local t and not account for scr refresh
        block1_wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block1_wait, 'tStartRefresh')  # time at next scr refresh
        block1_wait.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(block1_wait.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(block1_wait.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if block1_wait.status == STARTED and not waitOnFlip:
        theseKeys = block1_wait.getKeys(keyList=['space'], waitRelease=False)
        _block1_wait_allKeys.extend(theseKeys)
        if len(_block1_wait_allKeys):
            block1_wait.keys = _block1_wait_allKeys[-1].name  # just the last key pressed
            block1_wait.rt = _block1_wait_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *block1_points* updates
    if block1_points.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block1_points.frameNStart = frameN  # exact frame index
        block1_points.tStart = t  # local t and not account for scr refresh
        block1_points.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block1_points, 'tStartRefresh')  # time at next scr refresh
        block1_points.setAutoDraw(True)
    
    # *block1_points_earned* updates
    if block1_points_earned.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block1_points_earned.frameNStart = frameN  # exact frame index
        block1_points_earned.tStart = t  # local t and not account for scr refresh
        block1_points_earned.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block1_points_earned, 'tStartRefresh')  # time at next scr refresh
        block1_points_earned.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finish"-------
for thisComponent in FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Block_Finish.started', Block_Finish.tStartRefresh)
thisExp.addData('Block_Finish.stopped', Block_Finish.tStopRefresh)
# check responses
if block1_wait.keys in ['', [], None]:  # No response was made
    block1_wait.keys = None
thisExp.addData('block1_wait.keys',block1_wait.keys)
if block1_wait.keys != None:  # we had a response
    thisExp.addData('block1_wait.rt', block1_wait.rt)
thisExp.addData('block1_wait.started', block1_wait.tStartRefresh)
thisExp.addData('block1_wait.stopped', block1_wait.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('block1_points.started', block1_points.tStartRefresh)
thisExp.addData('block1_points.stopped', block1_points.tStopRefresh)
thisExp.addData('block1_points_earned.started', block1_points_earned.tStartRefresh)
thisExp.addData('block1_points_earned.stopped', block1_points_earned.tStopRefresh)
# the Routine "Finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
