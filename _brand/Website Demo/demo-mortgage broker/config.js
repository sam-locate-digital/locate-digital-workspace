// Harlow Home Loans demo – single source of truth for business details.
// Everything marked PLACEHOLDER is fictional demo data. Swap before showing a real broker.

const CONFIG = {
  brand: { name: "Harlow Home Loans", short: "Harlow", founded: 2011 },               // PLACEHOLDER
  contact: {
    phone: "(03) 5550 2861",                // reserved fictional number
    phoneHref: "tel:+61355502861",
    email: "hello@harlowhomeloans.example",
    office: "Box Hill VIC 3128"             // PLACEHOLDER street address
  },
  hours: "Mon–Fri 8:30am–6pm, Sat by appointment, evening video calls",
  compliance: {
    entity: "Harlow Home Loans Pty Ltd",
    abn: "[PLACEHOLDER]",
    creditRep: "[PLACEHOLDER]",
    licensee: "[Aggregator PLACEHOLDER] Pty Ltd",
    acl: "[PLACEHOLDER]",
    feePolicy: "Our service is usually free to you. Lenders pay us a commission when your loan settles, and we'll show you exactly how much before you choose.",
    generalInfo: "The information on this website is general only and doesn't take into account your objectives, financial situation or needs. Your full financial situation will need to be reviewed before any loan offer. Calculator results are estimates only.",
    calculatorDisclaimer: "This is an estimate only, based on the figures you entered and the assumptions shown. It isn't a loan offer or credit advice."
  },
  situations: [
    { id: "first-home",    label: "Buying my first home", url: "/buying/first-home", image: "images/situation-first-home.png" },
    { id: "next-home",     label: "Buying my next home",  url: "/buying/next-home",  image: "images/situation-next-home.png" },
    { id: "refinance",     label: "Refinancing",          url: "/refinancing",       image: "images/situation-refinance.png" },
    { id: "invest",        label: "Investing",            url: "/investing",         image: "images/situation-investing.png" },
    { id: "self-employed", label: "Self-employed",        url: "/self-employed",     image: "images/why-harlow.png" },
    { id: "building",      label: "Building",             url: "/building",          image: "images/situation-next-home.png" }
  ],
  team: [
    { id: "claire", name: "Claire Harlow", role: "Principal broker", languages: ["English"] },
    { id: "tom",    name: "Tom Nguyen",    role: "Broker",           languages: ["English", "Vietnamese"] },
    { id: "priya",  name: "Priya Shah",    role: "Broker",           languages: ["English", "Hindi", "Gujarati"] },
    { id: "mia",    name: "Mia Chen",      role: "Client support",   languages: ["English", "Mandarin"] }
  ],
  suburbs: ["Box Hill", "Blackburn", "Doncaster", "Balwyn", "Camberwell", "Surrey Hills", "Mont Albert", "Mitcham", "Ringwood", "Glen Waverley", "Burwood", "Vermont"],
  stats: { rating: 4.9, reviewCount: 280, settledMillions: 640, lenders: "30+" },     // PLACEHOLDER
  responseTime: "1 business day",                                                     // PLACEHOLDER
  promo: "Fixed rate ending soon? Book a free rate review before it rolls onto a higher variable rate.",

  // Calculator assumptions – demo values only. Check with the broker before going live.
  calculator: {
    exampleRate: 6.0,          // % p.a., shown as "Example rate only, not a current offer"
    bufferPoints: 3.0,         // serviceability buffer added to the example rate
    termYears: 30,
    cardLimitRepaymentPct: 3,  // % of credit card limits counted as a monthly repayment
    minMonthlyExpenses: { single: 2000, couple: 3000, perDependant: 400 },          // PLACEHOLDER
    // Resident income tax brackets – PLACEHOLDER, check current rates at ato.gov.au
    taxBrackets: [
      { upTo: 18200,    rate: 0 },
      { upTo: 45000,    rate: 0.15 },
      { upTo: 135000,   rate: 0.30 },
      { upTo: 190000,   rate: 0.37 },
      { upTo: Infinity, rate: 0.45 }
    ],
    medicareLevy: 0.02,
    refinanceNotWorthItMonths: 24
  },

  formEndpoint: null           // e.g. Formspree or webhook URL; null = demo mode (logs to console)
};

if (typeof module !== "undefined") module.exports = CONFIG;
