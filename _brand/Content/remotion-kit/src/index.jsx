import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {END_CARD_SECONDS, HOUSE_STYLE, OverlayStill, Reel} from './Reel';
import data from './data.json';

const FPS = 30;
const frames = Math.ceil(data.total * FPS);
// Length follows the style: an end card adds its seconds after the speech ends
const reelMetadata = ({props}) => ({
  durationInFrames: props.endCard ? Math.ceil((data.endCard + END_CARD_SECONDS) * FPS) : frames,
});

const Root = () => (
  <>
    {/* Pass style props (captionStyle, shotStyle, logoStyle, endCard) with --props to pick styles from the style menu */}
    <Composition id="Reel" component={Reel} defaultProps={HOUSE_STYLE} calculateMetadata={reelMetadata}
      durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    {/* CapCut pack: footage with the zooms only, and graphics alone on a transparent frame */}
    <Composition id="ReelClean" component={Reel} defaultProps={{...HOUSE_STYLE, clean: true}} durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    <Composition id="Graphics" component={Reel} defaultProps={{...HOUSE_STYLE, graphicsOnly: true}} durationInFrames={frames} fps={FPS} width={1080} height={1920} />
    <Composition id="Overlay" component={OverlayStill} defaultProps={{kind: 'shot', index: 0}} durationInFrames={1} fps={FPS} width={1080} height={1920} />
  </>
);

registerRoot(Root);
