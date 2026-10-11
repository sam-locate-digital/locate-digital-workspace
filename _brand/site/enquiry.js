// Sends website enquiries to sam@locatedigital.io via Web3Forms.
// The access key is public by design: it can only deliver to the account inbox.
window.sendEnquiry = function (source, d, message) {
  return fetch('https://api.web3forms.com/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify({
      access_key: '6752c14a-6290-41d9-b2d0-1564444aa155',
      subject: 'Website enquiry: ' + (d.company || d.name),
      from_name: 'Locate Digital website',
      replyto: d.email,
      name: d.name,
      email: d.email,
      phone: d.phone || '-',
      firm: d.company || '-',
      message: message || '-',
      page: source + ' (' + location.href + ')'
    })
  })
    .then((r) => r.json().catch(() => ({})))
    .then((j) => { if (!j.success) throw new Error(j.message || 'Send failed'); });
};
