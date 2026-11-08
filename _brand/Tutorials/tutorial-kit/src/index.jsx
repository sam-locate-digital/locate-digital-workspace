import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {Tutorial} from './Tutorial';
import tl from './timeline.json';

const Root = () => (
  <Composition id="Tutorial" component={Tutorial} durationInFrames={Math.max(1, Math.round(tl.length * tl.fps))}
    fps={tl.fps} width={1920} height={1080} />
);

registerRoot(Root);
