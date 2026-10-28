/*
  Site config: everything that changes from one tradie to the next.

  For a new tradie, edit this file and reviews.json, then swap the photos in
  images/ for theirs (keep the same file names). Every page reads from here.
  Values marked PLACEHOLDER are made up for the demo; they're highlighted on
  the page while showPlaceholders is true.
*/
window.CONFIG = {
  brand: { name: 'Eastside Trades', fullName: 'Eastside Trades Plumbing + Electrical', founded: 1998 }, // founded: PLACEHOLDER

  // 'plumbing', 'electrical' or both. One trade rewrites the copy and hides
  // the other trade's nav, mega panel column, services column and footer links.
  trades: ['plumbing', 'electrical'],

  // Brand colour. Hover and pressed shades are worked out from it.
  // images/brush.svg and images/brush-hero.svg are blue: recolour them if this changes.
  accent: '#1F45D6',

  // Highlights the PLACEHOLDER values in yellow. Set to false before going live.
  showPlaceholders: true,

  // false = demo: every page is hidden from Google. true = a client's live site:
  // Google can list it, and build.js writes sitemap.xml, robots.txt and vercel.json.
  // Run `node build.js` after changing anything in this block.
  production: false,
  siteUrl: 'https://demo.locatedigital.io/tradie/',   // the live address, ending in /
  ga4Id: '',                                          // e.g. 'G-XXXXXXXXXX'; '' = no analytics
  // Old website pages that should send visitors to a new page (production only).
  redirects: [
    // { from: '/services/hot-water.php', to: '/plumbing/hot-water' }
  ],

  contact: { phone: '(03) 5550 4127', email: 'jobs@eastsidetrades.example' },
  address: { street: '[street address]', suburb: 'Blackburn', state: 'VIC', postcode: '3130' }, // street: PLACEHOLDER
  hours: { weekdays: '7am–5pm', emergency: '24/7', schema: 'Mo-Fr 07:00-17:00' },
  licences: { plumbing: '[licence no.]', rec: '[REC no.]', abn: '[ABN]', insurance: '[$ cover]' }, // PLACEHOLDER

  suburbs: ['Box Hill', 'Blackburn', 'Mitcham', 'Nunawading', 'Vermont', 'Forest Hill', 'Ringwood', 'Croydon', 'Doncaster', 'Templestowe', 'Balwyn', 'Camberwell', 'Surrey Hills', 'Glen Waverley', 'Burwood', 'Mont Albert'],

  stats: { rating: 4.9, reviewCount: 612, jobsDone: 18400 },   // PLACEHOLDER
  guaranteeYears: 10,                                            // PLACEHOLDER
  responseTime: '1 business hour',                               // PLACEHOLDER
  promo: "Summer's coming: free switchboard safety check with any electrical job this month.", // '' hides the promo bar

  // Where booking requests are POSTed as JSON (Formspree, Make or a webhook URL).
  // null = front-end demo only: the booking is logged to the console.
  formEndpoint: null,
  bookingRefPrefix: 'HC-',

  // Jobs offered in the hero search and the booking form's job list.
  jobs: [
    { v: 'Blocked drain', t: 'plumbing' }, { v: 'Hot water not working', t: 'plumbing' },
    { v: 'Leaking tap or toilet', t: 'plumbing' }, { v: 'Gas heater service', t: 'plumbing' },
    { v: 'Power out or tripping', t: 'electrical' }, { v: 'New lights or power points', t: 'electrical' },
    { v: 'Switchboard upgrade', t: 'electrical' }, { v: 'Smoke alarms', t: 'electrical' }
  ],

  // page: links to that service page. emergency: links to the emergency page. Neither: links to the trade hub.
  // job: the booking form job it pre-fills.
  services: {
    plumbing: [
      { name: 'Hot water repairs and replacement', desc: 'Gas, electric and continuous flow. Often fixed the same day.', page: 'hot-water', job: 'Hot water not working' },
      { name: 'Blocked drains and CCTV inspection', desc: 'Cleared with a jetter, with camera footage sent to you.', page: 'blocked-drains', job: 'Blocked drain' },
      { name: 'Leaking taps, toilets and showers', desc: 'Drips, running toilets and leaking shower bases.', job: 'Leaking tap or toilet' },
      { name: 'Gas fitting and heater servicing', desc: 'Heater services, gas leaks and new appliance connections.', job: 'Gas heater service' },
      { name: 'Burst pipes and emergencies', desc: '24/7 for burst pipes, gas smells and no hot water.', emergency: true, job: 'Other' },
      { name: 'Bathroom and kitchen renovations', desc: 'All the plumbing and electrical for your reno, in one booking.', job: 'Other' }
    ],
    electrical: [
      { name: 'Power faults and emergencies', desc: 'Tripping safety switches, dead circuits and no power.', emergency: true, job: 'Power out or tripping' },
      { name: 'Switchboard upgrades', desc: 'Old fuse boards replaced with modern safety switches.', page: 'switchboards', job: 'Switchboard upgrade' },
      { name: 'Lights, power points and fans', desc: 'New lights, extra power points and ceiling fans.', job: 'New lights or power points' },
      { name: 'Smoke alarms and safety checks', desc: 'Testing, replacement and certificates for rentals.', page: 'smoke-alarms', job: 'Smoke alarms' },
      { name: 'Split system installs', desc: 'Installed, wired and tested by our own team.', job: 'Other' },
      { name: 'Appliance installs', desc: 'Ovens, cooktops and dishwashers connected safely.', job: 'Other' }
    ]
  },

  servicePages: {
    'hot-water': {
      trade: 'plumbing', job: 'Hot water not working', img: 'hot-water.webp', alt: 'New continuous-flow hot water unit being installed', key: 'hot water',
      h1: 'Hot water fixed or replaced, often same day', short: 'a hot water fix', topic: 'hot water',
      intro: 'Gas, electric and continuous-flow systems. We find the fault and explain your options in plain English before we start.',
      signs: ['No hot water, or it runs out fast', 'Rusty or smelly hot water', 'Water leaking from the tank or relief valve', 'Pilot light keeps going out'],
      included: ['Diagnosis on gas, electric and continuous-flow systems', 'Repairs to thermostats, valves and elements', 'Like-for-like or upgrade replacement, old unit taken away', 'Compliance certificate for every install'],
      note: 'Repair or replace, we explain the options and recommend what suits your home. If the unit is beyond saving, we tell you straight.',
      related: ['Blocked drains and CCTV inspection', 'Gas fitting and heater servicing', 'Burst pipes and emergencies']
    },
    'blocked-drains': {
      trade: 'plumbing', job: 'Blocked drain', img: 'drain-jet.webp', alt: 'A plumber jetting a blocked outdoor drain', key: 'drain',
      h1: 'Blocked drains cleared, with camera footage to show you', short: 'a drain clear', topic: 'that drain',
      intro: 'Kitchen, bathroom, toilet or stormwater. We clear it, run a camera through and send you the footage so you can see what caused it.',
      signs: ['Sinks or the shower draining slowly', 'Gurgling sounds from drains', 'Bad smells outside or from floor wastes', 'Gully trap overflowing after rain'],
      included: ['High-pressure jetting', 'CCTV camera inspection, footage sent to you', 'Tree-root cutting', 'Advice on relining or repair if the pipe is damaged'],
      note: 'We clear it, show you the footage and explain what caused it. If the camera finds a broken pipe, we talk you through the repair options before doing anything more.',
      related: ['Hot water repairs and replacement', 'Leaking taps, toilets and showers', 'Burst pipes and emergencies']
    },
    'switchboards': {
      trade: 'electrical', job: 'Switchboard upgrade', img: 'electrical.webp', alt: 'Electrician working on a home switchboard', key: 'switchboard',
      h1: 'Switchboard upgrades, explained in plain English', short: 'a switchboard check', topic: 'your switchboard',
      intro: 'Old fuse boards replaced with modern safety switches on every circuit, clearly labelled, tested and certified.',
      signs: ['Old ceramic fuses instead of switches', 'Power trips when appliances run together', 'The board feels warm or smells of burning', 'Adding solar, a battery or an EV charger'],
      included: ['New board with safety switches (RCDs) on every circuit', 'Every circuit clearly labelled', 'Testing and a certificate of compliance', 'A walk-through of how to reset it'],
      note: "We explain exactly what's needed before we start, and tell you how long the power will be off.",
      related: ['Smoke alarms and safety checks', 'Power faults and emergencies', 'Lights, power points and fans']
    },
    'smoke-alarms': {
      trade: 'electrical', job: 'Smoke alarms', img: 'smoke-alarm.webp', alt: 'An electrician testing a new ceiling smoke alarm in a hallway', key: 'smoke',
      h1: 'Smoke alarms checked, replaced and certified', short: 'a smoke alarm check', topic: 'your smoke alarms',
      intro: 'For homeowners and rentals. We test every alarm, replace the ones that are expired or faulty, and send a report with photos.',
      signs: ['Alarms more than 10 years old', 'Chirping or false alarms', 'A rental due for its safety check', 'Renovating or adding bedrooms'],
      included: ['Testing every alarm in the home', 'Replacing expired or faulty alarms', 'Hard-wired and interconnected options', 'Report, photos and certificate for landlords'],
      note: 'Homeowners get a walk-through of every alarm. Landlords get the report, photos and invoice sent straight through.',
      related: ['Switchboard upgrades', 'Lights, power points and fans', 'Power faults and emergencies']
    }
  },

  // Local copy for suburb pages. Suburbs not listed here get the generic copy.
  suburbDetail: {
    'Box Hill': { para: "From apartments near the station to post-war homes off Middleborough Road, we're in Box Hill most days. Older homes here often still have original gas hot water and fuse boards, and the apartments keep us busy with taps, toilets and appliances.", jobs: ['Hot water replacement', 'Switchboard upgrades', 'Leaking taps and toilets', 'Appliance installs in apartments'] },
    'Blackburn': { para: 'Blackburn is home. Our workshop is here, so most jobs are a short drive away. Leafy streets mean tree roots in old clay drains, and plenty of mid-century homes are due for a switchboard upgrade.', jobs: ['Blocked drains and tree roots', 'Switchboard upgrades', 'Gas heater servicing', 'Hot water repairs'] },
    'Ringwood': { para: 'Ringwood has a lot of 1970s and 80s brick homes, and many are on their second or third hot water unit. We also do plenty of drains and smoke alarm checks for local rentals.', jobs: ['Hot water replacement', 'Blocked drains', 'Smoke alarms for rentals', 'Power faults'] },
    'Doncaster': { para: "Doncaster's 1960s and 70s homes are being renovated and rebuilt street by street. We do the plumbing and electrical for renovations, plus everyday repairs for owners and landlords.", jobs: ['Bathroom and kitchen renovations', 'Switchboard upgrades', 'Lights and power points', 'Smoke alarms and leaks in rentals'] },
    'Camberwell': { para: "Camberwell's Edwardian and interwar homes are beautiful, and their old pipes and wiring need a careful hand. We work around period features and leave the house as we found it.", jobs: ['Old pipe and leak repairs', 'Rewiring and switchboards', 'Bathroom renovations', 'Gas heater servicing'] },
    'Glen Waverley': { para: 'Glen Waverley has plenty of 1960s and 70s brick homes alongside new townhouses. We see a lot of hot water upgrades, split system installs and power point work here.', jobs: ['Hot water upgrades', 'Split system installs', 'Lights and power points', 'Blocked drains'] }
  },

  nearby: {
    'Box Hill': ['Mont Albert', 'Blackburn', 'Surrey Hills', 'Burwood', 'Doncaster'], 'Blackburn': ['Nunawading', 'Box Hill', 'Forest Hill', 'Vermont', 'Mitcham'],
    'Mitcham': ['Nunawading', 'Vermont', 'Ringwood', 'Blackburn'], 'Nunawading': ['Blackburn', 'Mitcham', 'Forest Hill', 'Box Hill'],
    'Vermont': ['Mitcham', 'Forest Hill', 'Ringwood', 'Nunawading'], 'Forest Hill': ['Nunawading', 'Vermont', 'Blackburn', 'Burwood'],
    'Ringwood': ['Croydon', 'Mitcham', 'Vermont'], 'Croydon': ['Ringwood', 'Mitcham', 'Vermont'],
    'Doncaster': ['Templestowe', 'Balwyn', 'Box Hill'], 'Templestowe': ['Doncaster', 'Balwyn'],
    'Balwyn': ['Doncaster', 'Camberwell', 'Surrey Hills', 'Mont Albert'], 'Camberwell': ['Surrey Hills', 'Balwyn', 'Burwood', 'Mont Albert'],
    'Surrey Hills': ['Mont Albert', 'Camberwell', 'Box Hill', 'Balwyn'], 'Glen Waverley': ['Burwood', 'Forest Hill', 'Vermont'],
    'Burwood': ['Box Hill', 'Glen Waverley', 'Camberwell', 'Surrey Hills'], 'Mont Albert': ['Box Hill', 'Surrey Hills', 'Balwyn']
  },

  team: [
    { name: 'Pete Morgan', role: 'Founder · plumber and gas fitter' },
    { name: 'Jake Morgan', role: 'Electrician' },
    { name: 'Tom Nguyen', role: 'Plumber' },
    { name: 'Mia Russo', role: 'Bookings and accounts' }
  ]
};
