#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on April 28, 2020, at 11:31
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
    originPath='C:\\Users\\Carlos\\Documents\\Credit_Assignment_Study\\Behavioral_MBCA_lastrun.py',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
key_resp = keyboard.Keyboard()
Ins = visual.TextStim(win=win, name='Ins',
    text="Hello, in this task you will be presented with two separate stimuli a face and a house. You will see numbers overlayed on these images that stand for a number of points you can gamble for. Each image will have an independent probability of leading to that amount of reward. Once you see the choose screen, you will indicate which image you'd like to gamble for with the left and right arrow key. Press left for face and right for house. Based on the number of points you get at the end you will receive a cash payout! To start we will first be performing a few practice rounds. When you're ready press the spacebar to continue. ",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [key_resp, Ins]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
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
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
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
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('piloting.csv'),
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
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.0-frameTolerance:
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
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.0-frameTolerance:
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
            if tThisFlipGlobal > jitter1.tStartRefresh + 1.0-frameTolerance:
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
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    choiceComponents = [Choice, key_resp_2]
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
    
    # ------Prepare to start Routine "long_delay"-------
    continueRoutine = True
    routineTimer.add(6.000000)
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
            if tThisFlipGlobal > fix3.tStartRefresh + 6-frameTolerance:
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
    practice.addData('fix3.started', fix3.tStartRefresh)
    practice.addData('fix3.stopped', fix3.tStopRefresh)
    
    # ------Prepare to start Routine "Outcome"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    reveal.setText(option1)
    fix5.setImage(imageFix)
    # keep track of which components have finished
    OutcomeComponents = [reveal, fix5]
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
            if tThisFlipGlobal > reveal.tStartRefresh + .2-frameTolerance:
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
            if tThisFlipGlobal > fix5.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix5.tStop = t  # not accounting for scr refresh
                fix5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix5, 'tStopRefresh')  # time at next scr refresh
                fix5.setAutoDraw(False)
        
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
    practice.addData('reveal.started', reveal.tStartRefresh)
    practice.addData('reveal.stopped', reveal.tStopRefresh)
    practice.addData('fix5.started', fix5.tStartRefresh)
    practice.addData('fix5.stopped', fix5.tStopRefresh)
    
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
    
    # ------Prepare to start Routine "counterfactual"-------
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    reveal2.setText(option2)
    fix6.setImage(imageFix)
    # keep track of which components have finished
    counterfactualComponents = [reveal2, fix6]
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
            if tThisFlipGlobal > reveal2.tStartRefresh + .2-frameTolerance:
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
            if tThisFlipGlobal > fix6.tStartRefresh + .2-frameTolerance:
                # keep track of stop time/frame for later
                fix6.tStop = t  # not accounting for scr refresh
                fix6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix6, 'tStopRefresh')  # time at next scr refresh
                fix6.setAutoDraw(False)
        
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
    practice.addData('reveal2.started', reveal2.tStartRefresh)
    practice.addData('reveal2.stopped', reveal2.tStopRefresh)
    practice.addData('fix6.started', fix6.tStartRefresh)
    practice.addData('fix6.stopped', fix6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'practice'


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
