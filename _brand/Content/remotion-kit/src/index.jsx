import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {OverlayStill, Reel} from './Reel';
import data from './data.json';

const FPS = 30;
const frames = Math.ceil(data.total * FPS);

const Root = () => (
  <>
    <Composition id="Reel" component={Reel} durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    {/* CapCut pack: footage with the zooms only, and single overlays on a transparent frame */}
    <Composition id="ReelClean" component={Reel} defaultProps={{clean: true}} durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    <Composition id="Graphics" component={Reel} defaultProps={{graphicsOnly: true}} durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    <Composition id="Overlay" component={OverlayStill} defaultProps={{kind: 'shot', index: 0}} durationInFrames={1} fps={FPS} width={1080} height={1920} />
  </>
);

registerRoot(Root);
