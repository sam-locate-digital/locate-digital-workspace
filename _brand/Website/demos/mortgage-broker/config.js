/*
  Harlow Home Loans demo: all site content in one place.
  Read by build.js (to write the pages) and by the browser (enquiry form, reviews).
  After changing anything here, run:  node build.js
  Every [PLACEHOLDER] stays as is until the client supplies a real value.
*/
window.CONFIG = {
  production: false,
  brand: { name: 'Harlow Home Loans', short: 'Harlow' },
  contact: {
    phone: '(03) 5550 2861',
    phoneHref: 'tel:+61355502861',
    email: 'hello@harlowhomeloans.example',
    office: '[PLACEHOLDER suburb] VIC',
  },
  hours: 'Mon–Fri 8:30am–6pm, Sat by appointment, evening video calls',
  responseTime: '1 business day',
  promo: 'Fixed rate ending soon? Book a free rate review before it rolls onto a higher variable rate.',
  stats: { settledMillions: 640 },
  suburbs: [],
  formEndpoint: null,
  team: [
    { id: 'claire', name: 'Claire Harlow', first: 'Claire', role: 'Principal broker', languages: ['English'], href: 'claire.html', books: true },
    { id: 'tom', name: 'Tom Nguyen', first: 'Tom', role: 'Broker', languages: ['English', 'Vietnamese'], href: 'tom.html', books: true },
    { id: 'priya', name: 'Priya Shah', first: 'Priya', role: 'Broker', languages: ['English', 'Hindi', 'Gujarati'], href: 'priya.html', books: true },
    { id: 'mia', name: 'Mia Chen', first: 'Mia', role: 'Client support', languages: ['English', 'Mandarin'], href: 'mia.html', books: false },
  ],
  compliance: {
    entity: 'Harlow Home Loans Pty Ltd',
    abn: '[PLACEHOLDER]',
    creditRep: '[PLACEHOLDER]',
    licensee: '[Aggregator PLACEHOLDER] Pty Ltd',
    acl: '[PLACEHOLDER]',
    feePolicy: "Our service is usually free to you. Lenders pay us a commission when your loan settles, and we'll show you exactly how much before you choose.",
    generalInfo: "The information on this website is general only and doesn't take into account your objectives, financial situation or needs. Your full financial situation will need to be reviewed before any loan offer.",
  },
};

// Illustrative reviews for the demo only. Replace with genuine reviews used with the client's permission.
window.REVIEWS = {
  average: 4.9,
  reviews: [
    { name: 'Ben & Aisha R.', suburb: 'Doncaster', situation: 'first-home', situationLabel: 'First home', broker: 'claire', rating: 5, date: '2026-09-14', quote: 'We thought we were years away. Claire showed us what was possible and walked us through every form. Settled in six weeks.' },
    { name: 'Margaret L.', suburb: 'Blackburn', situation: 'refinance', situationLabel: 'Refinance', broker: 'tom', rating: 5, date: '2026-08-30', quote: "My fixed rate was about to end. Tom compared it, did the paperwork, and my repayments came down. I didn't call the bank once." },
    { name: 'Raj & Neha P.', suburb: 'Glen Waverley', situation: 'next-home', situationLabel: 'Next home', broker: 'priya', rating: 5, date: '2026-08-12', quote: 'Buying before selling scared us. Priya explained bridging finance in plain English, and in Hindi for my parents.' },
    { name: 'Jess T.', suburb: 'Mitcham', situation: 'self-employed', situationLabel: 'Self-employed', broker: 'claire', rating: 5, date: '2026-07-21', quote: "Two banks said no because I'm a sole trader. Harlow found a lender that understood my business." },
    { name: 'David K.', suburb: 'Northcote', situation: 'invest', situationLabel: 'Investing', broker: 'tom', rating: 5, date: '2026-07-03', quote: 'Quick and honest about what made sense for my second property, including when to wait.' },
    { name: 'Lucy & Sam W.', suburb: 'Camberwell', situation: 'next-home', situationLabel: 'Next home', broker: 'priya', rating: 5, date: '2026-06-18', quote: 'Evening video calls meant we never took time off work. Mia kept us updated at every step.' },
  ],
};
