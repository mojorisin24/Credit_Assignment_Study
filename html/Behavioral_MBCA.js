/************************ 
 * Behavioral_Mbca Test *
 ************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Behavioral_MBCA';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'age': '', 'biological sex (m/f/i)': '', 'handedness (l/r)': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Prac_InstructionsRoutineBegin());
flowScheduler.add(Prac_InstructionsRoutineEachFrame());
flowScheduler.add(Prac_InstructionsRoutineEnd());
const practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopBegin, practiceLoopScheduler);
flowScheduler.add(practiceLoopScheduler);
flowScheduler.add(practiceLoopEnd);
flowScheduler.add(practice_endRoutineBegin());
flowScheduler.add(practice_endRoutineEachFrame());
flowScheduler.add(practice_endRoutineEnd());
flowScheduler.add(Exp_InstructionsRoutineBegin());
flowScheduler.add(Exp_InstructionsRoutineEachFrame());
flowScheduler.add(Exp_InstructionsRoutineEnd());
const block1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(block1LoopBegin, block1LoopScheduler);
flowScheduler.add(block1LoopScheduler);
flowScheduler.add(block1LoopEnd);
flowScheduler.add(FinishRoutineBegin());
flowScheduler.add(FinishRoutineEachFrame());
flowScheduler.add(FinishRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var Prac_InstructionsClock;
var key_resp;
var Ins;
var iti2Clock;
var fix4;
var stim_presentation1Clock;
var stim1;
var fix;
var prob1;
var itiClock;
var jitter1;
var stim_presentation2Clock;
var stim2;
var fix2;
var prob2;
var choiceClock;
var Choice;
var choice_fix;
var key_resp_2;
var timeout_msgClock;
var timeout_text;
var key_resp_4;
var long_delayClock;
var fix3;
var OutcomeClock;
var reveal;
var fix5;
var outcome_circle;
var points_this_round;
var points_total;
var feedbacktext;
var counterfactualClock;
var reveal2;
var fix6;
var counter_square;
var feedbacktext_2;
var practice_endClock;
var practice_finish;
var key_resp_3;
var total_points_earned;
var points_earned;
var Exp_InstructionsClock;
var text_2;
var key_resp_5;
var choice_b1Clock;
var Choice_2;
var choice_fix_2;
var key_resp_6;
var Outcome_expClock;
var reveal_2;
var fix5_2;
var outcome_circle_2;
var points_b1;
var b1_total;
var counterfactual_expClock;
var reveal2_2;
var fix6_2;
var counter_square_2;
var FinishClock;
var Block_Finish;
var block1_wait;
var block1_points;
var block1_points_earned;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Prac_Instructions"
  Prac_InstructionsClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Ins = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ins',
    text: "Hello, in this task you will be presented with two separate images of a face and a house. You will see points overlayed on these images that you can gamble for. Each image will have an independent probability of leading to that amount of reward. Once you see the choose screen, you will indicate which image you'd like to gamble for with the left and right arrow key. Press left for the first image and right for the second. Based on the number of points you get in a given block, you will receive a cash payout! To start we will first be performing a few practice rounds. \nPlease note that loss does not mean that you will lose that amount of points for your gamble, it just means that you earned zero points. \nWhen you're ready press the spacebar to continue. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "iti2"
  iti2Clock = new util.Clock();
  fix4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix4', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stim_presentation1"
  stim_presentation1Clock = new util.Clock();
  stim1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [400, 400],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  fix = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  prob1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'prob1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  jitter1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jitter1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stim_presentation2"
  stim_presentation2Clock = new util.Clock();
  stim2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [400, 400],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  fix2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  prob2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'prob2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  jitter1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jitter1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "choice"
  choiceClock = new util.Clock();
  Choice = new visual.TextStim({
    win: psychoJS.window,
    name: 'Choice',
    text: 'Choose',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.01], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  choice_fix = new visual.ImageStim({
    win : psychoJS.window,
    name : 'choice_fix', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "timeout_msg"
  timeout_msgClock = new util.Clock();
  timeout_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timeout_text',
    text: 'You did not respond in time! This trial will not count. Please make sure that you are paying attention. Press the spacebar when ready to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "long_delay"
  long_delayClock = new util.Clock();
  fix3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix3', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "Outcome"
  OutcomeClock = new util.Clock();
  reveal = new visual.TextStim({
    win: psychoJS.window,
    name: 'reveal',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  fix5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix5', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  outcome_circle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'outcome_circle', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1280, 720],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  points_this_round = 0;
  points_total = 0;
  
  feedbacktext = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbacktext',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "iti2"
  iti2Clock = new util.Clock();
  fix4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix4', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "counterfactual"
  counterfactualClock = new util.Clock();
  reveal2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reveal2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  fix6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix6', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  counter_square = new visual.ImageStim({
    win : psychoJS.window,
    name : 'counter_square', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1280, 720],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  feedbacktext_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbacktext_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "practice_end"
  practice_endClock = new util.Clock();
  practice_finish = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_finish',
    text: 'This concludes the practice. Press the spacebar when ready to continue to the actual trials. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  total_points_earned = new visual.TextStim({
    win: psychoJS.window,
    name: 'total_points_earned',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  points_earned = new visual.TextStim({
    win: psychoJS.window,
    name: 'points_earned',
    text: 'Total Points Earned During Practice:  ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Exp_Instructions"
  Exp_InstructionsClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'We will now start the actual experiment. You will no longer be seeing text with your result, just the colored shapes associated with each outcome. You will be performing N blocks of this task, at the end of the experiment we will select the points you earned on one block and that will be converted to a dollar amount which we will send to you via email. Press the spacebar when ready to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "iti2"
  iti2Clock = new util.Clock();
  fix4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix4', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stim_presentation1"
  stim_presentation1Clock = new util.Clock();
  stim1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [400, 400],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  fix = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  prob1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'prob1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  jitter1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jitter1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "stim_presentation2"
  stim_presentation2Clock = new util.Clock();
  stim2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [400, 400],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  fix2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  prob2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'prob2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  jitter1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'jitter1', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "choice_b1"
  choice_b1Clock = new util.Clock();
  Choice_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Choice_2',
    text: 'Choose',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.01], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  choice_fix_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'choice_fix_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "timeout_msg"
  timeout_msgClock = new util.Clock();
  timeout_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timeout_text',
    text: 'You did not respond in time! This trial will not count. Please make sure that you are paying attention. Press the spacebar when ready to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "long_delay"
  long_delayClock = new util.Clock();
  fix3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix3', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "Outcome_exp"
  Outcome_expClock = new util.Clock();
  reveal_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reveal_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  fix5_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix5_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  outcome_circle_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'outcome_circle_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1280, 720],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  points_b1 = 0;
  b1_total = 0;
  
  // Initialize components for Routine "iti2"
  iti2Clock = new util.Clock();
  fix4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix4', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "counterfactual_exp"
  counterfactual_expClock = new util.Clock();
  reveal2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'reveal2_2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  fix6_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix6_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [25, 25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  counter_square_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'counter_square_2', units : 'pix', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1280, 720],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Finish"
  FinishClock = new util.Clock();
  Block_Finish = new visual.TextStim({
    win: psychoJS.window,
    name: 'Block_Finish',
    text: 'This concludes the first block. Please feel free to take a break and press the spacebar whenever you are ready to continue. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  block1_wait = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  block1_points = new visual.TextStim({
    win: psychoJS.window,
    name: 'block1_points',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  block1_points_earned = new visual.TextStim({
    win: psychoJS.window,
    name: 'block1_points_earned',
    text: 'Total Points Earned During Block 1:  ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var Prac_InstructionsComponents;
function Prac_InstructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Prac_Instructions'-------
    t = 0;
    Prac_InstructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    Prac_InstructionsComponents = [];
    Prac_InstructionsComponents.push(key_resp);
    Prac_InstructionsComponents.push(Ins);
    
    for (const thisComponent of Prac_InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function Prac_InstructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Prac_Instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Prac_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Ins* updates
    if (t >= 0.0 && Ins.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ins.tStart = t;  // (not accounting for frame time here)
      Ins.frameNStart = frameN;  // exact frame index
      
      Ins.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Prac_InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prac_InstructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Prac_Instructions'-------
    for (const thisComponent of Prac_InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Prac_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice;
var currentLoop;
function practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'practice.csv',
    seed: undefined, name: 'practice'
  });
  psychoJS.experiment.addLoop(practice); // add the loop to the experiment
  currentLoop = practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice of practice) {
    const snapshot = practice.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(iti2RoutineBegin(snapshot));
    thisScheduler.add(iti2RoutineEachFrame(snapshot));
    thisScheduler.add(iti2RoutineEnd(snapshot));
    thisScheduler.add(stim_presentation1RoutineBegin(snapshot));
    thisScheduler.add(stim_presentation1RoutineEachFrame(snapshot));
    thisScheduler.add(stim_presentation1RoutineEnd(snapshot));
    thisScheduler.add(itiRoutineBegin(snapshot));
    thisScheduler.add(itiRoutineEachFrame(snapshot));
    thisScheduler.add(itiRoutineEnd(snapshot));
    thisScheduler.add(stim_presentation2RoutineBegin(snapshot));
    thisScheduler.add(stim_presentation2RoutineEachFrame(snapshot));
    thisScheduler.add(stim_presentation2RoutineEnd(snapshot));
    thisScheduler.add(itiRoutineBegin(snapshot));
    thisScheduler.add(itiRoutineEachFrame(snapshot));
    thisScheduler.add(itiRoutineEnd(snapshot));
    thisScheduler.add(choiceRoutineBegin(snapshot));
    thisScheduler.add(choiceRoutineEachFrame(snapshot));
    thisScheduler.add(choiceRoutineEnd(snapshot));
    const message_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(message_loopLoopBegin, message_loopLoopScheduler);
    thisScheduler.add(message_loopLoopScheduler);
    thisScheduler.add(message_loopLoopEnd);
    const practice_timeoutLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(practice_timeoutLoopBegin, practice_timeoutLoopScheduler);
    thisScheduler.add(practice_timeoutLoopScheduler);
    thisScheduler.add(practice_timeoutLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var message_loop;
function message_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  message_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numReps, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'message_loop'
  });
  psychoJS.experiment.addLoop(message_loop); // add the loop to the experiment
  currentLoop = message_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMessage_loop of message_loop) {
    const snapshot = message_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(timeout_msgRoutineBegin(snapshot));
    thisScheduler.add(timeout_msgRoutineEachFrame(snapshot));
    thisScheduler.add(timeout_msgRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function message_loopLoopEnd() {
  psychoJS.experiment.removeLoop(message_loop);

  return Scheduler.Event.NEXT;
}


var practice_timeout;
function practice_timeoutLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice_timeout = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numReps2, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'practice_timeout'
  });
  psychoJS.experiment.addLoop(practice_timeout); // add the loop to the experiment
  currentLoop = practice_timeout;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice_timeout of practice_timeout) {
    const snapshot = practice_timeout.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(long_delayRoutineBegin(snapshot));
    thisScheduler.add(long_delayRoutineEachFrame(snapshot));
    thisScheduler.add(long_delayRoutineEnd(snapshot));
    thisScheduler.add(OutcomeRoutineBegin(snapshot));
    thisScheduler.add(OutcomeRoutineEachFrame(snapshot));
    thisScheduler.add(OutcomeRoutineEnd(snapshot));
    thisScheduler.add(iti2RoutineBegin(snapshot));
    thisScheduler.add(iti2RoutineEachFrame(snapshot));
    thisScheduler.add(iti2RoutineEnd(snapshot));
    thisScheduler.add(counterfactualRoutineBegin(snapshot));
    thisScheduler.add(counterfactualRoutineEachFrame(snapshot));
    thisScheduler.add(counterfactualRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function practice_timeoutLoopEnd() {
  psychoJS.experiment.removeLoop(practice_timeout);

  return Scheduler.Event.NEXT;
}


function practiceLoopEnd() {
  psychoJS.experiment.removeLoop(practice);

  return Scheduler.Event.NEXT;
}


var block1;
function block1LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  block1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'block1.csv',
    seed: undefined, name: 'block1'
  });
  psychoJS.experiment.addLoop(block1); // add the loop to the experiment
  currentLoop = block1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock1 of block1) {
    const snapshot = block1.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(iti2RoutineBegin(snapshot));
    thisScheduler.add(iti2RoutineEachFrame(snapshot));
    thisScheduler.add(iti2RoutineEnd(snapshot));
    thisScheduler.add(stim_presentation1RoutineBegin(snapshot));
    thisScheduler.add(stim_presentation1RoutineEachFrame(snapshot));
    thisScheduler.add(stim_presentation1RoutineEnd(snapshot));
    thisScheduler.add(itiRoutineBegin(snapshot));
    thisScheduler.add(itiRoutineEachFrame(snapshot));
    thisScheduler.add(itiRoutineEnd(snapshot));
    thisScheduler.add(stim_presentation2RoutineBegin(snapshot));
    thisScheduler.add(stim_presentation2RoutineEachFrame(snapshot));
    thisScheduler.add(stim_presentation2RoutineEnd(snapshot));
    thisScheduler.add(itiRoutineBegin(snapshot));
    thisScheduler.add(itiRoutineEachFrame(snapshot));
    thisScheduler.add(itiRoutineEnd(snapshot));
    thisScheduler.add(choice_b1RoutineBegin(snapshot));
    thisScheduler.add(choice_b1RoutineEachFrame(snapshot));
    thisScheduler.add(choice_b1RoutineEnd(snapshot));
    const timeout_msg_loopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(timeout_msg_loopLoopBegin, timeout_msg_loopLoopScheduler);
    thisScheduler.add(timeout_msg_loopLoopScheduler);
    thisScheduler.add(timeout_msg_loopLoopEnd);
    const timeoutLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(timeoutLoopBegin, timeoutLoopScheduler);
    thisScheduler.add(timeoutLoopScheduler);
    thisScheduler.add(timeoutLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var timeout_msg_loop;
function timeout_msg_loopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  timeout_msg_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numReps, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'timeout_msg_loop'
  });
  psychoJS.experiment.addLoop(timeout_msg_loop); // add the loop to the experiment
  currentLoop = timeout_msg_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTimeout_msg_loop of timeout_msg_loop) {
    const snapshot = timeout_msg_loop.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(timeout_msgRoutineBegin(snapshot));
    thisScheduler.add(timeout_msgRoutineEachFrame(snapshot));
    thisScheduler.add(timeout_msgRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function timeout_msg_loopLoopEnd() {
  psychoJS.experiment.removeLoop(timeout_msg_loop);

  return Scheduler.Event.NEXT;
}


var timeout;
function timeoutLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  timeout = new TrialHandler({
    psychoJS: psychoJS,
    nReps: numReps2, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'timeout'
  });
  psychoJS.experiment.addLoop(timeout); // add the loop to the experiment
  currentLoop = timeout;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTimeout of timeout) {
    const snapshot = timeout.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(long_delayRoutineBegin(snapshot));
    thisScheduler.add(long_delayRoutineEachFrame(snapshot));
    thisScheduler.add(long_delayRoutineEnd(snapshot));
    thisScheduler.add(Outcome_expRoutineBegin(snapshot));
    thisScheduler.add(Outcome_expRoutineEachFrame(snapshot));
    thisScheduler.add(Outcome_expRoutineEnd(snapshot));
    thisScheduler.add(iti2RoutineBegin(snapshot));
    thisScheduler.add(iti2RoutineEachFrame(snapshot));
    thisScheduler.add(iti2RoutineEnd(snapshot));
    thisScheduler.add(counterfactual_expRoutineBegin(snapshot));
    thisScheduler.add(counterfactual_expRoutineEachFrame(snapshot));
    thisScheduler.add(counterfactual_expRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function timeoutLoopEnd() {
  psychoJS.experiment.removeLoop(timeout);

  return Scheduler.Event.NEXT;
}


function block1LoopEnd() {
  psychoJS.experiment.removeLoop(block1);

  return Scheduler.Event.NEXT;
}


var iti2Components;
function iti2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'iti2'-------
    t = 0;
    iti2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    fix4.setImage(imageFix);
    // keep track of which components have finished
    iti2Components = [];
    iti2Components.push(fix4);
    
    for (const thisComponent of iti2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function iti2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'iti2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = iti2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix4* updates
    if (t >= 0.0 && fix4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix4.tStart = t;  // (not accounting for frame time here)
      fix4.frameNStart = frameN;  // exact frame index
      
      fix4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of iti2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function iti2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'iti2'-------
    for (const thisComponent of iti2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var stim_presentation1Components;
function stim_presentation1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stim_presentation1'-------
    t = 0;
    stim_presentation1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    stim1.setImage(imageFile);
    fix.setImage(imageFix);
    prob1.setText(option1);
    // keep track of which components have finished
    stim_presentation1Components = [];
    stim_presentation1Components.push(stim1);
    stim_presentation1Components.push(fix);
    stim_presentation1Components.push(prob1);
    
    for (const thisComponent of stim_presentation1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function stim_presentation1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stim_presentation1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stim_presentation1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stim1* updates
    if (t >= 0.0 && stim1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim1.tStart = t;  // (not accounting for frame time here)
      stim1.frameNStart = frameN;  // exact frame index
      
      stim1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stim1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stim1.setAutoDraw(false);
    }
    
    // *fix* updates
    if (t >= 0.0 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix.setAutoDraw(false);
    }
    
    // *prob1* updates
    if (t >= 0.0 && prob1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prob1.tStart = t;  // (not accounting for frame time here)
      prob1.frameNStart = frameN;  // exact frame index
      
      prob1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prob1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prob1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stim_presentation1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stim_presentation1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stim_presentation1'-------
    for (const thisComponent of stim_presentation1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var itiComponents;
function itiRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'iti'-------
    t = 0;
    itiClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    jitter1.setPos([0, 0]);
    jitter1.setImage(imageFix);
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(jitter1);
    
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function itiRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'iti'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *jitter1* updates
    if (t >= 0.0 && jitter1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      jitter1.tStart = t;  // (not accounting for frame time here)
      jitter1.frameNStart = frameN;  // exact frame index
      
      jitter1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (jitter1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      jitter1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of itiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'iti'-------
    for (const thisComponent of itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var stim_presentation2Components;
function stim_presentation2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'stim_presentation2'-------
    t = 0;
    stim_presentation2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.200000);
    // update component parameters for each repeat
    stim2.setImage(imageFile2);
    fix2.setImage(imageFix);
    prob2.setText(option2);
    // keep track of which components have finished
    stim_presentation2Components = [];
    stim_presentation2Components.push(stim2);
    stim_presentation2Components.push(fix2);
    stim_presentation2Components.push(prob2);
    
    for (const thisComponent of stim_presentation2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function stim_presentation2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'stim_presentation2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = stim_presentation2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stim2* updates
    if (t >= 0.0 && stim2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim2.tStart = t;  // (not accounting for frame time here)
      stim2.frameNStart = frameN;  // exact frame index
      
      stim2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stim2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stim2.setAutoDraw(false);
    }
    
    // *fix2* updates
    if (t >= 0.0 && fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix2.tStart = t;  // (not accounting for frame time here)
      fix2.frameNStart = frameN;  // exact frame index
      
      fix2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix2.setAutoDraw(false);
    }
    
    // *prob2* updates
    if (t >= 0.0 && prob2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prob2.tStart = t;  // (not accounting for frame time here)
      prob2.frameNStart = frameN;  // exact frame index
      
      prob2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prob2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prob2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stim_presentation2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stim_presentation2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'stim_presentation2'-------
    for (const thisComponent of stim_presentation2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var numReps;
var numReps2;
var choiceComponents;
function choiceRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'choice'-------
    t = 0;
    choiceClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    choice_fix.setImage(imageFix);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    numReps = 0;
    numReps2 = 1;
    
    // keep track of which components have finished
    choiceComponents = [];
    choiceComponents.push(Choice);
    choiceComponents.push(choice_fix);
    choiceComponents.push(key_resp_2);
    
    for (const thisComponent of choiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function choiceRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'choice'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = choiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Choice* updates
    if (t >= 0.0 && Choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Choice.tStart = t;  // (not accounting for frame time here)
      Choice.frameNStart = frameN;  // exact frame index
      
      Choice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Choice.setAutoDraw(false);
    }
    
    // *choice_fix* updates
    if (t >= 0.0 && choice_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_fix.tStart = t;  // (not accounting for frame time here)
      choice_fix.frameNStart = frameN;  // exact frame index
      
      choice_fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice_fix.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_2.keys == corr) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of choiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choiceRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'choice'-------
    for (const thisComponent of choiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corr)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    if ((! key_resp_2.keys)) {
        numReps = 1;
        numReps2 = 0;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var timeout_msgComponents;
function timeout_msgRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'timeout_msg'-------
    t = 0;
    timeout_msgClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    timeout_msgComponents = [];
    timeout_msgComponents.push(timeout_text);
    timeout_msgComponents.push(key_resp_4);
    
    for (const thisComponent of timeout_msgComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function timeout_msgRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'timeout_msg'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = timeout_msgClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *timeout_text* updates
    if (t >= 0.0 && timeout_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timeout_text.tStart = t;  // (not accounting for frame time here)
      timeout_text.frameNStart = frameN;  // exact frame index
      
      timeout_text.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of timeout_msgComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function timeout_msgRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'timeout_msg'-------
    for (const thisComponent of timeout_msgComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "timeout_msg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var long_delayComponents;
function long_delayRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'long_delay'-------
    t = 0;
    long_delayClock.reset(); // clock
    frameN = -1;
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    fix3.setImage(imageFix);
    // keep track of which components have finished
    long_delayComponents = [];
    long_delayComponents.push(fix3);
    
    for (const thisComponent of long_delayComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function long_delayRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'long_delay'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = long_delayClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix3* updates
    if (t >= 0.0 && fix3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix3.tStart = t;  // (not accounting for frame time here)
      fix3.frameNStart = frameN;  // exact frame index
      
      fix3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of long_delayComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function long_delayRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'long_delay'-------
    for (const thisComponent of long_delayComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var msg;
var msgColor;
var OutcomeComponents;
function OutcomeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Outcome'-------
    t = 0;
    OutcomeClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    reveal.setText(option1);
    fix5.setImage(imageFix);
    outcome_circle.setImage(outcome);
    if (key_resp_2.corr) {
        msg = outcome_msg_optimal;
        msgColor = "black";
        points_this_round = point_earned_optimal;
    } else {
        msg = outcome_msg_alt;
        msgColor = "black";
        points_this_round = point_earned_alt;
    }
    
    feedbacktext.setColor(new util.Color(msgColor));
    feedbacktext.setText(msg);
    // keep track of which components have finished
    OutcomeComponents = [];
    OutcomeComponents.push(reveal);
    OutcomeComponents.push(fix5);
    OutcomeComponents.push(outcome_circle);
    OutcomeComponents.push(feedbacktext);
    
    for (const thisComponent of OutcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function OutcomeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Outcome'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = OutcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *reveal* updates
    if (t >= 0.0 && reveal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reveal.tStart = t;  // (not accounting for frame time here)
      reveal.frameNStart = frameN;  // exact frame index
      
      reveal.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reveal.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reveal.setAutoDraw(false);
    }
    
    // *fix5* updates
    if (t >= 0.0 && fix5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix5.tStart = t;  // (not accounting for frame time here)
      fix5.frameNStart = frameN;  // exact frame index
      
      fix5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix5.setAutoDraw(false);
    }
    
    // *outcome_circle* updates
    if (t >= 0.0 && outcome_circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcome_circle.tStart = t;  // (not accounting for frame time here)
      outcome_circle.frameNStart = frameN;  // exact frame index
      
      outcome_circle.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outcome_circle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outcome_circle.setAutoDraw(false);
    }
    
    // *feedbacktext* updates
    if (t >= 0.0 && feedbacktext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbacktext.tStart = t;  // (not accounting for frame time here)
      feedbacktext.frameNStart = frameN;  // exact frame index
      
      feedbacktext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbacktext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbacktext.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of OutcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function OutcomeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Outcome'-------
    for (const thisComponent of OutcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((! key_resp_2.keys)) {
        points_total = (0 + points_total);
    } else {
        points_total = (points_this_round + points_total);
    }
    
    return Scheduler.Event.NEXT;
  };
}


var counterfactualComponents;
function counterfactualRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'counterfactual'-------
    t = 0;
    counterfactualClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    reveal2.setText(option2);
    fix6.setImage(imageFix);
    counter_square.setImage(counterfactual);
    if (key_resp_2.corr) {
        msg = counterfactual_msg_optimal;
        msgColor = "black";
    } else {
        msg = counterfactual_msg_alt;
        msgColor = "black";
    }
    
    feedbacktext_2.setColor(new util.Color(msgColor));
    feedbacktext_2.setText(msg);
    // keep track of which components have finished
    counterfactualComponents = [];
    counterfactualComponents.push(reveal2);
    counterfactualComponents.push(fix6);
    counterfactualComponents.push(counter_square);
    counterfactualComponents.push(feedbacktext_2);
    
    for (const thisComponent of counterfactualComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function counterfactualRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'counterfactual'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = counterfactualClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *reveal2* updates
    if (t >= 0.0 && reveal2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reveal2.tStart = t;  // (not accounting for frame time here)
      reveal2.frameNStart = frameN;  // exact frame index
      
      reveal2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reveal2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reveal2.setAutoDraw(false);
    }
    
    // *fix6* updates
    if (t >= 0.0 && fix6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix6.tStart = t;  // (not accounting for frame time here)
      fix6.frameNStart = frameN;  // exact frame index
      
      fix6.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix6.setAutoDraw(false);
    }
    
    // *counter_square* updates
    if (t >= 0.0 && counter_square.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      counter_square.tStart = t;  // (not accounting for frame time here)
      counter_square.frameNStart = frameN;  // exact frame index
      
      counter_square.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (counter_square.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      counter_square.setAutoDraw(false);
    }
    
    // *feedbacktext_2* updates
    if (t >= 0.0 && feedbacktext_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbacktext_2.tStart = t;  // (not accounting for frame time here)
      feedbacktext_2.frameNStart = frameN;  // exact frame index
      
      feedbacktext_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedbacktext_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbacktext_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of counterfactualComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function counterfactualRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'counterfactual'-------
    for (const thisComponent of counterfactualComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var practice_endComponents;
function practice_endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practice_end'-------
    t = 0;
    practice_endClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    total_points_earned.setText(points_total);
    // keep track of which components have finished
    practice_endComponents = [];
    practice_endComponents.push(practice_finish);
    practice_endComponents.push(key_resp_3);
    practice_endComponents.push(total_points_earned);
    practice_endComponents.push(points_earned);
    
    for (const thisComponent of practice_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function practice_endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practice_end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practice_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_finish* updates
    if (t >= 0.0 && practice_finish.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_finish.tStart = t;  // (not accounting for frame time here)
      practice_finish.frameNStart = frameN;  // exact frame index
      
      practice_finish.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *total_points_earned* updates
    if (t >= 0.0 && total_points_earned.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      total_points_earned.tStart = t;  // (not accounting for frame time here)
      total_points_earned.frameNStart = frameN;  // exact frame index
      
      total_points_earned.setAutoDraw(true);
    }

    
    // *points_earned* updates
    if (t >= 0.0 && points_earned.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      points_earned.tStart = t;  // (not accounting for frame time here)
      points_earned.frameNStart = frameN;  // exact frame index
      
      points_earned.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practice_end'-------
    for (const thisComponent of practice_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var Exp_InstructionsComponents;
function Exp_InstructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Exp_Instructions'-------
    t = 0;
    Exp_InstructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    Exp_InstructionsComponents = [];
    Exp_InstructionsComponents.push(text_2);
    Exp_InstructionsComponents.push(key_resp_5);
    
    for (const thisComponent of Exp_InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Exp_InstructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Exp_Instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Exp_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Exp_InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Exp_InstructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Exp_Instructions'-------
    for (const thisComponent of Exp_InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "Exp_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var choice_b1Components;
function choice_b1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'choice_b1'-------
    t = 0;
    choice_b1Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    choice_fix_2.setImage(imageFix);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    numReps = 0;
    numReps2 = 1;
    
    // keep track of which components have finished
    choice_b1Components = [];
    choice_b1Components.push(Choice_2);
    choice_b1Components.push(choice_fix_2);
    choice_b1Components.push(key_resp_6);
    
    for (const thisComponent of choice_b1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function choice_b1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'choice_b1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = choice_b1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Choice_2* updates
    if (t >= 0.0 && Choice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Choice_2.tStart = t;  // (not accounting for frame time here)
      Choice_2.frameNStart = frameN;  // exact frame index
      
      Choice_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Choice_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Choice_2.setAutoDraw(false);
    }
    
    // *choice_fix_2* updates
    if (t >= 0.0 && choice_fix_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_fix_2.tStart = t;  // (not accounting for frame time here)
      choice_fix_2.frameNStart = frameN;  // exact frame index
      
      choice_fix_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice_fix_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice_fix_2.setAutoDraw(false);
    }
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_6.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_6.keys == corr) {
            key_resp_6.corr = 1;
        } else {
            key_resp_6.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of choice_b1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choice_b1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'choice_b1'-------
    for (const thisComponent of choice_b1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_6.keys === undefined) {
      if (['None','none',undefined].includes(corr)) {
         key_resp_6.corr = 1;  // correct non-response
      } else {
         key_resp_6.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    psychoJS.experiment.addData('key_resp_6.corr', key_resp_6.corr);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    if ((! key_resp_6.keys)) {
        numReps = 1;
        numReps2 = 0;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var Outcome_expComponents;
function Outcome_expRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Outcome_exp'-------
    t = 0;
    Outcome_expClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    reveal_2.setText(option1);
    fix5_2.setImage(imageFix);
    outcome_circle_2.setImage(outcome);
    if (key_resp_6.corr) {
        points_b1 = point_earned_optimal;
    } else {
        points_b1 = point_earned_alt;
    }
    
    // keep track of which components have finished
    Outcome_expComponents = [];
    Outcome_expComponents.push(reveal_2);
    Outcome_expComponents.push(fix5_2);
    Outcome_expComponents.push(outcome_circle_2);
    
    for (const thisComponent of Outcome_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Outcome_expRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Outcome_exp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Outcome_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *reveal_2* updates
    if (t >= 0.0 && reveal_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reveal_2.tStart = t;  // (not accounting for frame time here)
      reveal_2.frameNStart = frameN;  // exact frame index
      
      reveal_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reveal_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reveal_2.setAutoDraw(false);
    }
    
    // *fix5_2* updates
    if (t >= 0.0 && fix5_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix5_2.tStart = t;  // (not accounting for frame time here)
      fix5_2.frameNStart = frameN;  // exact frame index
      
      fix5_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix5_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix5_2.setAutoDraw(false);
    }
    
    // *outcome_circle_2* updates
    if (t >= 0.0 && outcome_circle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcome_circle_2.tStart = t;  // (not accounting for frame time here)
      outcome_circle_2.frameNStart = frameN;  // exact frame index
      
      outcome_circle_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outcome_circle_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outcome_circle_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Outcome_expComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Outcome_expRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Outcome_exp'-------
    for (const thisComponent of Outcome_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((! key_resp_6.keys)) {
        b1_total = (0 + b1_total);
    } else {
        b1_total = (points_b1 + b1_total);
    }
    
    return Scheduler.Event.NEXT;
  };
}


var counterfactual_expComponents;
function counterfactual_expRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'counterfactual_exp'-------
    t = 0;
    counterfactual_expClock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.300000);
    // update component parameters for each repeat
    reveal2_2.setText(option2);
    fix6_2.setImage(imageFix);
    counter_square_2.setImage(counterfactual);
    // keep track of which components have finished
    counterfactual_expComponents = [];
    counterfactual_expComponents.push(reveal2_2);
    counterfactual_expComponents.push(fix6_2);
    counterfactual_expComponents.push(counter_square_2);
    
    for (const thisComponent of counterfactual_expComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function counterfactual_expRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'counterfactual_exp'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = counterfactual_expClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *reveal2_2* updates
    if (t >= 0.0 && reveal2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reveal2_2.tStart = t;  // (not accounting for frame time here)
      reveal2_2.frameNStart = frameN;  // exact frame index
      
      reveal2_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reveal2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reveal2_2.setAutoDraw(false);
    }
    
    // *fix6_2* updates
    if (t >= 0.0 && fix6_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix6_2.tStart = t;  // (not accounting for frame time here)
      fix6_2.frameNStart = frameN;  // exact frame index
      
      fix6_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix6_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix6_2.setAutoDraw(false);
    }
    
    // *counter_square_2* updates
    if (t >= 0.0 && counter_square_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      counter_square_2.tStart = t;  // (not accounting for frame time here)
      counter_square_2.frameNStart = frameN;  // exact frame index
      
      counter_square_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (counter_square_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      counter_square_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of counterfactual_expComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function counterfactual_expRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'counterfactual_exp'-------
    for (const thisComponent of counterfactual_expComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _block1_wait_allKeys;
var FinishComponents;
function FinishRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Finish'-------
    t = 0;
    FinishClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    block1_wait.keys = undefined;
    block1_wait.rt = undefined;
    _block1_wait_allKeys = [];
    block1_points.setText(b1_total);
    // keep track of which components have finished
    FinishComponents = [];
    FinishComponents.push(Block_Finish);
    FinishComponents.push(block1_wait);
    FinishComponents.push(block1_points);
    FinishComponents.push(block1_points_earned);
    
    for (const thisComponent of FinishComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function FinishRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Finish'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = FinishClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Block_Finish* updates
    if (t >= 0.0 && Block_Finish.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Block_Finish.tStart = t;  // (not accounting for frame time here)
      Block_Finish.frameNStart = frameN;  // exact frame index
      
      Block_Finish.setAutoDraw(true);
    }

    
    // *block1_wait* updates
    if (t >= 0.0 && block1_wait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block1_wait.tStart = t;  // (not accounting for frame time here)
      block1_wait.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { block1_wait.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { block1_wait.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { block1_wait.clearEvents(); });
    }

    if (block1_wait.status === PsychoJS.Status.STARTED) {
      let theseKeys = block1_wait.getKeys({keyList: ['space'], waitRelease: false});
      _block1_wait_allKeys = _block1_wait_allKeys.concat(theseKeys);
      if (_block1_wait_allKeys.length > 0) {
        block1_wait.keys = _block1_wait_allKeys[_block1_wait_allKeys.length - 1].name;  // just the last key pressed
        block1_wait.rt = _block1_wait_allKeys[_block1_wait_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *block1_points* updates
    if (t >= 0.0 && block1_points.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block1_points.tStart = t;  // (not accounting for frame time here)
      block1_points.frameNStart = frameN;  // exact frame index
      
      block1_points.setAutoDraw(true);
    }

    
    // *block1_points_earned* updates
    if (t >= 0.0 && block1_points_earned.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block1_points_earned.tStart = t;  // (not accounting for frame time here)
      block1_points_earned.frameNStart = frameN;  // exact frame index
      
      block1_points_earned.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FinishComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinishRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Finish'-------
    for (const thisComponent of FinishComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('block1_wait.keys', block1_wait.keys);
    if (typeof block1_wait.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('block1_wait.rt', block1_wait.rt);
        routineTimer.reset();
        }
    
    block1_wait.stop();
    // the Routine "Finish" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
